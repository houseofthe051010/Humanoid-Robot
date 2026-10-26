exec(compile((ROOT/'v10/common.py').read_text(),'<common>','exec'))
Y=23.343134;Z=685.;K=423.6;H=823.6
thigh='N04_Knee_pillow_block_L'
assert 'T01_Knee_motor_rail_shell_PROVISIONAL' not in parts,'Already built; inspect before retry'
progress('extend live thigh rails and position motor')
# Preserve the user's 200 mm rail extension and add 61.8 mm to a 798 mm top datum.
for side in ['L','R']:
 c=parts['N06_Upper_leg_oval_stub_'+side].component
 b=c.bRepBodies.item(0);top=b.boundingBox.maxPoint.z*10
 face=max((f for f in b.faces if abs(f.boundingBox.maxPoint.z-f.boundingBox.minPoint.z)<1e-6),key=lambda f:f.boundingBox.maxPoint.z)
 sk=c.sketches.add(face);sk.name='Upper_leg_400mm_axis_length_rail_extension'
 # A sketch on the annular end face includes the projected outer and inner loops.
 region=next(p for p in sk.profiles if p.profileLoops.count==2)
 ei=c.features.extrudeFeatures.createInput(region,OP.JoinFeatureOperation)
 ei.setDistanceExtent(False,V.createByReal((798-top)/10))
 c.features.extrudeFeatures.add(ei).name='Rail_top_798mm_for_400mm_thigh'
 sk.isLightBulbOn=False
 c.description='Continuous thigh rail: 351.8 mm cut length from Z446.2 to798; 18x10 oval, long axis Y; wall inherited assumption 0.55 mm.'
# Flip about vertical through X11 so stationary rear bosses face the right rail.
c=parts['R01_DJI_10018_77KV_ESTIMATED_REFERENCE'].component
j=root.asBuiltJoints.itemByName('DJI_reference_parked_only');j.deleteMe()
m=adsk.core.Matrix3D.create();m.setToRotation(math.pi,V3.create(0,0,1),pt((11,Y,Z)))
mi=c.features.moveFeatures.createInput2(obj(list(c.bRepBodies)));mi.defineAsFreeMove(m)
c.features.moveFeatures.add(mi).name='Stationary_rear_to_right_rail_drive_to_left'
joint('Knee_motor_on_thigh_LAYOUT',thigh,c.name)
c.description='DJI10018 estimated motor at knee+261.4 mm. Rear hub X33 to right rail inner face X38 leaves 5mm encoder gap. Gearbox omitted.'
progress('build thick split motor-to-rail shell')
c=part('T01_Knee_motor_rail_shell_PROVISIONAL','printed PA-CF - grade/orientation TBD','8mm rear mounting web; two split oval saddles; estimated motor pattern40x66; not strength-qualified')
rounded_solid(c,'Eight_mm_rear_web','x',29,8,(Y-29,Z-44),(Y+29,Z+44),9)
holes(c,'x',28.9,8.2,[(Y,Z,21)],'Central_hub_and_encoder_access_42mm')
holes(c,'x',28.9,8.2,[(Y+s*20,Z+t*33,2.25)for s in [-1,1]for t in [-1,1]],'Four_M4_clearance_EST_40x66')
# Saddles deliberately leave the shaft/encoder region open and do not drill thin steel rails.
for sign in [-1,1]:
 zz=Z+sign*44
 rounded_solid(c,'Rail_saddle_'+str(sign),'z',zz-14,28,(32,Y-30),(42.75,Y+30),3,OP.JoinFeatureOperation)
 # Exact Y-oriented 18x10 stadium plus 0.3 mm diametral provisional print clearance.
 sk=sketch(c,'z',zz-14.1,'Right_rail_socket_'+str(sign));hull(sk,'z',zz-14.1,(43,Y-4),(43,Y+4),5.15)
 extrude(c,sk,'z',28.2,OP.CutFeatureOperation,'Half_socket_'+str(sign))
 holes(c,'x',31.9,11,[(Y+s*22,Z+sign*48,2.25)for s in [-1,1]],'M4_clamp_clearances_'+str(sign))
