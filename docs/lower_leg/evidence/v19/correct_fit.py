exec(compile((ROOT/'v19/common.py').read_text(),'<common>','exec'))
source=json.loads((OUT/'live_source_inventory.json').read_text());F=adsk.core.Matrix3D.create();F.setWithArray(next(p['transform'] for g in source['groups'] if g['name']=='Right_leg' for p in g['parts'] if p['part']=='Q02_CNC_yaw_to_roll_cradle'))
for go,s in ((right,1),(left,-1)):
 progress('correct measured fit '+go.component.name)
 ps=parts(go)
 def place(sh):return transform(sh,F) if s>0 else reflect(sh)
 # Cut the tube register again after adding the exterior screw lugs.
 o=ps['H06_Roll_tube_recessed_endcaps'];rows=[]
 for b in o.createForAssemblyContext(go).bRepBodies:
  shape=TM.copy(b)
  for a,c in ((-26.05,-22.9),(16.9,20.05)):
   tool=sub(rcyl(a,c,55.1),rcyl(a-.1,c+.1,52.9));sub(shape,place(tool))
  rows.append((b.name,shape))
 world_replace(go,o,rows,o.component.description,silver)
 o=ps['Q03_CNC_roll_to_pitch_fork'];sh=TM.copy(o.createForAssemblyContext(go).bRepBodies.item(0))
 sub(sh,place(rcyl(-36.2,30.2,57.2)));world_replace(go,o,[(o.component.name+'_clear_endcap_seats',sh)],o.component.description,silver)
 o=ps['Q02_CNC_yaw_to_roll_cradle'];sh=TM.copy(o.createForAssemblyContext(go).bRepBodies.item(0))
 for b in ps['T04_GWK7010_Hip_yaw_REFERENCE'].createForAssemblyContext(go).bRepBodies:sub(sh,TM.copy(b))
 world_replace(go,o,[(o.component.name+'_actual_yaw_locator_relief',sh)],o.component.description,silver)
for key in ('W02_Waist_front_shell','W03_Waist_rear_shell'):
 o=wp[key];shape=TM.copy(o.createForAssemblyContext(wg).bRepBodies.item(0))
 for go in (right,left):
  for k in ('H05_DJI10018_pitch_gearbox_shell_ESTIMATE','H07_Pitch_tube_recessed_endcaps'):
   for b in parts(go)[k].createForAssemblyContext(go).bRepBodies:sub(shape,TM.copy(b))
 sub(shape,cy((0,Y,875.5),(0,Y,897),39.3))
 world_replace(wg,o,[(key+'_actual_housing_boss_clearances',shape)],o.component.description,plastic)
exec(compile((OUT/'validate_fit.py').read_text(),'<recheck fit>','exec'))
