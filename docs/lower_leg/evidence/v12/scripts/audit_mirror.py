import adsk.core,adsk.fusion,json
OUT=ROOT/'v12';doc=next(x for x in app.documents if x.name=='Bilateral_legs_v12');doc.activate();d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'));root=d.rootComponent;TM=adsk.fusion.TemporaryBRepManager.get()
gs={o.component.name:{x.component.partNumber:x.createForAssemblyContext(o) for x in o.component.occurrences}for o in root.occurrences}
m=adsk.core.Matrix3D.create();m.setCell(0,0,-1);bounds=[];shape=[];rel=[]
for n,ro in gs['Right_leg'].items():
 if not ro.isLightBulbOn:continue
 lo=gs['Left_leg'][n]
 assert ro.bRepBodies.count==lo.bRepBodies.count
 for rb,lb in zip(ro.bRepBodies,lo.bRepBodies):
  if not rb.isLightBulbOn:continue
  rt=TM.copy(rb);lt=TM.copy(lb);TM.transform(lt,m)
  e=max(abs(a-b)*10 for aa,bb in [(rt.boundingBox.minPoint,lt.boundingBox.minPoint),(rt.boundingBox.maxPoint,lt.boundingBox.maxPoint)]for a,b in zip(aa.asArray(),bb.asArray()))
  bounds.append({'part':n,'body':rb.name,'mirror_bound_error_mm':e})
  if n.startswith(('P03','P01','Q03')):
   vals=[]
   for a,b in [(rt,lt),(lt,rt)]:
    cp=TM.copy(a);ok=TM.booleanOperation(cp,TM.copy(b),adsk.fusion.BooleanTypes.DifferenceBooleanType);vals.append(cp.volume*1000 if ok else None)
   shape.append({'part':n,'body':rb.name,'bidirectional_difference_mm3':vals})
  if abs(rb.volume-lb.volume)*1000>.01:
   a=rb.getPhysicalProperties(adsk.fusion.CalculationAccuracy.HighCalculationAccuracy).volume;b=lb.getPhysicalProperties(adsk.fusion.CalculationAccuracy.HighCalculationAccuracy).volume
   rel.append({'part':n,'body':rb.name,'high_accuracy_volume_relative_difference':abs(a-b)/max(a,b),'high_accuracy_delta_mm3':abs(a-b)*1000})
result={'max_mirror_bound_error_mm':max(x['mirror_bound_error_mm']for x in bounds),'active_bodies_compared':len(bounds),'shape_difference_checks':shape,'higher_accuracy_volume_checks':rel}
(OUT/'mirror_geometry_audit.json').write_text(json.dumps(result,indent=2))
build=json.loads((OUT/'bilateral_build.json').read_text());build['initial_volume_estimate_deltas']=build.pop('mirrored_volume_errors',[]);build['mirror_geometry_audit']='mirror_geometry_audit.json';(OUT/'bilateral_build.json').write_text(json.dumps(build,indent=2))