# Bottom exit for the preserved motor phase-wire envelope.
box(c,'Motor_wire_exit',(28.8,Y-6,Z-60),(38.1,Y+6,Z-34),OP.CutFeatureOperation)
color(c);joint('Knee_mount_shell_to_thigh_LAYOUT',thigh,c.name)
for sign,label in [(-1,'Lower'),(1,'Upper')]:
 c=part('T02_Rail_clamp_cap_'+label+'_PROVISIONAL','printed PA-CF - grade/orientation TBD','Removable M4 split-clamp cap; no rail cross-drilling; preload and slip strength unresolved')
 zz=Z+sign*44
 rounded_solid(c,'Outer_split_cap','z',zz-14,28,(43.25,Y-30),(54,Y+30),3)
 sk=sketch(c,'z',zz-14.1,'Oval_half_socket');hull(sk,'z',zz-14.1,(43,Y-4),(43,Y+4),5.15)
 extrude(c,sk,'z',28.2,OP.CutFeatureOperation,'Outer_half_socket')
 holes(c,'x',43.2,11,[(Y+s*22,Z+sign*48,2.25)for s in [-1,1]],'M4_cap_clearances')
 color(c);joint('Knee_cap_'+label+'_to_thigh_LAYOUT',thigh,c.name)
c=part('T03_Upper_leg_mount_fastener_ENVELOPES','steel fastener envelopes - final lengths TBD','Four M4x25 clamp screws with bottom/outside nuts; four M4 motor screws have provisional engagement only')
for sign in [-1,1]:
 for s in [-1,1]:
  yy=Y+s*22;zz=Z+sign*48
  cylinder(c,'M4x25_clamp_shank',(32,yy,zz),(57,yy,zz),2)
  cylinder(c,'M4_socket_head',(28,yy,zz),(32,yy,zz),3.5)
  cylinder(c,'M4_nut_ENVELOPE',(54,yy,zz),(57.2,yy,zz),3.5)
  yy=Y+s*20;zz=Z+sign*33
  cylinder(c,'M4_motor_screw_provisional_12mm',(25,yy,zz),(37,yy,zz),2)
  cylinder(c,'M4_motor_screw_head',(37,yy,zz),(41,yy,zz),3.5)
joint('Thigh_mount_hardware_LAYOUT',thigh,c.name)
progress('hip yaw vendor geometry and pelvis references')
# Copy the actual fixed and rotating GWK7010 vendor geometry, omitting its ankle crank.
c=part('T04_GWK7010_Hip_yaw_REFERENCE','purchased GWK7010 reference','Vertical yaw axis. 40-50Nm peak is an untested user estimate. Structural bearing support undecided.')
m=adsk.core.Matrix3D.create();m.setToRotation(math.pi/2,V3.create(1,0,0),pt((0,0,0)))
# old motor axis Y; map its rear Y29.2 to Z808.8, front/output toward pelvis.
m.translation=V3.create(0,(Y+335)/10,(808.8-29.2)/10)
copybody(c,parts['M01_GWK7010_A'].component.bRepBodies.item(0),'GWK7010_vendor_fixed_yaw',m)
outbody=next(b for b in parts['M02_Aluminum_crank_A'].component.bRepBodies if 'vendor_visible_rotating' in b.name)
copybody(c,outbody,'GWK7010_vendor_output_yaw',m)
color(c,'DJI_(28, 29, 33)');joint('Yaw_envelope_to_thigh_LAYOUT_ONLY',thigh,c.name)
c.attributes.add('SHIN','exclude_from_mass_and_structure','true')
# Reference crosshead and pelvis intentionally have no bolts/bearing claims.
c=part('T05_Hip_crosshead_REFERENCE','reference envelope','Pitch axis Z823.6; yaw/pitch serial joint stack and external bearing unresolved. Not a manufactured load path.')
rounded_solid(c,'Rail_top_crosshead_REFERENCE','z',798,8,(-54,Y-22),(54,Y+22),8)
joint('Hip_crosshead_LAYOUT_ONLY',thigh,c.name)
c.attributes.add('SHIN','exclude_from_mass_and_structure','true')
c=part('T06_Pelvis_HALF_REFERENCE','reference envelope','Half-pelvis mass/volume placeholder; centerline provisionally X-100, leg centerline X0. Mirror other leg later.')
rounded_solid(c,'Half_pelvis_block_REFERENCE','z',886,50,(-116,Y-45),(52,Y+45),12)
joint('Pelvis_block_LAYOUT_ONLY',thigh,c.name)
c.attributes.add('SHIN','exclude_from_mass_and_structure','true')
c=part('T07_Hip_pitch_motor_ENVELOPE_REFERENCE','unspecified motor envelope','Provisional100mm diameter x40mm wide envelope; 10deg tilted lateral axis is a placeholder only, not selected hardware')
# Envelope medial to the leg, below the half-pelvis reference; selected hardware unknown.
b=cylinder(c,'Pitch_motor_100x40_ENVELOPE',(-106,Y,H),(-66,Y,H),50)
mt=adsk.core.Matrix3D.create();mt.setToRotation(math.radians(10),V3.create(0,1,0),pt((-86,Y,H)))
mi=c.features.moveFeatures.createInput2(obj(list(c.bRepBodies)));mi.defineAsFreeMove(mt);c.features.moveFeatures.add(mi).name='PROVISIONAL_10deg_pitch_axis_tilt'
joint('Pitch_motor_envelope_LAYOUT_ONLY',thigh,c.name)
c.attributes.add('SHIN','exclude_from_mass_and_structure','true')
progress('reference circles and height datums')
c=part('T08_Transmission_and_height_REFERENCE_SKETCHES','reference sketches only','2.5:1 primary plus1:1 final chain option; circles are pitch-diameter layout guides, no chain or gearbox CAD')
# Two provisional chain planes 6mm apart; real hub/chain widths may require more separation.
for name,x,centers in [
 ('Primary_2p5_to_1_PCD_guides',-30,[(Y,Z,20),(Y,577,50)]),
 ('Final_1_to_1_PCD_guides',-24,[(Y,577,35),(Y,K,35)])]:
 sk=sketch(c,'x',x,name)
 for yy,zz,r in centers:circle(sk,'x',x,yy,zz,r)
 sk.isLightBulbOn=True
