import adsk.core,adsk.fusion,json,math
OUT=ROOT/'v13';dest=OUT/'deliverables'
source=next(x for x in app.documents if x.name=='Bilateral_legs_v13')
path=dest/'Bilateral_legs_v13.f3d';check=app.importManager.importToNewDocument(app.importManager.createFusionArchiveImportOptions(str(path)));check.name='VERIFY_v13_archive'
d=adsk.fusion.Design.cast(check.products.itemByProductType('DesignProductType'));root=d.rootComponent
report={'archive':str(path),'groups':root.occurrences.count,'legs':{}}
for go in root.occurrences:
 c=go.component;side=c.name.removesuffix('_leg');ocs={o.component.partNumber:o.createForAssemblyContext(go) for o in c.occurrences}
 j=c.asBuiltJoints.itemByName(side+'_Knee_pitch').createForAssemblyContext(go)
 try:
  j.jointMotion.rotationValue=math.radians(30);adsk.doEvents();m=ocs['N04_Knee_pillow_block_L'].transform2
  errs={n:max(abs(a-b)for a,b in zip(m.asArray(),ocs[n].transform2.asArray()))for n in ['P03_Circular_motor_gearbox_case','Q03_CNC_roll_to_pitch_fork','R01_DJI_10018_77KV_ESTIMATED_REFERENCE']}
  expected=adsk.core.Matrix3D.create();expected.setToRotation(math.radians(30),adsk.core.Vector3D.create(1,0,0),adsk.core.Point3D.create(0,2.3343134,43.56))
  errs['measured_knee_vs_expected']=max(abs(a-b)for a,b in zip(m.asArray(),expected.asArray()))
 finally:j.jointMotion.rotationValue=0;adsk.doEvents()
 report['legs'][side]={'components':c.occurrences.count,'joints':c.asBuiltJoints.count,'invalid_joints':[j.name for j in c.asBuiltJoints if not j.isValid],'zero_or_nonsolid':[o.component.name+'/'+b.name for o in c.occurrences if o.isLightBulbOn for b in o.component.bRepBodies if not b.isSolid or b.volume<=0],'knee_attachment_follow_errors':errs}
check.close(False);source.activate()
# Independently reopen the solid source with reconstructed joints; do not conflate its timeline with the paired copy.
path=dest/'Leg_chain_v13_source.f3d';check=app.importManager.importToNewDocument(app.importManager.createFusionArchiveImportOptions(str(path)));check.name='VERIFY_v13_source'
pd=adsk.fusion.Design.cast(check.products.itemByProductType('DesignProductType'));pr=pd.rootComponent
report['source_with_reconstructed_joints']={'archive':str(path),'components':pr.occurrences.count,'joints':pr.asBuiltJoints.count,'timeline_features':pd.timeline.count,'invalid_joints':[j.name for j in pr.asBuiltJoints if not j.isValid]}
report['source_with_reconstructed_joints']['zero_or_nonsolid']=[o.component.name+'/'+b.name for o in pr.occurrences if o.isLightBulbOn for b in o.component.bRepBodies if not b.isSolid or b.volume<=0]
check.close(False);source.activate()
(OUT/'archive_reopen_verification.json').write_text(json.dumps(report,indent=2));result=report
for row in report['legs'].values():assert not row['invalid_joints'] and not row['zero_or_nonsolid'] and max(row['knee_attachment_follow_errors'].values())<1e-6,row
assert not report['source_with_reconstructed_joints']['invalid_joints'] and not report['source_with_reconstructed_joints']['zero_or_nonsolid'],report
