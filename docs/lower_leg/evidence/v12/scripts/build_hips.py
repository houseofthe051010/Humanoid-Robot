exec(compile((ROOT/'v12/common.py').read_text(),'<common>','exec'))
Y=23.343134;thigh='N04_Knee_pillow_block_L';BT=adsk.fusion.BooleanTypes
def cy(p,q,r):return TM.createCylinderOrCone(pt(p),r/10,pt(q),r/10)
def bx(lo,hi):
 return TM.createBox(adsk.core.OrientedBoundingBox3D.create(pt([(a+b)/2 for a,b in zip(lo,hi)]),V3.create(1,0,0),V3.create(0,1,0),*( (b-a)/10 for a,b in zip(lo,hi))))
def un(a,*bs):
 for b in bs:assert TM.booleanOperation(a,b,BT.UnionBooleanType)
 return a
def sub(a,b):
 assert TM.booleanOperation(a,b,BT.DifferenceBooleanType)
 return a
def oval(x,z0,z1,r=5.1):return un(bx((x-r,Y-4,z0),(x+r,Y+4,z1)),cy((x,Y-4,z0),(x,Y-4,z1),r),cy((x,Y+4,z0),(x,Y+4,z1),r))
def rrxy(x0,x1,y0,y1,z0,z1,r):
 a=un(bx((x0+r,y0,z0),(x1-r,y1,z1)),bx((x0,y0+r,z0),(x1,y1-r,z1)))
 for x in [x0+r,x1-r]:
  for y in [y0+r,y1-r]:un(a,cy((x,y,z0),(x,y,z1),r))
 return a
def beam_y(c0,c1,r,y0,y1):
 dx=c1[0]-c0[0];dz=c1[1]-c0[1];ll=math.hypot(dx,dz)
 b=TM.createBox(adsk.core.OrientedBoundingBox3D.create(pt(((c0[0]+c1[0])/2,(y0+y1)/2,(c0[1]+c1[1])/2)),V3.create(dx/ll,0,dz/ll),V3.create(0,1,0),ll/10,(y1-y0)/10,2*r/10))
 return un(b,cy((c0[0],y0,c0[1]),(c0[0],y1,c0[1]),r),cy((c1[0],y0,c1[1]),(c1[0],y1,c1[1]),r))
def emit(name,b,desc,ap='T06_Pelvis_HALF_REFERENCE_finish',material='6061-T6 nominal'):
 c=part(name,material,desc);addtemp(c,b,name);color(c,ap);joint(name+'_layout',thigh,name)
 assert all(x.isSolid and x.volume>0 for x in c.bRepBodies)
 return c
progress('CNC rail-to-yaw crosshead')
# Rail-supported stationary annulus. The output passes independently through its centre.
a=sub(cy((0,Y,681.6),(0,Y,689.6),38),cy((0,Y,681),(0,Y,690),18.4))
for x in [-51,51]:
 un(a,rrxy(x-12,x+12,Y-18,Y+18,666.5,693,3),bx((min(x,0),Y-10,681.6),(max(x,0),Y+10,689.6)))
 sub(a,oval(x,665,695))
 # Open clamp slit, with two transverse pinch screws above/below the rail end.
 sub(a,bx((x-.5,Y+8,666),(x+.5,Y+20,694)))
 for z in [673,686]:sub(a,cy((x-13,Y+13,z),(x+13,Y+13,z),2.2))
sub(a,cy((0,Y,681),(0,Y,690),18.4))
for deg in [0,90,180,270]:
 x=20.25*math.cos(math.radians(deg));y=Y+20.25*math.sin(math.radians(deg))
 sub(a,cy((x,y,681),(x,y,690),1.2))
emit('Q01_CNC_rail_to_yaw_crosshead',a,'8mm fixed yaw annulus with two 26.5mm slotted oval rail sockets and M4 pinch provisions. Four provisional M2 clearance locations at R20.25 follow visible donor geometry; measure motor mounting before CNC.')
progress('CNC yaw-to-roll output cradle')
a=un(cy((0,Y,684.8),(0,Y,692),17),cy((0,Y,688),(0,Y,703),14),rrxy(-53,53,Y-25,Y+31,698,708,4),cy((0,Y-25,758.6),(0,Y-15,758.6),54))
sub(a,cy((0,Y-26,758.6),(0,Y-14,758.6),14))
for deg in [45,135,225,315]:
 x=40*math.cos(math.radians(deg));z=758.6+40*math.sin(math.radians(deg));sub(a,cy((x,Y-26,z),(x,Y-14,z),2.75))
for deg in [0,60,120,180,240,300]:
 x=12.5*math.cos(math.radians(deg));y=Y+12.5*math.sin(math.radians(deg));sub(a,cy((x,y,684),(x,y,693),1.7))
