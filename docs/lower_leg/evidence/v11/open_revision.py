import adsk.core,adsk.fusion,json
out=ROOT/'v11'
source=next(x for x in app.documents if x.name=='Leg_layout_1600mm_v10');source.activate()
sd=adsk.fusion.Design.cast(source.products.itemByProductType('DesignProductType'))
backup=out/'Input_live_v10_preserved.f3d'
assert not backup.exists(),'Preserve existing input archive'
assert sd.exportManager.execute(sd.exportManager.createFusionArchiveExportOptions(str(backup)))
doc=app.importManager.importToNewDocument(app.importManager.createFusionArchiveImportOptions(str(backup)))
assert doc
doc.name='Leg_compact_shelled_v11'
result={'document':doc.name,'backup':str(backup)}
