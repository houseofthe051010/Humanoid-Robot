exec(compile((ROOT/'v18/common.py').read_text(),'<v18 common>','exec'))
OPENING=50.0
u=(math.cos(math.radians(25)),0,-math.sin(math.radians(25)))
w=(math.sin(math.radians(25)),0,math.cos(math.radians(25)))
P=(62,Y,798.6);R=(140,Y,759.6)
def pp(t,a=0,b=0):return (P[0]+u[0]*t+w[0]*b,Y+a,P[2]+u[2]*t+w[2]*b)
def pcyl(a,b,r):return cy(pp(a),pp(b),r)
def rcyl(a,b,r):return cy((R[0],Y+a,R[2]),(R[0],Y+b,R[2]),r)
construction=root.occurrences.addNewComponent(adsk.core.Matrix3D.create());construction.component.name='ZZ_V18_blended_fork_lofts_NOT_A_PART'
cc=construction.component;construction.isLightBulbOn=False
progress('loft broad transitions between pitch output flange and roll fork arms')
gussets=[]
for side,last_y in ((-1,40),(1,36)):
    inp=cc.features.loftFeatures.createInput(adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    for i,(yy,ww,minor,major) in enumerate(((20,22,6,16),(28,18,8,18),(last_y,10,12,20))):
        y=Y+side*yy
        pi=cc.constructionPlanes.createInput();pi.setByOffset(cc.xZConstructionPlane,adsk.core.ValueInput.createByReal(-y/10))
        pl=cc.constructionPlanes.add(pi);pl.isLightBulbOn=False;sk=cc.sketches.add(pl);sk.isLightBulbOn=False
        center=pp(36,side*yy,ww)
        majorpt=tuple(center[k]+w[k]*major for k in range(3));minorpt=tuple(center[k]+u[k]*minor for k in range(3))
        sk.sketchCurves.sketchEllipses.add(sk.modelToSketchSpace(pt(center)),sk.modelToSketchSpace(pt(majorpt)),sk.modelToSketchSpace(pt(minorpt)))
        inp.loftSections.add(sk.profiles.item(0));sk.name=f'V18_fork_blend_{side}_{i}'
    feat=cc.features.loftFeatures.add(inp);feat.name=f'V18_broad_fork_transition_{side}'
    g=TM.copy(feat.bodies.item(0))
    sub(g,pcyl(-35,28.3,60));sub(g,rcyl(-35,29,59))
    gussets.append(g)

fork=pcyl(30,42,42)
un(fork,pcyl(20,31,19.95))
sub(fork,pcyl(19,43,8))
end=pp(36)
for a,b in ((-43,-35),(29,37)):
    un(fork,beam_y((R[0],R[2]),(end[0],end[2]),20,Y+a,Y+b),rcyl(a,b,36))
for g in gussets:un(fork,g)
# Large straight, flush openings. The previous small projecting journals and
# their bearing references are deliberately replaced by an unselected interface.
sub(fork,rcyl(-45,39,OPENING/2))
for k in range(4):
    ang=math.radians(45+90*k)
    x,z=R[0]+30*math.cos(ang),R[2]+30*math.sin(ang)
    for a,b in ((-44,-34),(28,38)):sub(fork,cy((x,Y+a,z),(x,Y+b,z),2.2))
    aa,bb=15*math.cos(ang),15*math.sin(ang)
    sub(fork,cy(pp(19,aa,bb),pp(43,aa,bb),2.2))
sub(fork,rcyl(-34,28,58.6))

report={'clear_opening_mm':OPENING,'roll_fork_end_OD_mm':72,'arm_width_mm':40,
        'pitch_flange_thickness_mm':12,'construction':'native three-section elliptical lofts plus broad arms and flange',
        'roll_bearing_status':'old 40x52 references and narrow journals removed; enlarged gearbox/output/bearing interface remains provisional',
        'parts':[],'fillets':[]}
for go,sg in ((right,1),(left,-1)):
    progress('apply matching flush roll openings and fork blends '+go.component.name)
    ps=parts(go);o=ps['Q02_CNC_yaw_to_roll_cradle'];proxy=o.createForAssemblyContext(go)
    body=TM.copy(proxy.bRepBodies.item(0));frame=proxy.transform2
    for a,b in ((-34,-26),(20,28)):
        fill=rcyl(a,b,27)
        if sg<0:reflect(fill)
        transform(fill,frame)
        un(body,fill)
    hole=rcyl(-35,29,OPENING/2)
    if sg<0:reflect(hole)
    transform(hole,frame);sub(body,hole)
    inv=proxy.transform2.copy();inv.invert()
    replace(o.component,[('Q02_v18_flat_50mm_roll_openings',transform(body,inv))],
            'V18 flat annular roll mounts with straight 50 mm clear center openings. Small raised journal lips removed. Larger gearbox/output/bearing interface remains an estimate.',silver)

    o=ps['Q03_CNC_roll_to_pitch_fork'];frame=o.createForAssemblyContext(go).transform2
    b=TM.copy(fork)
    if sg<0:reflect(b)
    transform(b,frame);inv=frame.copy();inv.invert();transform(b,inv)
    replace(o.component,[('Q03_v18_broad_lofted_fork',b)],
            'V18 40 mm-wide paired arms, flat 50 mm roll openings in 72 mm end rings, 12 mm pitch flange and broad three-section lofted webs. Output bolt/bearing design remains provisional.',silver)
    # A small native edge fillet supplements the broad lofted load-spreading webs.
    target=o.component.bRepBodies.item(0)
    try:
        def junction(e):
            return e.faces.count==2 and any(adsk.core.NurbsSurface.cast(f.geometry) for f in e.faces) and any(adsk.core.Plane.cast(f.geometry) for f in e.faces) and e.length*10>4
        f=fillet_edges(o.component,target,1.5,junction,'V18_loft_to_plate_junction_fillets')
        report['fillets'].append({'leg':go.component.name,'success':bool(f),'radius_mm':1.5})
    except Exception as e:report['fillets'].append({'leg':go.component.name,'success':False,'error':str(e)})
    c=ps['H02_Hip_pitch_roll_bearing_REFERENCES'].component
    for old in list(c.bRepBodies):
        if old.name.startswith('roll'):c.features.removeFeatures.add(old)
    c.description='Pitch 40x52x7 bearing reservations retained. Old small roll bearings removed after changing to the provisional straight 50 mm interface; roll bearing selection/journal remains to design.'
    report['parts'].append(go.component.name)
construction.isLightBulbOn=False
(OUT/'opening_and_blend_build.json').write_text(json.dumps(report,indent=2));result=report
