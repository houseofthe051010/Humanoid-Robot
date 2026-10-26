import adsk.core,adsk.fusion,json
doc=next(x for x in app.documents if x.name=='Bilateral_legs_v12');doc.activate();d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'));root=d.rootComponent
go=root.occurrences.item(0);j=go.component.asBuiltJoints.itemByName('Right_Knee_pitch');j.timelineObject.rollTo(True)
try:j.jointMotion.rotationAxis=adsk.fusion.JointDirections.XAxisJointDirection
finally:d.timeline.moveToEnd()
adsk.doEvents();jp=j.createForAssemblyContext(go);jp.jointMotion.rotationValue=.5;adsk.doEvents()
co=next(o for o in go.component.occurrences if o.component.partNumber=='N04_Knee_pillow_block_L').createForAssemblyContext(go)
result={'axis':jp.jointMotion.rotationAxisVector.asArray(),'rotation_axis_enum':int(jp.jointMotion.rotationAxis),'matrix':co.transform2.asArray()}
jp.jointMotion.rotationValue=0;adsk.doEvents()
