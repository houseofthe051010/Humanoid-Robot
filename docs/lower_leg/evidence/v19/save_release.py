exec(compile((ROOT/'v19/common.py').read_text(),'<v19 common>','exec'))
import csv
check=json.loads((OUT/'fit_validation.json').read_text())
assert not check['hits'],check['hits']
assert not check['geometry_issues'] and not check['feature_issues'] and not check['invalid_joints']
motion=json.loads((OUT/'waist_motion_validation.json').read_text())
assert not any(x['hits'] for x in motion['poses'])
assert motion['max_closure_error_mm']<.05,motion
assert motion['max_pose_error_deg']<.05,motion
assert motion['max_rod_end_tilt_deg']<=6.25,motion
dest=OUT/'deliverables';dest.mkdir(exist_ok=True)
bom=[]
for go in (right,left,wg):
    for o in go.component.occurrences:
        p=o.createForAssemblyContext(go)
        if not p.isVisible:continue
        c=o.component;bs=[b for b in p.bRepBodies if b.isVisible]
        if not bs:continue
        a=c.attributes.itemByName('SHIN','material')
        bom.append({'assembly':go.component.name,'part_number':c.partNumber,'name':c.name,'quantity':1,'active_bodies':len(bs),
                    'material_reference':a.value if a else '', 'description':c.description})
with (dest/'BOM_V19.csv').open('w',newline='',encoding='utf-8-sig') as f:
    ww=csv.DictWriter(f,fieldnames=list(bom[0]));ww.writeheader();ww.writerows(bom)
path=dest/'Legs_hip_waist_v19.f3d';assert not path.exists()
assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(path)))
result={'archive':str(path),'bytes':path.stat().st_size,'bom_component_rows':len(bom),'document':doc.name}
(OUT/'export.json').write_text(json.dumps(result,indent=2))
