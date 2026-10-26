exec(compile((ROOT/'v13/common.py').read_text(),'<v13common>','exec'))
progress('motor position and aluminum tube')
# Live right motor retained a -30mm edit; normalize its measured front-disc centre to Z565.
c=parts['R01_DJI_10018_77KV_ESTIMATED_REFERENCE'].component
can=next(b for b in c.bRepBodies if 'can' in b.name.lower())
bb=can.boundingBox;actual_z=(bb.minPoint.z+bb.maxPoint.z)*5
shift(c.name,Z-actual_z)
c.description+=' V13 axis Z565: 25mm below released v12, reconciled against surviving live edit.'
for name in ['P04_Case_rail_cap_R_546','P04_Case_rail_cap_R_634','P04_Case_rail_cap_L_646','P10_Output_support_rail_block','P11_Output_support_cap','P14_Motor_to_backplate_M4_screws']:
 shift(name,-25)
 parts[name].component.description+=' V13 moved down25mm; name retains historical identifier.'
silver=ap('aluminum');plastic=ap('plastic');orange=ap('orange')
a=sub(cy((-8,Y,Z),(37,Y,Z),55),cy((-9,Y,Z),(38,Y,Z),53))
sub(a,bx((33,Y-6,Z-66),(38,Y+6,Z-34)))
emit('P03_Circular_motor_gearbox_case',a,'Aluminum tube:106mm ID,110mm OD,2mm wall,45mm axial length X-8..37. Rear wire notch. Gearbox cavity13mm nominal; final reduction depth deferred.','aluminum tubing, grade unconfirmed',silver)

def plate(x0,x1):
 a=cy((x0,Y,Z),(x1,Y,Z),55)
 # Four external ears put longitudinal fasteners outside the110mm tube.
 for deg in [45,135,225,315]:
  yy=Y+60*math.cos(math.radians(deg));zz=Z+60*math.sin(math.radians(deg))
  inner=(Y+52*math.cos(math.radians(deg)),Z+52*math.sin(math.radians(deg)))
  # Overlapping radial pads are explicitly united into the plate.
  for rr in [52,55,58,60]:un(a,cy((x0,Y+rr*math.cos(math.radians(deg)),Z+rr*math.sin(math.radians(deg))),(x1,Y+rr*math.cos(math.radians(deg)),Z+rr*math.sin(math.radians(deg))),4))
  sub(a,cy((x0-1,yy,zz),(x1+1,yy,zz),1.7))
 return a
progress('separate rear plate, front plate and rail bridge')
a=plate(37,45);sub(a,cy((36,Y,Z),(46,Y,Z),16))
for z in [521,609]:un(a,rrxy(43,50.6,Y-18,Y+18,z-12,z+12,3))
sub(a,oval(51,508,622,5.15))
for yy in [-20,20]:
 for zz in [-33,33]:
  sub(a,cy((36,Y+yy,Z+zz),(46,Y+yy,Z+zz),2.2));sub(a,cy((41,Y+yy,Z+zz),(46,Y+yy,Z+zz),4))
sub(a,bx((33,Y-6,Z-66),(46,Y+6,Z-34)))
for z in [521,609]:
 for yy in [-14,14]:sub(a,cy((38,Y+yy,z),(52,Y+yy,z),2.2))
emit('P15_Separate_motor_backplate_and_rail_saddles',a,'Separate8mm printed rear plate and two right-rail saddles. Aluminum tube is clamped between plates by four external M3 tie screws. Mount pattern remains estimated.','PA-CF provisional',plastic)
a=plate(-11,-8);sub(a,cy((-12,Y,Z),(-7,Y,Z),9))
un(a,rrxy(-50.6,-8,Y-18,Y+18,612,630,4));sub(a,oval(-51,610,634,5.15))
for yy in [-14,14]:sub(a,cy((-52,Y+yy,621),(-35,Y+yy,621),2.2))
# The estimated prop posts remain reference solids; holes give them passage through the cover.
for b in c.bRepBodies:
 bb=b.boundingBox
 if bb.minPoint.x*10 < -8 and bb.maxPoint.x*10 > -11:
  cyy=(bb.minPoint.y+bb.maxPoint.y)*5;czz=(bb.minPoint.z+bb.maxPoint.z)*5
  r=max(bb.maxPoint.y-bb.minPoint.y,bb.maxPoint.z-bb.minPoint.z)*5+.5
  if r<15:sub(a,cy((-12,cyy,czz),(-7,cyy,czz),r))
