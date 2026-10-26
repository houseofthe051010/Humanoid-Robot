exec(compile((ROOT/'v15/common.py').read_text(),'<common>','exec'))
progress('curved rear slide-on mount')
right=next(o for o,s in groups()if s==1);parts={o.component.partNumber:o for o in right.component.occurrences}
rear=trans(TM.copy(parts['P15_Separate_motor_backplate_and_rail_saddles'].bRepBodies.item(0)),dx=-130)
ix(rear,bx((-100,-100,450),(45,140,650)))
bulge=loft('x',[(43,45,54),(47,32,59),(54,17,61),(61,14,60)],'Rear_full_length_curved_load_spread')
un(rear,bulge,oval(51,498,623,9))
sub(rear,oval(51,497,624,5.1))
for yy in [-20,20]:
 for zz in [-33,33]:
  sub(rear,cy((36,Y+yy,Z+zz),(64,Y+yy,Z+zz),2.2));sub(rear,cy((41,Y+yy,Z+zz),(64,Y+yy,Z+zz),4))
# Keep the rear hub passage through the original mounting plate. The full
# sleeve occupies the old encoder reservation: final encoder packaging deferred.
sub(rear,cy((36,Y,Z),(42,Y,Z),16))
progress('sprocket-side curved upper half shell')
front=trans(TM.copy(parts['P05_Gearbox_front_cover'].bRepBodies.item(0)),dx=-130)
ix(front,bx((-11,-100,450),(10,140,650)))
outerrows=[(-61,14,64),(-51,18,64),(-38,34,62),(-24,49,59),(-8,57,58)]
outer=loft('x',outerrows,'Front_upper_180deg_outer')
innerrows=[(x,a-6,b-6)for x,a,b in outerrows];innerrows[0]=(-62,*innerrows[0][1:]);innerrows[-1]=(-7,*innerrows[-1][1:])
inner=loft('x',innerrows,'Front_upper_180deg_inner')
sub(outer,inner);ix(outer,bx((-70,-100,Z),(10,140,640)))
un(front,outer,oval(-51,548,626,10))
sub(front,oval(-51,547,627,5.1));sub(front,cy((-63,Y,Z),(-39,Y,Z),3.3))
for go,sgn in groups():
 progress('install slide mounts '+go.component.name)
 ps={o.component.partNumber:o for o in go.component.occurrences}
 replace(ps['P15_Separate_motor_backplate_and_rail_saddles'].component,place(TM.copy(rear),sgn),'V15_continuous_slide_sleeve_rear','V15 continuous125mm oval slide-on sleeve,10.2x18.2 passage, broad smooth rear load spread. No split clamp. Rear encoder packaging must be reconsidered; strength not qualified.')
 replace(ps['P05_Gearbox_front_cover'].component,place(TM.copy(front),sgn),'V15_upper_half_cradle_slide_sleeve','V15 continuous78mm slide-on sleeve with curved upper180-degree shell and side connections. Nominal6mm section offsets; lower half remains open.6.6mm support-pin reference passage, bearing TBD.')
 for n in ['P04_Case_rail_cap_R_546','P04_Case_rail_cap_R_634','P04_Case_rail_cap_L_646','P10_Output_support_rail_block','P11_Output_support_cap']:
  ps[n].isLightBulbOn=False;ps[n].component.description+=' Retired/hidden inV15; replaced by integral slide-on sleeve.'
 c=ps['P12_Case_clamp_and_cover_hardware'].component
 for b in list(c.bRepBodies):
  if b.name.startswith('M4_clamp'):c.features.removeFeatures.add(b)
 c.description='V15 four externalM3x60 case ties/head/nut envelopes retained. Former split-clamp M4 hardware removed.'
 # Same mounting/output face,110OD,50mm depth with extra10mm only behind.
 u=(math.cos(math.radians(25)),0,-math.sin(math.radians(25)));center=(-78,Y,798.6)
 along=lambda t:tuple(center[i]+u[i]*t for i in range(3))
 pitch=cy(along(-30),along(20),55)
 replace(ps['T07_Hip_pitch_motor_ENVELOPE_REFERENCE'].component,place(pitch,sgn),'Hip_pitch_110x50_REFERENCE','V15 110mm OD x50mm axial depth,25degree tilt. Output/front mounting face unchanged; additional10mm behind. Unselected motor envelope, not vendor CAD.')
result={'mounts':'continuous slide-on oval sleeves, curved load spread','rear_sleeve_length':125,'front_sleeve_length':78,'hip_pitch_OD':110,'hip_pitch_depth':50,'rear_extension':10,'chain_dimensions_calculated':False}
(OUT/'mount_parameters.json').write_text(json.dumps(result,indent=2))
