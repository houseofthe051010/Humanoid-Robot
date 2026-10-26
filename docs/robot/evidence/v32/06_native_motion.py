exec(compile((ROOT/'v32/common32.py').read_text(),'<common32>','exec'))
source=doc;source_root=root
poses={o.component.name:o.transform2.asArray() for o in root.occurrences}
source_angles={j.name:j.jointMotion.rotationValue for j in root.allAsBuiltJoints if j.jointMotion.jointType==1}
archive=OUT/'Organized_v32_motion_test_copy.f3d'
if not archive.exists():assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(archive)))
opened=None;records=[]
def rel(group,owner):
 a=owner.transform2.copy();a.invert();a=a.asArray();b=group.transform2.asArray()
 return [sum(a[r*4+k]*b[k*4+c] for k in range(4)) for r in range(4) for c in range(4)]
try:
 opened=app.importManager.importToNewDocument(app.importManager.createFusionArchiveImportOptions(str(archive)));assert opened
 d=adsk.fusion.Design.cast(opened.products.itemByProductType('DesignProductType'));root=d.rootComponent
 joints={j.name:j for j in root.allAsBuiltJoints}
 mapping=json.loads((ROOT/'v29/native_joint_map_saved.json').read_text());names=[x['name'] for x in mapping if x['anatomical'] and any(k in x['name'] for k in ('Hip','Knee','Ankle'))]
 groups={o.component.name[len('Covers_'):]:o for o in root.allOccurrences if o.component.name.startswith('Covers_')}
 baseline={name:rel(g,exact(name)) for name,g in groups.items()}
 for name in names:
  j=joints[name];motion=j.jointMotion;old=motion.rotationValue;base=math.atan2(math.sin(old),math.cos(old));lim=motion.rotationLimits
  # Fusion's native motion setter honors 0.1-degree display quantization here.
  # Use representable commands on a disposable reopened copy, preserving live pose.
  target=math.radians(round(math.degrees(base),1)+1.)
  if lim.isMaximumValueEnabled and target>lim.maximumValue:target=math.radians(round(math.degrees(base),1)-1.)
  assert not lim.isMinimumValueEnabled or target>=lim.minimumValue
  before=j.occurrenceOne.transform2.asArray()
  try:
   motion.rotationValue=target;adsk.doEvents()
   err=abs(math.atan2(math.sin(motion.rotationValue-target),math.cos(motion.rotationValue-target)))
   moved=max(abs(a-b) for a,b in zip(before,j.occurrenceOne.transform2.asArray()))
   cover_error=max(abs(a-b) for owner,g in groups.items() for a,b in zip(baseline[owner],rel(g,exact(owner))))
   rec=dict(joint=name,target_rad=target,actual_rad=motion.rotationValue,angle_error_rad=err,movement_matrix_delta=moved,max_cover_owner_relative_matrix_error=cover_error)
   records.append(rec);journal('native_cover_motion_progress31',records)
   assert err<1e-5 and moved>1e-6 and cover_error<1e-5,rec
  finally:motion.rotationValue=old;adsk.doEvents()
 assert len(records)==12 and all(j.isValid and not j.isSuppressed for j in root.allAsBuiltJoints)
 compound=[]
 for prefix in ('Left','Right'):
  pj=joints[prefix+'_Hip_pitch'].jointMotion;rj=joints[prefix+'_Hip_roll'].jointMotion
  po,ro=pj.rotationValue,rj.rotationValue
  try:
   for dp,dr in ((10,10),(-10,-10),(15,-10),(-15,10)):
    tp=math.radians(round(math.degrees(po),1)+dp);tr=math.radians(round(math.degrees(ro),1)+dr)
    pj.rotationValue=tp;rj.rotationValue=tr;adsk.doEvents()
    errors=[abs(math.atan2(math.sin(m.rotationValue-t),math.cos(m.rotationValue-t))) for m,t in ((pj,tp),(rj,tr))]
    ce=max(abs(a-b) for owner,g in groups.items() for a,b in zip(baseline[owner],rel(g,exact(owner))))
    assert max(errors)<1e-5 and ce<1e-5
    compound.append(dict(side=prefix,pitch_offset_deg=dp,roll_offset_deg=dr,max_angle_error_rad=max(errors),cover_error=ce))
  finally:pj.rotationValue=po;rj.rotationValue=ro;adsk.doEvents()
 journal('native_compound_motion32',dict(pass_=True,records=compound))
finally:
 if opened:opened.close(False)
 source.activate();doc=source;d=adsk.fusion.Design.cast(source.products.itemByProductType('DesignProductType'));root=d.rootComponent
pose_error=max(abs(a-b) for name,vs in poses.items() for a,b in zip(vs,exact(name).transform2.asArray()))
angle_error=max(abs(source_angles[j.name]-j.jointMotion.rotationValue) for j in root.allAsBuiltJoints if j.name in source_angles)
assert pose_error<1e-10 and angle_error<1e-10
journal('native_cover_motion32',dict(pass_=True,body_axes_tested=len(records),owner_groups=len(groups),records=records,max_reset_matrix_error=pose_error,max_reset_angle_error_rad=angle_error,scope='Twelve leg single-axis native tests performed on reopened disposable copy; covers follow physical owners. Live source angles/transforms untouched. Not full combined collision or strength qualification.'))
result=dict(pass_=True,body_axes_tested=len(records),owner_groups=len(groups),source_pose_matrix_error=pose_error,source_angle_error=angle_error)
