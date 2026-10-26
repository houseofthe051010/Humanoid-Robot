exec(compile((ROOT/'v12/common.py').read_text(),'<common>','exec'))
Y=23.343134;Z=590.;K=423.6;thigh='N04_Knee_pillow_block_L'
old_vis={n:o.isLightBulbOn for n,o in parts.items()}
for o in root.occurrences:o.isLightBulbOn=False
for b in root.bRepBodies:b.isLightBulbOn=False
# Explicit same-component Combine operations avoid Fusion's automatic Join scope.
def join_all(c,name):
 bs=list(c.bRepBodies)
 if len(bs)>1:
  ci=c.features.combineFeatures.createInput(bs[0],obj(bs[1:]));ci.operation=OP.JoinFeatureOperation
  f=c.features.combineFeatures.add(ci);f.name=name
 assert c.bRepBodies.count==1,(c.name,c.bRepBodies.count)
 return c.bRepBodies.item(0)
def oval_cut(c,x,z,length,name,r=5.15):
 sk=sketch(c,'z',z,name);capsule(sk,x,Y,r,4)
 extrude(c,sk,'z',length,OP.CutFeatureOperation,name)
def finish(c,material='plastic'):
 src={'plastic':'S01_Ankle_to_oval_rail_adapter_finish','aluminum':'T06_Pelvis_HALF_REFERENCE_finish','orange':'T07_Hip_pitch_motor_ENVELOPE_REFERENCE_finish'}[material]
 color(c,src)
 joint(c.name+'_to_thigh_LAYOUT',thigh,c.name)
 for b in c.bRepBodies:assert b.isSolid and b.volume>0
def ring(c,name,x0,x1,r,ri):
 cylinder(c,name,(x0,Y,Z),(x1,Y,Z),r)
 holes(c,'x',x0,x1-x0,[(Y,Z,ri)],name+'_bore')
def cylcut(c,p,q,r,name):
 return cuttemp(c,c.bRepBodies.item(0),TM.createCylinderOrCone(pt(p),r/10,pt(q),r/10),name)

progress('fitted aluminum knee rail seats')
for side,s in [('L',-1),('R',1)]:
 x=s*51
 c=part('P01_Knee_side_rail_seat_'+side,'6061-T6 nominal','CNC side-saddle; two M4 nominal tapped interfaces into the block, matched curved oval seat. Provisional machining details.')
 lo,hi=sorted([s*51,s*33])
 rounded_solid(c,'Aluminum_saddle_blank','z',438.2,39,(lo,Y-30),(hi,Y+30),3)
 oval_cut(c,x,438.2,40,'Matched_oval_side_seat',5.05)
 holes(c,'z',438.2,39,[(s*43,Y-20.9,2.7),(s*43,Y+20.9,2.7)],'Bearing_mount_M5_through')
 holes(c,'z',470.2,7,[(s*43,Y-20.9,4.5),(s*43,Y+20.9,4.5)],'M5_head_access')
 holes(c,'x',lo,hi-lo,[(Y,453,2),(Y,469,2)],'M4_thread_nominal_envelopes')
 finish(c,'aluminum')
 rail=parts['N06_Upper_leg_oval_stub_'+side].component
 holes(rail,'x',x-6,12,[(Y,453,2.2),(Y,469,2.2)],'Two_M4_side_attachment_clearances')
 c=part('P02_Knee_rail_screws_and_sleeves_'+side,'steel','Two M4x25 nominal side screws and internal crush sleeves; finish threads and bolt length on measured stock.')
 for z in [453,469]:
  cylinder(c,'M4x25_side_screw',(s*60,Y,z),(s*35,Y,z),2)
  cylinder(c,'M4_socket_head',(s*64,Y,z),(s*60,Y,z),3.5)
  b=cylinder(c,'Crush_sleeve',(x-4.4,Y,z),(x+4.4,Y,z),3)
  cuttemp(c,b,TM.createCylinderOrCone(pt((x-4.5,Y,z)),.21,pt((x+4.5,Y,z)),.21),'Sleeve_4p2_bore')
 finish(c,'aluminum')

