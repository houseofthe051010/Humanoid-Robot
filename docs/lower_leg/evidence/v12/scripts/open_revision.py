import adsk.core,adsk.fusion,json
out=ROOT/'v12'
source=next(x for x in app.documents if x.name=='Leg_compact_shelled_v11');source.activate()
sd=adsk.fusion.Design.cast(source.products.itemByProductType('DesignProductType'))
backup=out/'Input_live_v11_user_edits_preserved.f3d'
assert not backup.exists(),'Preserve existing input archive'
assert sd.exportManager.execute(sd.exportManager.createFusionArchiveExportOptions(str(backup)))
doc=app.importManager.importToNewDocument(app.importManager.createFusionArchiveImportOptions(str(backup)))
assert doc
doc.name='Legs_gearbox_hip_v12'
d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'))
def body(b):return {'name':b.name,'visible':b.isVisible,'bounds':[[v*10 for v in b.boundingBox.minPoint.asArray()],[v*10 for v in b.boundingBox.maxPoint.asArray()]],'volume_mm3':b.volume*1000}
result={'document':doc.name,'root_bodies':[body(b)for b in d.rootComponent.bRepBodies],'root_features':[f.name for f in d.rootComponent.features],'backup':str(backup)}
(out/'root_user_edits.json').write_text(json.dumps(result,indent=2))
