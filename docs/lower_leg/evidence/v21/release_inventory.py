exec(compile((ROOT/'v21/common.py').read_text(),'<common>','exec'))
import csv
rows=[]
for go in (right,left,wg):
 for o in go.component.occurrences:
  c=o.component
  if not o.isLightBulbOn or c.partNumber.startswith('ZZ_') or c.bRepBodies.count==0:continue
  at=c.attributes.itemByName('SHIN','material')
  rows.append({'assembly':go.component.name,'part_number':c.partNumber,'name':c.name,'quantity':1,'active_bodies':c.bRepBodies.count,'material_reference':at.value if at else 'Source reference; see part record','description':c.description})
with (OUT/'BOM_V21.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
rep={'parts':len(rows),'active_waist_parts':sum(r['assembly']==wg.component.name for r in rows),'unhealthy_features':[]}
for go in (right,left,wg):
 for o in [go]+list(go.component.occurrences):
  for f in o.component.features:
   if int(f.healthState)!=0:rep['unhealthy_features'].append({'part':o.component.name,'feature':f.name,'health':int(f.healthState),'message':f.errorOrWarningMessage})
(OUT/'release_inventory.json').write_text(json.dumps(rep,indent=2));result=rep
