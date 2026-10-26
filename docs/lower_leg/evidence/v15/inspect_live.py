import adsk.core,adsk.fusion,json
OUT=ROOT/'v15';doc=app.activeDocument;d=adsk.fusion.Design.cast(app.activeProduct);assert doc.name=='Bilateral_legs_v14',doc.name
rows=[]
for go in d.rootComponent.occurrences:
 for co in go.component.occurrences:
  if co.component.partNumber.startswith(('P','T04','T07','T09','Q','N06','R01')) and co.isLightBulbOn:
   bs=[]
   for b in co.bRepBodies:
    bb=b.boundingBox;bs.append({'name':b.name,'min':[x*10 for x in bb.minPoint.asArray()],'max':[x*10 for x in bb.maxPoint.asArray()],'volume':b.volume*1000})
   rows.append({'side':go.component.name,'part':co.component.partNumber,'description':co.component.description,'bodies':bs})
(OUT/'live_inventory.json').write_text(json.dumps(rows,indent=2))
result={'document':doc.name,'parts':len(rows),'pitch_yaw':[r for r in rows if r['side']=='Right_leg'and r['part'].startswith(('T04','T07'))]}
