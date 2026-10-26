"""Bodyweight-only beam sensitivity screen. N, mm, MPa. No FEA or CAD edits."""
from pathlib import Path
import math,json
D=8.0; E=200000.0; SY=250.0; W=90*4.4482216152605
I=math.pi*D**4/64; Z=math.pi*D**3/32
geometry={'Ankle roll':(39.0,21.0),'Ankle pitch':(74.3,28.0),'Knee':(86.3,42.0)}
out={'weight_N':W,'diameter_mm':D,'E_MPa':E,'assumed_yield_MPa':SY,'shafts':{}}
for name,(L,b) in geometry.items():
 a=(L-b)/2
 rows=[]
 for multiple in [0.5,1,3,5]:
  F=W*multiple
  edge=F*a/2/Z
  uniform=F*(2*L-b)/8/Z
  point=F*L/4/Z
  rows.append({'bodyweight_multiple':multiple,'total_joint_force_N':F,
   'edge_bending_MPa':edge,'uniform_bending_MPa':uniform,'center_point_bending_MPa':point,
   'edge_bare_shaft_deflection_mm':F*a*(3*L**2-4*a**2)/(48*E*I),
   'uniform_bare_shaft_deflection_mm':F*(8*L**3-4*L*b*b+b**3)/(384*E*I),
   'ideal_stiff_block_stub_deflection_mm':F/2*a**3/(3*E*I),
   'max_transverse_shear_MPa':4*(F/2)/(3*math.pi*D*D/4),
   'edge_yield_ratio':SY/edge,'uniform_yield_ratio':SY/uniform})
 peak=rows[-1]
 out['shafts'][name]={'race_center_span_mm':L,'load_block_width_mm':b,'edge_arm_mm':a,'cases':rows,
  'diameter_for_5BW_factor2_edge_mm':D*(2*peak['edge_bending_MPa']/SY)**(1/3),
  'diameter_for_5BW_factor2_uniform_mm':D*(2*peak['uniform_bending_MPa']/SY)**(1/3)}
out['limitations']=['Bare smooth shaft; no collar/composite stiffness credit.',
 'Symmetric transverse loads only, roll center offset 0.025 mm neglected.',
 '250 MPa is an assumption, not certification of the purchased shaft.',
 'Actuator forces, joint moments, axial loading, fatigue and contact compliance excluded.',
 'Models are sensitivity cases, not rigorous bounds on the actual contact assembly.',
 'Elastic deflections above yield are extrapolations, not permanent-set predictions.']
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
for name,s in out['shafts'].items():
 print(name,'L/b/a',s['race_center_span_mm'],s['load_block_width_mm'],s['edge_arm_mm'])
 for r in s['cases']:
  print(r['bodyweight_multiple'],*[round(r[k],3) for k in ['edge_bending_MPa','uniform_bending_MPa','center_point_bending_MPa','uniform_bare_shaft_deflection_mm','ideal_stiff_block_stub_deflection_mm']])
 print('factor2 diameters',s['diameter_for_5BW_factor2_edge_mm'],s['diameter_for_5BW_factor2_uniform_mm'])
