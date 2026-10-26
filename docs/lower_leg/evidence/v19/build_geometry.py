exec(compile((ROOT/'v19/common.py').read_text(),'<v19 common>','exec'))
assert not any(o.component.name=='ZZ_V19_construction' for o in root.occurrences)
co=root.occurrences.addNewComponent(adsk.core.Matrix3D.create());cc=co.component;cc.name='ZZ_V19_construction';co.isLightBulbOn=False
report={'leg_spacing_mm':240,'roll_centers_x_mm':[-RX,RX],'pitch_centers_x_mm':[-PX,PX],'pitch_z_mm':PZ,'roll_z_mm':RZ,'tube_OD_ID_mm':[110,106],'features':[]}
def loft_z(rows,name):
    inp=cc.features.loftFeatures.createInput(adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    for i,(z,x,y,rx,ry) in enumerate(rows):
        pi=cc.constructionPlanes.createInput();pi.setByOffset(cc.xYConstructionPlane,adsk.core.ValueInput.createByReal(z/10))
        pl=cc.constructionPlanes.add(pi);pl.isLightBulbOn=False;sk=cc.sketches.add(pl);sk.isLightBulbOn=False
        center=sk.modelToSketchSpace(pt((x,y,z)))
        if rx>=ry:major=(x+rx,y,z);minor=(x,y+ry,z)
        else:major=(x,y+ry,z);minor=(x+rx,y,z)
        sk.sketchCurves.sketchEllipses.add(center,sk.modelToSketchSpace(pt(major)),sk.modelToSketchSpace(pt(minor)))
        inp.loftSections.add(sk.profiles.item(0));sk.name=name+'_section_'+str(i)
    f=cc.features.loftFeatures.add(inp);f.name=name;return TM.copy(f.bodies.item(0))
def loft_y(rows,name):
    inp=cc.features.loftFeatures.createInput(adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    for i,(y,x,z,ru,rw) in enumerate(rows):
        pi=cc.constructionPlanes.createInput();pi.setByOffset(cc.xZConstructionPlane,adsk.core.ValueInput.createByReal(-y/10))
        pl=cc.constructionPlanes.add(pi);pl.isLightBulbOn=False;sk=cc.sketches.add(pl);sk.isLightBulbOn=False
        center=(x,y,z)
        aa=tuple(center[k]+u[k]*ru for k in range(3));bb=tuple(center[k]+w[k]*rw for k in range(3))
        major,minor=(aa,bb) if ru>=rw else (bb,aa)
        sk.sketchCurves.sketchEllipses.add(sk.modelToSketchSpace(pt(center)),sk.modelToSketchSpace(pt(major)),sk.modelToSketchSpace(pt(minor)))
        inp.loftSections.add(sk.profiles.item(0));sk.name=name+'_section_'+str(i)
    f=cc.features.loftFeatures.add(inp);f.name=name;return TM.copy(f.bodies.item(0))
def save(b,name,ap=silver):
    assert b.isSolid and b.volume>0,name
    add(cc,b,name,ap)
    report['features'].append({'name':name,'volume_mm3':b.volume*1000,'shells':sum(not s.isVoid for s in b.shells)})

progress('build centered sculpted yaw to paired roll-output yoke')
# Six-bolt 7010 output and 6007 journal retain their already verified interface.
yoke=un(cy((RX,Y,662.3),(RX,Y,673),18),cy((RX,Y,672),(RX,Y,689.5),17.45),cy((RX,Y,689),(RX,Y,696),22))
bell=loft_z([(690,RX,Y,21,21),(696,RX,Y,26,33),(702,RX,Y,24,45)],'V19_centered_yaw_bell')
un(yoke,bell)
for s,ya,yb in ((-1,-46,-38),(1,32,40)):
    ym=(ya+yb)/2
    web=loft_z([(694,RX,Y+s*24,22,13),(708,RX,Y+ym,22,4),(735,RX,Y+ym,26,4)],f'V19_roll_output_swept_web_{s}')
    un(yoke,web,rcyl(ya,yb,33))
    # Large hollow output journals on both sides of the unmodeled gearbox.
    un(yoke,rcyl(-38,-27 if s<0 else -27,24.95) if s<0 else rcyl(20.8,32,24.95))
    sub(yoke,rcyl(ya-1,yb+1,18))
    sub(yoke,rcyl(-38.1,-26.9,18) if s<0 else rcyl(20.7,32.1,18))
    # Rounded lightening window beneath each bearing/output center.
    window=beam_y((RX,710),(RX,724),8,Y+ya-1,Y+yb+1)
    sub(yoke,window)
    for k in range(4):
        az=math.radians(45+90*k);x=RX+21*math.cos(az);z=RZ+21*math.sin(az)
        sub(yoke,cy((x,Y+ya-1,z),(x,Y+yb+1,z),2.2))
# Open saddle clearance leaves the tube untouched and no rectangular floor.
sub(yoke,rcyl(-35.5,29.5,57.8))
un(yoke,rcyl(-38,-27.1,24.95),rcyl(20.8,32,24.95))
sub(yoke,rcyl(-47,41,18))
for k in range(4):
    az=math.radians(45+90*k);x=RX+21*math.cos(az);z=RZ+21*math.sin(az)
    sub(yoke,cy((x,Y-47,z),(x,Y-27,z),2.2));sub(yoke,cy((x,Y+20,z),(x,Y+41,z),2.2))
sub(yoke,cy((RX,Y,661),(RX,Y,673),7.3))
for k in range(6):
    az=math.radians(30+60*k);x=RX+12.5*math.cos(az);y=Y+12.5*math.sin(az)
    sub(yoke,cy((x,y,661),(x,y,709),1.7));sub(yoke,cy((x,y,668),(x,y,709),2.8))
save(yoke,'Q02_centered_dual_output_yoke')

progress('build 110 OD aluminum tubes and recessed endcaps')
rolltube=sub(rcyl(-26,20,55),rcyl(-27,21,53));save(rolltube,'H01_roll_110OD_106ID_tube')
pitchtube=sub(pcyl(-26,20,55),pcyl(-27,21,53));save(pitchtube,'H05_pitch_110OD_106ID_tube')
rollcaps=[]
for side,lo,hi,groove in ((-1,-36,-23,(-26,-23)),(1,17,30,(17,20))):
    cap=rcyl(lo,hi,57)
    sub(cap,rcyl(lo-1,hi+1,25.2))
    # Tube enters a 3 mm deep female annular register; no thread in 2 mm wall.
    sub(cap,sub(rcyl(groove[0]-.001,groove[1]+.001,55.05),rcyl(groove[0]-.01,groove[1]+.01,52.95)))
    # Open inner cavity beyond the bearing shoulder.
    if side<0:
        sub(cap,rcyl(-27,-22,52.95));sub(cap,rcyl(-36.1,-29,32.5))
    else:
        sub(cap,rcyl(16,21,52.95));sub(cap,rcyl(23,30.1,32.5))
    for ang in (85,120,155):
        az=math.radians(ang);x=RX+45*math.cos(az);z=RZ+45*math.sin(az)
        sub(cap,cy((x,Y+lo-1,z),(x,Y+hi+1,z),2.2))
    # Four small external tie-bolt lugs avoid threading the 2 mm tube wall.
    for k in range(4):
        az=math.radians(45+90*k);x=RX+58.8*math.cos(az);z=RZ+58.8*math.sin(az)
        un(cap,cy((x,Y+lo,z),(x,Y+hi,z),4.5))
        sub(cap,cy((x,Y+lo-1,z),(x,Y+hi+1,z),1.7))
    rollcaps.append(cap);save(cap,'H06_roll_endcap_'+str(side))
rear=cone(pp(-34),pp(-26),28,55)
un(rear,pcyl(-26,-23,52.95));sub(rear,pcyl(-35,-22,17))
sub(rear,pcyl(-34.1,-27,26))
front=pcyl(17,28,57);sub(front,pcyl(16,29,20.2));sub(front,pcyl(21,28.1,26))
sub(front,sub(pcyl(17,20,55.05),pcyl(16.9,20.1,52.95)))
sub(front,pcyl(16,20,52.95))
for a in (-20,20):
    for b in (-33,33):sub(rear,cy(pp(-35,a,b),pp(-22,a,b),2.2))
for k in range(4):
    az=math.radians(45+90*k);a,b=58.8*math.cos(az),58.8*math.sin(az)
    for cap,lo,hi in ((front,20,28),(rear,-28,-26)):
        un(cap,cy(pp(lo,a,b),pp(hi,a,b),4.5))
        sub(cap,cy(pp(lo-1,a,b),pp(hi+1,a,b),1.7))
save(rear,'H07_pitch_conical_rear_endcap');save(front,'H07_pitch_front_endcap')

progress('build compact pitch output fork with smooth curved side transitions')
fork=un(pcyl(28.5,35.5,30),pcyl(20.1,28.6,19.95));sub(fork,pcyl(19,36,10))
for side,ya,yb in ((-1,-41,-36),(1,30,35)):
    pad=None
    points=[]
    for ang in (85,120,155):
        az=math.radians(ang);points.append((RX+45*math.cos(az),RZ+45*math.sin(az)))
    for aa,bb in zip(points,points[1:]):
        segment=beam_y(aa,bb,7,Y+ya,Y+yb)
        pad=segment if pad is None else un(pad,segment)
    center=pp(32,0,0)
    target=((points[0][0]+points[-1][0])/2,(points[0][1]+points[-1][1])/2)
    g=loft_y([(Y+side*13,center[0],center[2],5,19),(Y+side*24,(center[0]+target[0])/2,(center[2]+target[1])/2,8,23),
              (Y+(ya+yb)/2,target[0],target[1],13,27)],f'V19_pitch_to_roll_curved_side_{side}')
    un(fork,g,pad)
    for x,z in points:sub(fork,cy((x,Y+ya-1,z),(x,Y+yb+1,z),2.2))
for k in range(4):
    az=math.radians(45+90*k);a,b=15*math.cos(az),15*math.sin(az)
    sub(fork,cy(pp(19,a,b),pp(37,a,b),2.2))
# Exact stationary housing clearance; broad loft roots are outside the motor cavity.
sub(fork,pcyl(-35,28,55.3));sub(fork,rcyl(-36,30,57.1))
save(fork,'Q03_curved_pitch_to_tube_fork')
co.isLightBulbOn=False
(OUT/'geometry_build.json').write_text(json.dumps(report,indent=2));result=report
