import adsk.core,adsk.fusion,json,math
OUT=ROOT/'v14';doc=next(x for x in app.documents if x.name=='Bilateral_legs_v14');doc.activate();d=adsk.fusion.Design.cast(app.activeProduct);root=d.rootComponent
TM=adsk.fusion.TemporaryBRepManager.get();BT=adsk.fusion.BooleanTypes;P3=adsk.core.Point3D;V3=adsk.core.Vector3D
def pt(a):return P3.create(*(v/10 for v in a))
def cy(p,q,r):return TM.createCylinderOrCone(pt(p),r/10,pt(q),r/10)
def bx(lo,hi):return TM.createBox(adsk.core.OrientedBoundingBox3D.create(pt([(a+b)/2 for a,b in zip(lo,hi)]),V3.create(1,0,0),V3.create(0,1,0),*((b-a)/10 for a,b in zip(lo,hi))))
def boolean(a,b,op):assert TM.booleanOperation(a,b,op);return a
def un(a,b):return boolean(a,b,BT.UnionBooleanType)
def sub(a,b):return boolean(a,b,BT.DifferenceBooleanType)
def oval(x,z0,z1,r):return un(un(bx((x-4,6-r,z0),(x+4,6+r,z1)),cy((x-4,6,z0),(x-4,6,z1),r)),cy((x+4,6,z0),(x+4,6,z1),r))
report={'chain_analysis_performed':False,'knee_z_mm':430.6,'legs':{}}
for go in root.occurrences:
 side=go.component.name.removesuffix('_leg');sgn=1 if side=='Right'else -1;g=go.component;parts={o.component.partNumber:o.createForAssemblyContext(go)for o in g.occurrences}
 cparts={o.component.partNumber:o for o in g.occurrences}
 tr=adsk.core.Matrix3D.create();tr.setCell(0,0,sgn);tr.translation=V3.create(sgn*13,0,0)
 stack=None
 for n,o in parts.items():
  if n.startswith('N01'):
   for b in o.bRepBodies:stack=TM.copy(b)if stack is None else un(stack,TM.copy(b))
 probes=[]
 for x in [-10,10]:
  for z in [395,405,420,428]:
   ring=sub(oval(x,z,z+.1,5.6),oval(x,z-.1,z+.2,5.15));assert TM.transform(ring,tr);sub(ring,TM.copy(stack));missing=ring.volume*1000
   probes.append({'tube_x':x,'z':z,'missing_enclosing_material_mm3':missing})
 tubes={n:[o.bRepBodies.item(0).boundingBox.minPoint.z*10,o.bRepBodies.item(0).boundingBox.maxPoint.z*10]for n,o in parts.items()if n.startswith('S05')}
 overlaps=[]
 for n,o in parts.items():
  if n.startswith('S05'):
   cp=TM.copy(o.bRepBodies.item(0));boolean(cp,TM.copy(stack),BT.IntersectionBooleanType);overlaps.append({'tube':n,'adapter_overlap_mm3':cp.volume*1000})
 j=g.asBuiltJoints.itemByName(side+'_Knee_pitch').createForAssemblyContext(go);samples=[]
 try:
  for angle in [0,30]:
   j.jointMotion.rotationValue=math.radians(angle);adsk.doEvents();m=parts['N04_Knee_pillow_block_L'].transform2
   expected=adsk.core.Matrix3D.create();expected.setToRotation(math.radians(angle),V3.create(1,0,0),P3.create(0,2.3343134,43.06))
   samples.append({'angle':angle,'matrix_error':max(abs(a-b)for a,b in zip(m.asArray(),expected.asArray())),'motor_follow_error':max(abs(a-b)for a,b in zip(m.asArray(),parts['P03_Circular_motor_gearbox_case'].transform2.asArray()))})
 finally:j.jointMotion.rotationValue=0;adsk.doEvents()
 invalid=[j.name for j in g.asBuiltJoints if not j.isValid]
 health=[{'component':o.component.name,'feature':f.name,'message':f.errorOrWarningMessage}for o in cparts.values()for f in o.component.features if f.healthState!=adsk.fusion.FeatureHealthStates.HealthyFeatureHealthState]
 report['legs'][side]={'enclosure_cross_sections':probes,'tube_bounds_z_mm':tubes,'tube_fit':overlaps,'knee_motion':samples,'invalid_joints':invalid,'feature_issues':health,'joint_count':g.asBuiltJoints.count}
(OUT/'validation.json').write_text(json.dumps(report,indent=2))
for r in report['legs'].values():
 assert max(x['missing_enclosing_material_mm3']for x in r['enclosure_cross_sections'])<.001,r
 assert max(x['adapter_overlap_mm3']for x in r['tube_fit'])<.001,r
 assert all(abs(a-69)<1e-6 and abs(b-430.6)<1e-6 for a,b in r['tube_bounds_z_mm'].values()),r
 assert not r['invalid_joints'] and not r['feature_issues'],r
 assert max(x['matrix_error']for x in r['knee_motion'])<1e-6 and max(x['motor_follow_error']for x in r['knee_motion'])<1e-6,r
result=report
