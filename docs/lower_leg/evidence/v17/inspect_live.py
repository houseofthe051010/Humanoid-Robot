import adsk.core, adsk.fusion, json

OUT=ROOT/'v17';OUT.mkdir(exist_ok=True)
data={'documents':[{'name':x.name,'active':x==app.activeDocument} for x in app.documents],
      'active':app.activeDocument.name if app.activeDocument else None,'groups':[]}
d=adsk.fusion.Design.cast(app.activeProduct)
def xyz(p):return [round(v*10,5) for v in p.asArray()]
if d:
    for go in d.rootComponent.occurrences:
        gc=go.component
        group={'name':gc.name,'transform':list(go.transform2.asArray()),'parts':[],
               'joints':[{'name':j.name,'valid':j.isValid,'suppressed':j.isSuppressed,
                          'angle':getattr(j.jointMotion,'rotationValue',None)} for j in gc.asBuiltJoints]}
        for o in gc.occurrences:
            c=o.component
            part={'name':c.name,'part':c.partNumber,'visible':o.isLightBulbOn,
                  'transform':list(o.transform2.asArray()),'bodies':[]}
            detail=c.partNumber.startswith(('W','Q','T04','T07','T09','N04','P01'))
            for b in c.bRepBodies:
                bb=b.boundingBox
                row={'name':b.name,'volume':b.volume*1000,'min':xyz(bb.minPoint),'max':xyz(bb.maxPoint)}
                if detail:
                    row['cylinders']=[]
                    row['planes']=[]
                    for f in b.faces:
                        g=adsk.core.Cylinder.cast(f.geometry)
                        if g:
                            row['cylinders'].append({'radius':round(g.radius*10,5),'origin':xyz(g.origin),
                                'axis':list(g.axis.asArray()),'min':xyz(f.boundingBox.minPoint),'max':xyz(f.boundingBox.maxPoint)})
                        plane=adsk.core.Plane.cast(f.geometry)
                        if plane and f.area>0.05:
                            row['planes'].append({'origin':xyz(plane.origin),'normal':list(plane.normal.asArray()),
                                'area':round(f.area*100,5),'loops':f.loops.count})
                part['bodies'].append(row)
            group['parts'].append(part)
        data['groups'].append(group)
(OUT/'live_inventory.json').write_text(json.dumps(data,indent=2))
result={'documents':data['documents'],'groups':[{'name':g['name'],'parts':len(g['parts'])} for g in data['groups']]}
