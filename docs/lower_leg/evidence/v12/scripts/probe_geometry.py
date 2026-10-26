import adsk.core,adsk.fusion,json
d=adsk.fusion.Design.cast(app.activeProduct);r=d.rootComponent;tm=adsk.fusion.TemporaryBRepManager.get()
ocs={o.component.name:o for o in r.occurrences}
fixed=ocs['T04_GWK7010_Hip_yaw_REFERENCE'].component.bRepBodies.item(0)
cyl=[]
for f in fixed.faces:
 g=adsk.core.Cylinder.cast(f.geometry)
 if g and abs(g.axis.z)>.99 and g.radius<.4:cyl.append({'r':g.radius*10,'o':[v*10 for v in g.origin.asArray()]})
a=tm.copy(ocs['T07_Hip_pitch_motor_ENVELOPE_REFERENCE'].bRepBodies.item(0));b=tm.copy(ocs['T09_Hip_roll_motor_ENVELOPE_REFERENCE'].bRepBodies.item(0));tm.booleanOperation(a,b,adsk.fusion.BooleanTypes.IntersectionBooleanType)
mirror=adsk.core.Matrix3D.create();mirror.setCell(0,0,-1);test=tm.copy(fixed)
ok=tm.transform(test,mirror)
result={'yaw_small_cylinders':cyl,'pitch_roll_overlap_mm3':a.volume*1000,'temporary_reflection_ok':ok,'mirror_volume':test.volume,'joints':[{'name':j.name,'one':j.occurrenceOne.component.name,'two':j.occurrenceTwo.component.name,'type':j.jointMotion.jointType}for j in r.asBuiltJoints]}
(ROOT/'v12/geometry_probe.json').write_text(json.dumps(result,indent=2))
