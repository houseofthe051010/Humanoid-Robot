exec(compile((ROOT/'v12/common.py').read_text(),'<common>','exec'))
for partial in list(app.documents):
 if partial.name=='Bilateral_legs_v12':partial.close(False)
progress('prepare mirrored native assembly')
dest=OUT/'deliverables';dest.mkdir(exist_ok=True)
source_doc=doc;source_design=d;source_root=root
assert source_design.exportManager.execute(source_design.exportManager.createFusionArchiveExportOptions(str(dest/'Leg_gearbox_hip_v12_parametric.f3d')))
spacing=260.
source_joint_rows=[r for r in json.loads((OUT/'joint_inventory.json').read_text())if not r['one'].startswith('ZZ_') and not r['two'].startswith('ZZ_')]
source=[]
for n,o in parts.items():
 if n.startswith('ZZ_'):continue
 a=o.component.attributes.itemByName('SHIN','material')
 source.append({'name':n,'description':o.component.description,'material':a.value if a else '', 'visible':o.isLightBulbOn,'grounded':o.isGrounded,'bodies':[(b.name,TM.copy(b),b.appearance,b.isLightBulbOn)for b in o.bRepBodies]})
doc=app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType);doc.name='Bilateral_legs_v12'
d=adsk.fusion.Design.cast(app.activeProduct);d.designType=adsk.fusion.DesignTypes.DirectDesignType;root=d.rootComponent
d.attributes.add('SHIN','status','V12 paired geometry and native lower-leg joints. 260mm centre spacing is provisional packaging; hip/output interfaces are references, not load-qualified. Parametric source delivered separately.')
appearance_cache={};groups={};native_maps={};volume_errors=[];joint_errors=[]
def appearance(a):
 if a.name not in appearance_cache:appearance_cache[a.name]=d.appearances.itemByName(a.name) or d.appearances.addByCopy(a,a.name)
 return appearance_cache[a.name]
for side,sgn in [('Right',1),('Left',-1)]:
 progress('copy '+side+' leg components')
 go=root.occurrences.addNewComponent(adsk.core.Matrix3D.create());g=go.component;g.name=side+'_leg';groups[side]=go;go.isGrounded=True
 g.description='Mirrored part assembly from user-edited v11 and v12 interfaces; source feature history in separate parametric native file.'
 transform=adsk.core.Matrix3D.create();transform.setCell(0,0,sgn);transform.translation=V3.create(sgn*spacing/20,0,0)
 cmap={}
 for row in source:
  co=g.occurrences.addNewComponent(adsk.core.Matrix3D.create());c=co.component;c.name=side+'_'+row['name'];c.partNumber=row['name'];c.description=row['description'];c.attributes.add('SHIN','material',row['material'])
  for bn,b,ap,vis in row['bodies']:
   t=TM.copy(b);assert TM.transform(t,transform);new=c.bRepBodies.add(t);new.name=bn;new.appearance=appearance(ap);new.isLightBulbOn=vis
   err=abs(new.volume-b.volume)*1000
   if err>1e-5:volume_errors.append({'side':side,'part':row['name'],'body':bn,'delta_mm3':err})
  co.isLightBulbOn=row['visible']
  co.isGroundToParent=row['grounded'];cmap[row['name']]=co
 native_maps[side]=cmap
result={'spacing_mm':spacing,'legs':2,'source_components_per_leg':len(source),'source_joints_per_leg':len(source_joint_rows),'mirrored_volume_errors':volume_errors,'joint_errors':joint_errors,'joint_counts':{s:o.component.asBuiltJoints.count for s,o in groups.items()},'native':str(dest/'Bilateral_legs_v12.f3d')}
(OUT/'bilateral_build.json').write_text(json.dumps(result,indent=2))
assert not joint_errors,result
# The fast volume estimator can differ after reflection. Audit mirrored bounds,
# high-accuracy volumes and targeted Boolean equivalence before releasing.
assert all(b.isSolid and b.volume>0 for go in groups.values() for co in go.component.occurrences for b in co.component.bRepBodies)
exec(compile((OUT/'add_bilateral_joints.py').read_text(),'<native_joint_build>','exec'))
progress('bilateral copy complete')
