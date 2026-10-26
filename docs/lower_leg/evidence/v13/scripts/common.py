import adsk.core,adsk.fusion,json,math,time
OUT=ROOT/'v13';doc=next(x for x in app.documents if x.name=='Leg_chain_v13_source');doc.activate();d=adsk.fusion.Design.cast(app.activeProduct);root=d.rootComponent
parts={o.component.name:o for o in root.occurrences};TM=adsk.fusion.TemporaryBRepManager.get();BT=adsk.fusion.BooleanTypes;V3=adsk.core.Vector3D;P3=adsk.core.Point3D
Y=23.343134;Z=565.;K=435.6;CHAIN_X=-31.;FACE=7.21
def pt(p):return P3.create(*(v/10 for v in p))
def trans(b,dx=0,dy=0,dz=0):
 m=adsk.core.Matrix3D.create();m.translation=V3.create(dx/10,dy/10,dz/10);assert TM.transform(b,m);return b
def cy(p,q,r):return TM.createCylinderOrCone(pt(p),r/10,pt(q),r/10)
def bx(lo,hi):return TM.createBox(adsk.core.OrientedBoundingBox3D.create(pt([(a+b)/2 for a,b in zip(lo,hi)]),V3.create(1,0,0),V3.create(0,1,0),*((b-a)/10 for a,b in zip(lo,hi))))
def un(a,*bs):
 for b in bs:assert TM.booleanOperation(a,b,BT.UnionBooleanType)
 return a
def sub(a,b):
 assert TM.booleanOperation(a,b,BT.DifferenceBooleanType)
 return a
def ix(a,b):
 assert TM.booleanOperation(a,b,BT.IntersectionBooleanType)
 return a
def oval(x,z0,z1,r=5.1):return un(bx((x-r,Y-4,z0),(x+r,Y+4,z1)),cy((x,Y-4,z0),(x,Y-4,z1),r),cy((x,Y+4,z0),(x,Y+4,z1),r))
def shinoval(x,z0,z1,r=5):return un(bx((x-4,6-r,z0),(x+4,6+r,z1)),cy((x-4,6,z0),(x-4,6,z1),r),cy((x+4,6,z0),(x+4,6,z1),r))
def rrxy(x0,x1,y0,y1,z0,z1,r):
 a=un(bx((x0+r,y0,z0),(x1-r,y1,z1)),bx((x0,y0+r,z0),(x1,y1-r,z1)))
 for x in [x0+r,x1-r]:
  for y in [y0+r,y1-r]:un(a,cy((x,y,z0),(x,y,z1),r))
 return a
def ap(name):
 if name=='orange':return d.appearances.itemByName('v12_sprocket_orange')
 ref='S01_Ankle_to_oval_rail_adapter' if name=='plastic' else 'P01_Knee_side_rail_seat_L'
 return parts[ref].component.bRepBodies.item(0).appearance
def emit(name,bodies,desc=None,material=None,appearance=None):
 if not isinstance(bodies,list):bodies=[(name,bodies)]
 if name in parts:
  c=parts[name].component
  oldap=c.bRepBodies.item(0).appearance if c.bRepBodies.count else ap('aluminum')
  for b in list(c.bRepBodies):b.deleteMe()
 else:
  o=root.occurrences.addNewComponent(adsk.core.Matrix3D.create());c=o.component;c.name=name;c.partNumber=name;parts[name]=o;oldap=ap('aluminum')
 if desc is not None:c.description=desc
 if material is not None:c.attributes.add('SHIN','material',material)
 for bn,b in bodies:
  nb=c.bRepBodies.add(b);nb.name=bn;nb.appearance=appearance or oldap;nb.isLightBulbOn=True
 parts[name].isLightBulbOn=True
 return c
def shift(name,dz):
 c=parts[name].component;bs=[(b.name,trans(TM.copy(b),dz=dz),b.appearance,b.isLightBulbOn)for b in c.bRepBodies]
 for b in list(c.bRepBodies):b.deleteMe()
 for bn,b,a,v in bs:
  nb=c.bRepBodies.add(b);nb.name=bn;nb.appearance=a;nb.isLightBulbOn=v
def progress(s):(OUT/'progress.json').write_text(json.dumps({'stage':s,'time':time.time()}))
