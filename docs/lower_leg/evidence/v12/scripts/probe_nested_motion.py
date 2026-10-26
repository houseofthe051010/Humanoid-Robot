import adsk.core,adsk.fusion,json,math
OUT=ROOT/'v12';doc=next(x for x in app.documents if x.name=='Bilateral_legs_v12');doc.activate();d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'));root=d.rootComponent
go=next(o for o in root.occurrences if o.component.name=='Right_leg');g=go.component;j=g.asBuiltJoints.itemByName('Right_Knee_pitch');co=next(o for o in g.occurrences if o.component.partNumber=='N04_Knee_pillow_block_L');proxy=co.createForAssemblyContext(go)
rows=[]
for label,jj in [('native',j),('context',j.createForAssemblyContext(go))]:
 try:
  jj.jointMotion.rotationValue=.5;adsk.doEvents()
  rows.append({'set_on':label,'value':jj.jointMotion.rotationValue,'native_matrix':co.transform2.asArray(),'proxy_matrix':proxy.transform2.asArray(),'root_path_matrices':[(o.fullPathName,o.transform2.asArray())for o in root.allOccurrences if o.component.partNumber=='N04_Knee_pillow_block_L'],'group_matrix':go.transform2.asArray(),'axis':jj.jointMotion.rotationAxisVector.asArray(),'joint_transform':jj.transform.asArray(),'group_grounded':go.isGrounded,'child_ground_to_parent':co.isGroundToParent})
 finally:jj.jointMotion.rotationValue=0;adsk.doEvents()
result=rows;(OUT/'nested_motion_probe.json').write_text(json.dumps(rows,indent=2))
