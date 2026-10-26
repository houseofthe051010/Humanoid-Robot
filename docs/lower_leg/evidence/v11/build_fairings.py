exec(compile((ROOT/'v11/common.py').read_text(),'<common>','exec'))
Y=23.343134;Z=600.;thigh='N04_Knee_pillow_block_L'
# Build additions as new bodies,then explicitly combine only bodies in this component.
# Automatic Join can consume intersecting bodies from neighboring components.
_native_extrude=extrude
def extrude(comp,sk,axis,length,op,name,*args,**kwargs):
 if op!=OP.JoinFeatureOperation:return _native_extrude(comp,sk,axis,length,op,name,*args,**kwargs)
 targets=list(comp.bRepBodies)
 assert len(targets)==1,(comp.name,'join target must be exactly one shell body')
 added=_native_extrude(comp,sk,axis,length,OP.NewBodyFeatureOperation,name+'_addition',*args,**kwargs)
 ci=comp.features.combineFeatures.createInput(targets[0],obj([added]));ci.operation=OP.JoinFeatureOperation
 f=comp.features.combineFeatures.add(ci);f.name=name
 return f.bodies.item(0)
sections=[(478,54,27,14),(500,57,38,18),(545,63,57,23),(600,65,63,24),(640,65,52,23),(660,63,43,21),(678,58,32,17)]
progress('loft curved motor-contoured thigh shell')
c=part('T10_Thigh_front_fairing_PROVISIONAL','printed plastic - grade TBD','Curved cosmetic/protective clamshell,nominal3.2mm section offset. Tapers at knee;bulges around105mm knee motor. Separate from structural motor mount.')
def loft_sections(comp,name,rows,inset,op):
 li=comp.features.loftFeatures.createInput(op)
 if op==OP.CutFeatureOperation:li.participantBodies=list(comp.bRepBodies)
 for i,(z,hw,hd,r) in enumerate(rows):
  sk=sketch(comp,'z',z,name+'_section_'+str(i));roundrect(sk,'z',z,(-hw+inset,Y-hd+inset),(hw-inset,Y+hd-inset),r-inset)
  li.loftSections.add(sk.profiles.item(0))
 f=comp.features.loftFeatures.add(li);f.name=name
 return f.bodies.item(0)
loft_sections(c,'Smooth_thigh_outer_envelope',sections,0,OP.NewBodyFeatureOperation)
inner=list(sections);inner[0]=(477.9,*sections[0][1:]);inner[-1]=(678.1,*sections[-1][1:])
loft_sections(c,'Hollow_shell_3p2mm_section_offset',inner,3.2,OP.CutFeatureOperation)
progress('add shell rail saddles and removable panel interfaces')
for zz,halfwidth in [(486,55),(670,59)]:
 box(c,'Internal_rail_locating_web_'+str(zz),(-halfwidth,Y-12,zz-4),(halfwidth,Y+12,zz+4),OP.JoinFeatureOperation)
 for x in [-43,43]:
  sk=sketch(c,'z',zz-4.1,'Rail_socket_'+str(zz)+'_'+str(x));hull(sk,'z',zz-4.1,(x,Y-4),(x,Y+4),5.15)
  extrude(c,sk,'z',8.2,OP.CutFeatureOperation,'Oval_rail_locating_clearance')
 # Through-corridor for the two provisional chain planes;no chain designed here.
 box(c,'Transmission_corridor_'+str(zz),(-37,Y-14,zz-4.1),(-17,Y+14,zz+4.1),OP.CutFeatureOperation)
# Reinforce the side seam at four M3 panel joining locations.
for x in [-54,54]:
 for zz in [495,670]:
  sk=sketch(c,'y',Y-16,'Panel_join_boss');circle(sk,'y',Y-16,x,zz,4.5)
  extrude(c,sk,'y',32,OP.JoinFeatureOperation,'Panel_join_boss')
