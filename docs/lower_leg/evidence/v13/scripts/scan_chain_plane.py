exec(compile((ROOT/'v13/common.py').read_text(),'<common>','exec'))
env=TM.copy(parts['V13_Chain_clearance_ENVELOPE'].component.bRepBodies.item(0));report=[]
for x in [-27,-28,-29,-30,-31,-32,-33]:
 e=trans(TM.copy(env),dx=x+24);hits=[]
 for name in ['S05_Continuous_oval_steel_rail_L','P01_Knee_side_rail_seat_L','N04_Knee_pillow_block_L','N01_Aluminum_knee_stack_1','N06_Upper_leg_oval_stub_L']:
  for b in parts[name].component.bRepBodies:
   q=TM.copy(e);assert TM.booleanOperation(q,TM.copy(b),BT.IntersectionBooleanType)
   v=q.volume*1000 if q.isSolid else 0
   if v>.01:hits.append({'part':name,'body':b.name,'mm3':v})
 report.append({'plane_x_mm':x,'hits':hits})
(OUT/'chain_plane_scan.json').write_text(json.dumps(report,indent=2));result=report
