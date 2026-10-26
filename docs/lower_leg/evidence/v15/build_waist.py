exec(compile((ROOT/'v15/common.py').read_text(),'<common>','exec'))
progress('central waist yaw motor from vendor7010 geometry')
assert not any(o.component.name=='Waist_layout_v15' for o in root.occurrences)
right=next(o for o,s in groups()if s==1);rp={o.component.partNumber:o for o in right.component.occurrences}
wg=root.occurrences.addNewComponent(adsk.core.Matrix3D.create());wg.component.name='Waist_layout_v15';wg.isGrounded=True
def part(n,desc,mat):
 o=wg.component.occurrences.addNewComponent(adsk.core.Matrix3D.create());c=o.component;c.name=n;c.partNumber=n;c.description=desc;c.attributes.add('SHIN','material',mat);o.isGroundToParent=True;return c
motor=part('W01_GWK7010_Waist_yaw_REFERENCE','Existing vendor7010 geometry duplicated, vertical waist yaw axis atX0/Y23.343134. BottomZ876. Placement/reference only; hip articulation and mounting interfaces unfinished.','purchased GWK7010 reference')
donor=rp['T04_GWK7010_Hip_yaw_REFERENCE'];bottom=min(b.boundingBox.minPoint.z*10 for b in donor.bRepBodies);dz=876-bottom
for b in donor.bRepBodies:addtemp(motor,trans(TM.copy(b),dx=-130,dz=dz),b.name.replace('yaw','waist_yaw'),b.appearance)
progress('curved waist skin and integral motor saddles')
rows=[(734,90,30),(752,112,50),(800,118,66),(840,113,64),(870,86,56),(888,54,46),(902,47,43)]
outer=loft('z',rows,'Waist_anatomical_outer',(0,Y))
inside=[(z,a-5,b-5)for z,a,b in rows];inside[0]=(733,*inside[0][1:]);inside[-1]=(903,*inside[-1][1:])
inner=loft('z',inside,'Waist_5mm_skin_inner',(0,Y));sub(outer,inner)
u=(math.cos(math.radians(25)),0,-math.sin(math.radians(25)));center=(-78,Y,798.6)
along=lambda t:tuple(center[i]+t*u[i] for i in range(3))
for sg in [1,-1]:
 # Integral curved motor barrels plus a rear annular seat; no generic solid
 # fill in the torso cavity. Motor's front mounting face remains accessible.
 sleeve=cy(along(-33),along(20),61)
 sub(sleeve,cy(along(-34),along(21),18))
 un(outer,place(sleeve,sg))
un(outer,sub(cy((0,Y,871),(0,Y,901),46.5),cy((0,Y,870),(0,Y,903),18)))
for x,z in [(-111,805),(111,805),(-48,887),(48,887)]:un(outer,cy((x,Y-9,z),(x,Y+9,z),5))
# Exact motor-envelope cavities, then actual neighboring reference solids.
for go,sgn in groups():
 ps={o.component.partNumber:o.createForAssemblyContext(go)for o in go.component.occurrences}
 for n,o in ps.items():
  if not o.isLightBulbOn or not n.startswith(('T07','T09','Q02','Q03')):continue
  for b in o.bRepBodies:
   if outer.boundingBox.intersects(b.boundingBox):sub(outer,TM.copy(b))
sub(outer,cy((0,Y,876),(0,Y,901),39))
sub(outer,cy((0,Y,900.7),(0,Y,909),18))
for b in motor.bRepBodies:
 if outer.boundingBox.intersects(b.boundingBox):sub(outer,TM.copy(b))
for x,z in [(-111,805),(111,805),(-48,887),(48,887)]:
 sub(outer,cy((x,Y-11,z),(x,Y+11,z),2.2));sub(outer,cy((x,Y-11,z),(x,Y-5,z),4));sub(outer,cy((x,Y+5,z),(x,Y+11,z),3.8))
# Small rounded rear wiring opening, away from pitch motor mounting faces.
slot=un(bx((-10,Y+40,853),(10,Y+80,863)),cy((-10,Y+40,858),(-10,Y+80,858),5),cy((10,Y+40,858),(10,Y+80,858),5));sub(outer,slot)
front=ix(TM.copy(outer),bx((-250,Y-150,700),(250,Y-.2,930)))
back=ix(TM.copy(outer),bx((-250,Y+.2,700),(250,Y+150,930)))
ap=rp['P15_Separate_motor_backplate_and_rail_saddles'].component.bRepBodies.item(0).appearance
for name,b in [('W02_Waist_front_shell',front),('W03_Waist_rear_shell',back)]:
 c=part(name,'V15 curved printed waist half,5mm nominal skin offsets,6mm pitch-motor barrels, central7010 yaw pocket and fourM4 seam provisions.0.4mm seam. Motor pockets follow reference geometry; print fit, fasteners, cooling and structural loads unverified.','printed plastic, grade TBD');addtemp(c,b,name,ap)
wg.component.description='Standing-pose waist layout. Independent fixed reference group; no new pelvis/hip kinematic constraints or load qualification.'
result={'waist_axis':'vertical yaw','motor':'duplicate vendor GWK7010','motor_base_z':876,'motor_output_top_z':max(b.boundingBox.maxPoint.z*10 for b in motor.bRepBodies),'skin_section_offset':5,'pitch_sleeve_radial_wall':6,'split_gap':.4,'shell_volume_mm3':(front.volume+back.volume)*1000,'shell_sections':rows,'articulated_hip_pelvis':False}
(OUT/'waist_parameters.json').write_text(json.dumps(result,indent=2))
