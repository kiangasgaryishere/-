"""Extend recovered approved mix with original narrator and sparse CC0 Foley.
Original master stems unavailable. Requires external prepared narrator and decoded v003.
"""
from pathlib import Path
import json
import numpy as np,soundfile as sf
from scipy.ndimage import uniform_filter1d
p=Path(__file__).parent; sr=48000
voice,s=sf.read('/workspace/production-inputs/garage/voice-prepared.wav');assert s==sr
old,s=sf.read('/workspace/garage-production-v004/approved-audio.wav');assert s==sr
# Preserve exactly the first twenty seconds of recovered PCM. Match narrator
# gain over the last four seconds with a least-squares fit; no speed changes.
i,j=16*sr,20*sr;g=np.dot(old[i:j],voice[i:j])/np.dot(voice[i:j],voice[i:j])
out=voice[:30*sr]*g;out[:20*sr]=old[:20*sr]
# Residual soundtrack bridge only. Voice timing/gain is never faded at the join.
n=int(.18*sr);res=old[20*sr-n:20*sr]-voice[20*sr-n:20*sr]*g
out[20*sr:20*sr+n]+=res*np.linspace(1,0,n)
by={a['id']:a for a in json.load(open('/workspace/video-tools/sfx-kit/sounds.json'))['sounds']};cues=[]
for ident,moment,gain,dur in [('props-page-turn',21.4,.04,.55),('writing-pencil-write',24.5,.055,1.5),('foley-paper-touch',27.3,.05,.3),('mechanical-switch-heavy',29.1,.035,.25)]:
 m=by[ident];a,s=sf.read('/workspace/video-tools/sfx-kit/'+m['file']);assert s==sr
 if a.ndim==2:a=a.mean(axis=1)
 a=a[:int(dur*sr)].copy();f=min(480,len(a));a[:f]*=np.linspace(0,1,f);a[-f:]*=np.linspace(1,0,f)
 start=round((moment-m['sync']['at'])*sr);out[start:start+len(a)]+=a*gain
 cues.append(dict(id=ident,moment=moment,start=start/sr,sync=m['sync']['at'],gain=gain,asset=m['file'],license='CC0-1.0'))
tail=out[20*sr:]; mag=np.abs(tail); out[20*sr:]=np.sign(tail)*np.where(mag>.65,.65+.23*np.tanh((mag-.65)/.23),mag)
assert np.max(np.abs(out))<1
sf.write(p/'audio/mix-030s-v004.wav',out,sr,subtype='PCM_24')
t=json.loads((p/'timeline.json').read_text());t['sound_events']=[a for a in t['sound_events'] if a.get('start',0)<20]+cues;(p/'timeline.json').write_text(json.dumps(t,ensure_ascii=False,indent=2))
print('Narrator gain',g,'PCM peak',np.max(np.abs(out)),'first 20s recovered mix preserved; source voice uncut')
