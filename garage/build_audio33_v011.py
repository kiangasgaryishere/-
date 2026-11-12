"""Deterministic V011 effects-only enhancement; preserve original base samples/time."""
from pathlib import Path
import hashlib,json,os
import numpy as np
import soundfile as sf
from scipy.signal import butter,sosfilt
from scipy.ndimage import uniform_filter1d,minimum_filter1d
P=Path(__file__).resolve().parent
WORK=Path(os.environ.get('GARAGE_BUILD_DIR','/workspace/garage-production-v011'));WORK.mkdir(parents=True,exist_ok=True)
T=json.loads((P/'timeline.json').read_text());CFG=T['sound_design_v011'];SR=CFG['sample_rate'];N=CFG['source_samples']
rng=np.random.default_rng(CFG['seed'])
base_path=P/CFG['base_master'];assert hashlib.sha256(base_path.read_bytes()).hexdigest()==CFG['base_sha256']
base,sr=sf.read(base_path);assert sr==SR and base.ndim==1 and len(base)==N
voice,sr=sf.read('/workspace/production-inputs/garage/voice-prepared.wav');assert sr==SR
if voice.ndim>1:voice=voice.mean(axis=1)
def band(a,lo,hi):return sosfilt(butter(2,[lo,hi],btype='bandpass',fs=SR,output='sos'),a)
def fades(a,attack=.008,release=.025):
 a=a.copy();n=min(len(a)//2,round(attack*SR));m=min(len(a)//2,round(release*SR))
 a[:n]*=np.sin(np.linspace(0,np.pi/2,n))**2;a[-m:]*=np.cos(np.linspace(0,np.pi/2,m))**2
 return a
def synth(kind,dur):
 n=round(dur*SR);t=np.arange(n)/SR;noise=rng.standard_normal(n)
 if kind=='entry-air':
  u=t/dur;env=(np.sin(np.pi*u)**2.4)*(0.7+0.3*u)
  a=band(noise,220,1900)*env
 elif kind=='metal-grain':
  env=np.sin(np.pi*t/dur)**1.5
  a=.6*band(noise,650,3600)*env
  for f,d in [(417,.15),(739,.11),(1271,.08),(2107,.05)]:a+=.09*np.sin(2*np.pi*f*t)*np.exp(-t/d)
 elif kind=='metal-track':
  env=np.sin(np.pi*t/dur)**1.1
  a=.28*band(noise,250,1900)*env
  # Irregularly spaced damped modal excitations, not a repeated UI click.
  for at in np.cumsum(rng.uniform(.036,.084,25)):
   if at>=dur-.025:break
   tt=t-at;on=tt>=0
   for f in [293,607,1061]:a+=np.where(on,.10*np.sin(2*np.pi*f*np.maximum(tt,0))*np.exp(-np.maximum(tt,0)/.026),0)*env
 elif kind=='stone-contact':
  a=.65*band(noise,100,1700)*np.exp(-t/.045)
  for f,d in [(117,.065),(241,.044),(523,.023)]:a+=.18*np.sin(2*np.pi*f*t)*np.exp(-t/d)
 else:raise ValueError(kind)
 a=fades(a,attack=.001 if kind=='stone-contact' else .009,release=.04)
 return a/max(np.max(np.abs(a)),1e-9)
fx=np.zeros((N,2));raw_events=[]
for ev in [s for s in T['sound_events'] if s.get('revision')=='v011']:
 if ev['kind']=='library':
  path=P/ev['asset'];meta=next(v for v in CFG['sources'].values() if v['asset']==ev['asset']);assert hashlib.sha256(path.read_bytes()).hexdigest()==meta['sha256']
  a,sr=sf.read(path);assert sr==SR
  # Retain original stereo width; mono files receive modest constant-power positioning.
  a=a[:round(ev['duration']*SR)]
  if a.ndim==1:a=np.column_stack([a,a])
  a=np.column_stack([fades(a[:,c],.003,.02) for c in range(2)])
 else:
  a=synth(ev['asset'],ev['duration']);a=np.column_stack([a,a])
 pan=ev['pan'];a[:,0]*=np.sqrt(1-max(0,pan));a[:,1]*=np.sqrt(1+min(0,pan));a*=ev['gain']
 if ev['id'].startswith('v011-garage'):
  # Subtle interior early reflections only on designed effects; never process narrator.
  dry=a.copy();a=np.pad(a,((0,round(.13*SR)),(0,0)))
  for delay,g,swap in [(.033,.12,False),(.061,.075,True),(.103,.035,False)]:
   k=round(delay*SR);a[k:k+len(dry)]+=dry[:,::-1] * g if swap else dry*g
 start=ev['start_sample'];lo=max(0,start);hi=min(N,start+len(a));chunk=a[lo-start:hi-start];fx[lo:hi]+=chunk
 raw_events.append({'id':ev['id'],'start_sample':start,'sync_sample':round(ev['moment']*SR),'source_sync_sample':round(ev['sync']*SR),'raw_peak':float(np.max(np.abs(chunk))),'duration_samples':len(a)})
# Filter effect bus, preserve material transients and reduce broad speech-band competition.
for c in range(2):
 fx[:,c]=band(fx[:,c],CFG['effect_bus_hp_hz'],CFG['effect_bus_lp_hz'])
 fx[:,c]-=.18*band(fx[:,c],1200,3600)
rms=np.sqrt(np.maximum(0,uniform_filter1d(voice[:N]**2,size=1920)))
activity=np.clip((rms-.015)/.045,0,1);duck=1-(1-10**(CFG['speech_duck_db']/20))*activity
fx*=duck[:,None]
# Effects-only, polarity-aware headroom reduction: original master is never compressed/scaled.
ceiling=CFG['fx_only_peak_ceiling'];scale=np.ones(N)
for c in range(2):
 z=fx[:,c];need=np.ones(N);pos=z>1e-10;neg=z< -1e-10
 need[pos]=np.minimum(1,(ceiling-base[pos])/z[pos]);need[neg]=np.minimum(1,(-ceiling-base[neg])/z[neg]);scale=np.minimum(scale,np.maximum(0,need))
# 2ms lookahead hold,40ms release. Gain cannot exceed per-sample safety bound.
held=minimum_filter1d(scale,size=193,mode='nearest');release=1-sosfilt(butter(1,12,fs=SR,output='sos'),1-held);scale=np.minimum(held,release)
fx*=scale[:,None];out=base[:,None]+fx
assert np.max(np.abs(out))<=ceiling+1e-7
assert np.max(np.abs((out-fx)-base[:,None]))<1e-14
panlaw=10**(CFG['stereo_center_pan_db']/20)
sf.write(WORK/'effects-033s-v011.wav',fx*panlaw,SR,subtype='PCM_24');sf.write(WORK/'mix-033s-v011.wav',out*panlaw,SR,subtype='PCM_24')
# Measured effect presence by cue; not a perceptual listening claim.
for r in raw_events:
 i=max(0,r['start_sample']);j=min(N,i+r['duration_samples']);r['final_fx_bus_rms_dbfs']=float(20*np.log10(np.sqrt(np.mean(fx[i:j]**2))+1e-12));r['base_rms_dbfs']=float(20*np.log10(np.sqrt(np.mean(base[i:j]**2))+1e-12))
mono=out.mean(axis=1);report={'source_base_sha256':CFG['base_sha256'],'samples':N,'sample_rate':SR,'channels':2,'peak':float(np.max(np.abs(out*panlaw))),'center_pan_db':CFG['stereo_center_pan_db'],'level_reference':'Cue metrics are mono-equivalent before equal-power stereo center pan','base_samples_preserved_before_encode':True,'voice_source_time_edits':0,'max_fx_only_headroom_reduction_db':float(20*np.log10(max(float(np.min(scale)),1e-12))),'stereo_mono_rms_difference_db':float(20*np.log10(np.sqrt(np.mean(mono**2))/np.sqrt(np.mean(out**2)))),'events':raw_events,'listening_review':'not performed; no audio listening tool available'}
(WORK/'audio-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='events'},indent=2))
