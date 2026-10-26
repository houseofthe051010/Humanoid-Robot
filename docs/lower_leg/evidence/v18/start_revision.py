import adsk.fusion,json
OUT=ROOT/'v18';OUT.mkdir(exist_ok=True)
doc=next(x for x in app.documents if x.name=='Legs_hip_waist_v17')
doc.activate()
assert (ROOT/'v17/deliverables/Legs_hip_waist_v17.f3d').exists()
doc.name='Legs_hip_waist_v18'
result={'source_archive':str(ROOT/'v17/deliverables/Legs_hip_waist_v17.f3d'),
        'document':doc.name,'scope':'separate estimated hip shells, larger flush roll openings, inward 6010 outputs, thicker blended fork junctions'}
(OUT/'source.json').write_text(json.dumps(result,indent=2))
