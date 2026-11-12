"""V005: continuous original 94BPM score reconstruction; preserve approved first20 PCM."""
from pathlib import Path
import json
import numpy as np,soundfile as sf
from scipy.ndimage import uniform_filter1d
p=Path(__file__).parent;sr=48000
voice,s=sf.read('/workspace/production-inputs/garage/voice-prepared.wav');old,_=sf.read('/workspace/garage-production-v004/approved-audio.wav');music,_=sf.read('/workspace/garage-production-v005/audio/music-full-draft.wav')
# Fit both original score and voice over four seconds; source voice has zero lag.
i,j=16*sr,20*sr;A=np.column_stack([voice[i:j],music[i:j]]);g,mg=np.linalg.lstsq(A,old[i:j],rcond=None)[0];mg=max(.7,min(float(mg),3))
out=voice[:30*sr]*g;mag=np.abs(out);out=np.sign(out)*np.where(mag>.62,.62+.23*np.tanh((mag-.62)/.23),mag)
out+=music[:30*sr]*mg
# Continue music through boundary; crossfade soundtrack residual only, never speech.
k=20*sr;n=240
# Five-millisecond continuity correction, not recycled speech or a voice fade.
delta=old[k-1]-out[k];out[k:k+n]+=delta*np.linspace(1,0,n);out[:k]=old[:k]
by={a['id']:a for a in json.load(open('/workspace/video-tools/sfx-kit/sounds.json'))['sounds']};cues=[]
for ident,moment,gain,dur in [('props-page-turn',21.05,.045,.55),('writing-pencil-write',22.1,.045,1.3),('foley-paper-touch',26.75,.05,.3),('mechanical-switch-heavy',29.05,.04,.25)]:
 m=by[ident];a,s=sf.read('/workspace/video-tools/sfx-kit/'+m['file']);assert s==sr
 if a.ndim==2:a=a.mean(axis=1)
 a=a[:int(dur*sr)].copy();f=min(480,len(a));a[:f]*=np.linspace(0,1,f);a[-f:]*=np.linspace(1,0,f)
 start=round((moment-m['sync']['at'])*sr);out[start:start+len(a)]+=a*gain
 cues.append(dict(id=ident,moment=moment,start=start/sr,sync=m['sync']['at'],gain=gain,asset=m['file'],license='CC0-1.0'))
# Headroom for final AAC; local limiter only on new section, no whole-film gain reset.
tail=out[k:];mag=np.abs(tail);out[k:]=np.sign(tail)*np.where(mag>.7,.7+.16*np.tanh((mag-.7)/.16),mag)
assert np.max(np.abs(out))<.9
sf.write(p/'audio/mix-030s-v005.wav',out,sr,subtype='PCM_24')
sf.write(p/'audio/music-030s-v005.wav',music[:30*sr]*mg,sr,subtype='PCM_24')
energy=[float(np.sqrt(np.mean((music[z*sr:(z+1)*sr]*mg)**2))) for z in range(20,30)]
assert min(energy)>0.001
report=dict(voice_gain=float(g),music_gain=mg,music_rms_per_second_20_30=energy,peak=float(np.max(np.abs(out))),source_map='continuous source samples 0–1439999; no time edits')
Path('/workspace/garage-production-v005/audio-report.json').write_text(json.dumps(report,indent=2))
t=json.loads((p/'timeline.json').read_text());t['sound_events']=[a for a in t['sound_events'] if a.get('start',0)<20]+cues;(p/'timeline.json').write_text(json.dumps(t,ensure_ascii=False,indent=2));print(report)
