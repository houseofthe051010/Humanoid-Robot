import adsk.core,adsk.fusion,json
OUT=ROOT/'v13';doc=next(x for x in app.documents if x.name=='Bilateral_legs_v12');doc.activate();d=adsk.fusion.Design.cast(app.activeProduct)
backup=OUT/'Input_live_v12_20260921_preserved.f3d'
assert not backup.exists()
assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(backup)))
go=next(o for o in d.rootComponent.occurrences if o.component.name=='Right_leg');g=go.component
rows=[]
for j in g.asBuiltJoints:
 jp=j.createForAssemblyContext(go);mo=jp.jointMotion
 row={'name':j.name.removeprefix('Right_'),'one':j.occurrenceOne.component.partNumber,'two':j.occurrenceTwo.component.partNumber,'type':int(mo.jointType),'suppressed':j.isSuppressed,'transform':jp.transform.asArray()}
 if mo.jointType==1:
  l=mo.rotationLimits;row.update(axis=mo.rotationAxisVector.asArray(),angle=mo.rotationValue,limits={'min':l.minimumValue,'max':l.maximumValue,'min_on':l.isMinimumValueEnabled,'max_on':l.isMaximumValueEnabled})
 rows.append(row)
(OUT/'source_joint_inventory.json').write_text(json.dumps(rows,indent=2))
result={'backup':str(backup),'joints':len(rows)}
