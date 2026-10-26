import adsk.fusion,json
OUT=ROOT/'v19'
assert (OUT/'Input_live_v18_user_edits_preserved.f3d').exists()
doc=next(x for x in app.documents if x.name=='Legs_hip_waist_v18');doc.activate()
doc.name='Legs_hip_waist_v19'
result={'document':doc.name,'preserved_source':str(OUT/'Input_live_v18_user_edits_preserved.f3d')}
