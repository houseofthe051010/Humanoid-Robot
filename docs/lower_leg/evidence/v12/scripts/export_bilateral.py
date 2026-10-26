import adsk.core,adsk.fusion,json
OUT=ROOT/'v12';dest=OUT/'deliverables';dest.mkdir(exist_ok=True);TM=adsk.fusion.TemporaryBRepManager.get()
doc=next(x for x in app.documents if x.name=='Bilateral_legs_v12');doc.activate();d=adsk.fusion.Design.cast(app.activeProduct);root=d.rootComponent
native=dest/'Bilateral_legs_v12.f3d';assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(native)))
rows=[]
for go in root.occurrences:
 for local in go.component.occurrences:
  o=local.createForAssemblyContext(go)
  if o.isLightBulbOn:
   a=o.component.attributes.itemByName('SHIN','material')
   rows.append({'side':go.component.name,'name':o.component.partNumber,'description':o.component.description,'material':a.value if a else '', 'bodies':[TM.copy(b)for b in o.bRepBodies if b.isLightBulbOn], 'body_names':[b.name for b in o.bRepBodies if b.isLightBulbOn]})
edoc=app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType);edoc.name='TEMP_v12_visible_STEP';ed=adsk.fusion.Design.cast(app.activeProduct);ed.designType=adsk.fusion.DesignTypes.DirectDesignType
egs={s:ed.rootComponent.occurrences.addNewComponent(adsk.core.Matrix3D.create()).component for s in ['Right_leg','Left_leg']}
for s,c in egs.items():c.name=s
for row in rows:
 c=egs[row['side']].occurrences.addNewComponent(adsk.core.Matrix3D.create()).component;c.name=row['name']
 for bn,b in zip(row['body_names'],row['bodies']):c.bRepBodies.add(TM.copy(b)).name=bn
assert ed.exportManager.execute(ed.exportManager.createSTEPExportOptions(str(dest/'Bilateral_legs_v12.step')))
edoc.close(False);doc.activate()
# Export each new custom component once per handed side. Purchasing/reference hardware excluded.
partdir=dest/'parts';partdir.mkdir(exist_ok=True);exports=[]
custom=('P01','P03','P04','P05','P08','P10','P11','Q01','Q02','Q03')
for row in rows:
 if not row['name'].startswith(custom):continue
 edoc=app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType);edoc.name='TEMP_v12_part';ed=adsk.fusion.Design.cast(app.activeProduct);ed.designType=adsk.fusion.DesignTypes.DirectDesignType
 for bn,b in zip(row['body_names'],row['bodies']):ed.rootComponent.bRepBodies.add(TM.copy(b)).name=bn
 p=partdir/(row['side']+'_'+row['name']+'.step');assert ed.exportManager.execute(ed.exportManager.createSTEPExportOptions(str(p)));exports.append(str(p));edoc.close(False)
doc.activate()
inventory=[{k:v for k,v in r.items()if k!='bodies'}|{'body_count':len(r['bodies']),'volume_mm3':sum(b.volume for b in r['bodies'])*1000}for r in rows]
(dest/'cad_inventory.json').write_text(json.dumps({'source':'live user v11 -> v12','spacing_mm':260,'inventory':inventory,'part_exports':exports,'native':str(native)},indent=2))
result={'native':str(native),'step':str(dest/'Bilateral_legs_v12.step'),'custom_parts':len(exports),'active_component_rows':len(inventory)}
