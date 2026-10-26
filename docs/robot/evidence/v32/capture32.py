def capture(design):
 r=design.rootComponent;shapes={};grounds={};joints={};parts=[];occurrences=[];z=[]
 anatomical={j['name'] for j in json.loads((ROOT/'v29/native_joint_map_saved.json').read_text()) if j['anatomical']}
 for o in r.allOccurrences:
  grounds[o.fullPathName]=o.isGroundToParent
  attribute=o.component.attributes.itemByName('Robot','physical_owner')
  owner=attribute.value if attribute else o.fullPathName.split(':')[0]
  occurrences.append(dict(path=o.fullPathName,name=o.component.name,owner=owner,visible=o.isVisible,lightbulb=o.isLightBulbOn,ground_parent=o.isGroundToParent,referenced=o.isReferencedComponent,transform=o.transform2.asArray()))
  for collection,kind in ((o.bRepBodies,'brep'),(o.meshBodies,'mesh')):
   for b in collection:
    if not o.isVisible or not b.isVisible or b.name.startswith('_joint_datum_'):continue
    bb=bounds(b);shapes[o.fullPathName+'|'+b.name]=bb;z.extend((bb[0][2],bb[1][2]))
    if kind=='brep':assert b.isSolid and b.isValid,(o.component.name,b.name)
    color=None
    for key in ('opaque_albedo','generic_diffuse'):
     cp=adsk.core.ColorProperty.cast(b.appearance.appearanceProperties.itemById(key))
     if cp:
      v=cp.value;color=[v.red,v.green,v.blue];break
    parts.append(dict(path=o.fullPathName,part=o.component.name,body=b.name,owner=owner,kind=kind,bounds_mm=bb,volume_mm3=b.volume*1000 if kind=='brep' else None,appearance=b.appearance.name,color_rgb=color))
 for j in r.allAsBuiltJoints:
  m=j.jointMotion;row=dict(frame=j.transform.asArray(),valid=j.isValid,suppressed=j.isSuppressed,type=m.jointType,one=j.occurrenceOne.fullPathName,two=j.occurrenceTwo.fullPathName,anatomical=j.name in anatomical)
  if m.jointType==1:row.update(angle=m.rotationValue,axis=m.rotationAxisVector.asArray(),limits=[m.rotationLimits.minimumValue,m.rotationLimits.maximumValue],enabled=[m.rotationLimits.isMinimumValueEnabled,m.rotationLimits.isMaximumValueEnabled])
  joints[j.name]=row
 return dict(shapes=shapes,grounds=grounds,joints=joints,parts=parts,occurrences=occurrences,height_mm=max(z)-min(z),sole_z_mm=min(z),top_z_mm=max(z),visible_breps=sum(p['kind']=='brep' for p in parts),visible_meshes=sum(p['kind']=='mesh' for p in parts),anatomical_count=sum(j['anatomical'] for j in joints.values()),external_referenced_occurrences=sum(o.isReferencedComponent for o in r.allOccurrences))
