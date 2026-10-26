exec(compile((ROOT/'v17/common.py').read_text(),'<v17 common>','exec'))
def row(b):return {'name':b.name,'visible':b.isLightBulbOn,'volume':b.volume*1000,'bounds':[[x*10 for x in b.boundingBox.minPoint.asArray()],[x*10 for x in b.boundingBox.maxPoint.asArray()]]}
report={'root_bodies':[row(b) for b in root.bRepBodies],'waist':[],'hips':[]}
for o in wg.component.occurrences:
    p=o.createForAssemblyContext(wg)
    report['waist'].append({'name':o.component.name,'visible':o.isLightBulbOn,'transform':list(p.transform2.asArray()),'bodies':[row(b) for b in p.bRepBodies]})
for go in (right,left):
    report['hips'].append({'leg':go.component.name,'group_bodies':[row(b) for b in go.component.bRepBodies],
        'parts':[{'name':o.component.name,'part':o.component.partNumber,'bodies':[row(b) for b in o.component.bRepBodies]} for o in go.component.occurrences if o.component.partNumber.startswith(('Q','T07','T09'))]})
(OUT/'review_state.json').write_text(json.dumps(report,indent=2));result={'file':str(OUT/'review_state.json'),'root_bodies':report['root_bodies']}
