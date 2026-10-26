import adsk.core,adsk.fusion
doc=next(x for x in app.documents if x.name=='Bilateral_legs_v12');doc.activate();d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'));root=d.rootComponent;result=[]
for go in root.occurrences:
 for name in ['Knee_pitch','Ankle_roll']:
  line=go.component.sketches.itemByName(name+'_axis').sketchCurves.sketchLines.item(0)
  geo=adsk.fusion.JointGeometry.createByCurve(line,adsk.fusion.JointKeyPointTypes.StartKeyPoint)
  result.append({'side':go.component.name,'name':name,'line':line.worldGeometry.startPoint.vectorTo(line.worldGeometry.endPoint).asArray(),'primary':geo.primaryAxisVector.asArray(),'secondary':geo.secondaryAxisVector.asArray(),'third':geo.thirdAxisVector.asArray()})
