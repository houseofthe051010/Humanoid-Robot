import adsk.fusion,json
OUT=ROOT/'v17'
source=next(x for x in app.documents if x.name=='Legs_waist_gimbal_v16')
source.activate();d=adsk.fusion.Design.cast(app.activeProduct)
path=OUT/'Input_live_v16_user_edits_preserved.f3d'
assert not path.exists(),'Source already preserved; inspect before repeating'
assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(path)))
new=app.importManager.importToNewDocument(app.importManager.createFusionArchiveImportOptions(str(path)))
assert new;new.name='Legs_hip_waist_v17'
result={'source':source.name,'preserved':str(path),'bytes':path.stat().st_size,'new':new.name}
(OUT/'source_preservation.json').write_text(json.dumps(result,indent=2))
