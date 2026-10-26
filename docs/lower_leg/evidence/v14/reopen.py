import adsk.core,adsk.fusion,json,math
OUT=ROOT/'v14';path=OUT/'deliverables'/'Bilateral_legs_v14.f3d';source=next(x for x in app.documents if x.name=='Bilateral_legs_v14')
check=app.importManager.importToNewDocument(app.importManager.createFusionArchiveImportOptions(str(path)));check.name='VERIFY_v14_archive';d=adsk.fusion.Design.cast(app.activeProduct)
report={'archive':str(path),'legs':{}}
for go in d.rootComponent.occurrences:
 c=go.component;side=c.name.removesuffix('_leg');parts={o.component.partNumber:o.createForAssemblyContext(go)for o in c.occurrences};j=c.asBuiltJoints.itemByName(side+'_Knee_pitch').createForAssemblyContext(go)
 try:
  j.jointMotion.rotationValue=math.radians(30);adsk.doEvents();m=parts['N04_Knee_pillow_block_L'].transform2
  expected=adsk.core.Matrix3D.create();expected.setToRotation(math.radians(30),adsk.core.Vector3D.create(1,0,0),adsk.core.Point3D.create(0,2.3343134,43.06))
  err=max(abs(a-b)for a,b in zip(m.asArray(),expected.asArray()))
 finally:j.jointMotion.rotationValue=0;adsk.doEvents()
 row={'joints':c.asBuiltJoints.count,'invalid_joints':[j.name for j in c.asBuiltJoints if not j.isValid],'zero_or_nonsolid':[o.component.name+'/'+b.name for o in c.occurrences if o.isLightBulbOn for b in o.component.bRepBodies if not b.isSolid or b.volume<=0],'knee_axis_motion_error':err}
 report['legs'][side]=row
check.close(False);source.activate();(OUT/'archive_reopen_verification.json').write_text(json.dumps(report,indent=2))
for r in report['legs'].values():assert not r['invalid_joints'] and not r['zero_or_nonsolid'] and r['knee_axis_motion_error']<1e-6,r
result=report
