import adsk.core,adsk.fusion,math,json
def add_joints(design,group,component_map,rows,side='',sgn=1,offset_mm=0):
 design.designType=adsk.fusion.DesignTypes.ParametricDesignType
 def sk_at(axis,coord,name):
  base={'x':group.yZConstructionPlane,'y':group.xZConstructionPlane,'z':group.xYConstructionPlane}[axis]
  sign=base.geometry.normal.asArray()[{'x':0,'y':1,'z':2}[axis]]
  pi=group.constructionPlanes.createInput();pi.setByOffset(base,adsk.core.ValueInput.createByReal(coord*sign));pl=group.constructionPlanes.add(pi);pl.isLightBulbOn=False
  sk=group.sketches.add(pl);sk.name=name;sk.isLightBulbOn=False;return sk
 for row in sorted(rows,key=lambda x:x['type']!=0):
  name=(side+'_'if side else '')+row['name']
  if group.asBuiltJoints.itemByName(name):continue
  geom=None
  if row['type']!=0:
   m=adsk.core.Matrix3D.create();m.setWithArray(row['transform']);o=m.translation
   origin=adsk.core.Point3D.create(sgn*(o.x-13+offset_mm/10),o.y,43.56 if row['name']=='Knee_pitch'else o.z)
   if row['type']==1:
    a=row['axis'];ax=(a[0],sgn*a[1],sgn*a[2]);plane='y'if abs(ax[1])<1e-8 else'x';idx=1 if plane=='y'else 0
    sk=sk_at(plane,origin.asArray()[idx],name+'_axis');end=adsk.core.Point3D.create(*(x+v for x,v in zip(origin.asArray(),ax)))
    line=sk.sketchCurves.sketchLines.addByTwoPoints(sk.modelToSketchSpace(origin),sk.modelToSketchSpace(end));geom=adsk.fusion.JointGeometry.createByCurve(line,adsk.fusion.JointKeyPointTypes.StartKeyPoint)
   else:
    sk=sk_at('z',origin.z,name+'_point');p=sk.sketchPoints.add(sk.modelToSketchSpace(origin));geom=adsk.fusion.JointGeometry.createByPoint(p)
  inp=group.asBuiltJoints.createInput(component_map[row['one']],component_map[row['two']],geom)
  if row['type']==0:inp.setAsRigidJointMotion()
  elif row['type']==1:inp.setAsRevoluteJointMotion(adsk.fusion.JointDirections.ZAxisJointDirection)
  elif row['type']==6:inp.setAsBallJointMotion(adsk.fusion.JointDirections.ZAxisJointDirection,adsk.fusion.JointDirections.XAxisJointDirection)
  else:raise RuntimeError(str(row))
  j=group.asBuiltJoints.add(inp);j.name=name;j.isLightBulbOn=False;j.isSuppressed=row['suppressed']
  if row['type']==1:
   lim=row['limits'];l=j.jointMotion.rotationLimits;l.minimumValue=lim['min'];l.maximumValue=lim['max'];l.isMinimumValueEnabled=lim['min_on'];l.isMaximumValueEnabled=lim['max_on']
 for n,parent in [('P15_Separate_motor_backplate_and_rail_saddles','N04_Knee_pillow_block_L'),('V13_Chain_clearance_ENVELOPE','N04_Knee_pillow_block_L'),('N09_Knee_sprocket_standoff_hub','N00_Knee_joint_datum_NO_PHYSICAL_PART'),('N10_Drive_side_pedestal_hardware','N04_Knee_pillow_block_L')]:
  inp=group.asBuiltJoints.createInput(component_map[parent],component_map[n],None);inp.setAsRigidJointMotion();j=group.asBuiltJoints.add(inp);j.name=(side+'_'if side else '')+n+'_layout';j.isLightBulbOn=False
 for n,o in component_map.items():o.isGroundToParent=(n=='S01_Ankle_to_oval_rail_adapter')
 adsk.doEvents()
