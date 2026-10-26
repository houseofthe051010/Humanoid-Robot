import math,json
import numpy as np
from pathlib import Path
OUT=Path(__file__).parent
def rx(a):
 c,s=np.cos(a),np.sin(a);return np.array([[1,0,0],[0,c,-s],[0,s,c]])
def ry(a):
 c,s=np.cos(a),np.sin(a);return np.array([[c,0,s],[0,1,0],[-s,0,c]])
# Frame origin lower pitch joint; 15 mm rearward move leaves link anchors and
# motor/crank centers in their original world locations.
P=np.array([0.,0.,27.]);theta0=np.radians(160);cr=26
def solve(p=0,r=0):
 R=rx(p);T=R@ry(r);out=[]
 for s in (-1,1):
  B=np.array([s*30.,-45.,8.]);M=np.array([s*30.,-25.,68.])
  a0=M+np.array([0,cr*np.cos(theta0),cr*np.sin(theta0)]);L=np.linalg.norm(a0-B)
  q=ry(r).T@(R.T@B-P)+P;v=q-M;rho=np.linalg.norm(v[1:])
  value=(v@v+cr*cr-L*L)/(2*cr*rho)
  if abs(value)>1:return None
  alpha=np.arctan2(v[2],v[1]);ac=np.arccos(value)
  th=min((alpha+ac,alpha-ac),key=lambda t:abs((t-theta0+np.pi)%(2*np.pi)-np.pi))
  delta=(th-theta0+np.pi)%(2*np.pi)-np.pi
  A=R@(P+ry(r)@(M-P+np.array([0,cr*np.cos(th),cr*np.sin(th)])))
  n=(A-B)/L;axis=T@np.array([1.,0,0])
  tilts=np.degrees(np.arcsin(np.clip([abs(n[0]),abs(n@axis)],0,1)))
  out.append({'delta':float(delta),'tilts':tilts.tolist(),'A':A.tolist(),'B':B.tolist()})
 return out
def valid(p,r):
 a=solve(*np.radians([p,r]))
 return bool(a is not None and max(t for v in a for t in v['tilts'])<=35 and max(abs(np.degrees(v['delta'])) for v in a)<=60)
def jac(p=0,r=0):
 e=1e-5;cols=[]
 for dp,dr in ((e,0),(0,e)):
  a=solve(p+dp,r+dr);b=solve(p-dp,r-dr)
  cols.append([(aa['delta']-bb['delta'])/(2*e) for aa,bb in zip(a,b)])
 return np.array(cols).T
if __name__=='__main__':
 report={'neutral_jacobian_motor_rad_per_waist_rad':jac().tolist(),'pure_axis_kinematic_limits_deg':{},'scope':'Link closure, 35 degree rod-end angular budget and 60 degree crank travel. No physical contact or strength certification.'}
 for i,n in enumerate(('pitch','roll')):
  lim=[]
  for s in (-1,1):
   last=0
   for a in np.arange(.1,60.01,.1):
    q=[0.,0.];q[i]=s*a
    if not valid(*q):break
    last=s*a
   lim.append(round(last,2))
  report['pure_axis_kinematic_limits_deg'][n]=lim
 report['target_poses']={str((p,r)):{'kinematically_valid':valid(p,r),'solution':solve(*np.radians([p,r]))} for p,r in [(0,0),(-30,0),(30,0),(0,-30),(0,30),(-20,-20),(-20,20),(20,-20),(20,20)]}
 (OUT/'kinematics.json').write_text(json.dumps(report,indent=2));print(json.dumps({k:v for k,v in report.items() if k!='target_poses'},indent=2))
