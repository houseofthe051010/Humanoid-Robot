import adsk.core, adsk.fusion, json, math, time
from pathlib import Path
OUT=Path(ROOT)/'v32'
doc=next(x for x in app.documents if x.name=='Humanoid_complete_v32')
doc.activate()
d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'))
assert d.designType==adsk.fusion.DesignTypes.ParametricDesignType
root=d.rootComponent
TM=adsk.fusion.TemporaryBRepManager.get(); BT=adsk.fusion.BooleanTypes
P3=adsk.core.Point3D; V3=adsk.core.Vector3D; M3=adsk.core.Matrix3D
Y=23.343134; PX=46.80800685869137; PZ=854.6; RX=120.; RZ=783.6
C=math.cos(math.radians(25)); S=math.sin(math.radians(25))
def pt(a): return P3.create(*(x/10 for x in a))
def bounds(b):
 q=b.preciseBoundingBox if hasattr(b,'preciseBoundingBox') else b.boundingBox
 return [[x*10 for x in p.asArray()] for p in (q.minPoint,q.maxPoint)]
def bx(a,b):
 return TM.createBox(adsk.core.OrientedBoundingBox3D.create(pt([(x+y)/2 for x,y in zip(a,b)]),V3.create(1,0,0),V3.create(0,1,0),*((y-x)/10 for x,y in zip(a,b))))
def cy(a,b,r): return TM.createCylinderOrCone(pt(a),r/10,pt(b),r/10)
def un(a,*bs):
 for b in bs: assert TM.booleanOperation(a,b,BT.UnionBooleanType)
 return a
def sub(a,b): assert TM.booleanOperation(a,b,BT.DifferenceBooleanType); return a
def ix(a,b): assert TM.booleanOperation(a,b,BT.IntersectionBooleanType); return a
def transform(b,m): assert TM.transform(b,m); return b
def rotate(b,p,axis,angle):
 m=M3.create(); assert m.setToRotation(angle,V3.create(*axis),pt(p)); return transform(b,m)
def exact(name):
 rows=[o for o in root.allOccurrences if o.component.name==name]
 assert len(rows)==1,(name,len(rows)); return rows[0]
def add(c,b,name,appearance=None):
 assert b and b.isSolid and b.volume>0,name
 bf=c.features.baseFeatures.add(); assert bf.startEdit()
 try: c.bRepBodies.add(b,bf)
 finally: bf.finishEdit()
 nb=bf.bodies.item(0); nb.name=name
 if appearance: nb.appearance=appearance
 return nb
def replace_world(o,rows,description=None):
 old=list(o.component.bRepBodies)
 ap=old[0].appearance if old else None
 inv=o.transform2.copy(); inv.invert()
 for b in old: o.component.features.removeFeatures.add(b)
 out=[]
 for name,shape in rows: out.append(add(o.component,transform(TM.copy(shape),inv),name,ap))
 if description: o.component.description=description
 return out
def new_part(owner,name,shape,description='',appearance=None):
 existing=[o for o in root.allOccurrences if o.component.name==name]
 if existing:
  assert len(existing)==1; o=existing[0]
  bodies=replace_world(o,[(name,shape)],description)
  if appearance:
   for b in bodies:b.appearance=appearance
  return o
 g=exact(owner); native=g.component.occurrences.addNewComponent(M3.create())
 native.component.name=name; native.component.partNumber=name; native.component.description=description
 native.isGroundToParent=True
 o=native.createForAssemblyContext(g) if g.assemblyContext else native
 inv=o.transform2.copy();inv.invert(); add(o.component,transform(TM.copy(shape),inv),name,appearance)
 return o
def color(name,rgb):
 ap=d.appearances.itemByName(name)
 if not ap: ap=d.appearances.addByCopy(d.appearances.item(0),name)
 for key in ('opaque_albedo','generic_diffuse'):
  p=adsk.core.ColorProperty.cast(ap.appearanceProperties.itemById(key))
  if p: p.value=adsk.core.Color.create(*rgb,255); break
 return ap
def beam(a,b,width,depth):
 u=V3.create(*[b[i]-a[i] for i in range(3)]); length=u.length; u.normalize()
 v=V3.create(1,0,0)
 if abs(u.dotProduct(v))>.99: v=V3.create(0,1,0)
 dot=u.dotProduct(v); v.subtract(V3.create(u.x*dot,u.y*dot,u.z*dot));v.normalize()
 return TM.createBox(adsk.core.OrientedBoundingBox3D.create(pt([(a[i]+b[i])/2 for i in range(3)]),u,v,length/10,width/10,depth/10))
def capsule_xz(a,b,r,y0,y1):
 out=un(cy((a[0],y0,a[1]),(a[0],y1,a[1]),r),cy((b[0],y0,b[1]),(b[0],y1,b[1]),r))
 return un(out,beam((a[0],(y0+y1)/2,a[1]),(b[0],(y0+y1)/2,b[1]),2*r,y1-y0))
