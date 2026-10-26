import adsk.core,adsk.fusion,json,math
OUT=ROOT/'waist_strength';source=app.activeDocument
d=adsk.fusion.Design.cast(app.activeProduct);r=d.rootComponent
TM=adsk.fusion.TemporaryBRepManager.get();P=adsk.core.Point3D;V=adsk.core.Vector3D
def p(a):return P.create(*(x/10 for x in a))
def box(lo,hi):return TM.createBox(adsk.core.OrientedBoundingBox3D.create(p([(a+b)/2 for a,b in zip(lo,hi)]),V.create(1,0,0),V.create(0,1,0),*((b-a)/10 for a,b in zip(lo,hi))))
def inter(t,b):TM.booleanOperation(t,b,adsk.fusion.BooleanTypes.IntersectionBooleanType);return t
wg=next(o for o in r.occurrences if o.component.name=='Waist_layout_v15')
shells=[(b.name,TM.copy(b))for o in wg.component.occurrences if o.component.name.startswith(('W02','W03'))for b in o.createForAssemblyContext(wg).bRepBodies]
scratch=app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
sd=adsk.fusion.Design.cast(app.activeProduct);sd.designType=adsk.fusion.DesignTypes.DirectDesignType
rows=[]
def props(t,info):
 if t.volume<=1e-12:return
 b=sd.rootComponent.bRepBodies.add(t)
 try:
  pp=b.getPhysicalProperties(adsk.fusion.CalculationAccuracy.HighCalculationAccuracy)
  info.update(volume_mm3=pp.volume*1000,mass=pp.mass,com_mm=[v*10 for v in pp.centerOfMass.asArray()],inertia_kgcm2=pp.getXYZMomentsOfInertia(),min_mm=[v*10 for v in b.boundingBox.minPoint.asArray()],max_mm=[v*10 for v in b.boundingBox.maxPoint.asArray()])
  assert pp.mass>0
  rows.append(info)
 finally:b.deleteMe()
try:
 for axis,values in [('x',[0,15,30,45,52,60,75]),('z',[850,865,870,871.5,873.5,875.5,877,880,887])]:
  for value in values:
   lo=[-200,-100,700];hi=[200,150,920];i=0 if axis=='x'else 2;lo[i]=value-.1;hi[i]=value+.1
   for name,b in shells:props(inter(TM.copy(b),box(lo,hi)),dict(kind='global',axis=axis,position_mm=value,body=name,thickness_mm=.2))
 # Motor rear plate in coordinates with pitch axis along X, motor centre at origin.
 for name,b in shells:
  t=TM.copy(b);tr=adsk.core.Matrix3D.create();tr.translation=V.create(-5.2,-2.3343134,-79.86);TM.transform(t,tr)
  rot=adsk.core.Matrix3D.create();rot.setToRotation(math.radians(-25),V.create(0,1,0),P.create(0,0,0));TM.transform(t,rot)
  # limit to motor-contact disc so surrounding loft is not counted as seat.
  disc=TM.createCylinderOrCone(p((-31.6,0,0)),5.5,p((-31.4,0,0)),5.5)
  props(inter(t,disc),dict(kind='hip_seat',axis='local_x',position_mm=-31.5,body=name,thickness_mm=.2))
 for name,b in shells:
  disc=TM.createCylinderOrCone(p((0,23.343134,873.4)),3.9,p((0,23.343134,873.6)),3.9)
  props(inter(TM.copy(b),disc),dict(kind='yaw_seat',axis='z',position_mm=873.5,body=name,thickness_mm=.2))
finally:
 scratch.close(False);source.activate()
(OUT/'sections_verified.json').write_text(json.dumps({'source':source.name,'sections':rows},indent=2))
result={'sections':len(rows),'file':str(OUT/'sections_verified.json')}
