import adsk.core,adsk.fusion,json
out=ROOT/'v10'
source=next(x for x in app.documents if x.name=='Shin_PA12CF_7010_392mm_v9');source.activate()
sd=adsk.fusion.Design.cast(source.products.itemByProductType('DesignProductType'))
backup=out/'Input_live_v9_preserved.f3d'
assert not backup.exists(),'Do not overwrite live-input backup'
assert sd.exportManager.execute(sd.exportManager.createFusionArchiveExportOptions(str(backup)))
doc=app.importManager.importToNewDocument(app.importManager.createFusionArchiveImportOptions(str(backup)))
assert doc,'Could not import live archive; stop before any fallback'
doc.name='Leg_layout_1600mm_v10'
d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'));d.activateRootComponent()
result={'document':doc.name,'backup':str(backup),'components':d.rootComponent.occurrences.count}
