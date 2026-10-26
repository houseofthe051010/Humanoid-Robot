import adsk.core,adsk.fusion,json,time
OUT=ROOT/'v19';OUT.mkdir(exist_ok=True)
d=adsk.fusion.Design.cast(app.activeProduct)
assert d,'Active product must be a Fusion design'
doc=app.activeDocument;root=d.rootComponent
assert 'Legs_' in doc.name,doc.name
def bounds(b):
    bb=b.boundingBox
    return [[10*v for v in p.asArray()] for p in (bb.minPoint,bb.maxPoint)]
report={'document':doc.name,'documents':[x.name for x in app.documents], 'root_bodies':[], 'groups':[]}
for b in root.bRepBodies:report['root_bodies'].append({'name':b.name,'visible':b.isVisible,'bounds':bounds(b)})
for go in root.occurrences:
    if go.component.name.startswith('ZZ_'):continue
    row={'name':go.component.name,'transform':list(go.transform2.asArray()),'grounded':go.isGrounded,'parts':[],'joints':[]}
    for o in go.component.occurrences:
        c=o.component;p=o.createForAssemblyContext(go)
        if c.partNumber.startswith(('T07','T09','Q0','H0','W0')):
            row['parts'].append({'name':c.name,'part':c.partNumber,'visible':p.isVisible,'native_transform':list(o.transform2.asArray()),'transform':list(p.transform2.asArray()),'bodies':[{'name':b.name,'visible':b.isVisible,'volume_mm3':b.volume*1000,'bounds':bounds(b)} for b in p.bRepBodies]})
    for j in go.component.asBuiltJoints:row['joints'].append({'name':j.name,'one':j.occurrenceOne.component.partNumber,'two':j.occurrenceTwo.component.partNumber,'type':j.jointMotion.jointType})
    report['groups'].append(row)
(OUT/'live_source_inventory.json').write_text(json.dumps(report,indent=2))
path=OUT/'Input_live_v18_user_edits_preserved.f3d'
assert not path.exists(),'Do not overwrite preserved source'
assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(path)))
report['backup']=str(path)
(OUT/'source.json').write_text(json.dumps({'document':doc.name,'backup':str(path)},indent=2))
result={'document':doc.name,'backup':str(path),'groups':[(r['name'],len(r['parts']),len(r['joints'])) for r in report['groups']]}
