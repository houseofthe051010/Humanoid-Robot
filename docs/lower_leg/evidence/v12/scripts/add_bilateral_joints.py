import adsk.core,adsk.fusion,json,math
OUT=ROOT/'v12';dest=OUT/'deliverables';doc=next(x for x in app.documents if x.name=='Bilateral_legs_v12');doc.activate();d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'));root=d.rootComponent
# Solid reflection/copy is complete. As-built joints require parametric mode.
d.designType=adsk.fusion.DesignTypes.ParametricDesignType
rows=[r for r in json.loads((OUT/'joint_inventory.json').read_text())if not r['one'].startswith('ZZ_')and not r['two'].startswith('ZZ_')]
def sk_at(c,axis,coord,name):
 base={'x':c.yZConstructionPlane,'y':c.xZConstructionPlane,'z':c.xYConstructionPlane}[axis]
 sign=base.geometry.normal.asArray()[{'x':0,'y':1,'z':2}[axis]];pi=c.constructionPlanes.createInput();pi.setByOffset(base,adsk.core.ValueInput.createByReal(coord*sign));pl=c.constructionPlanes.add(pi);pl.isLightBulbOn=False
 sk=c.sketches.add(pl);sk.name=name;sk.isLightBulbOn=False;return sk
for go in root.occurrences:
 g=go.component;side=g.name.removesuffix('_leg');sgn=1 if side=='Right' else -1;cmap={o.component.partNumber:o for o in g.occurrences}
 for row in sorted(rows,key=lambda r:r['type']!=0):
  if g.asBuiltJoints.itemByName(side+'_'+row['name']):continue
  geom=None;origin=None
  if row['type']!=0:
   m=adsk.core.Matrix3D.create();m.setWithArray(row['transform']);origin=adsk.core.Point3D.create(sgn*(m.translation.x+13),m.translation.y,m.translation.z)
   sk=sk_at(g,'z',origin.z,row['name']+'_point');p=sk.sketchPoints.add(sk.modelToSketchSpace(origin));geom=adsk.fusion.JointGeometry.createByPoint(p)
  inp=g.asBuiltJoints.createInput(cmap[row['one']],cmap[row['two']],geom)
  if row['type']==0:inp.setAsRigidJointMotion()
  elif row['type']==1:
   a=row['axis'];ax=(a[0],sgn*a[1],sgn*a[2]);plane='y'if abs(ax[1])<1e-10 else'x';idx=1 if plane=='y'else 0
   sk=sk_at(g,plane,origin.asArray()[idx],row['name']+'_axis');end=adsk.core.Point3D.create(*(x+v for x,v in zip(origin.asArray(),ax)))
   line=sk.sketchCurves.sketchLines.addByTwoPoints(sk.modelToSketchSpace(origin),sk.modelToSketchSpace(end))
   geom=adsk.fusion.JointGeometry.createByCurve(line,adsk.fusion.JointKeyPointTypes.StartKeyPoint)
   inp=g.asBuiltJoints.createInput(cmap[row['one']],cmap[row['two']],geom)
   assert inp.setAsRevoluteJointMotion(adsk.fusion.JointDirections.ZAxisJointDirection)
  elif row['type']==6:inp.setAsBallJointMotion(adsk.fusion.JointDirections.ZAxisJointDirection,adsk.fusion.JointDirections.XAxisJointDirection)
  else:raise RuntimeError(str(row))
  j=g.asBuiltJoints.add(inp);j.name=side+'_'+row['name'];j.isLightBulbOn=False;j.isSuppressed=row['suppressed']
  if row['type']==1:
   lim=row['limits'];rl=j.jointMotion.rotationLimits;rl.minimumValue=lim['min'];rl.maximumValue=lim['max'];rl.isMinimumValueEnabled=lim['min_on'];rl.isMaximumValueEnabled=lim['max_on']
 for o in g.occurrences:o.isGroundToParent=o.component.partNumber=='S01_Ankle_to_oval_rail_adapter'
 for p in g.constructionPoints:p.isLightBulbOn=False
report=json.loads((OUT/'bilateral_build.json').read_text());report['joint_errors']=[];report['joint_counts']={go.component.name:go.component.asBuiltJoints.count for go in root.occurrences};report['joint_mode']='Parametric assembly after direct solid copy; source part history separately retained.'
(OUT/'bilateral_build.json').write_text(json.dumps(report,indent=2));assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(dest/'Bilateral_legs_v12.f3d')));result=report
