import numpy as np, math, json
from pathlib import Path
OUT=Path(__file__).parent
def rx(a):
 c,s=np.cos(a),np.sin(a);return np.array([[1,0,0],[0,c,-s],[0,s,c]])
def ry(a):
 c,s=np.cos(a),np.sin(a);return np.array([[c,0,s],[0,1,0],[-s,0,c]])
P=np.array([0.,0.,27.])
def solve(config,p=0,r=0):
 b,by,bz,my,mz,cr,th=config;R=ry(r);T=R@rx(p);out=[]
 for s in (-1,1):
  B=np.array([s*b,by,bz]);M=np.array([s*b,my,mz]);a0=M+np.array([0,cr*np.cos(th),cr*np.sin(th)])
  L=np.linalg.norm(a0-B);q=R.T@B-P;q=rx(p).T@q+P
  v=q-M;rho=np.linalg.norm(v[1:]);value=(np.dot(v,v)+cr*cr-L*L)/(2*cr*rho)
  if abs(value)>1:return None
  alpha=np.arctan2(v[2],v[1]);acos=np.arccos(value)
  candidates=[alpha+acos,alpha-acos];theta=min(candidates,key=lambda t:abs((t-th+np.pi)%(2*np.pi)-np.pi))
  A=R@(P+rx(p)@(M-P+np.array([0,cr*np.cos(theta),cr*np.sin(theta)])))
  n=(A-B)/L; axis=T@np.array([1.,0,0]);tilts=[np.degrees(np.arcsin(np.clip(abs(n[0]),0,1))),np.degrees(np.arcsin(np.clip(abs(n@axis),0,1)))]
  out.append(dict(theta=theta,L=L,A=A.tolist(),B=B.tolist(),tilts=tilts))
 return out
def jac(config,p=0,r=0):
 eps=1e-5;cols=[]
 for dp,dr in ((eps,0),(0,eps)):
  aa=solve(config,p+dp,r+dr);bb=solve(config,p-dp,r-dr)
  if aa is None or bb is None:return None
  cols.append([((a['theta']-b['theta']+np.pi)%(2*np.pi)-np.pi)/(2*eps) for a,b in zip(aa,bb)])
 return np.array(cols).T
if __name__=='__main__':
 best=[]
 for b in (26,28,30,32):
  for mz in (65,70,75,80):
   for cr in (18,20,22,24):
    for th in np.radians((160,170,180,190,200)):
     c=(b,-30,8,-10,mz,cr,th);a=solve(c);J=jac(c)
     if min(v['L'] for v in a)<65 or np.min(abs(J))<1 or np.max(abs(J))>2:continue
     poses=[(-30,0),(30,0),(0,-30),(0,30),(-15,-15),(15,15),(-15,15),(15,-15)];valid=True;ratios=[];tilts=[]
     for p,r in poses:
      pose=solve(c,*np.radians([p,r]));jj=jac(c,*np.radians([p,r]))
      if pose is None or jj is None:valid=False;break
      ratios.extend(abs(jj).ravel());tilts.extend([t for v in pose for t in v['tilts']])
     if valid:best.append((mz+max(tilts)*.05,c,dict(neutral=a,J=J.tolist(),corner_ratio=[min(ratios),max(ratios)],tilt_max=max(tilts))))
 best.sort(key=lambda a:a[0]);chosen=best[0] if best else None
 print(json.dumps(best[:5],indent=2));(OUT/'waist_linkage_screen.json').write_text(json.dumps(best[:30],indent=2))
