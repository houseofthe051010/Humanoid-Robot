exec(compile((ROOT/'v11/common.py').read_text(),'<common>','exec'))
Y=23.343134;K=423.6;Z=600.;H=743.6;thigh='N04_Knee_pillow_block_L'
progress('shorten thigh and lower motor')
for side in ['L','R']:
 c=parts['N06_Upper_leg_oval_stub_'+side].component
 box(c,'Trim_thigh_rail_to_680mm',(-70,Y-60,680),(70,Y+60,810),OP.CutFeatureOperation)
 c.description='V11 thigh rail:18x10 oval,233.8mm long fromZ446.2to680;320mm knee-to-hip reference.'
for n in list(parts):
 if n.startswith(('R01','T01','T02','T03')):move_bodies(parts[n].component,(0,0,-85),'Knee_motor_package_down_85mm')
move_bodies(parts['T04_GWK7010_Hip_yaw_REFERENCE'].component,(0,0,-118),'Yaw_to_thigh_neck_below_roll')
move_bodies(parts['T05_Hip_crosshead_REFERENCE'].component,(0,0,-118),'Crosshead_to_shorter_rail_top')
c=rebuild('T07_Hip_pitch_motor_ENVELOPE_REFERENCE')
c.description='Hip pitch reference,unselected100x40mm motor envelope;user-specified25 degree tilt. Axis orientation sign remains layout convention.'
cylinder(c,'Hip_pitch_100x40_REFERENCE',(-108,Y,H),(-68,Y,H),50)
m=adsk.core.Matrix3D.create();m.setToRotation(math.radians(25),V3.create(0,1,0),pt((-88,Y,H)))
mi=c.features.moveFeatures.createInput2(obj(list(c.bRepBodies)));mi.defineAsFreeMove(m);c.features.moveFeatures.add(mi).name='User_specified_25deg_pitch_tilt'
color(c,'T07_Hip_pitch_motor_ENVELOPE_REFERENCE_finish')
c=rebuild('T06_Pelvis_HALF_REFERENCE')
rounded_solid(c,'Compact_pelvis_reference','z',803,32,(-116,Y-35),(52,Y+88),10)
color(c,'T06_Pelvis_HALF_REFERENCE_finish')
c.description='Compact half-pelvis reference only;load path and full-width pelvis unresolved.'
c=part('T09_Hip_roll_motor_ENVELOPE_REFERENCE','unselected motor envelope','Distinct hip roll:90mm diameter x36mm reference,axis alongY throughX0/Z743.6. Positioned fore-aft clear of yaw;motor and bearing design unresolved.')
cylinder(c,'Hip_roll_90x36_REFERENCE',(0,Y+45,H),(0,Y+81,H),45)
joint('Hip_roll_reference_to_thigh_LAYOUT_ONLY',thigh,c.name)
c.attributes.add('SHIN','exclude_from_mass_and_structure','true')
ap=d.appearances.addByCopy(d.appearances.itemByName('T07_Hip_pitch_motor_ENVELOPE_REFERENCE_finish'),'Hip_roll_reference_teal')
prop=ap.appearanceProperties.itemById('opaque_albedo') or ap.appearanceProperties.itemById('generic_diffuse')
if prop:adsk.core.ColorProperty.cast(prop).value=adsk.core.Color.create(68,130,137,255)
for b in c.bRepBodies:b.appearance=ap
c=parts['T08_Transmission_and_height_REFERENCE_SKETCHES'].component
for sk in c.sketches:sk.isLightBulbOn=False
for name,x,centers in [('V11_primary_2p5_reference',-30,[(Y,Z,20),(Y,500,50)]),('V11_final_1to1_reference',-24,[(Y,500,35),(Y,K,35)])]:
 sk=sketch(c,'x',x,name)
 for yy,zz,r in centers:circle(sk,'x',x,yy,zz,r)
 sk.isLightBulbOn=False
sk=sketch(c,'x',37.99,'V11_encoder_28dia_5axial');circle(sk,'x',37.99,Y,Z,14)
sk=sketch(c,'y',Y,'V11_hip_axes_and_320mm_height')
for a,b in [((-110,Y,H),(65,Y,H)),((0,Y,688),(0,Y,763)),((-88-45*math.cos(math.radians(25)),Y,H+45*math.sin(math.radians(25))),(-88+45*math.cos(math.radians(25)),Y,H-45*math.sin(math.radians(25))))]:
 sk.sketchCurves.sketchLines.addByTwoPoints(sk.modelToSketchSpace(pt(a)),sk.modelToSketchSpace(pt(b)))
for n,value in [('layout_thigh_axis_length',320),('layout_knee_motor_height',176.4)]:d.userParameters.itemByName(n).value=value/10
d.userParameters.add('layout_hip_pitch_tilt',V.createByString('25 deg'),'deg','User specified angle;motor envelope only')
params={'target_height_mm':1600.2,'ground_z_mm':-14,'knee_axis_z_mm':K,'hip_pitch_roll_reference_z_mm':H,'thigh_axis_length_mm':320,'standing_hip_height_mm':H+14,'thigh_rail_length_mm':233.8,'rail_top_z_mm':680,'motor_axis_z_mm':Z,'motor_down_from_v10_mm':85,'motor_above_knee_mm':Z-K,'encoder_axial_gap_mm':5,'hip_pitch_tilt_deg':25,'yaw_axis':'Z','yaw_motor_rear_z_mm':690.8,'roll_axis':'Y','roll_envelope_diameter_mm':90,'roll_envelope_width_mm':36,'pitch_envelope_diameter_mm':100,'pitch_envelope_width_mm':40,'intermediate_reference_z_mm':500,'primary_plane_x_mm':-30,'secondary_plane_x_mm':-24}
(OUT/'layout_parameters.json').write_text(json.dumps(params,indent=2))
save_checkpoint('Compact_layout_checkpoint')
result=params