emit('Q02_CNC_yaw_to_roll_cradle',a,'Integral 10mm roll backplate and floor on yaw output hub. Roll motor 100x36 reference, provisional 80 PCD M5; yaw output pattern and bearing/fastener access require vendor confirmation. Layout only, no hip joint qualification.')
progress('CNC roll-to-25degree-pitch fork')
u=(math.cos(math.radians(25)),0,-math.sin(math.radians(25)))
center=(-78,Y,803.6)
along=lambda t:tuple(center[i]+t*u[i] for i in range(3))
a=cy(along(20),along(28),54)
sub(a,cy(along(19),along(29),15))
# Opposed cheeks join at the angled pitch flange; the front cheek attaches to roll output.
un(a,beam_y((0,758.6),(-55,795),19,Y+23,Y+31),cy((0,Y+21,758.6),(0,Y+27,758.6),20))
un(a,beam_y((-22,776),(-55,795),16,Y-35,Y-27))
v=(math.sin(math.radians(25)),0,math.cos(math.radians(25)))
for deg in [45,135,225,315]:
 az=math.radians(deg);off=(40*math.cos(az)*v[0],40*math.sin(az),40*math.cos(az)*v[2])
 p=[along(19)[i]+off[i] for i in range(3)];q=[along(29)[i]+off[i] for i in range(3)];sub(a,cy(p,q,2.75))
for deg in [0,90,180,270]:
 x=13*math.cos(math.radians(deg));z=758.6+13*math.sin(math.radians(deg));sub(a,cy((x,Y+20,z),(x,Y+32,z),2.2))
emit('Q03_CNC_roll_to_pitch_fork',a,'Opposed curved cheeks and 8mm tilted pitch mounting flange, 25 degrees. Reference M5 80 PCD pitch and M4 26 PCD roll output. Output bearing, access, motor interfaces and final CNC split/stock plan remain to design.')

# Hardware for the functional clamp and cover interfaces, drawn without cosmetic threads.
progress('motor case clamp and cover hardware')
c=part('P12_Case_clamp_and_cover_hardware','steel reference','M4 clamp, cover and output flange hardware shown as nominal cylinders; lengths provisional.')
for x0,x1,z in [(39,63,546),(39,63,634),(-63,-37,646),(-63,-41,590)]:
 for yy in [-14,14] if z!=590 else [-13,13]:
  cylinder(c,'M4_clamp_shank',(x0,Y+yy,z),(x1,Y+yy,z),2)
  hx=x1 if x1>0 else x0-4
  cylinder(c,'M4_clamp_head',(hx,Y+yy,z),(hx+4,Y+yy,z),3.5)
for deg in range(0,360,45):
 yy=Y+58*math.cos(math.radians(deg));zz=590+58*math.sin(math.radians(deg))
 cylinder(c,'M4_cover_screw',(-35.8,yy,zz),(-18,yy,zz),2)
 cylinder(c,'M4_cover_head',(-39.8,yy,zz),(-35.8,yy,zz),3.5)
color(c,'T06_Pelvis_HALF_REFERENCE_finish');joint(c.name+'_layout',thigh,c.name)
# Replace the thin loose flange with a solid output shoulder attached to the existing output shaft.
c=parts['P08_Sprocket_output_flange'].component
for f in reversed(list(c.features)):f.deleteMe()
a=cy((-38,Y,590),(-36.5,Y,590),23)
for deg in [45,135,225,315]:
 yy=Y+16*math.cos(math.radians(deg));zz=590+16*math.sin(math.radians(deg));sub(a,cy((-39,yy,zz),(-35,yy,zz),2.2))
sub(a,cy((-39,Y,590),(-35,Y,590),8))
# This shoulder is the output assembly's idealized coupling; no key/spline strength implied.
addtemp(c,a,'Integral_output_shoulder_REFERENCE');color(c,'T06_Pelvis_HALF_REFERENCE_finish')
# The shaft overlaps the integral shoulder by intent (same rigid output assembly).
c=part('P13_Sprocket_M4_mount_screws','steel reference','Four nominal M4 bolts connect blank to output shoulder; thread/retention detail pending.')
for deg in [45,135,225,315]:
 yy=Y+16*math.cos(math.radians(deg));zz=590+16*math.sin(math.radians(deg))
 cylinder(c,'M4_output_screw',(-48,yy,zz),(-36.5,yy,zz),2)
 cylinder(c,'M4_output_head',(-48,yy,zz),(-44,yy,zz),3.5)
color(c,'T06_Pelvis_HALF_REFERENCE_finish');joint(c.name+'_layout',thigh,c.name)
for c in [root]+[o.component for o in root.occurrences]:
 for sk in c.sketches:sk.isLightBulbOn=False
 for pl in c.constructionPlanes:pl.isLightBulbOn=False
for j in root.asBuiltJoints:j.isLightBulbOn=False
d.computeAll();save_checkpoint('Hip_interfaces_checkpoint')
(OUT/'hip_parameters.json').write_text(json.dumps({'new_components':records,'pitch_deg':25,'roll_center_mm':[0,Y+3,758.6],'pitch_center_mm':list(center),'manufacturing_ready':False},indent=2))
result={'new_components':[r['name']for r in records]}
