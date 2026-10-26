exec(compile((ROOT/'v21/common.py').read_text(),'<common>','exec'))
cfg=json.loads((OUT/'upper_layout.json').read_text())
report={'document':doc.name,'parts':[],'interferences':[],'joint_counts':{}}
for go in (right,left,wg):
 c=go.component
 report['joint_counts'][c.name]={'count':c.asBuiltJoints.count,'invalid':[j.name for j in c.asBuiltJoints if not j.isValid]}
 assert not report['joint_counts'][c.name]['invalid']
ps={o.component.partNumber:o.createForAssemblyContext(wg) for o in wg.component.occurrences}
for key,o in ps.items():
 if key.startswith(('U','W07','W08','W16')):
  for b in o.bRepBodies:
   row={'part':key,'body':b.name,'solid':b.isSolid,'volume_mm3':b.volume*1000,'bounds_mm':bounds(b),'outer_shells':sum(not s.isVoid for s in b.shells)}
   report['parts'].append(row)
   assert b.isSolid and b.volume>0 and row['outer_shells']==1,row
sp=getpart(wg,'W08_').createForAssemblyContext(wg).bRepBodies.item(0)
bb=bounds(sp);size=[bb[1][i]-bb[0][i] for i in range(3)]
assert max(abs(a-b) for a,b in zip(size[:2],[18,10]))<.01,size
assert abs(bb[1][2]-(cfg['ground_z_mm']+1400.2))<.01,bb
report['spine_dimensions_mm']=size
bat=getpart(wg,'U01_').createForAssemblyContext(wg).bRepBodies.item(0)
bb=bounds(bat);size=[bb[1][i]-bb[0][i] for i in range(3)]
assert max(abs(a-b) for a,b in zip(size,[140,85,160]))<.01,size
report['battery_dimensions_mm']=size
def overlap(a,b):
 q,r=a.boundingBox,b.boundingBox
 return all(min(getattr(q.maxPoint,k),getattr(r.maxPoint,k))-max(getattr(q.minPoint,k),getattr(r.minPoint,k))>1e-6 for k in ('x','y','z'))
def volume(a,b):
 if not overlap(a,b):return 0.0
 t=TM.copy(a)
 assert TM.booleanOperation(t,TM.copy(b),BT.IntersectionBooleanType),'Intersection failed'
 return t.volume*1000
# The battery must clear every existing waist component and its new supports.
for key,o in ps.items():
 if key.startswith(('U01','U06')):continue
 for b in o.bRepBodies:
  v=volume(bat,b)
  if v>.001:report['interferences'].append({'first':'U01','second':key,'body':b.name,'volume_mm3':v})
# New cradle pieces, spine and fastener references must also fit one another.
selected=[(k,b) for k,o in ps.items() if k.startswith(('U02','U03','U04','U05','W08')) for b in o.bRepBodies]
for i,(ka,a) in enumerate(selected):
 for kb,b in selected[i+1:]:
  v=volume(a,b)
  if v>.001:report['interferences'].append({'first':ka,'second':kb,'body_a':a.name,'body_b':b.name,'volume_mm3':v})
report['sketches']=[s.name for s in getpart(wg,'U06_').component.sketches]
assert len(report['sketches'])==3
report['height_mm']=cfg['height_mm']
report['pass']=not report['interferences']
(OUT/'validation.json').write_text(json.dumps(report,indent=2))
assert report['pass'],report['interferences']
result=report
