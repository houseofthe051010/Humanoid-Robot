exec(compile((ROOT/'v17/common.py').read_text(),'<v17 common>','exec'))
progress('rebuild smooth waist shell around real DJI reference diameters')
oldcc=next(o.component for o in root.occurrences if o.component.name=='ZZ_V15_construction_lofts_NOT_A_PART')
lo=oldcc.features.loftFeatures.itemByName('Waist_anatomical_outer')
li=oldcc.features.loftFeatures.itemByName('Waist_5mm_skin_inner')
assert lo and li
outer=TM.copy(lo.bodies.item(0));sub(outer,TM.copy(li.bodies.item(0)))
cc=next(o.component for o in root.occurrences if o.component.name=='ZZ_V17_motor_interface_construction')
u=(math.cos(math.radians(25)),0,-math.sin(math.radians(25)))
v=(0,1,0);w=(math.sin(math.radians(25)),0,math.cos(math.radians(25)))
for go,sg in ((right,1),(left,-1)):
    seed=cc.bRepBodies.itemByName(go.component.name+'_pitch_case_seed');assert seed
    un(outer,TM.copy(seed))
    c=(62,Y,798.6)
    def pos(t,a=0,b=0):
        p=tuple(c[i]+t*u[i]+a*v[i]+b*w[i] for i in range(3))
        return (sg*p[0],p[1],p[2])
    def tool(a,b,r):return cy(pos(a),pos(b),r)
    # Two complete annular end seats. The shell ends at these faces, leaving
    # the central output and all material beyond the face clear to rotate.
    for a,b,r in ((-26,20,53),(-35,29,17),(-34,-27,26),(20,29,20.2),(21,28.1,26),(-85,-34,60),(28,85,60)):
        sub(outer,tool(a,b,r))
    for a in (-20,20):
        for b in (-33,33):
            sub(outer,cy(pos(-35,a,b),pos(-25,a,b),2.2))
            sub(outer,cy(pos(19,a,b),pos(29,a,b),2.2))
    # Roll housing and its paired fork are outside the pelvis skin.
    sub(outer,cy((sg*140,Y-46,759.6),(sg*140,Y+41,759.6),60))
    ps=parts(go)
    for key in ('Q02_CNC_yaw_to_roll_cradle','Q03_CNC_roll_to_pitch_fork'):
        for b in ps[key].component.bRepBodies:
            if outer.boundingBox.intersects(b.boundingBox):sub(outer,TM.copy(b))

# Closed, flat shoulder for the separate correct-profile waist mount.
sub(outer,bx((-250,Y-180,896.8),(250,Y+180,940)))
for deg in (45,135,225,315):
    x,y=43*math.cos(math.radians(deg)),Y+43*math.sin(math.radians(deg))
    un(outer,cy((x,y,888),(x,y,896.8),5.8))
    sub(outer,cy((x,y,887),(x,y,898),2.3))
sub(outer,cy((0,Y,875.8),(0,Y,896.81),39))
for x,z in ((-111,805),(111,805),(-48,882),(48,882)):
    un(outer,cy((x,Y-9,z),(x,Y+9,z),5))
    sub(outer,cy((x,Y-10,z),(x,Y+10,z),2.2))
slot=un(bx((-10,Y+40,850),(10,Y+85,860)),cy((-10,Y+40,855),(-10,Y+85,855),5),cy((10,Y+40,855),(10,Y+85,855),5))
sub(outer,slot)
report=[]
for key,tool in (('W02_Waist_front_shell',bx((-250,Y-180,700),(250,Y-.2,940))),('W03_Waist_rear_shell',bx((-250,Y+.2,700),(250,Y+180,940)))):
    shape=ix(TM.copy(outer),tool);before=shape.volume*1000
    shells=[s for s in shape.shells if not s.isVoid]
    if len(shells)>1:
        main=max(shells,key=lambda s:sum(f.area for f in s.faces))
        assert TM.deleteFaces(list(main.faces),False)
    assert shape.isSolid and shape.volume>0 and sum(not s.isVoid for s in shape.shells)==1
    assert shape.volume*1000>before*.98,(key,'detached material is not a sliver')
    replace(wp[key].component,[(key+'_v17_DJI_seats_open_outputs',shape)],
            'V17 PA12-CF curved waist half, hollow electronics cavity, 117 OD /106 ID DJI pitch barrels, paired central output/bearing openings, 40x66 estimated stator pattern, clean terminations before rotating outputs and separate corrected fixed-yaw mount.',plastic)
    report.append({'part':key,'volume_mm3':shape.volume*1000,'removed_detached_mm3':before-shape.volume*1000,'outer_shells':1})
(OUT/'waist_shell_build.json').write_text(json.dumps(report,indent=2));result=report
