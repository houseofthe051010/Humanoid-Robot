exec(compile((ROOT/'v32/common32.py').read_text(),'<common32>','exec'))
exec(compile((ROOT/'v32/capture32.py').read_text(),'<capture32>','exec'))
d.activateRootComponent()
journal('prechange_pose32',capture(d))
parts=[]
for o in root.allOccurrences:
 if not o.isVisible or not (o.component.name.startswith('Left_') or o.component.name=='C28_Right_hip_yaw_shroud'):continue
 if not any(k in o.component.name for k in ('S06','S05','S01','P05','P15','N06','T02','T01','H01_Steel','hip_yaw_shroud')):continue
 for b in o.bRepBodies:
  cs=[]
  for f in b.faces:
   c=adsk.core.Cylinder.cast(f.geometry)
   if c:cs.append(dict(origin=[v*10 for v in c.origin.asArray()],axis=c.axis.asArray(),radius=c.radius*10))
  parts.append(dict(part=o.component.name,body=b.name,bounds=bounds(b),cylinders=cs))
journal('interfaces32',parts)
exact('Casings').isLightBulbOn=False
save_view('bare_shin32',(120,20,255),(1700,-2800,1100),450)
save_view('bare_thigh32',(120,20,590),(1800,-3300,1450),440)
exact('Casings').isLightBulbOn=True
save_view('before_lower_covers32',(0,20,455),(1200,-3300,1100),870)
result=dict(document=doc.name,parts=len(parts))
