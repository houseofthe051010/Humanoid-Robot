import adsk.core,adsk.fusion,json
OUT=ROOT/'v12';dest=OUT/'deliverables';changed=[]
for name in ['Legs_gearbox_hip_v12','Bilateral_legs_v12']:
 doc=next(x for x in app.documents if x.name==name);doc.activate()
 d=adsk.fusion.Design.cast(app.activeProduct)
 ap=d.appearances.itemByName('v12_sprocket_orange')
 prop=adsk.core.ColorProperty.cast(ap.appearanceProperties.itemById('metal_f0'))
 assert prop
 prop.value=adsk.core.Color.create(205,135,45,255)
 changed.append({'document':name,'appearance':ap.name,'property':prop.id,'rgb':[205,135,45]})
 if name=='Legs_gearbox_hip_v12':
  assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(dest/'Leg_gearbox_hip_v12_parametric.f3d')))
(OUT/'appearance_finish.json').write_text(json.dumps({'changes':changed,'geometry_changed':False},indent=2))
exec(compile((OUT/'capture_bilateral.py').read_text(encoding='utf-8'),str(OUT/'capture_bilateral.py'),'exec'))
