exec(compile((ROOT/'v11/common.py').read_text(),'<common>','exec'))
dest=OUT/'deliverables';dest.mkdir(exist_ok=True)
status='V11 compact upper-leg layout:320mm thigh,85mm lower knee motor,25deg pitch and distinct roll reference;curved removable fairings. Geometry prototype,not strength-qualified.'
d.attributes.add('SHIN','build_status',status);d.attributes.add('SHIN','status',status)
root.asBuiltJoints.itemByName('Knee_pitch').jointMotion.rotationValue=0;adsk.doEvents()
# Restore reviewed views and reference-sketch visibility before saving native design.
scope={'ROOT':ROOT,'app':app,'adsk':adsk,'result':None}
exec(compile((OUT/'capture_layout.py').read_text(),'capture_layout','exec'),scope)
native=dest/'Leg_compact_shelled_v11.f3d'
assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(native)))
exchange=app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType);exchange.name='TEMP_v11_exchange'
ed=adsk.fusion.Design.cast(app.activeProduct);ed.designType=adsk.fusion.DesignTypes.DirectDesignType
inventory=[]
for o in root.occurrences:
 c=o.component;n=c.name
 if n.startswith(('U0','K01','GIM','N00','S04')):continue
 if c.bRepBodies.count:
  target=ed.rootComponent.occurrences.addNewComponent(adsk.core.Matrix3D.create()).component;target.name=n
  for b in o.bRepBodies:target.bRepBodies.add(TM.copy(b)).name=b.name
 attr=c.attributes.itemByName('SHIN','material')
 inventory.append({'name':n,'description':c.description,'material':attr.value if attr else 'See BOM','body_count':c.bRepBodies.count,'volume_cm3':sum(b.volume for b in c.bRepBodies)})
assert ed.exportManager.execute(ed.exportManager.createSTEPExportOptions(str(dest/'Leg_compact_shelled_v11.step')))
exchange.close(False);doc.activate()
exports=[];(dest/'upper_leg_parts').mkdir(exist_ok=True)
for n in parts:
 if not n.startswith(('T01','T02','T10','T11','T12')):continue
 c=parts[n].component
 pd=app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType);pd.name='TEMP_v11_mount_part'
 dd=adsk.fusion.Design.cast(app.activeProduct);dd.designType=adsk.fusion.DesignTypes.DirectDesignType
 for b in c.bRepBodies:dd.rootComponent.bRepBodies.add(TM.copy(b)).name=b.name
 path=dest/'upper_leg_parts'/(c.name+'.step')
 assert dd.exportManager.execute(dd.exportManager.createSTEPExportOptions(str(path)))
 exports.append(str(path));pd.close(False)
doc.activate()
(dest/'cad_inventory.json').write_text(json.dumps({'status':status,'native':str(native),'components':root.occurrences.count,'joints':root.asBuiltJoints.count,'inventory':inventory,'part_exports':exports},indent=2))
result={'native':str(native),'step':str(dest/'Leg_compact_shelled_v11.step'),'components':root.occurrences.count,'joints':root.asBuiltJoints.count,'part_exports':len(exports)}