# Circular service-port flange on the drive-facing side;stops3mm short of left rail.
sk=sketch(c,'x',-68,'Motor_access_bezel')
circle(sk,'x',-68,Y,Z,61);circle(sk,'x',-68,Y,Z,53)
extrude(c,sk,'x',17,OP.JoinFeatureOperation,'Motor_contoured_side_bezel',ring=True)
holes(c,'x',-72,23,[(Y,Z,53)],'Motor_service_port_106mm')
port_centres=[(Y+57*math.cos(a),Z+57*math.sin(a),1.25) for a in [math.pi/4,3*math.pi/4,5*math.pi/4,7*math.pi/4]]
holes(c,'x',-68.1,10.1,port_centres,'Four_motor_cover_pilot_holes_PROVISIONAL')
holes(c,'y',Y-80,160,[(x,zz,1.7)for x in [-54,54]for zz in [495,670]],'Four_M3_panel_join_through_holes')
holes(c,'y',Y-80,70,[(x,zz,3.2)for x in [-54,54]for zz in [495,670]],'Panel_join_front_driver_access')
holes(c,'y',Y+10,70,[(x,zz,3.3)for x in [-54,54]for zz in [495,670]],'Panel_join_rear_nut_access_ENVELOPE')
for zz in [649,658,667]:
 rounded_solid(c,'Upper_front_vent_'+str(zz),'y',Y-80,75,(-17,zz),(17,zz+3.5),1.5,OP.CutFeatureOperation)
progress('separate front and rear curved panels')
assert c.bRepBodies.count==1, 'Whole shell must be connected before split'
rear=part('T11_Thigh_rear_fairing_PROVISIONAL','printed plastic - grade TBD','Removable rear half of curved shell;0.8mm assembly seam;internal rail locating saddles;M3 joining holes')
copybody(rear,c.bRepBodies.item(0),'Rear_panel_full_blank')
box(c,'Front_half_parting_seam',(-100,Y-.4,475),(100,Y+100,681),OP.CutFeatureOperation)
box(rear,'Rear_half_parting_seam',(-100,Y-100,475),(100,Y+.4,681),OP.CutFeatureOperation)
assert c.bRepBodies.count==1 and rear.bRepBodies.count==1,'Panels must each be one solid'
joint('Front_fairing_to_thigh_LAYOUT',thigh,c.name);joint('Rear_fairing_to_thigh_LAYOUT',thigh,rear.name)
cap=part('T12_Circular_motor_service_cover_PROVISIONAL','printed plastic - grade TBD','Removable122mm motor-contoured cover,3mm thick with central30mm inspection opening;does not represent motor or gearbox')
sk=sketch(cap,'x',-71,'Circular_motor_cover_profile');circle(sk,'x',-71,Y,Z,61);circle(sk,'x',-71,Y,Z,15)
extrude(cap,sk,'x',3,OP.NewBodyFeatureOperation,'Motor_service_cover_3mm',ring=True)
holes(cap,'x',-71.1,3.2,[(yy,zz,1.7)for yy,zz,r in port_centres],'Four_M3_cover_clearances')
joint('Service_cover_to_thigh_LAYOUT',thigh,cap.name)
# A small ring highlights the motor diameter without pretending to be the motor itself.
for comp,rgb,name in [(c,(159,177,189),'Thigh_front_silver_blue'),(rear,(87,106,121),'Thigh_rear_slate'),(cap,(29,35,43),'Motor_access_graphite')]:
 ap=d.appearances.addByCopy(d.appearances.itemByName('S01_Ankle_to_oval_rail_adapter_finish'),name)
 prop=ap.appearanceProperties.itemById('opaque_albedo') or ap.appearanceProperties.itemById('generic_diffuse')
 if prop:adsk.core.ColorProperty.cast(prop).value=adsk.core.Color.create(*rgb,255)
 for b in comp.bRepBodies:b.appearance=ap
for comp in [c,rear,cap]:
 for sk in comp.sketches:sk.isLightBulbOn=False
 comp.attributes.add('SHIN','strength_status','Non-qualified protective shell;attachment tolerances and hardware not finalized')
(OUT/'shell_parameters.json').write_text(json.dumps({'section_rows_z_halfwidth_halfdepth_radius_mm':sections,'section_wall_offset_mm':3.2,'parting_gap_mm':.8,'port_diameter_mm':106,'cover_diameter_mm':122,'cover_thickness_mm':3,'motor_center_z_mm':600,'cosmetic_reference':'User supplied Unitree H2 and Atlas-style images;original fitted geometry','components':[c.name,rear.name,cap.name],'panel_join_hardware':'4 M3 screws/nuts,nominal25mm grip arrangement;lengths and pockets provisional','port_hardware':'4 M3 screws,pilot holes2.5mm;retention/insert choice TBD'},indent=2))
save_checkpoint('Curved_fairing_checkpoint')
result={'panels':[(co.name,co.bRepBodies.count,sum(b.volume for b in co.bRepBodies)*1000)for co in [c,rear,cap]]}
