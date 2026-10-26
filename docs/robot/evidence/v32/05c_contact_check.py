exec(compile((ROOT/'v32/common32.py').read_text(),'<common32>','exec'))
rows=[]
for prefix,xc in (('Left',-120),('Right',120)):
 frames=[TM.copy(b) for n in (prefix+'_S06_Dual_7010_motor_carrier',prefix+'_S05_Continuous_oval_steel_rail_L',prefix+'_S05_Continuous_oval_steel_rail_R') for b in exact(n).bRepBodies]
 for dx in (-10,10):
  for z in (244,314,366):
   plate=exact('C27_'+prefix+'_shin_front'+('_upper' if z>244 else '')).bRepBodies.item(0)
   region=cy((xc+dx,-8,z),(xc+dx,3.1,z),5.01);ix(region,TM.copy(plate))
   m=M3.create();m.translation=V3.create(0,.002,0);transform(region,m)
   contact=0
   for f in frames:
    q=TM.copy(region);ix(q,TM.copy(f));contact+=q.volume*1000
   row=dict(part=prefix,x=xc+dx,z=z,inward_probe_mm=.02,contact_probe_volume_mm3=contact)
   rows.append(row)
journal('mount_contact32',dict(pass_=all(r['contact_probe_volume_mm3']>.001 for r in rows),records=rows,scope='A 0.02 mm inward virtual probe at each mount intersects its unchanged carrier/rail mating surface, confirming geometric seating. Not preload or strength qualification.'))
assert all(r['contact_probe_volume_mm3']>.001 for r in rows),rows
result=dict(pass_=True,mounts_checked=len(rows))
