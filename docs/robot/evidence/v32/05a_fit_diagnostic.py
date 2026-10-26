exec(compile((ROOT/'v32/common32.py').read_text(),'<common32>','exec'))
rows=[]
for prefix in ('Left','Right'):
 for suffix,other in (('hip_yaw_shroud',prefix+'_Q02_CNC_yaw_to_roll_cradle'),):
  o=exact('C28_'+prefix+'_'+suffix)
  for b in o.bRepBodies:
   for ob in exact(other).bRepBodies:
    q=TM.copy(b);ix(q,TM.copy(ob))
    if q.volume>0:rows.append(dict(part=o.component.name,overlap=bounds(q),volume=q.volume*1000))
 for dx in (-10,10):
  for z in (244,314,366):
   x=(-120 if prefix=='Left' else 120)+dx
   test=cy((x,-4,z),(x,-3.9,z),5);ix(test,TM.copy(exact(prefix+'_S06_Dual_7010_motor_carrier').bRepBodies.item(0)))
   rows.append(dict(contact_mount=[prefix,dx,z],carrier_contact_area_mm2=test.volume*10000))
 for b in exact(prefix+'_S05_Continuous_oval_steel_rail_L').bRepBodies:
  q=TM.copy(b);ix(q,TM.copy(exact('C27_'+prefix+'_shin_front').bRepBodies.item(0)))
  if q.volume>0:rows.append(dict(rail_interference=bounds(q),volume=q.volume*1000))
journal('fit_diagnostic32',rows);result=rows
