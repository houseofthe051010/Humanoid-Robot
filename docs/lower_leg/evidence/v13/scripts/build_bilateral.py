exec(compile((ROOT/'v13/common.py').read_text(),'<common>','exec'))
exec(compile((OUT/'native_joints.py').read_text(),'<joint_helpers>','exec'))
dest=OUT/'deliverables';dest.mkdir(exist_ok=True)
assert not any(x.name=='Bilateral_legs_v13' for x in app.documents),'Existing v13 pair; inspect before replacing'
assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(dest/'Leg_chain_v13_source.f3d')))
rows=json.loads((OUT/'source_joint_inventory.json').read_text())
source=[]
for n,o in parts.items():
 a=o.component.attributes.itemByName('SHIN','material')
 source.append({'name':n,'description':o.component.description,'material':a.value if a else '', 'visible':o.isLightBulbOn,'bodies':[(b.name,TM.copy(b),b.appearance,b.isLightBulbOn)for b in o.bRepBodies]})
doc=app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType);doc.name='Bilateral_legs_v13'
d=adsk.fusion.Design.cast(app.activeProduct);d.designType=adsk.fusion.DesignTypes.DirectDesignType;root=d.rootComponent
d.attributes.add('SHIN','status','V13 paired chain packaging from preserved live v12 right-leg solids. Reconstructed native joints; original part feature history remains in preserved input. Provisional 260mm spacing, no strength qualification.')
cache={};groups={};maps={}
for side,sgn in [('Right',1),('Left',-1)]:
 progress('reflect solids '+side)
 go=root.occurrences.addNewComponent(adsk.core.Matrix3D.create());g=go.component;g.name=side+'_leg';groups[side]=go;go.isGrounded=True
 tr=adsk.core.Matrix3D.create();tr.setCell(0,0,sgn);tr.translation=V3.create(sgn*13,0,0);cmap={}
 for row in source:
  co=g.occurrences.addNewComponent(adsk.core.Matrix3D.create());c=co.component;c.name=side+'_'+row['name'];c.partNumber=row['name'];c.description=row['description'];c.attributes.add('SHIN','material',row['material'])
  for bn,b,ap0,vis in row['bodies']:
   cp=TM.copy(b);assert TM.transform(cp,tr);nb=c.bRepBodies.add(cp);nb.name=bn
   if ap0.name not in cache:cache[ap0.name]=d.appearances.itemByName(ap0.name)or d.appearances.addByCopy(ap0,ap0.name)
   nb.appearance=cache[ap0.name];nb.isLightBulbOn=vis
  co.isLightBulbOn=row['visible'];cmap[row['name']]=co
 maps[side]=cmap
for side,sgn in [('Right',1),('Left',-1)]:
 progress('native joints '+side);add_joints(d,groups[side].component,maps[side],rows,side,sgn,130)
result={'spacing_mm':260,'components_per_leg':len(source),'joints':{s:o.component.asBuiltJoints.count for s,o in groups.items()}}
(OUT/'bilateral_build.json').write_text(json.dumps(result,indent=2))
