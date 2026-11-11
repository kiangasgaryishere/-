from pathlib import Path
import sys,json
import numpy as np,soundfile as sf
from scipy.ndimage import uniform_filter1d
sys.path.insert(0,'/workspace/video-tools/lemo-opuscar')
from core.audio import sampler as S
p=Path(__file__).parent;sr=48000;base,s=sf.read(p/'audio/mix-full-master.wav');assert s==sr
extra=np.zeros(len(base));cues=[]
def put(a,t,g):
 a=a.mean(axis=1) if a.ndim==2 else a;start=round(t*sr);n=min(len(a),len(extra)-start)
 if n>0:extra[start:start+n]+=a[:n]*g
S.seed(25)
for t,note,dur,g in [(10.65,'A4',.28,.024),(11.02,'F4',.23,.02),(15.78,'D4',.19,.02),(18.58,'A4',.27,.021)]:
 a=S.note('harmonica',note,dur,vel=.5,release=.06,attack=.02);put(a,t,g);cues.append(dict(id='harmonica-response',start=t,note=note,duration=dur,license='CC0-1.0'))
meta=json.load(open('/workspace/video-tools/sfx-kit/sounds.json'));by={s['id']:s for s in meta['sounds']}
for ident,moment,g,limit in [('foley-paper-touch',10.6,.045,.3),('mechanical-switch-heavy',12.0,.05,.3),('props-page-turn',15.72,.045,.65),('foley-paper-touch',17.0,.035,.3),('mechanical-switch-heavy',18.8,.055,.3)]:
 m=by[ident];a,s=sf.read('/workspace/video-tools/sfx-kit/'+m['file']);assert s==sr;a=a[:int(limit*sr)].copy();fade=min(480,len(a));a[-fade:]*=np.linspace(1,0,fade)[:,None] if a.ndim==2 else np.linspace(1,0,fade)
 start=moment-m['sync']['at'];put(a,start,g);cues.append(dict(id=ident,moment=moment,start=start,sync=m['sync']['at'],gain=g,asset=m['file'],license='CC0-1.0'))
voice,s=sf.read(p/'audio/voice-prepared.wav');env=np.sqrt(uniform_filter1d(voice*voice,int(sr*.08)));extra*=1-.4*np.clip(env/.06,0,1)
out=base+extra;assert np.array_equal(out[:480000],base[:480000]);assert np.max(np.abs(out[:960000]))<.89
sf.write(p/'audio/mix-020s-v003.wav',out[:960000],sr,subtype='PCM_24')
sf.write(p/'audio/extra-010-020s-v003.wav',extra,sr,subtype='PCM_24')
T=json.loads((p/'timeline.json').read_text());T['sound_events']=[v for v in T['sound_events'] if v.get('start',0)<10]+cues;(p/'timeline.json').write_text(json.dumps(T,ensure_ascii=False,indent=2))
print('20s PCM ready. Original first 480000 master samples unchanged. Peak:',np.max(np.abs(out[:960000])))
