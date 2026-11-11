from pathlib import Path
import sys,json
import numpy as np,soundfile as sf
from scipy.ndimage import uniform_filter1d
sys.path.insert(0,'/workspace/video-tools/lemo-opuscar')
from core.audio import sampler as S
SR=48000;root=Path(__file__).parent
voice,sr=sf.read(root/'audio/voice-prepared.wav');assert sr==SR
N=len(voice);music=np.zeros(N);fx=np.zeros(N);rng=np.random.default_rng(810)
def put(buf,a,t,g=1):
 a=np.asarray(a);a=a.mean(axis=1) if a.ndim==2 else a
 k=round(t*SR);src=max(0,-k);k=max(k,0);n=min(len(a)-src,len(buf)-k)
 if n>0:buf[k:k+n]+=a[src:src+n]*g
def pluck(freq,dur,guitar=False):
 n=int(dur*SR);delay=round(SR/freq);noise=rng.uniform(-1,1,delay);a=np.zeros(n);a[:delay]=noise
 for k in range(delay,n):a[k]=.497*(a[k-delay]+a[k-delay+1]) if k-delay+1<k else .99*a[k-delay]
 a*=np.minimum(1,np.arange(n)/150)
 if guitar:a=np.tanh(a*2.8)*.7
 return a
# Original restrained swung riff. Continuous global clock, no ten-second boundary fades.
beat=60/94
for j in range(int(N/SR/beat)+1):
 t=.55+j*beat
 freq=[73.416,87.307,97.999,110][j%4]
 put(music,pluck(freq,.5),t,.14)
 # dry brushed tick and muted low drum, with swing second eighth
 for dt,g in [(0,.025),(beat*2/3,.012)]:
  n=int(.055*SR);a=rng.normal(0,1,n)*np.exp(-np.arange(n)/(SR*.012));a-=uniform_filter1d(a,15);put(music,a,t+dt,g)
 if j%2==0:
  tt=np.arange(int(.17*SR))/SR;a=np.sin(2*np.pi*(47*tt+22*.035*(1-np.exp(-tt/.035))))*np.exp(-tt*29);put(music,a,t,.095)
 if j>=10 and j%2==0:
  for f in [146.83,220,293.66]:put(music,pluck(f,.23,True),t,.018)
# Actual CC0 VCSL Hohner harmonica, placed in detected voice pauses.
S.seed(15)
for t,note,dur,g in [(3.29,'D4',.27,.035),(6.4,'F4',.24,.03),(6.68,'D4',.21,.025)]:
 put(music,S.note('harmonica',note,dur,vel=.55,release=.06,attack=.025),t,g)
# Start the music quietly; leave first unexpected physical contact exposed.
music*=np.minimum(1,np.arange(N)/(SR*.85))
meta=json.load(open('/workspace/video-tools/sfx-kit/sounds.json'));by={s['id']:s for s in meta['sounds']};cues=[]
for ident,moment,g,trim in [('foley-paper-touch',.1,.09,None),('props-page-turn',3.35,.065,.65),('writing-pencil-write',4.3,.045,1.6),('mechanical-switch-heavy',6.65,.07,None),('foley-paper-touch',8.9,.07,None)]:
 m=by[ident];a,s=sf.read('/workspace/video-tools/sfx-kit/'+m['file']);assert s==SR
 if trim:a=a[:int(trim*SR)].copy();a[-min(len(a),480):]*=np.linspace(1,0,min(len(a),480))[:,None] if a.ndim==2 else np.linspace(1,0,min(len(a),480))
 start=moment-m['sync']['at'];put(fx,a,start,g);cues.append(dict(id=ident,moment=moment,start=start,sync=m['sync']['at'],gain=g,license='CC0-1.0',asset=m['file']))
# Local ducking based on actual voice energy, rather than arbitrary heavy blanket ducking.
env=np.sqrt(uniform_filter1d(voice*voice,int(SR*.08)));duck=1-.5*np.clip(env/.06,0,1);music*=duck
sf.write(root/'audio/music-full-draft.wav',music,SR,subtype='PCM_24');sf.write(root/'audio/effects-full.wav',fx,SR,subtype='PCM_24')
mix=voice+music+fx
sf.write(root/'audio/mix-full-unmastered.wav',mix,SR,subtype='PCM_24');(root/'audio/sound-cues.json').write_text(json.dumps(cues,indent=2))
print('Master timeline samples',N,'Peak',np.max(np.abs(mix)))