progress('circular motor and 33mm gearbox case')
c=part('P03_Circular_motor_gearbox_case','PA-CF provisional','124 OD /108 ID barrel, 8mm circular backplate; 33mm axial gearbox reservation from motor front X5 to X-28. No gears or ring teeth.')
ring(c,'Motor_and_gearbox_barrel',-28,37,62,54)
cylinder(c,'Circular_8mm_backplate',(37,Y,Z),(45,Y,Z),62)
join_all(c,'Barrel_to_backplate')
holes(c,'x',36.9,8.2,[(Y,Z,16)],'Encoder_and_rear_hub_access')
holes(c,'x',37,8,[(Y+yy,Z+zz,2.2) for yy in [-20,20]for zz in [-33,33]],'Four_M4_motor_mounts')
holes(c,'x',41,4,[(Y+yy,Z+zz,4) for yy in [-20,20]for zz in [-33,33]],'Motor_screw_head_access')
box(c,'Phase_wire_exit',(33,Y-6,526),(46,Y+6,540),OP.CutFeatureOperation)
# Right split saddles merge into the circular backplate.
for z in [546,634]:
 rounded_solid(c,'Right_rail_saddle_'+str(z),'z',z-12,24,(43,Y-18),(50.6,Y+18),3)
join_all(c,'Right_saddles_to_case')
oval_cut(c,51,529,122,'Right_rail_running_socket')
# Curved top arm closes the frame onto the opposite rail.
rounded_solid(c,'Top_bridge_to_opposite_rail','z',637,18,(-50.6,Y-18),(-20,Y+18),5)
join_all(c,'Upper_bridge_to_case')
oval_cut(c,-51,632,30,'Left_rail_top_socket')
holes(c,'x',-51,40,[(Y-14,646,2.2),(Y+14,646,2.2)],'Left_top_clamp_M4')
for z in [546,634]:holes(c,'x',43,8,[(Y-14,z,2.2),(Y+14,z,2.2)],'Right_clamp_M4_'+str(z))
flangeholes=[(Y+58*math.cos(math.radians(a)),Z+58*math.sin(math.radians(a)),2.2)for a in range(0,360,45)]
holes(c,'x',-28,12,flangeholes,'Cover_M4_nominal_insert_pilots')
finish(c)
for side,x,zs in [('R',51,[546,634]),('L',-51,[646])]:
 for z in zs:
  cc=part('P04_Case_rail_cap_'+side+'_'+str(z),'PA-CF provisional','Separate split cap with 0.8mm seam and M4 access; print calibration required.')
  lo,hi=(51.4,63) if side=='R' else (-63,-51.4)
  rounded_solid(cc,'Removable_rail_clamp_cap','z',z-12,24,(lo,Y-18),(hi,Y+18),3)
  oval_cut(cc,x,z-12,24,'Matching_oval_socket')
  holes(cc,'x',lo,hi-lo,[(Y-14,z,2.2),(Y+14,z,2.2)],'M4_clamp_clearances')
  finish(cc)
c=part('P05_Gearbox_front_cover','PA-CF provisional','7mm front cover; output/bearing hole is a reference interface, bearing not selected.')
ring(c,'Front_cover',-35.8,-28.8,62,9)
holes(c,'x',-35.8,7,flangeholes,'Eight_M4_cover_clearances')
finish(c)

