exec(compile((ROOT/'v19/common.py').read_text(),'<v19 common>','exec'))
co=next(o for o in root.occurrences if o.component.name=='ZZ_V19_construction');cc=co.component
src=(OUT/'build_geometry.py').read_text();exec(compile(src[src.index('def loft_z'):src.index('def save')],'<loft helpers>','exec'))
def orient_loft(rows,name):
    inp=cc.features.loftFeatures.createInput(adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    for i,(y,center,axis0,r0,axis1,r1) in enumerate(rows):
        pi=cc.constructionPlanes.createInput();pi.setByOffset(cc.xZConstructionPlane,adsk.core.ValueInput.createByReal(-y/10))
        pl=cc.constructionPlanes.add(pi);pl.isLightBulbOn=False;sk=cc.sketches.add(pl);sk.isLightBulbOn=False
        p=(center[0],y,center[1]);a=(p[0]+axis0[0]*r0,y,p[2]+axis0[1]*r0);b=(p[0]+axis1[0]*r1,y,p[2]+axis1[1]*r1)
        major,minor=(a,b) if r0>=r1 else (b,a)
        # Keep the ellipse parameter direction consistent between profiles.
        if (major[0]-p[0])*(minor[2]-p[2])-(major[2]-p[2])*(minor[0]-p[0])>0:
            minor=(2*p[0]-minor[0],y,2*p[2]-minor[2])
        sk.sketchCurves.sketchEllipses.add(sk.modelToSketchSpace(pt(p)),sk.modelToSketchSpace(pt(major)),sk.modelToSketchSpace(pt(minor)))
        inp.loftSections.add(sk.profiles.item(0));sk.name=name+'_section_'+str(i)
    f=cc.features.loftFeatures.add(inp);f.name=name;return TM.copy(f.bodies.item(0))
progress('resculpt yoke and housing fork to eliminate cut-off fins')
yoke=un(cy((RX,Y,662.3),(RX,Y,673),18),cy((RX,Y,672),(RX,Y,689.5),17.45),cy((RX,Y,689),(RX,Y,696),22))
un(yoke,loft_z([(692,RX,Y,21.5,21.5),(694,RX,Y,24,38),(696,RX,Y,22,46)],'V19_clean_low_yaw_bell'))
for side,ya,yb in ((-1,-46,-38),(1,32,40)):
    ym=(ya+yb)/2
    web=loft_z([(695,RX,Y+ym,20,4),(711,RX,Y+ym,20,4),(735,RX,Y+ym,26,4)],'V19_clean_output_web_'+str(side))
    un(yoke,web,rcyl(ya,yb,33))
    sub(yoke,beam_y((RX,710),(RX,724),8,Y+ya-1,Y+yb+1))
un(yoke,rcyl(-38,-27.1,24.95),rcyl(20.8,32,24.95));sub(yoke,rcyl(-47,41,18))
for k in range(4):
    a=math.radians(45+90*k);x,z=RX+21*math.cos(a),RZ+21*math.sin(a)
    sub(yoke,cy((x,Y-47,z),(x,Y-27,z),2.2));sub(yoke,cy((x,Y+20,z),(x,Y+41,z),2.2))
sub(yoke,cy((RX,Y,661),(RX,Y,673),7.3))
for k in range(6):
    a=math.radians(30+60*k);x,y=RX+12.5*math.cos(a),Y+12.5*math.sin(a)
    sub(yoke,cy((x,y,661),(x,y,697),1.7));sub(yoke,cy((x,y,668),(x,y,697),2.8))
fork=un(pcyl(28.5,35.5,30),pcyl(20.1,28.6,19.95));sub(fork,pcyl(19,37,10))
tangent=(math.sqrt(3)/2,.5);radial=(-.5,math.sqrt(3)/2)
for side,ya,yb,turn,last in ((-1,-41,-36,36.5,39),(1,30,35,30.5,33)):
    start=pp(32)
    outside=(RX+radial[0]*68+u[0]*6,RZ+radial[1]*68+u[2]*6)
    bend=(RX+radial[0]*70+u[0]*9,RZ+radial[1]*70+u[2]*9)
    target=(RX+radial[0]*45,RZ+radial[1]*45)
    # Maintain the same ellipse parameterization and principal direction.
    g=loft_y([(Y+side*12,start[0],start[2],3.5,14),
              (Y+side*25,outside[0],outside[1],4,10),
              (Y+side*last,target[0],target[1],5,24)],'V19_clean_curved_housing_arm_'+str(side))
    un(fork,g)
    points=[]
    for ang in (85,120,155):
        a=math.radians(ang);points.append((RX+45*math.cos(a),RZ+45*math.sin(a)))
    for a,b in zip(points,points[1:]):un(fork,beam_y(a,b,7,Y+ya,Y+yb))
    for x,z in points:sub(fork,cy((x,Y+ya-1,z),(x,Y+yb+1,z),2.2))
for k in range(4):
    a=math.radians(45+90*k);sub(fork,cy(pp(19,15*math.cos(a),15*math.sin(a)),pp(37,15*math.cos(a),15*math.sin(a)),2.2))
# Only the output/bearing bore is relieved; the arm lofts are routed outside
# the stationary motor envelope rather than carving thin fins from thick blocks.
sub(fork,rcyl(-48,42,34))
source=json.loads((OUT/'live_source_inventory.json').read_text())
F=adsk.core.Matrix3D.create();F.setWithArray(next(p['transform'] for g in source['groups'] if g['name']=='Right_leg' for p in g['parts'] if p['part']=='Q02_CNC_yaw_to_roll_cradle'))
report=[]
for go,s in ((right,1),(left,-1)):
    for key,shape in (('Q02_CNC_yaw_to_roll_cradle',yoke),('Q03_CNC_roll_to_pitch_fork',fork)):
        b=TM.copy(shape)
        if s<0:reflect(b)
        else:transform(b,F)
        o=parts(go)[key]
        world_replace(go,o,[(key+'_v19_continuous_curved_profile',b)],o.component.description,silver)
        report.append({'part':go.component.name+'/'+key,'volume_mm3':b.volume*1000,'shells':sum(not ss.isVoid for ss in b.shells)})
# Restore exact bilateral endcap geometry after the right assembly pin/ground
# distinction made the first follow-up cuts use an incorrect tool frame.
for key in ('H06_Roll_tube_recessed_endcaps','H07_Pitch_tube_recessed_endcaps'):
    src=parts(left)[key].createForAssemblyContext(left);rows=[]
    for b in src.bRepBodies:rows.append((b.name,transform(reflect(TM.copy(b)),F)))
    o=parts(right)[key];world_replace(right,o,rows,o.component.description,silver)
co.isLightBulbOn=False
(OUT/'resculpted_brackets.json').write_text(json.dumps(report,indent=2));result=report
