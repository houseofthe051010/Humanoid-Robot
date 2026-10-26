exec(compile((ROOT/'v12/common.py').read_text(),'<common>','exec'))
Y=23.343134;Z=590;thigh='N04_Knee_pillow_block_L'
for side,s in [('L',-1),('R',1)]:
 c=parts['P02_Knee_rail_screws_and_sleeves_'+side].component
 move_bodies(c,(-4*s,0,0),'Seat_side_screw_heads_against_oval',selected=[b for b in c.bRepBodies if b.name.startswith('M4')])
c=part('P14_Motor_to_backplate_M4_screws','steel reference','Four M4x14 nominal bolts through the circular backplate into estimated motor bosses. Actual motor thread and depth unmeasured.')
for yy in [-20,20]:
 for zz in [-33,33]:
  # Counterbore floor X41; 12mm shank reaches X29, 4mm head lies flush at X45.
  cylinder(c,'Motor_mount_M4x12',(29,Y+yy,Z+zz),(41,Y+yy,Z+zz),2)
  cylinder(c,'Motor_mount_head',(41,Y+yy,Z+zz),(45,Y+yy,Z+zz),3.5)
color(c,'T06_Pelvis_HALF_REFERENCE_finish');joint(c.name+'_layout',thigh,c.name)
c.description='Four M4x12 nominal bolts seat in X41 counterbores of the circular backplate; actual motor thread/depth unmeasured.'
# Recess the sprocket bolt heads so they clear the adjacent oval rail.
c=parts['P07_Motor_output_sprocket_BLANK'].component
centres=[(Y+16*math.cos(math.radians(a)),Z+16*math.sin(math.radians(a)),3.6)for a in [45,135,225,315]]
holes(c,'x',-44,2.2,centres,'Recessed_low_profile_output_screw_heads')
old=parts['P13_Sprocket_M4_mount_screws'];old.isLightBulbOn=False;old.component.name='ZZ_v12_fit_pass1_P13_Sprocket_M4_mount_screws'
c=part('P13_Sprocket_M4_mount_screws','steel reference','Four recessed low-profile M4 screw envelopes, head diameter7,height2; select actual hardware before machining.')
for yy,zz,r in centres:
 cylinder(c,'M4_shank',(-42,yy,zz),(-36.5,yy,zz),2)
 cylinder(c,'Recessed_M4_head',(-44,yy,zz),(-42,yy,zz),3.5)
color(c,'T06_Pelvis_HALF_REFERENCE_finish');joint(c.name+'_layout',thigh,c.name)
for j in root.asBuiltJoints:j.isLightBulbOn=False
result={'seated_lower_rail_screws':4,'motor_backplate_screws':4}
