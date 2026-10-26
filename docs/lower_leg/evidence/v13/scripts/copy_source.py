import adsk.core,adsk.fusion,json,time
OUT=ROOT/'v13';TM=adsk.fusion.TemporaryBRepManager.get()
source=next(x for x in app.documents if x.name=='Bilateral_legs_v12');sd=adsk.fusion.Design.cast(source.products.itemByProductType('DesignProductType'))
go=next(o for o in sd.rootComponent.occurrences if o.component.name=='Right_leg')
rows=[]
for co in go.component.occurrences:
 o=co.createForAssemblyContext(go);a=co.component.attributes.itemByName('SHIN','material')
 rows.append({'name':co.component.partNumber,'description':co.component.description,'material':a.value if a else '', 'visible':co.isLightBulbOn,'bodies':[(b.name,TM.copy(b),b.appearance,b.isLightBulbOn)for b in o.bRepBodies]})
doc=app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType);doc.name='Leg_chain_v13_source';d=adsk.fusion.Design.cast(app.activeProduct);d.designType=adsk.fusion.DesignTypes.DirectDesignType
m=adsk.core.Matrix3D.create();m.translation=adsk.core.Vector3D.create(-13,0,0)
for i,row in enumerate(rows):
 c=d.rootComponent.occurrences.addNewComponent(adsk.core.Matrix3D.create());c.component.name=row['name'];c.component.partNumber=row['name'];c.component.description=row['description'];c.component.attributes.add('SHIN','material',row['material'])
 for bn,b,ap,vis in row['bodies']:
  TM.transform(b,m);nb=c.component.bRepBodies.add(b);nb.name=bn;nb.appearance=d.appearances.itemByName(ap.name)or d.appearances.addByCopy(ap,ap.name);nb.isLightBulbOn=vis
 c.isLightBulbOn=row['visible']
 (OUT/'progress.json').write_text(json.dumps({'stage':'copy source','component':i+1,'total':len(rows)}))
result={'document':doc.name,'copied_components':len(rows),'provenance':'Live Right_leg solids with world transform, translated -130mm X; original archive retained. New revision uses copied geometry, not recovered source feature history.'}
(OUT/'source_copy.json').write_text(json.dumps(result,indent=2))
