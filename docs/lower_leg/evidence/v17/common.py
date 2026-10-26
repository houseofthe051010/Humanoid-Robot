import adsk.core,adsk.fusion,json,math,time
OUT=ROOT/'v17'
doc=next(x for x in app.documents if x.name=='Legs_hip_waist_v17');doc.activate()
d=adsk.fusion.Design.cast(app.activeProduct);root=d.rootComponent
TM=adsk.fusion.TemporaryBRepManager.get();BT=adsk.fusion.BooleanTypes
P3=adsk.core.Point3D;V3=adsk.core.Vector3D;Y=23.343134
def progress(stage):
    (OUT/'progress.json').write_text(json.dumps({'stage':stage,'time':time.time()}))
def pt(a):return P3.create(*(v/10 for v in a))
def cy(a,b,r):return TM.createCylinderOrCone(pt(a),r/10,pt(b),r/10)
def cone(a,b,r0,r1):return TM.createCylinderOrCone(pt(a),r0/10,pt(b),r1/10)
def bx(a,b):return TM.createBox(adsk.core.OrientedBoundingBox3D.create(pt([(x+y)/2 for x,y in zip(a,b)]),V3.create(1,0,0),V3.create(0,1,0),*((y-x)/10 for x,y in zip(a,b))))
def un(a,*bs):
    for b in bs:assert TM.booleanOperation(a,b,BT.UnionBooleanType)
    return a
def sub(a,b):assert TM.booleanOperation(a,b,BT.DifferenceBooleanType);return a
def ix(a,b):assert TM.booleanOperation(a,b,BT.IntersectionBooleanType);return a
def tx(b,dx=0,dy=0,dz=0):
    m=adsk.core.Matrix3D.create();m.translation=V3.create(dx/10,dy/10,dz/10);assert TM.transform(b,m);return b
def transform(b,m):assert TM.transform(b,m);return b
def reflect(b,cx=0):
    m=adsk.core.Matrix3D.create();m.setCell(0,0,-1);m.setCell(0,3,2*cx/10);return transform(b,m)
def rrxy(x0,x1,y0,y1,z0,z1,r):
    a=un(bx((x0+r,y0,z0),(x1-r,y1,z1)),bx((x0,y0+r,z0),(x1,y1-r,z1)))
    for x in (x0+r,x1-r):
        for y in (y0+r,y1-r):un(a,cy((x,y,z0),(x,y,z1),r))
    return a
def beam_y(a,b,r,y0,y1):
    dx,dz=b[0]-a[0],b[1]-a[1];ll=math.hypot(dx,dz)
    mid=((a[0]+b[0])/2,(y0+y1)/2,(a[1]+b[1])/2)
    tool=TM.createBox(adsk.core.OrientedBoundingBox3D.create(pt(mid),V3.create(dx/ll,0,dz/ll),V3.create(0,1,0),ll/10,(y1-y0)/10,2*r/10))
    return un(tool,cy((a[0],y0,a[1]),(a[0],y1,a[1]),r),cy((b[0],y0,b[1]),(b[0],y1,b[1]),r))
def oval(x,y,z0,z1,r=5,flat=4):
    return un(bx((x-r,y-flat,z0),(x+r,y+flat,z1)),cy((x,y-flat,z0),(x,y-flat,z1),r),cy((x,y+flat,z0),(x,y+flat,z1),r))
def parts(group):return {o.component.partNumber:o for o in group.component.occurrences}
def newpart(parent,name,desc,material):
    o=parent.occurrences.addNewComponent(adsk.core.Matrix3D.create());c=o.component;c.name=name;c.partNumber=name;c.description=desc
    c.attributes.add('SHIN','material',material);return o
def add(c,b,name,ap=None):
    assert b and b.isSolid and b.volume>0,(name,'bad solid')
    bf=c.features.baseFeatures.add();bf.name=name;bf.startEdit();c.bRepBodies.add(b,bf);bf.finishEdit();nb=bf.bodies.item(0);nb.name=name
    if ap:nb.appearance=ap
    return nb
def replace(c,bodies,desc,ap=None):
    old=list(c.bRepBodies)
    if ap is None and old:ap=old[0].appearance
    for b in old:c.features.removeFeatures.add(b)
    rows=[]
    for name,b in bodies:rows.append(add(c,b,name,ap))
    c.description=desc;return rows
def fillet_edges(c,b,r,predicate,label):
    es=adsk.core.ObjectCollection.create()
    for e in b.edges:
        if predicate(e):es.add(e)
    if not es.count:return None
    fi=c.features.filletFeatures.createInput();fi.addConstantRadiusEdgeSet(es,adsk.core.ValueInput.createByReal(r/10),False)
    f=c.features.filletFeatures.add(fi);f.name=label;return f
def rigid(c,a,b,name):
    ji=c.asBuiltJoints.createInput(a,b,None);ji.setAsRigidJointMotion();j=c.asBuiltJoints.add(ji);j.name=name;j.isLightBulbOn=False;return j
def basis(origin,u,v,w):
    m=adsk.core.Matrix3D.create();m.setWithCoordinateSystem(pt(origin),V3.create(*u),V3.create(*v),V3.create(*w));return m

right=next(o for o in root.occurrences if o.component.name=='Right_leg')
left=next(o for o in root.occurrences if o.component.name=='Left_leg')
wg=next(o for o in root.occurrences if o.component.name.startswith('Waist_'))
rp=parts(right);wp=parts(wg)
silver=rp['Q01_CNC_rail_to_yaw_crosshead'].component.bRepBodies.item(0).appearance
plastic=wp['W02_Waist_front_shell'].component.bRepBodies.item(0).appearance
black=rp['R01_DJI_10018_77KV_ESTIMATED_REFERENCE'].component.bRepBodies.item(0).appearance
