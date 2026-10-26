import adsk.core,adsk.fusion,json
from pathlib import Path
out=ROOT/'v12';out.mkdir(exist_ok=True)
rows=[]
for doc in app.documents:
 d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'))
 row={'name':doc.name,'active':doc==app.activeDocument,'design':bool(d)}
 if d:
  row['components']=[]
  for o in d.rootComponent.occurrences:
   c=o.component
   cr={'name':c.name,'visible':o.isLightBulbOn,'transform':o.transform2.asArray(),'bodies':[]}
   for b in o.bRepBodies:
    cr['bodies'].append({'name':b.name,'volume_mm3':b.volume*1000,'bounds':[[v*10 for v in b.boundingBox.minPoint.asArray()],[v*10 for v in b.boundingBox.maxPoint.asArray()]]})
   if c.name.startswith(('N06','R01','T04','T07')):cr['features']=[f.name for f in c.features]
   row['components'].append(cr)
 rows.append(row)
(out/'live_inventory.json').write_text(json.dumps(rows,indent=2))
result={'documents':[{'name':r['name'],'active':r['active'],'components':len(r.get('components',[]))}for r in rows],'details':str(out/'live_inventory.json')}

