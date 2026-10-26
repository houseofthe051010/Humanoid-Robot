import adsk.core,adsk.fusion,json,math
OUT=ROOT/'v12';dest=OUT/'deliverables'
source=next(x for x in app.documents if x.name=='Bilateral_legs_v12')
path=dest/'Bilateral_legs_v12.f3d';check=app.importManager.importToNewDocument(app.importManager.createFusionArchiveImportOptions(str(path)));check.name='VERIFY_v12_archive'
d=adsk.fusion.Design.cast(check.products.itemByProductType('DesignProductType'));root=d.rootComponent
report={'archive':str(path),'groups':root.occurrences.count,'legs':{}}
for go in root.occurrences:
 c=go.component;side=c.name.removesuffix('_leg');ocs={o.component.partNumber:o.createForAssemblyContext(go) for o in c.occurrences}
 j=c.asBuiltJoints.itemByName(side+'_Knee_pitch').createForAssemblyContext(go)
 try:
  j.jointMotion.rotationValue=math.radians(30);adsk.doEvents();m=ocs['N04_Knee_pillow_block_L'].transform2
  errs={n:max(abs(a-b)for a,b in zip(m.asArray(),ocs[n].transform2.asArray()))for n in ['P03_Circular_motor_gearbox_case','Q03_CNC_roll_to_pitch_fork','R01_DJI_10018_77KV_ESTIMATED_REFERENCE']}
 finally:j.jointMotion.rotationValue=0;adsk.doEvents()
 report['legs'][side]={'components':c.occurrences.count,'joints':c.asBuiltJoints.count,'invalid_joints':[j.name for j in c.asBuiltJoints if not j.isValid],'zero_or_nonsolid':[o.component.name+'/'+b.name for o in c.occurrences if o.isLightBulbOn for b in o.component.bRepBodies if not b.isSolid or b.volume<=0],'knee_attachment_follow_errors':errs}
check.close(False);source.activate()
# Independently reopen the history-bearing source; do not conflate its timeline with the paired copy.
path=dest/'Leg_gearbox_hip_v12_parametric.f3d';check=app.importManager.importToNewDocument(app.importManager.createFusionArchiveImportOptions(str(path)));check.name='VERIFY_v12_parametric'
pd=adsk.fusion.Design.cast(check.products.itemByProductType('DesignProductType'));pr=pd.rootComponent
report['parametric_source']={'archive':str(path),'components':pr.occurrences.count,'joints':pr.asBuiltJoints.count,'timeline_features':pd.timeline.count,'invalid_joints':[j.name for j in pr.asBuiltJoints if not j.isValid]}
check.close(False);source.activate()
(OUT/'archive_reopen_verification.json').write_text(json.dumps(report,indent=2));result=report
