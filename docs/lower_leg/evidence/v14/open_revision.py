import adsk.core,adsk.fusion,json
OUT=ROOT/'v14';(OUT/'deliverables').mkdir(exist_ok=True)
doc=next(x for x in app.documents if x.name=='Bilateral_legs_v13');doc.activate();d=adsk.fusion.Design.cast(app.activeProduct)
path=OUT/'Input_live_v13_preserved.f3d';assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(path)))
assert not any(x.name=='Bilateral_legs_v14' for x in app.documents)
new=app.importManager.importToNewDocument(app.importManager.createFusionArchiveImportOptions(str(path)));new.name='Bilateral_legs_v14'
result={'document':new.name,'preserved':str(path)}
