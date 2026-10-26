import adsk.core,adsk.fusion,json,math
OUT=ROOT/'v12';doc=next(x for x in app.documents if x.name=='Bilateral_legs_v12');doc.activate();d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'));root=d.rootComponent
rows={r['name']:r for r in json.loads((OUT/'joint_inventory.json').read_text())if r['type']==1}
out=[]
for go in root.occurrences:
 g=go.component;side=g.name.removesuffix('_leg');sgn=1 if side=='Right'else -1
 for name,row in rows.items():
  j=g.asBuiltJoints.itemByName(side+'_'+name);j.jointMotion.rotationValue=0
  a=row['axis'];ax=(a[0],sgn*a[1],sgn*a[2]);sk=g.sketches.itemByName(name+'_axis');line=sk.sketchCurves.sketchLines.item(0)
  # A curve-derived joint frame puts its primary Z axis exactly along the line.
  # The custom-axis property had silently retained the old sketch-normal axis.
  j.timelineObject.rollTo(True)
  try:
   j.geometry=adsk.fusion.JointGeometry.createByCurve(line,adsk.fusion.JointKeyPointTypes.StartKeyPoint)
   j.jointMotion.rotationAxis=adsk.fusion.JointDirections.ZAxisJointDirection
  finally:d.timeline.moveToEnd()
  adsk.doEvents()
  got=j.createForAssemblyContext(go).jointMotion.rotationAxisVector.asArray()
  out.append({'side':side,'joint':name,'wanted':ax,'got':got,'axis_error':max(abs(a-b)for a,b in zip(ax,got))})
(OUT/'axis_repair.json').write_text(json.dumps(out,indent=2));result=out
