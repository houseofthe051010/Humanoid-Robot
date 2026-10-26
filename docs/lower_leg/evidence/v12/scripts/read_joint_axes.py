import adsk.core,adsk.fusion,json
OUT=ROOT/'v12';doc=next(x for x in app.documents if x.name=='Bilateral_legs_v12');doc.activate();d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'));d.computeAll();adsk.doEvents();root=d.rootComponent
result=[]
for go in root.occurrences:
 for j in go.component.asBuiltJoints:
  if j.jointMotion.jointType!=1:continue
  m=j.createForAssemblyContext(go).jointMotion;ax=m.customRotationAxisEntity
  row={'name':j.name,'axis':m.rotationAxisVector.asArray(),'type':int(m.rotationAxis),'angle_deg':m.rotationValue*180/3.141592653589793,'custom':ax.objectType if ax else None}
  if ax and ax.objectType==adsk.fusion.SketchLine.classType():
   geo=ax.worldGeometry;row['line_world_vector']=geo.startPoint.vectorTo(geo.endPoint).asArray()
  result.append(row)
(OUT/'current_joint_axes.json').write_text(json.dumps(result,indent=2))
