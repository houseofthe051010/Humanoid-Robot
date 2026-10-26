exec(compile((ROOT/'v18/common.py').read_text(),'<v18 common>','exec'))
progress('separate explicit estimated pitch shells from the waist skin')
cc=next(o.component for o in root.occurrences if o.component.name=='ZZ_V17_motor_interface_construction')
report={'shells':[],'motor_output_faces':[]}
def local_from_world(o,go,b):
    inv=o.createForAssemblyContext(go).transform2.copy();inv.invert();return transform(b,inv)
for go in (right,left):
    ps=parts(go)
    sg=1 if go==right else -1
    uu=(math.cos(math.radians(25)),0,-math.sin(math.radians(25)))
    def at(t):return (sg*(62+uu[0]*t),Y,798.6+uu[2]*t)
    # Use a slightly oversized simple partition volume, not a coincident copy
    # of the perforated casing, to avoid ambiguous coincident Boolean faces.
    seed=cy(at(-34.05),at(28.05),59)
    frame=ps['T07_Hip_pitch_motor_ENVELOPE_REFERENCE'].createForAssemblyContext(go).transform2
    transform(seed,frame)
    housing=ps.get('H05_DJI10018_pitch_gearbox_shell_ESTIMATE')
    if housing is None:
        housing=newpart(go.component,'H05_DJI10018_pitch_gearbox_shell_ESTIMATE',
            'Separate estimated motor-plus-gearbox housing around the existing 105 mm DJI10018 reference. 117 OD /106 ID, overall axial estimate 62 mm including annular endplates; no planetary internals designed. Split shell follows existing waist seam.','PA12-CF provisional housing estimate')
    assert housing.component.bRepBodies.count==0
    for key in ('W02_Waist_front_shell','W03_Waist_rear_shell'):
        o=wp[key];p=o.createForAssemblyContext(wg);before=TM.copy(p.bRepBodies.item(0))
        cutout=ix(TM.copy(before),TM.copy(seed))
        assert cutout.volume>0
        add(housing.component,cutout,key+'_pitch_shell_half',plastic)
        remaining=sub(before,TM.copy(seed))
        assert remaining.isSolid and remaining.volume>0
        replace(o.component,[(key+'_v18_separate_motor_shell_interface',local_from_world(o,wg,remaining))],
            'V18 hollow central waist skin; the estimated pitch motor/gearbox shells are separate visible H05 components. Output regions remain open.',plastic)
    rigid(go.component,ps['T07_Hip_pitch_motor_ENVELOPE_REFERENCE'],housing,'H05_pitch_shell_layout')
    case=ps['H01_Hip_roll_117OD_106ID_case'].component
    case.name=go.component.name+'_H01_DJI10018_roll_gearbox_shell_ESTIMATE'
    case.description='Estimated motor-plus-gearbox cover around the copied 105 mm DJI10018. The roll cradle supplies its endplates. Internal planetary is not designed; envelope remains provisional.'
    report['shells'].append({'leg':go.component.name,'pitch_shell_bodies':housing.component.bRepBodies.count})

progress('turn measured GIM6010 output faces inward')
for n,sg in (('W19',-1),('W20',1)):
    o=next(o for o in wg.component.occurrences if o.component.partNumber.startswith(n+'_'))
    p=o.createForAssemblyContext(wg)
    m=adsk.core.Matrix3D.create();m.setToRotation(math.pi,V3.create(0,0,1),pt((sg*73,Y,1040)))
    rows=[]
    for b in p.bRepBodies:rows.append((b.name,local_from_world(o,wg,transform(TM.copy(b),m))))
    replace(o.component,rows,'Actual standard GIM6010-8 floating reference, six-hole output face directed inward toward the spine. No cranks or differential rods yet.',black)
    p=o.createForAssemblyContext(wg)
    face=next(f for b in p.bRepBodies for f in b.faces if adsk.core.Plane.cast(f.geometry) and abs(f.area*100-550.69756)<.1)
    plane=adsk.core.Plane.cast(face.geometry)
    face_x=plane.origin.x*10
    assert sg*face_x<73,(n,face_x)
    report['motor_output_faces'].append({'part':n,'output_face_x_mm':face_x,'inward':True,'normal':list(plane.normal.asArray())})
wg.component.name='Waist_roll_pitch_v18'
for o in wg.component.occurrences:o.isLightBulbOn=True;o.createForAssemblyContext(wg).isLightBulbOn=True
(OUT/'shells_and_motor_orientation.json').write_text(json.dumps(report,indent=2));result=report
