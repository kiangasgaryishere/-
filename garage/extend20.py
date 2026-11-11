from pathlib import Path
import json
p=Path(__file__).parent
s=(p/'index.html').read_text()
s=s.replace("</style>","@font-face{font-family:GarageLatin;src:url('fonts/GarageLatin.ttf')}</style>")
s=s.replace("const T=await", "const parts=new Image();parts.src='assets/chair-parts.png';await parts.decode();const portal=new Image();portal.src='assets/garage-portal.png';await portal.decode();await document.fonts.load('bold 100px GarageLatin');\nconst T=await")
end='};window.render(0);window.READY=true;'
assert end in s
s=s.replace(end,''' };
const opening=window.render;
// Capture approved boundary state once. All later frames derive from absolute master time.
opening(10-1/30000);const held=document.createElement('canvas');held.width=W;held.height=H;held.getContext('2d').drawImage(c,0,0);
function sprite(i,cx,cy,w,angle=0,alpha=1){x.save();x.globalAlpha=alpha;x.translate(cx,cy);x.rotate(angle);x.shadowColor='rgba(0,0,0,.5)';x.shadowBlur=22;x.shadowOffsetY=12;const sw=parts.width/3,sh=parts.height/2;x.drawImage(parts,(i%3)*sw,Math.floor(i/3)*sh,sw,sh,-w/2,-w*sh/sw/2,w,w*sh/sw);x.restore()}
const exploded=[[510,560,600,-.045],[520,960,620,.025],[850,1000,430,.06],[230,1100,430,-.08],[190,750,350,-.13],[880,730,350,.12]];
function explodedView(t){const a=e(t,12,13.7),settle=e(t,13.7,15.5);for(let i=0;i<6;i++){const [tx,ty,tw,rot]=exploded[i];sprite(i,lerp(540,tx,a),lerp(1040,ty,a),lerp(300,tw,a),rot*a+Math.sin(i*2.3+t*.4)*.012*settle,e(t,12+i*.045,12.35+i*.045))}x.save();x.globalAlpha=.35*e(t,13.2,13.8);x.setLineDash([7,12]);for(const [a,b] of [[[230,980],[230,860]],[[850,880],[850,820]],[[530,760],[530,860]]])path([a,b],1,WHITE,1.2);x.setLineDash([]);x.restore()}
function garageWord(cx,cy,size,alpha=1){x.save();x.globalAlpha=alpha;x.translate(cx,cy);x.scale(.76,1);x.font=`bold ${size}px GarageLatin`;x.textAlign='center';x.textBaseline='middle';x.fillStyle=WHITE;x.fillText('GARAGE',0,0);x.restore()}
function master(t){
 if(t<10){opening(t);return}
 x.setTransform(1,0,0,1,0,0);x.drawImage(paper,0,0);
 if(t<12){
  const q=e(t,10,11.6),z=lerp(1,.63,q);redSheet(1,490,1090,1080);
  // Original chair becomes one among accepted repeated objects.
  for(const [cx,cy,delay] of [[-100,640,.15],[1180,640,.25],[-100,1420,.35],[1180,1420,.45]]){const a=e(t,10+delay,11.4+delay);photo(lerp(540,cx,a),lerp(1035,cy,a),lerp(875,360,a),0,a*.8)}
  x.save();x.translate(540,1035);x.scale(z,z);x.drawImage(held,-540,-1035);x.restore();
  if(t>11.45){x.save();const a=e(t,11.45,12);x.fillStyle=BLACK;x.globalAlpha=a;x.fillRect(0,0,W,H);x.restore();redSheet(1,lerp(490,780,a),1040,1080);photo(540,1035,lerp(552,875,a),0,1)}
 }else if(t<15.72){
  redSheet(1,780,1040,1080);const q=e(t,12,12.65);photo(540,1035,875,0,1-q);explodedView(t);
 }else if(t<18.55){
  const q=e(t,15.72,16.55);redSheet(1,lerp(780,490,q),1040,1080);
  // Parts travel out of an imposed repeating arrangement; the opening is the new possibility.
  for(let i=0;i<6;i++){const [tx,ty,tw,rot]=exploded[i];const side=i%2?-1:1;sprite(i,lerp(tx,540+side*(510+i*35),q),lerp(ty,650+(i%3)*300,q),lerp(tw,260,q),lerp(rot,side*.15,q),1-q*.7)}
  const a=e(t,16.1,17.15);const w=lerp(360,1160,a),h=w*portal.height/portal.width;x.save();x.globalAlpha=a;x.translate(540,1030);x.rotate(lerp(-.04,0,a));x.drawImage(portal,-w/2,-h/2,w,h);x.restore();
  // Red is physically behind the doorway, revealed through its opening.
  if(t>17){const a=e(t,17,18);x.save();x.globalAlpha=a;x.beginPath();x.rect(230,960,620,310*a);x.clip();redSheet(1,310,1110,620);x.restore()}
 }else{
  const q=e(t,18.55,19.65),w=1160+70*q,h=w*portal.height/portal.width;redSheet(1,490,1040,1080);x.save();x.translate(540,1030);x.drawImage(portal,-w/2,-h/2,w,h);x.restore();
  // The same red support becomes the space inside the GARAGE entrance, not a stray stroke.
  x.save();x.beginPath();x.rect(220-20*q,940,640+40*q,340);x.clip();redSheet(1,340,1110,680);x.restore();
  garageWord(540,1060,lerp(100,180,e(t,18.75,19.45)),e(t,18.75,19.25));
  if(t>19.2)type('بزنیم گاراژ',540,1190,62,e(t,19.2,19.6));
 }
}
const offset=Number(new URLSearchParams(location.search).get('start')||0);window.DUR=T.preview_frames/T.fps-offset;
window.render=t=>master(t+offset);window.render(0);window.READY=true;''')
(p/'index.html').write_text(s)
t=json.loads((p/'timeline.json').read_text());t['preview_frames']=600;t['duration_frames']=600;t['source_map'][0]['output_end_sample']=960000;t['source_map'][0]['source_end_sample']=960000
t['shots']+= [dict(id='accepted-world',start_seconds=10,end_seconds=12),dict(id='open-the-object',start_seconds=12,end_seconds=15.72),dict(id='enter-workshop',start_seconds=15.72,end_seconds=18.55),dict(id='garage-invitation',start_seconds=18.55,end_seconds=20)]
t['milestones'] += [10.5,11.45,12,13.7,15.72,17,18.55,19.2]
t['notes']='Cumulative 0–20s. Exact voice samples 0–959999, unchanged wording/speed. Existing 0–10 picture reused, new section rendered at master time start=10. No voice word timestamps asserted.'
(p/'timeline.json').write_text(json.dumps(t,ensure_ascii=False,indent=2))
