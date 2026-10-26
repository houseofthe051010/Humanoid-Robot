import adsk.core,adsk.fusion,json,math,time
OUT=ROOT/'v15';doc=next(x for x in app.documents if x.name=='Legs_and_waist_v15');doc.activate();d=adsk.fusion.Design.cast(app.activeProduct);root=d.rootComponent
TM=adsk.fusion.TemporaryBRepManager.get();BT=adsk.fusion.BooleanTypes;OP=adsk.fusion.FeatureOperations;P3=adsk.core.Point3D;V3=adsk.core.Vector3D;V=adsk.core.ValueInput
Y=23.343134;Z=560.
def pt(a):return P3.create(*(v/10 for v in a))
def obj(items):
 o=adsk.core.ObjectCollection.create()
 for x in items:o.add(x)
 return o
def cy(p,q,r):return TM.createCylinderOrCone(pt(p),r/10,pt(q),r/10)
def bx(lo,hi):return TM.createBox(adsk.core.OrientedBoundingBox3D.create(pt([(a+b)/2 for a,b in zip(lo,hi)]),V3.create(1,0,0),V3.create(0,1,0),*((b-a)/10 for a,b in zip(lo,hi))))
def boolean(a,b,op):assert TM.booleanOperation(a,b,op);return a
def un(a,*bs):
 for b in bs:boolean(a,b,BT.UnionBooleanType)
 return a
def sub(a,b):return boolean(a,b,BT.DifferenceBooleanType)
def ix(a,b):return boolean(a,b,BT.IntersectionBooleanType)
def oval(x,z0,z1,r):return un(bx((x-r,Y-4,z0),(x+r,Y+4,z1)),cy((x,Y-4,z0),(x,Y-4,z1),r),cy((x,Y+4,z0),(x,Y+4,z1),r))
def trans(b,dx=0,dy=0,dz=0):
 m=adsk.core.Matrix3D.create();m.translation=V3.create(dx/10,dy/10,dz/10);assert TM.transform(b,m);return b
def place(b,sgn=1):
 m=adsk.core.Matrix3D.create();m.setCell(0,0,sgn);m.translation=V3.create(sgn*13,0,0);assert TM.transform(b,m);return b
def addtemp(c,b,name,ap=None):
 bf=c.features.baseFeatures.add();bf.name=name;bf.startEdit();c.bRepBodies.add(b,bf);bf.finishEdit();nb=bf.bodies.item(0);nb.name=name
 if ap:nb.appearance=ap
 return nb
def replace(c,bs,name,description=None):
 old=list(c.bRepBodies);ap=old[0].appearance
 for b in old:c.features.removeFeatures.add(b)
 if not isinstance(bs,list):bs=[(name,bs)]
 for bn,b in bs:addtemp(c,b,bn,ap)
 if description:c.description=description
 return c
def factory():
 n='ZZ_V15_construction_lofts_NOT_A_PART'
 o=next((o for o in root.occurrences if o.component.name==n),None)
 if not o:o=root.occurrences.addNewComponent(adsk.core.Matrix3D.create());o.component.name=n
 o.isLightBulbOn=False;return o.component
def loft(axis,rows,name,center=(Y,Z)):
 c=factory();li=c.features.loftFeatures.createInput(OP.NewBodyFeatureOperation)
 for i,(coord,ra,rb)in enumerate(rows):
  base=c.yZConstructionPlane if axis=='x'else c.xYConstructionPlane;idx=0 if axis=='x'else 2
  pi=c.constructionPlanes.createInput();pi.setByOffset(base,V.createByReal(coord/10*base.geometry.normal.asArray()[idx]));pl=c.constructionPlanes.add(pi);pl.isLightBulbOn=False
  sk=c.sketches.add(pl);sk.name=name+'_section_'+str(i)
  if axis=='x':p=(coord,center[0],center[1]);a=(coord,center[0]+ra,center[1]);b=(coord,center[0],center[1]+rb)
  else:p=(center[0],center[1],coord);a=(center[0]+ra,center[1],coord);b=(center[0],center[1]+rb,coord)
  if ra<rb:a,b=b,a
  sk.sketchCurves.sketchEllipses.add(sk.modelToSketchSpace(pt(p)),sk.modelToSketchSpace(pt(a)),sk.modelToSketchSpace(pt(b)))
  li.loftSections.add(sk.profiles.item(0));sk.isLightBulbOn=False
 f=c.features.loftFeatures.add(li);f.name=name;assert f.bodies.count==1
 return TM.copy(f.bodies.item(0))
def groups():return [(o,1 if o.component.name=='Right_leg'else -1)for o in root.occurrences if o.component.name in ['Right_leg','Left_leg']]
def progress(s):(OUT/'progress.json').write_text(json.dumps({'stage':s,'time':time.time()}))
