import adsk.core,adsk.fusion,json,math
OUT=ROOT/'v21'
source_doc=next(q for q in app.documents if q.name.startswith('Humanoid_waist_battery_v21'))
opened=next(q for q in app.documents if q.name in ('Untitled','Waist_battery_v21'));opened.activate()
od=adsk.fusion.Design.cast(opened.products.itemByProductType('DesignProductType'));wc=od.rootComponent
assert any(o.component.name.startswith('U01_') for o in wc.occurrences)
report={'path':str(OUT/'deliverables/Waist_battery_v21.f3d'),'opened_document':opened.name,'joint_count':wc.asBuiltJoints.count,'axes':[],'bodies':0,'bad_bodies':[],'battery_dimensions_mm':None,'restored_part_numbers':[]}
assert wc.asBuiltJoints.count==32
src=adsk.fusion.Design.cast(source_doc.products.itemByProductType('DesignProductType'))
sg=next(o.component for o in src.rootComponent.occurrences if o.component.name.startswith('Waist_'))
for o in wc.occurrences:
 c=o.component;original=next((q.component for q in sg.occurrences if c.name==q.component.name or c.name==q.component.name+' (1)'),None)
 if original:
  c.partNumber=original.partNumber;c.description=original.description
  report['restored_part_numbers'].append(c.partNumber)
 for b in o.bRepBodies:
  report['bodies']+=1
  if not b.isSolid or b.volume<=0:report['bad_bodies'].append(o.name+'/'+b.name)
  if c.name.startswith('U01_'):
   bb=b.boundingBox;report['battery_dimensions_mm']=[(getattr(bb.maxPoint,k)-getattr(bb.minPoint,k))*10 for k in ('x','y','z')]
for n,want in (('WJ01_lower_waist_pitch',[1,0,0]),('WJ02_upper_waist_roll',[0,1,0])):
 j=wc.asBuiltJoints.itemByName(n);assert j and j.isValid
 a=list(j.jointMotion.rotationAxisVector.asArray());assert max(abs(abs(v)-w) for v,w in zip(a,want))<1e-6
 report['axes'].append({'name':n,'axis':a})
assert not report['bad_bodies'];assert max(abs(a-b) for a,b in zip(report['battery_dimensions_mm'],[140,85,160]))<.01
report['pass']=True
# Component exports reset metadata on import; retain the restored IDs in a full
# archive of the compact document, which already contains all 32 native joints.
opened.name='Waist_battery_v21'
p=OUT/'deliverables/Waist_battery_v21.f3d'
assert od.exportManager.execute(od.exportManager.createFusionArchiveExportOptions(str(p)))
report['bytes_after_metadata_restore']=p.stat().st_size
(OUT/'archive_reopen_validation.json').write_text(json.dumps(report,indent=2))
opened.close(False);source_doc.activate();result=report
