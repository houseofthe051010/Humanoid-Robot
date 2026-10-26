import adsk.core,adsk.fusion,math,json
from pathlib import Path
OUT=ROOT/'v12';dest=OUT/'deliverables';TM=adsk.fusion.TemporaryBRepManager.get()
doc=next(x for x in app.documents if x.name=='Bilateral_legs_v12');doc.activate();d=adsk.fusion.Design.cast(app.activeProduct);root=d.rootComponent
groups={o.component.name:o for o in root.occurrences};report={'spacing_mm':260,'legs':{}}
source_joints={r['name']:r for r in json.loads((OUT/'joint_inventory.json').read_text())if r['type']==1}
allb={}
for side in ['Right','Left']:
 go=groups[side+'_leg'];c=go.component;native={o.component.partNumber:o.createForAssemblyContext(go) for o in c.occurrences};bodies=[]
 # Copied posed solids define zero at the source's current pose, so retain the
 # original physical travel limits by subtracting its wrapped angle offset.
 rebases={}
 for name,row in source_joints.items():
  jj=c.asBuiltJoints.itemByName(side+'_'+name)
  offset=(row['value']+math.pi)%(2*math.pi)-math.pi
  lim=row['limits'];rl=jj.jointMotion.rotationLimits
  rl.minimumValue=lim['min']-offset;rl.maximumValue=lim['max']-offset
  rl.isMinimumValueEnabled=lim['min_on'];rl.isMaximumValueEnabled=lim['max_on']
  if name in ['Rod_A_pin_swivel','Rod_B_pin_swivel']:
   rl.isMinimumValueEnabled=False;rl.isMaximumValueEnabled=False
  rebases[name]={'source_pose_offset_deg':math.degrees(offset),'current_copy_angle_deg':math.degrees(jj.jointMotion.rotationValue),'continuous_full_turn_pin':name in ['Rod_A_pin_swivel','Rod_B_pin_swivel']}
 for o in native.values():
  if o.isLightBulbOn:
   for b in o.bRepBodies:
    if b.isLightBulbOn:bodies.append((o.component.partNumber,b.name,TM.copy(b)))
 allb[side]=bodies
 report['legs'][side]={'components':c.occurrences.count,'visible_components':sum(o.isLightBulbOn for o in c.occurrences),'visible_bodies':len(bodies),'joints':c.asBuiltJoints.count,'invalid_joints':[j.name for j in c.asBuiltJoints if not j.isValid],'empty_bodies':[n+'/'+bn for n,bn,b in bodies if not b.isSolid or b.volume<1e-8]}
 report['legs'][side]['pose_angle_rebases']=rebases
 # Confirm the output case, motor, and hip structure follow the native knee.
 j=c.asBuiltJoints.itemByName(side+'_Knee_pitch').createForAssemblyContext(go);samples=[]
 try:
  for ang in [0,45,90]:
   j.jointMotion.rotationValue=math.radians(ang);adsk.doEvents();m=native['N04_Knee_pillow_block_L'].transform2
   diffs={}
   for n in ['P03_Circular_motor_gearbox_case','R01_DJI_10018_77KV_ESTIMATED_REFERENCE','Q01_CNC_rail_to_yaw_crosshead','Q03_CNC_roll_to_pitch_fork']:
    diffs[n]=max(abs(a-b)for a,b in zip(m.asArray(),native[n].transform2.asArray()))
   expected=adsk.core.Matrix3D.create();expected.setToRotation(math.radians(ang),adsk.core.Vector3D.create(1,0,0),adsk.core.Point3D.create(0,2.3343134,42.36))
   samples.append({'command_deg':ang,'measured_deg':math.degrees(j.jointMotion.rotationValue),'knee_matrix_error':max(abs(a-b)for a,b in zip(m.asArray(),expected.asArray())),'attachment_matrix_errors':diffs})
 finally:j.jointMotion.rotationValue=0;adsk.doEvents()
 report['legs'][side]['knee_native_samples']=samples
mins={s:min(b.boundingBox.minPoint.x for _,_,b in bs)*10 for s,bs in allb.items()};maxs={s:max(b.boundingBox.maxPoint.x for _,_,b in bs)*10 for s,bs in allb.items()}
report['neutral_global_x_ranges_mm']={s:[mins[s],maxs[s]] for s in mins};report['neutral_sagittal_gap_mm']=mins['Right']-maxs['Left']
# A positive gap between disjoint X half-spaces is a stronger neutral separation check
# than body-by-body approximate meshes. Knee rotations about X retain this separation.
report['neutral_pair_separated']=report['neutral_sagittal_gap_mm']>0
report['hip_range_checked']=False
report['volume_symmetry_error_mm3']=abs(sum(b.volume for _,_,b in allb['Right'])-sum(b.volume for _,_,b in allb['Left']))*1000
(OUT/'bilateral_validation.json').write_text(json.dumps(report,indent=2))
result=report
