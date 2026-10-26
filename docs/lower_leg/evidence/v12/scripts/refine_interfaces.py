exec(compile((ROOT/'v12/common.py').read_text(),'<common>','exec'))
# Reuse only the transient-solid helpers, never rerun the preceding build.
src=(OUT/'build_hips.py').read_text();exec(compile(src[src.index('Y=23.343134'):src.index("progress('CNC rail-to-yaw")],'<temporary_helpers>','exec'))
def replace(name,b,desc,material='PA-CF provisional',rgb=(48,59,68)):
 old=parts[name];old.isLightBulbOn=False;old.component.name='ZZ_v12_fit_pass1_'+name
 c=part(name,material,desc);addtemp(c,b,name)
 ap=d.appearances.itemByName('v12_'+str(rgb))
 if not ap:
  ap=d.appearances.addByCopy(parts['S01_Ankle_to_oval_rail_adapter'].component.bRepBodies.item(0).appearance,'v12_'+str(rgb)) if 'S01_Ankle_to_oval_rail_adapter' in parts else d.appearances.addByCopy(parts['P01_Knee_side_rail_seat_L'].component.bRepBodies.item(0).appearance,'v12_'+str(rgb))
  prop=ap.appearanceProperties.itemById('opaque_albedo') or ap.appearanceProperties.itemById('generic_diffuse')
  if prop:prop.value=adsk.core.Color.create(*rgb,255)
 for x in c.bRepBodies:x.appearance=ap
 joint(name+'_fitted_layout',thigh,name)
 assert c.bRepBodies.count==1 and c.bRepBodies.item(0).volume>0,(name,c.bRepBodies.count)
 return c
Z=590.;silver=(150,158,166)
progress('correct oval sockets to measured rail orientation')
for side,s in [('L',-1),('R',1)]:
 lo,hi=sorted([s*51,s*33]);a=rrxy(lo,hi,Y-30,Y+30,438.2,477.2,3)
 sub(a,oval(s*51,438,478,5.05))
 for yy in [-20.9,20.9]:
  sub(a,cy((s*43,Y+yy,438),(s*43,Y+yy,478),2.7));sub(a,cy((s*43,Y+yy,470.2),(s*43,Y+yy,478),4.5))
 for z in [453,469]:sub(a,cy((lo-1,Y,z),(hi+1,Y,z),2))
 replace('P01_Knee_side_rail_seat_'+side,a,'Matched 18Y x 10X oval side saddle; two nominal M4 side threads and two M5 bearing mount clearances. CNC dimensions provisional.','6061-T6 nominal',silver)
progress('case bridge cover and wire clearances')
a=sub(cy((-28,Y,Z),(37,Y,Z),62),cy((-29,Y,Z),(37.1,Y,Z),54))
un(a,cy((37,Y,Z),(45,Y,Z),62));sub(a,cy((36.9,Y,Z),(46,Y,Z),16))
for z in [546,634]:un(a,rrxy(43,50.6,Y-18,Y+18,z-12,z+12,3))
sub(a,oval(51,529,652,5.15))
un(a,rrxy(-50.6,-20,Y-18,Y+18,637,655,5));sub(a,oval(-51,632,663,5.15))
for yy in [-20,20]:
 for zz in [-33,33]:
  sub(a,cy((36,Y+yy,Z+zz),(46,Y+yy,Z+zz),2.2));sub(a,cy((41,Y+yy,Z+zz),(46,Y+yy,Z+zz),4))
sub(a,bx((33,Y-6,524),(46,Y+6,556)))
for yy in [-14,14]:
 sub(a,cy((-52,Y+yy,646),(-35,Y+yy,646),2.2))
 for z in [546,634]:sub(a,cy((38,Y+yy,z),(52,Y+yy,z),2.2))
angles=[22.5+45*i for i in range(8)]
for deg in angles:
 yy=Y+58*math.cos(math.radians(deg));zz=Z+58*math.sin(math.radians(deg));sub(a,cy((-29,yy,zz),(-16,yy,zz),2.2))
replace('P03_Circular_motor_gearbox_case',a,'124 OD,108 ID,33mm gearbox reservation X-28 to X5; 8mm circular backplate; correctly oriented rail saddles and wire exit. No gears.')
for side,x,zs in [('R',51,[546,634]),('L',-51,[646])]:
 for z in zs:
  lo,hi=(51.4,63)if side=='R' else(-63,-51.4)
  a=rrxy(lo,hi,Y-18,Y+18,z-12,z+12,3);sub(a,oval(x,z-13,z+13,5.15))
  for yy in [-14,14]:sub(a,cy((lo-1,Y+yy,z),(hi+1,Y+yy,z),2.2))
  replace('P04_Case_rail_cap_'+side+'_'+str(z),a,'Split cap, 18x10 rail socket,0.8mm seam and two M4 clearances.')
