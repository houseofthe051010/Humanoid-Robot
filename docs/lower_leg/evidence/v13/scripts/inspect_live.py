import adsk.core,adsk.fusion,json
OUT=ROOT/'v13';OUT.mkdir(exist_ok=True)
doc=app.activeDocument;d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'));r=d.rootComponent
def body(b):
 return {'name':b.name,'visible':b.isVisible,'volume_mm3':b.volume*1000,'bounds':[[v*10 for v in p.asArray()]for p in [b.boundingBox.minPoint,b.boundingBox.maxPoint]]}
rows=[]
for go in r.occurrences:
 g=go.component
 for co in g.occurrences:
  o=co.createForAssemblyContext(go)
  rows.append({'group':g.name,'name':co.component.name,'part':co.component.partNumber,'visible':co.isLightBulbOn,'transform':o.transform2.asArray(),'bodies':[body(b)for b in o.bRepBodies]})
report={'document':doc.name,'rows':rows,'root_bodies':[body(b)for b in r.bRepBodies],'timeline':d.timeline.count}
(OUT/'live_inventory.json').write_text(json.dumps(report,indent=2))
result={'document':doc.name,'groups':[o.component.name for o in r.occurrences],'rows':len(rows)}