def nominal_pitch(side,t=0,a=0,b=0): return (side*(PX+C*t+S*b),Y+a,PZ-S*t+C*b)
def nominal_roll(side,a): return (side*RX,Y+a,RZ)
def pitch_cyl(side,a,b,r): return cy(nominal_pitch(side,a),nominal_pitch(side,b),r)

def pitch_box(side,t0,t1,a0=-400,a1=400,b0=-400,b1=400):
 return TM.createBox(adsk.core.OrientedBoundingBox3D.create(pt(nominal_pitch(side,(t0+t1)/2,(a0+a1)/2,(b0+b1)/2)),V3.create(side*C,0,-S),V3.create(0,1,0),(t1-t0)/10,(a1-a0)/10,(b1-b0)/10))
def roll_cyl(side,a,b,r): return cy(nominal_roll(side,a),nominal_roll(side,b),r)
def placement(side):
 prefix='Left' if side<0 else 'Right'
 hc=exact(prefix+'_H07_Pitch_tube_recessed_endcaps')
 front=next(b for b in hc.bRepBodies if 'front' in b.name)
 circles=[adsk.core.Cylinder.cast(f.geometry) for f in front.faces]
 circles=[x for x in circles if x and abs(x.radius*10-57)<1e-4]
 q=circles[0]; u=q.axis.copy()
 if u.x*side<0:u.scaleBy(-1)
 origin=q.origin.copy(); off=u.copy();off.scaleBy(-22.5/10);origin.translateBy(off)
 cap=exact(prefix+'_H06_Roll_tube_recessed_endcaps')
 axes=[adsk.core.Cylinder.cast(f.geometry) for f in cap.bRepBodies.item(0).faces]
 v=next(x.axis.copy() for x in axes if x and abs(x.radius*10-57)<1e-4)
 if v.y<0:v.scaleBy(-1)
 v.normalize(); w=u.crossProduct(v);w.scaleBy(side);w.normalize()
 m=M3.create();assert m.setToAlignCoordinateSystems(pt(nominal_pitch(side)),V3.create(side*C,0,-S),V3.create(0,1,0),V3.create(side*S,0,C),origin,u,v,w)
 return m
def placed(body,side): return transform(body,placement(side))
def save_view(name,center=(0,28,820),eye=(2000,-3800,2100),extent=950):
 app.userInterface.activeSelections.clear()
 cam=app.activeViewport.camera;cam.isFitView=False;cam.isSmoothTransition=False
 cam.target=pt(center);cam.eye=pt(eye);cam.upVector=V3.create(0,0,1)
 cam.cameraType=adsk.core.CameraTypes.OrthographicCameraType;cam.viewExtents=extent/10
 app.activeViewport.camera=cam;app.activeViewport.refresh();adsk.doEvents()
 path=OUT/(name+'.png'); assert app.activeViewport.saveAsImageFile(str(path),1800,1400)
 return str(path)
def journal(name,value): (OUT/(name+'.json')).write_text(json.dumps(value,indent=2),encoding='utf-8')
def separate_lumps(body):
 pieces=[]
 for ii in range(body.lumps.count):
  cp=TM.copy(body);drop=[]
  for jj in range(cp.lumps.count):
   if jj!=ii:
    for shell in cp.lumps.item(jj).shells:drop.extend(list(shell.faces))
  if drop:assert TM.deleteFaces(drop,True)
  pieces.append(cp)
 return pieces
def loft_round_xy(rows,name):
 stage=exact('V30_construction_reference');c=stage.component
 inp=c.features.loftFeatures.createInput(adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
 for i,(z,xh,y0,y1,r) in enumerate(rows):
  pi=c.constructionPlanes.createInput();pi.setByOffset(c.xYConstructionPlane,adsk.core.ValueInput.createByReal(z/10))
  plane=c.constructionPlanes.add(pi);plane.isLightBulbOn=False
  sk=c.sketches.add(plane);sk.name=name+'_section_'+str(i);sk.isComputeDeferred=True
  points=[(-xh+r,y0,0),(xh-r,y0,0),(xh,y0+r,0),(xh,y1-r,0),(xh-r,y1,0),(-xh+r,y1,0),(-xh,y1-r,0),(-xh,y0+r,0)]
  centers=[(xh-r,y0+r,0),(xh-r,y1-r,0),(-xh+r,y1-r,0),(-xh+r,y0+r,0)]
  for k in range(8):
   a,b=points[k],points[(k+1)%8]
   if k%2==0:sk.sketchCurves.sketchLines.addByTwoPoints(pt(a),pt(b))
   else:
    q=centers[k//2];mid=(q[0]+(a[0]+b[0]-2*q[0])/math.sqrt(2),q[1]+(a[1]+b[1]-2*q[1])/math.sqrt(2),0)
    sk.sketchCurves.sketchArcs.addByThreePoints(pt(a),pt(mid),pt(b))
  sk.isComputeDeferred=False;sk.isLightBulbOn=False
  assert sk.profiles.count==1,(name,i,sk.profiles.count);inp.loftSections.add(sk.profiles.item(0))
 inp.isSolid=True;feature=c.features.loftFeatures.add(inp);feature.name=name
 return TM.copy(feature.bodies.item(0))
