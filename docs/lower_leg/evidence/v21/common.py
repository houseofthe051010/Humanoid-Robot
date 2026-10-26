source=(ROOT/'v18/common.py').read_text().replace("OUT=ROOT/'v18'","OUT=ROOT/'v21'").replace("x.name=='Legs_hip_waist_v18'","x.name.startswith('Humanoid_waist_battery_v21')")
exec(compile(source,'<v20 helpers>','exec'))
def getpart(go,key):return next(o for o in go.component.occurrences if o.component.partNumber.startswith(key))
def world_replace(go,o,rows,desc,ap):
 inv=o.createForAssemblyContext(go).transform2.copy();inv.invert()
 return replace(o.component,[(n,transform(b,inv)) for n,b in rows],desc,ap)
def rotoval(z0,z1,r=5,flat=4):
 b=oval(0,Y+10,z0,z1,r,flat)
 m=adsk.core.Matrix3D.create();m.setToRotation(math.pi/2,V3.create(0,0,1),pt((0,Y+10,0)))
 return transform(b,m)
def bounds(b):
 q=b.boundingBox
 return [[round(10*v,6) for v in p.asArray()] for p in (q.minPoint,q.maxPoint)]
