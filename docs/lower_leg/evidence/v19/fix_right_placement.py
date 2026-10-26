exec(compile((ROOT/'v19/common.py').read_text(),'<v19 common>','exec'))
for b in root.bRepBodies:
    if b.name=='Body3':b.name='ZZ_User_roll_output_guide_replaced_v19';b.isLightBulbOn=False
before=list(right.transform2.asArray())
assert abs(right.transform2.translation.x)<1e-6,'Unexpected right position; avoid double motion'
right.isGrounded=False
right.isGroundToParent=False
adsk.doEvents()
m=adsk.core.Matrix3D.create();m.translation=V3.create(-1,0,0)
root.transformOccurrences([right],[m],True)
adsk.doEvents()
if d.snapshots.hasPendingSnapshot:d.snapshots.add()
adsk.doEvents()
after=list(right.transform2.asArray())
assert abs(right.transform2.translation.x+1)<1e-6,after
# Existing replacement hip solids were authored in final world coordinates
# before the right root motion was lost. Compensate those solids only.
keys=('Q02_CNC_yaw_to_roll_cradle','Q03_CNC_roll_to_pitch_fork','T07_Hip_pitch_motor_ENVELOPE_REFERENCE',
      'T09_Hip_roll_motor_ENVELOPE_REFERENCE','H01_Hip_roll_117OD_106ID_case','H02_Hip_pitch_roll_bearing_REFERENCES',
      'H05_DJI10018_pitch_gearbox_shell_ESTIMATE','H06_Roll_tube_recessed_endcaps','H07_Pitch_tube_recessed_endcaps','H08_Roll_61810_bearing_references')
for key in keys:
    o=parts(right)[key];p=o.createForAssemblyContext(right)
    inv=p.transform2.copy();inv.invert();vec=V3.create(1,0,0);vec.transformBy(inv)
    move=adsk.core.Matrix3D.create();move.translation=vec
    bs=adsk.core.ObjectCollection.create()
    for b in o.component.bRepBodies:bs.add(b)
    fi=o.component.features.moveFeatures.createInput2(bs);fi.defineAsFreeMove(move)
    f=o.component.features.moveFeatures.add(fi);f.name='V19_compensate_right_group_reposition'
adsk.doEvents()
if d.snapshots.hasPendingSnapshot:d.snapshots.add()
right.isGrounded=True
adsk.doEvents()
result={'before':before,'after':list(right.transform2.asArray()),'compensated_parts':keys}
(OUT/'right_placement_correction.json').write_text(json.dumps(result,indent=2))
assert abs(right.transform2.translation.x+1)<1e-6,result
