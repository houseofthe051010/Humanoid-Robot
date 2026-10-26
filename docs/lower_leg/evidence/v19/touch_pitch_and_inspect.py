exec(compile((ROOT/'v19/common.py').read_text(),'<common>','exec'))
assert not (OUT/'pitch_touch_committed.json').exists()
delta=PX-53;report={'pitch_center_x_mm':PX,'shift_per_side_mm':delta}
for go,s in ((right,1),(left,-1)):
 for key in ('T07_Hip_pitch_motor_ENVELOPE_REFERENCE','H05_DJI10018_pitch_gearbox_shell_ESTIMATE','H07_Pitch_tube_recessed_endcaps','H02_Hip_pitch_roll_bearing_REFERENCES'):
  o=parts(go)[key];inv=o.createForAssemblyContext(go).transform2.copy();inv.invert();vec=V3.create(s*delta/10,0,0);vec.transformBy(inv)
  mm=adsk.core.Matrix3D.create();mm.translation=vec;bs=adsk.core.ObjectCollection.create()
  for b in o.component.bRepBodies:bs.add(b)
  mi=o.component.features.moveFeatures.createInput2(bs);mi.defineAsFreeMove(mm);o.component.features.moveFeatures.add(mi).name='V19_rear_pitch_rims_touch_centerline'
report['ankle_parts']=[]
for o in right.component.occurrences:
 if o.component.partNumber.startswith(('L01','F08','M02')):
  report['ankle_parts'].append({'name':o.component.partNumber,'transform':list(o.createForAssemblyContext(right).transform2.asArray()),'bodies':[{'name':b.name,'volume':b.volume,'bounds':[list(b.boundingBox.minPoint.asArray()),list(b.boundingBox.maxPoint.asArray())]} for b in o.component.bRepBodies]})
report['waist']=[]
for o in wg.component.occurrences:
 if o.component.partNumber.startswith(('W05','W07','W19','W20')):
  p=o.createForAssemblyContext(wg);report['waist'].append({'part':o.component.partNumber,'transform':list(p.transform2.asArray()),'bodies':[{'name':b.name,'bounds':[list(b.boundingBox.minPoint.asArray()),list(b.boundingBox.maxPoint.asArray())]} for b in p.bRepBodies]})
(OUT/'pitch_touch_committed.json').write_text(json.dumps(report,indent=2));result=report
