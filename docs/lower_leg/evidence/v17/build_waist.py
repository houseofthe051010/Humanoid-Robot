exec(compile((ROOT/'v17/common.py').read_text(),'<v17 common>','exec'))
wc=wg.component
progress('project exact stationary 7010 scalloped interface')
for j in wc.asBuiltJoints:
    if j.name.startswith(('WJ00','WJ01','WJ02')):j.jointMotion.rotationValue=0
adsk.doEvents()
fixed=wp['W01_GWK7010_Waist_yaw_REFERENCE'].component.bRepBodies.item(0)
vendor=next(b for b in wp['W05_CNC_yaw_output_pitch_yoke'].component.bRepBodies if 'vendor' in b.name)
vendor_copy=TM.copy(vendor);vendor_ap=vendor.appearance
face=next(f for f in fixed.faces if abs(f.area*100-643.85)<.1)
inner=max((lp for lp in face.loops if not lp.isOuter),key=lambda lp:lp.edges.count)
construction=next((o for o in root.occurrences if o.component.name=='ZZ_V17_motor_interface_construction'),None)
if construction is None:construction=root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
cc=construction.component
cc.name='ZZ_V17_motor_interface_construction';construction.isLightBulbOn=False
if cc.sketches.count:
    sk=cc.sketches.item(0)
else:
    pi=cc.constructionPlanes.createInput();pi.setByOffset(cc.xYConstructionPlane,adsk.core.ValueInput.createByReal(89.68));plane=cc.constructionPlanes.add(pi)
    sk=cc.sketches.add(plane);sk.name='Exact_7010_star_outline_from_fixed_mount_face'