emit('P05_Gearbox_front_cover',a,'3mm front cover atX-11..-8 plus upper bridge/clamp to opposite rail. External tie ears avoid threading a2mm tube wall. Prop-post passages are provisional.','PA-CF provisional',plastic)

progress('8T driver and independent output support')
def sprocket(n,pd,od,bore,z):
 x0=CHAIN_X-FACE/2;x1=CHAIN_X+FACE/2
 a=sub(cy((x0,Y,z),(x1,Y,z),od/2),cy((x0-1,Y,z),(x1+1,Y,z),bore/2))
 for i in range(n):
  t=2*math.pi*i/n;yy=Y+pd/2*math.cos(t);zz=z+pd/2*math.sin(t)
  sub(a,cy((x0-1,yy,zz),(x1+1,yy,zz),3.96))
 return a
emit('P07_Motor_output_sprocket_BLANK',sprocket(8,33.19,38.28,16.2,Z),'Approximate8T #40 sprocket:12.7pitch,33.19PD,38.28OD,7.21face; roller-pocket visualization only, not CNC tooth form. Common chain plane X-24.','sprocket material undecided',orange)
a=un(cy((-7,Y,Z),(-3,Y,Z),16),cy((-27.605,Y,Z),(-3,Y,Z),8))
sub(a,cy((-28,Y,Z),(-19,Y,Z),3.1))
emit('P06_Gearbox_output_REFERENCE',a,'16mm output shaft and32mm flange reference moved to shortened housing. Planet carrier, bearing and coupling remain undesigned.','aluminum reference',silver)
a=sub(cy((-20.395,Y,Z),(-13,Y,Z),9.5),cy((-21,Y,Z),(-12,Y,Z),8))
emit('P08_Sprocket_output_flange',a,'19mm OD compact sprocket hub replaces oversized four-bolt flange for8T root clearance. Coupling/key/spline and retention TBD.','aluminum reference',silver)
emit('P09_Opposite_output_support_pin_6mm',cy((-67,Y,Z),(-20,Y,Z),3),'6mm support pin,47mm reference length to opposite oval rail. Bearing interface not designed.','steel reference',silver)
parts['P13_Sprocket_M4_mount_screws'].isLightBulbOn=False
parts['P13_Sprocket_M4_mount_screws'].component.description+=' Retired in v13: four-bolt flange does not fit8T sprocket root.'
hw=[]
for x0,x1,z in [(39,63,521),(39,63,609),(-63,-37,621),(-63,-46.5,565)]:
 for yy in [-14,14]if z!=565 else[-13,13]:
  hw.append(('M4_clamp_shank',cy((x0,Y+yy,z),(x1,Y+yy,z),2)))
  hx=x1 if x1>0 else x0-4;hw.append(('M4_clamp_head',cy((hx,Y+yy,z),(hx+4,Y+yy,z),3.5)))
for deg in [45,135,225,315]:
 yy=Y+60*math.cos(math.radians(deg));zz=Z+60*math.sin(math.radians(deg))
 hw.extend([('M3x60_tie_shank',cy((-11,yy,zz),(49,yy,zz),1.5)),('M3_tie_head',cy((-14,yy,zz),(-11,yy,zz),2.75)),('M3_nut_envelope',sub(cy((45,yy,zz),(47.4,yy,zz),2.9),cy((44,yy,zz),(48,yy,zz),1.55)))])
emit('P12_Case_clamp_and_cover_hardware',hw,'Eight M4 rail-clamp screws and four external M3x60 case ties with nut envelopes; verify stock screw lengths and print retention.','steel reference',silver)
(OUT/'housing_parameters.json').write_text(json.dumps({'motor_axis_z_mm':Z,'motor_adjustment_from_live_mm':Z-actual_z,'motor_change_from_v12_mm':-25,'tube_id_mm':106,'tube_od_mm':110,'wall_mm':2,'tube_length_mm':45,'tube_x_mm':[-8,37],'front_cover_x_mm':[-11,-8],'gearbox_space_mm':13,'chain_plane_x_mm':CHAIN_X,'driver_teeth':8,'driver_PD_mm':33.19,'driver_OD_mm':38.28,'face_mm':FACE,'tooth_profile':'approximate roller pockets, not manufacturing geometry','gearbox_design_deferred':True},indent=2))
result={'motor_z':Z,'tube':'106ID/110OD','driver':'8T,38.28OD,7.21face','gearbox_space_mm':13}
