import adsk.core,adsk.fusion,json
OUT=ROOT/'v14'
doc=next(x for x in app.documents if x.name=='Bilateral_legs_v13');doc.activate();d=adsk.fusion.Design.cast(app.activeProduct)
rows=[]
for go in d.rootComponent.occurrences:
 for co in go.component.occurrences:
  if not co.isLightBulbOn:continue
  bs=[]
  for b in co.bRepBodies:
   bb=b.boundingBox;bs.append({'name':b.name,'min':[v*10 for v in bb.minPoint.asArray()],'max':[v*10 for v in bb.maxPoint.asArray()],'volume':b.volume*1000})
  rows.append({'side':go.component.name,'part':co.component.partNumber,'bodies':bs})
(OUT/'live_inventory.json').write_text(json.dumps(rows,indent=2))
result={'document':doc.name,'modified':doc.isModified,'rows':len(rows),'selected':[r for r in rows if r['side']=='Right_leg' and r['part'].startswith(('N01','S05','S06','P01'))]}