sk=sketch(c,'x',-30,'Alternative_2_to_1_primary_large_PCD80')
circle(sk,'x',-30,Y,577,40);sk.isLightBulbOn=False
sk=sketch(c,'x',37.99,'Encoder_KEEP_OUT_28dia_by_5axial')
circle(sk,'x',37.99,Y,Z,14);sk.isLightBulbOn=False
sk=sketch(c,'y',Y,'Height_budget_1600p2mm_and_400mm_thigh')
for zz,x0,x1 in [(-14,-115,70),(K,-70,70),(H,-100,70),(1586.2,-120,70)]:
 sk.sketchCurves.sketchLines.addByTwoPoints(sk.modelToSketchSpace(pt((x0,Y,zz))),sk.modelToSketchSpace(pt((x1,Y,zz))))
sk.isLightBulbOn=False
joint('Transmission_guides_to_thigh_LAYOUT',thigh,c.name)
# Muted reference colors distinguish speculative hip architecture from the printed mount.
for name,rgb in [('T05_Hip_crosshead_REFERENCE',(103,125,155)),('T06_Pelvis_HALF_REFERENCE',(121,133,151)),('T07_Hip_pitch_motor_ENVELOPE_REFERENCE',(162,126,67))]:
 ap=d.appearances.addByCopy(d.appearances.itemByName('S01_Ankle_to_oval_rail_adapter_finish'),name+'_finish')
 prop=ap.appearanceProperties.itemById('opaque_albedo') or ap.appearanceProperties.itemById('generic_diffuse')
 if prop:adsk.core.ColorProperty.cast(prop).value=adsk.core.Color.create(*rgb,255)
 for b in parts[name].component.bRepBodies:b.appearance=ap
for name,value,desc in [('layout_total_height',1600.2,'5ft3 target, not built full body'),('layout_thigh_axis_length',400,'Knee to pitch-axis reference'),('layout_knee_motor_height',261.4,'Motor axis above knee'),('layout_encoder_axial_gap',5,'Rear hub to right rail inner face')]:
 d.userParameters.add(name,V.createByReal(value/10),'mm',desc)
params={'target_height_mm':1600.2,'ground_z_mm':-14,'knee_axis_z_mm':K,'hip_pitch_datum_z_mm':H,'thigh_axis_length_mm':400,'hip_height_above_ground_mm':H+14,'thigh_rail_length_mm':351.8,'knee_motor_axis_z_mm':Z,'motor_rear_plane_x_mm':27,'rear_hub_outer_x_mm':33,'right_rail_inner_x_mm':38,'encoder_gap_mm':5,'estimated_mount_pattern_mm':[40,66],'shell_web_mm':8,'hip_pitch_tilt_deg_PROVISIONAL':10,'internal_reduction_options':[6,8],'primary_chain_ratio_options':[2,2.5],'final_chain_ratio':1,'pcd_guides_mm':{'motor':40,'intermediate_primary':100,'intermediate_secondary':70,'knee':70},'primary_plane_x_mm':-30,'secondary_plane_x_mm':-24,'intermediate_center_z_mm':577,'reference_only_hip_architecture':True}
(OUT/'layout_parameters.json').write_text(json.dumps(params,indent=2))
save_checkpoint('Upper_leg_layout_checkpoint')
result={'components':root.occurrences.count,'parameters':params}