motor_context=wp['W01_GWK7010_Waist_yaw_REFERENCE'].createForAssemblyContext(wg)
for edge in inner.edges:sk.project(edge.createForAssemblyContext(motor_context))
sk.sketchCurves.sketchCircles.addByCenterRadius(sk.modelToSketchSpace(pt((0,Y,896.8))),4.9)
prof=max(list(sk.profiles),key=lambda pr:pr.areaProperties().area)
ei=cc.features.extrudeFeatures.createInput(prof,adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
ei.setDistanceExtent(False,adsk.core.ValueInput.createByReal(.6));ef=cc.features.extrudeFeatures.add(ei)
template=ef.bodies.item(0);template.name='Exact_star_mount_template_896p8_902p8'
mount=TM.copy(template)
fixed_holes=[(24*math.cos(math.radians(22.5+45*k)),Y+24*math.sin(math.radians(22.5+45*k))) for k in range(8)]
shell_holes=[(43*math.cos(math.radians(45+90*k)),Y+43*math.sin(math.radians(45+90*k))) for k in range(4)]
for x,y in fixed_holes:sub(mount,cy((x,y,896),(x,y,904),1.7))
for x,y in shell_holes:sub(mount,cy((x,y,896),(x,y,904),2.3))

progress('build nylon lower roll and upper pitch with shorter separation')
yr=Y+10;zr=927.;zp=954.
base=un(cy((0,Y,901.5),(0,Y,910),18.5),rrxy(-42,42,Y-24,Y+35,909,916,8))
for y0,y1 in ((yr-21,yr-13),(yr+13,yr+21)):
    un(base,bx((-12,y0,913),(12,y1,zr)),cy((0,y0,zr),(0,y1,zr),12))
sub(base,cy((0,yr-23,zr),(0,yr+23,zr),5.05))
for x in (-35,35):
    un(base,cy((x,Y-23,918),(x,Y-12,918),7))
    sub(base,cy((x,Y-24,918),(x,Y-11,918),3.1))
sub(base,TM.copy(vendor))
sub(base,cy((0,Y,901),(0,Y,911),7.3))
output_holes=[(12.5*math.cos(math.radians(30+60*k)),Y+12.5*math.sin(math.radians(30+60*k))) for k in range(6)]
for x,y in output_holes:
    sub(base,cy((x,y,901),(x,y,917),1.7))
    sub(base,cy((x,y,906.5),(x,y,917),2.9))

bridge=cy((0,yr-12,zr),(0,yr+12,zr),10.5)
un(bridge,bx((-9,yr-9,934),(9,yr+9,939)),rrxy(-20,20,yr-12,yr+12,936.5,942,3))
for x0,x1 in ((-20,-12),(12,20)):
    un(bridge,bx((x0,yr-12,940),(x1,yr+12,zp)),cy((x0,yr,zp),(x1,yr,zp),12))
sub(bridge,cy((0,yr-13,zr),(0,yr+13,zr),6.1))
sub(bridge,cy((-21,yr,zp),(21,yr,zp),4.05))

socket=cy((-10,yr,zp),(10,yr,zp),11)
un(socket,cy((0,yr,963),(0,yr,979),9),oval(0,yr,973,1011,11,4))
sub(socket,cy((-11,yr,zp),(11,yr,zp),5.1))
sub(socket,oval(0,yr,981,1012,5.15,4))
for z in (993,1004):sub(socket,cy((-13,yr,z),(13,yr,z),2.15))
spine=oval(0,yr,982,1091,5,4);sub(spine,oval(0,yr,981,1092,4.45,4))
for z in (993,1004):sub(spine,cy((-6,yr,z),(6,yr,z),2.15))
roll_bush=[sub(cy((0,a,zr),(0,b,zr),6),cy((0,a-.01,zr),(0,b+.01,zr),5)) for a,b in ((yr-12,yr),(yr,yr+12))]
pitch_bush=[sub(cy((a,yr,zp),(b,yr,zp),5),cy((a-.01,yr,zp),(b+.01,yr,zp),4)) for a,b in ((-10,0),(0,10))]
roll_pin=un(cy((0,yr-21,zr),(0,yr+21,zr),4.95),cy((0,yr-22.5,zr),(0,yr-21,zr),7),cy((0,yr+21,zr),(0,yr+22.5,zr),7))
sub(roll_pin,cy((0,yr-23,zr),(0,yr+23,zr),1.7))
pitch_pin=un(cy((-20,yr,zp),(20,yr,zp),3.95),cy((-21.5,yr,zp),(-20,yr,zp),6),cy((20,yr,zp),(21.5,yr,zp),6))
sub(pitch_pin,cy((-22,yr,zp),(22,yr,zp),1.7))

progress('commit waist interface, trim casing under removable mount')
for j in reversed(list(wc.asBuiltJoints)):j.deleteMe()
for o in wc.occurrences:o.isGroundToParent=True
for key in ('W02_Waist_front_shell','W03_Waist_rear_shell'):
    c=wp[key].component;shape=TM.copy(c.bRepBodies.item(0))
    sub(shape,cy((0,Y,896.8),(0,Y,912),49.1))
    replace(c,[(key+'_v17_mount_recess',shape)],'V17 printed shell, recessed below the removable exact-profile fixed motor mount; hip output relief rebuilt in following operation.',plastic)
replace(wp['W04_PA12CF_fixed_yaw_mount'].component,[('W04_exact_scalloped_fixed_mount',mount)],'PA12-CF fixed mount follows actual scalloped gearbox interface. Eight small holes on 48 mm PCD; gearbox cover screws at 40.5 mm PCD are untouched. Four external M4 casing connections.',plastic)
c5=wp['W05_CNC_yaw_output_pitch_yoke'].component
replace(c5,[('GWK7010_vendor_output_MOVING',vendor_copy),('W05_nylon_output_base_lower_roll',base)],'V17 moving output base: six measured small output holes on 25 mm PCD, profile relief for locating pins. Lower roll Y axis, two M6 rod ears. PA12-CF prototype; CNC base alternative.',plastic)
c5.bRepBodies.item(0).appearance=vendor_ap;c5.name='W05_PA12CF_yaw_output_lower_roll_base'
c6=wp['W06_CNC_pitch_roll_bridge'].component
replace(c6,[('W06_nylon_roll_to_pitch_short_link',bridge)],'V17 nylon lower-roll to upper-pitch bridge; axes 27 mm apart, 10 mm lower / 8 mm upper nominal pins.',plastic);c6.name='W06_PA12CF_roll_to_pitch_short_link'
c7=wp['W07_CNC_roll_oval_adapter'].component
replace(c7,[('W07_nylon_pitch_eye_oval_socket',socket)],'V17 nylon upper-pitch eye and fully enclosed 18x10 oval socket. Central yaw-relative rear offset 10 mm. Crossbolts and crush sleeves remain prototype.',plastic);c7.name='W07_PA12CF_pitch_oval_socket'
replace(wp['W08_spine_oval_REFERENCE'].component,[('W08_spine_oval_reference',spine)],'Reference hollow oval spine 18x10; 0.55 mm wall assumption retained.',silver)
replace(wp['W09_pitch_bushings'].component,[(f'W09_lower_roll_bushing_{i}',b) for i,b in enumerate(roll_bush)],'Two lower roll plain sleeves: 10 ID / 12 OD x12 nominal.',silver);wp['W09_pitch_bushings'].component.name='W09_lower_roll_bushings'
replace(wp['W10_pitch_pin'].component,[('W10_lower_roll_nylon_pin',roll_pin)],'Nominal 10 mm lower-roll nylon pin reference with through M3 reinforcement passage. Fit and creep not qualified.',plastic);wp['W10_pitch_pin'].component.name='W10_lower_roll_pin'
replace(wp['W11_roll_bushings'].component,[(f'W11_upper_pitch_bushing_{i}',b) for i,b in enumerate(pitch_bush)],'Two upper pitch plain sleeves: 8 ID / 10 OD x10 nominal.',silver);wp['W11_roll_bushings'].component.name='W11_upper_pitch_bushings'
replace(wp['W12_roll_pin'].component,[('W12_upper_pitch_nylon_pin',pitch_pin)],'Nominal 8 mm upper-pitch nylon pin reference with M3 reinforcement passage. Fit and creep not qualified.',plastic);wp['W12_roll_pin'].component.name='W12_upper_pitch_pin'

hardware=[]
for x,y in fixed_holes:hardware.append(('M3_fixed_flange_reference',un(cy((x,y,891.8),(x,y,902.8),1.5),cy((x,y,902.8),(x,y,905.8),2.75))))
replace(wp['W13_fixed_motor_M4_bolt_REFERENCES'].component,hardware,'Eight M3 reference screws in the correct stationary flange at R24. They do not replace the R20.25 gearbox assembly screws.',silver)
wp['W13_fixed_motor_M4_bolt_REFERENCES'].component.name='W13_fixed_motor_M3_correct_flange_REFERENCES'
hardware=[]
for x,y in shell_holes:hardware.append(('M4_shell_mount_reference',un(cy((x,y,890.8),(x,y,902.8),2),cy((x,y,902.8),(x,y,906.8),3.5))))
replace(wp['W14_casing_M4_bolt_REFERENCES'].component,hardware,'Four external M4 mount-to-casing screws; final nuts/insert selection pending.',silver)
hardware=[]
for x,y in output_holes:hardware.append(('M3_output_reference',un(cy((x,y,897.5),(x,y,906.5),1.4),cy((x,y,906.5),(x,y,909.5),2.7))))
replace(wp['W15_output_bolt_REFERENCES'].component,hardware,'Six small M3-pattern output bolts on 25 PCD. Three larger locating features clear through profile pockets.',silver)
hardware=[]
for z in (993,1004):hardware.append(('M4_spine_reference',un(cy((-11,yr,z),(11,yr,z),2),cy((-14,yr,z),(-11,yr,z),3.5),cy((11,yr,z),(14,yr,z),3.5))))
replace(wp['W16_spine_crossbolt_REFERENCES'].component,hardware,'Two M4 oval retention references; add crush protection after measuring tube wall.',silver)
reinf=newpart(wc,'W17_M3_pin_reinforcement_REFERENCES','M3 through-bolt reinforcement in both nylon pivot pins; head/nut cylinders are packaging references.','steel reference')
add(reinf.component,un(cy((0,yr-22.5,zr),(0,yr+22.5,zr),1.5),cy((0,yr-25.5,zr),(0,yr-22.5,zr),2.75),cy((0,yr+22.5,zr),(0,yr+25.5,zr),2.75)),'W17_roll_M3_through_reference',silver)
add(reinf.component,un(cy((-21.5,yr,zp),(21.5,yr,zp),1.5),cy((-24.5,yr,zp),(-21.5,yr,zp),2.75),cy((21.5,yr,zp),(24.5,yr,zp),2.75)),'W17_pitch_M3_through_reference',silver)

# Root fillets remain editable Fusion features. Restrict each to the explicitly
# modeled planar junction rather than rounding the hole/shaft interfaces.
fillets=[]
for c,z,r in ((c5,916,2.0),(c6,942,2.0)):
    b=c.bRepBodies.item(c.bRepBodies.count-1)
    try:
        f=fillet_edges(c,b,r,lambda e: isinstance(e.geometry,adsk.core.Line3D) and abs(e.boundingBox.minPoint.z*10-z)<.001 and abs(e.boundingBox.maxPoint.z*10-z)<.001 and e.length*10>4,'V17_blended_yoke_roots')
        fillets.append({'part':c.name,'success':bool(f),'radius':r})
    except Exception as e:fillets.append({'part':c.name,'success':False,'error':str(e)})

for o in wc.occurrences:o.isLightBulbOn=True
for sk0 in cc.sketches:sk0.isLightBulbOn=False
for pl in cc.constructionPlanes:pl.isLightBulbOn=False
construction.isLightBulbOn=False
wc.name='Waist_roll_pitch_v17';wc.description='V17 corrected fixed/rotating 7010 interfaces, nylon roll below pitch, shorter link and symmetric M6 rod ears. Prototype only.'
result={'fixed_PCD_mm':48,'output_PCD_mm':25,'lower_axis':'roll Y','upper_axis':'pitch X',
        'roll_center_mm':[0,yr,zr],'pitch_center_mm':[0,yr,zp],'axis_separation_mm':zp-zr,
        'rod_anchor_centers_mm':[[-35,Y-17.5,918],[35,Y-17.5,918]],'fillets':fillets}
(OUT/'waist_build.json').write_text(json.dumps(result,indent=2));progress('waist geometry committed; joints pending')
