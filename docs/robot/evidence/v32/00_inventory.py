import adsk.core, adsk.fusion, json, time
from pathlib import Path
OUT=Path(__file__).parent
OUT.mkdir(exist_ok=True)
doc=app.activeDocument
d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'))
assert d is not None, 'Active document is not a design'
root=d.rootComponent
def xyz(p): return [x*10 for x in p.asArray()]
def bounds(b):
    q=b.preciseBoundingBox if hasattr(b,'preciseBoundingBox') else b.boundingBox
    return [xyz(q.minPoint),xyz(q.maxPoint)]
def cyls(b):
    out=[]
    for f in b.faces:
        c=adsk.core.Cylinder.cast(f.geometry)
        if c: out.append(dict(origin_mm=xyz(c.origin),axis=c.axis.asArray(),radius_mm=c.radius*10))
    return out
parts=[]
for o in root.allOccurrences:
    detail=any(n in o.fullPathName.lower() for n in ('hip','waist','pelvis','shoulder','torso','knee','sprocket'))
    bodies=[dict(name=b.name,visible=b.isVisible,bounds_mm=bounds(b),volume_cm3=b.volume,
                 cylinders=cyls(b) if detail else [],token=b.entityToken) for b in o.bRepBodies]
    parts.append(dict(path=o.fullPathName,name=o.component.name,visible=o.isVisible,
                      lightbulb=o.isLightBulbOn,ground_parent=o.isGroundToParent,
                      transform_cm=o.transform2.asArray(),bodies=bodies,
                      mesh_count=len(list(o.meshBodies)),token=o.entityToken))
root_bodies=[dict(name=b.name,visible=b.isVisible,bounds_mm=bounds(b),volume_cm3=b.volume,
                  cylinders=cyls(b),token=b.entityToken) for b in root.bRepBodies]
joints=[]
for j in root.allAsBuiltJoints:
    m=j.jointMotion
    joints.append(dict(name=j.name,valid=j.isValid,suppressed=j.isSuppressed,
                       one=j.occurrenceOne.fullPathName,two=j.occurrenceTwo.fullPathName,
                       angle=getattr(m,'rotationValue',None),type=m.jointType,
                       frame_cm=j.transform.asArray() if j.geometry else None))
data=dict(document=doc.name,modified=doc.isModified,design_type=d.designType,
          documents=[x.name for x in app.documents],root_bodies=root_bodies,parts=parts,
          joints=joints,root_sketches=[dict(name=s.name,visible=s.isVisible) for s in root.sketches],
          datafile=dict(name=doc.dataFile.name,id=doc.dataFile.id,version=doc.dataFile.versionNumber) if doc.dataFile else None,
          epoch=time.time())
(OUT/'live_input_inventory.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
result=dict(document=doc.name,modified=doc.isModified,occurrences=len(parts),
            root_bodies=len(root_bodies),joints=len(joints),file=str(OUT/'live_input_inventory.json'))