a=sub(cy((-35.8,Y,Z),(-28.8,Y,Z),62),cy((-36,Y,Z),(-28,Y,Z),9))
sub(a,bx((-36,Y-18.5,636.5),(-28,Y+18.5,657)))
for deg in angles:
 yy=Y+58*math.cos(math.radians(deg));zz=Z+58*math.sin(math.radians(deg));sub(a,cy((-36,yy,zz),(-28,yy,zz),2.2))
replace('P05_Gearbox_front_cover',a,'7mm removable cover with clearance for the integral upper bridge; eight M4 holes at 22.5degree offset. Bearing seat pending.')
progress('compact opposite pin support and pitch fork clearance')
for name,lo,hi in [('P10_Output_support_rail_block',-50.6,-45),('P11_Output_support_cap',-63,-51.4)]:
 a=rrxy(lo,hi,Y-17,Y+17,Z-6,Z+6,2)
 if name.startswith('P10'):un(a,cy((-46,Y,Z),(-44.5,Y,Z),7.5))
 sub(a,oval(-51,Z-7,Z+7,5.15))
 for yy,r in [(0,3.3),(-13,2.2),(13,2.2)]:sub(a,cy((lo-1,Y+yy,Z),(hi+2,Y+yy,Z),r))
 replace(name,a,'Compact split support around 6mm pin; clears sprocket bolts. 6.6mm passage only, bearing and load-bearing section require final design.')
q=parts['Q03_CNC_roll_to_pitch_fork'].component.bRepBodies.item(0);a=TM.copy(q)
u=(math.cos(math.radians(25)),0,-math.sin(math.radians(25)));along=lambda t:(-78+t*u[0],Y,803.6+t*u[2])
sub(a,cy(along(-22),along(19.95),50.5))
replace('Q03_CNC_roll_to_pitch_fork',a,'Opposed CNC cheek concept and 25deg pitch flange, relieved around the motor with0.5mm radial clearance. Mount patterns and machining split provisional.','6061-T6 nominal',silver)
# Replace hardware batch with seated screws and a bridge-clearing cover pattern.
old=parts['P12_Case_clamp_and_cover_hardware'];old.isLightBulbOn=False;old.component.name='ZZ_v12_fit_pass1_P12_Case_clamp_and_cover_hardware'
c=part('P12_Case_clamp_and_cover_hardware','steel reference','Eight M4 rail clamps and eight M4 cover screws; placeholder thread retention.')
for x0,x1,z in [(39,63,546),(39,63,634),(-63,-37,646),(-63,-46.5,590)]:
 for yy in [-14,14]if z!=590 else[-13,13]:
  addtemp(c,cy((x0,Y+yy,z),(x1,Y+yy,z),2),'M4_clamp_shank')
  hx=x1 if x1>0 else x0-4;addtemp(c,cy((hx,Y+yy,z),(hx+4,Y+yy,z),3.5),'M4_clamp_head')
for deg in angles:
 yy=Y+58*math.cos(math.radians(deg));zz=Z+58*math.sin(math.radians(deg))
 addtemp(c,cy((-35.8,yy,zz),(-18,yy,zz),2),'M4_cover_screw');addtemp(c,cy((-39.8,yy,zz),(-35.8,yy,zz),3.5),'M4_cover_head')
color(c,'T06_Pelvis_HALF_REFERENCE_finish');joint(c.name+'_fitted_layout',thigh,c.name)
# Shorter socket heads clear the adjacent oval tube, keeping the 4-hole flange pattern.
c=parts['P13_Sprocket_M4_mount_screws'].component
move_bodies(c,(.5,0,0),'Shift_output_fasteners_to_clear_rail')
# Keep the orange transmission reference visually distinct.
c=parts['P07_Motor_output_sprocket_BLANK'].component
ap=d.appearances.addByCopy(c.bRepBodies.item(0).appearance,'v12_sprocket_orange');prop=ap.appearanceProperties.itemById('metal_f0')or ap.appearanceProperties.itemById('opaque_albedo')or ap.appearanceProperties.itemById('generic_diffuse')
if prop:prop.value=adsk.core.Color.create(205,135,45,255)
for b in c.bRepBodies:b.appearance=ap
for side in ['L','R']:parts['N06_Upper_leg_oval_stub_'+side].component.description='User v11 thigh rail:18Yx10X oval,246.8mm long from438.2to685; centresX+/-51. Wall0.55 assumed; added fastener passages.'
for j in root.asBuiltJoints:j.isLightBulbOn=False
save_checkpoint('Refined_interfaces_checkpoint')
result={'replaced_components':[x['name']for x in records]}