progress('output flange sprocket and opposite 6mm support')
c=part('P06_Gearbox_output_REFERENCE','aluminum reference','Independent output flange/shaft envelope; no planet carrier, reduction or output bearing designed.')
cylinder(c,'Carrier_output_flange',(-27,Y,Z),(-23,Y,Z),22)
cylinder(c,'Output_shaft_16mm',(-44,Y,Z),(-23,Y,Z),8)
join_all(c,'Output_flange_and_shaft')
holes(c,'x',-44,8,[(Y,Z,3.1)],'Six_mm_support_pin_socket')
holes(c,'x',-27,4,[(Y+16*math.cos(math.radians(a)),Z+16*math.sin(math.radians(a)),2.2)for a in [45,135,225,315]],'Carrier_reference_M4')
finish(c,'aluminum')
c=part('P07_Motor_output_sprocket_BLANK','aluminum reference','User orange sprocket retained as 70x6 blank, now coaxial with motor. No teeth or ratio commitment.')
ring(c,'Orange_sprocket_blank',-44,-38,35,8.1)
holes(c,'x',-44,6,[(Y+16*math.cos(math.radians(a)),Z+16*math.sin(math.radians(a)),2.2)for a in [45,135,225,315]],'Four_M4_output_connection')
finish(c,'orange')
# A flanged output adapter gives the blank an actual bolted interface.
c=part('P08_Sprocket_output_flange','aluminum reference','Flange immediately behind sprocket; shaft coupling and final fasteners require drivetrain design.')
ring(c,'Sprocket_mount_flange',-38,-36.5,23,8.1)
holes(c,'x',-38,1.5,[(Y+16*math.cos(math.radians(a)),Z+16*math.sin(math.radians(a)),2.2)for a in [45,135,225,315]],'Matching_M4_pattern')
finish(c,'aluminum')
c=part('P09_Opposite_output_support_pin_6mm','steel reference','6mm smooth support pin to opposite oval rail; bearing/retention not designed, not a torque capacity claim.')
cylinder(c,'Six_mm_support_pin',(-67,Y,Z),(-36,Y,Z),3);finish(c,'aluminum')
rail=parts['N06_Upper_leg_oval_stub_L'].component
holes(rail,'x',-57,12,[(Y,Z,3.3)],'Output_support_pin_passage')
c=part('P10_Output_support_rail_block','PA-CF provisional','Split support block around opposite rail. 6.6mm shaft passage; bearing interface deliberately unfinished.')
rounded_solid(c,'Support_block','z',Z-14,28,(-50.6,Y-17),(-45,Y+17),2)
oval_cut(c,-51,Z-14,28,'Side_oval_seat')
holes(c,'x',-51,7,[(Y,Z,3.3),(Y-13,Z,2.2),(Y+13,Z,2.2)],'Pin_and_clamp_holes')
finish(c)
c=part('P11_Output_support_cap','PA-CF provisional','Separate opposite-rail support cap; actual bearing added later.')
rounded_solid(c,'Support_cap','z',Z-14,28,(-63,Y-17),(-51.4,Y+17),3)
oval_cut(c,-51,Z-14,28,'Side_oval_seat')
holes(c,'x',-63,12,[(Y,Z,3.3),(Y-13,Z,2.2),(Y+13,Z,2.2)],'Pin_and_clamp_holes')
finish(c)

# Restore current assembly; discard old fairing/mount concepts from the working view.
hidden=('T01','T02','T03','T05','T06','T08','T10','T11','T12','N05','N08','U0','K01','GIM','S04')
for n,o in parts.items():
 o.isLightBulbOn=n.startswith('P') or (old_vis.get(n,False) and not n.startswith(hidden))
for n in parts:
 if n.startswith(('N01','N07')):parts[n].isLightBulbOn=True
for c in [root]+[o.component for o in root.occurrences]:
 for sk in c.sketches:sk.isLightBulbOn=False
 for pl in c.constructionPlanes:pl.isLightBulbOn=False
for j in root.asBuiltJoints:j.isLightBulbOn=False
d.computeAll();adsk.doEvents();save_checkpoint('Motor_case_checkpoint')
result={'new_components':records,'motor_center_mm':[20,Y,Z],'rail_centers_x_mm':[-51,51],'gearbox_clear_axial_mm':33,'case_OD_mm':124,'case_ID_mm':108,'backplate_mm':8,'front_cover_mm':7,'gearbox_gears_modeled':False,'support_pin_diameter_mm':6}
(OUT/'motor_case_parameters.json').write_text(json.dumps(result,indent=2))
