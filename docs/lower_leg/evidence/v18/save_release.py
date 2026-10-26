exec(compile((ROOT/'v18/common.py').read_text(),'<v17 common>','exec'))
check=json.loads((OUT/'validation.json').read_text())
assert not check['static_interferences'],check['static_interferences']
assert not any(p['interferences'] for p in check['waist_poses'])
assert not check['geometry_issues'] and not check['feature_issues'] and not check['invalid_joints']
for o in wg.component.occurrences:
    if o.component.partNumber.startswith(('W02_','W03_','W04_','W05_','W06_','W07_','W10_','W12_')):
        value='PA12-CF printed prototype; grade and strength unqualified'
        if o.component.partNumber.startswith('W05_'):value='Vendor output plus PA12-CF base/yoke prototype'
        o.component.attributes.add('SHIN','material',value)
import csv
bom=[]
for go in (right,left,wg):
    for o in go.component.occurrences:
        proxy=o.createForAssemblyContext(go)
        if not proxy.isVisible:continue
        c=o.component;bs=[b for b in proxy.bRepBodies if b.isVisible]
        if not bs:continue
        attr=c.attributes.itemByName('SHIN','material')
        bom.append({'assembly':go.component.name,'part_number':c.partNumber,'name':c.name,'quantity':1,
                    'active_bodies':len(bs),'material_reference':attr.value if attr else '', 'description':c.description})
with (OUT/'deliverables'/'BOM_V18.csv').open('w',newline='',encoding='utf-8-sig') as f:
    writer=csv.DictWriter(f,fieldnames=list(bom[0]));writer.writeheader();writer.writerows(bom)
path=OUT/'deliverables'/'Legs_hip_waist_v18.f3d';assert not path.exists()
assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(path)))
result={'archive':str(path),'bytes':path.stat().st_size,'document':doc.name,'bom_component_rows':len(bom)}
(OUT/'export.json').write_text(json.dumps(result,indent=2))
