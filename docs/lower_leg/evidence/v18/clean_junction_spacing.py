exec(compile((ROOT/'v18/common.py').read_text(),'<v18 common>','exec'))
progress('create clean full pitch flange and flat-ended fork arms with working space')
def beam_y(a,b,r,y0,y1):
    dx,dz=b[0]-a[0],b[1]-a[1];ll=math.hypot(dx,dz)
    return TM.createBox(adsk.core.OrientedBoundingBox3D.create(pt(((a[0]+b[0])/2,(y0+y1)/2,(a[1]+b[1])/2)),V3.create(dx/ll,0,dz/ll),V3.create(0,1,0),ll/10,(y1-y0)/10,2*r/10))
source=(OUT/'enlarge_openings_and_blend_forks.py').read_text()
shape_code=source[source.index('OPENING='):source.index('report=')]
shape_code=shape_code.replace('R=(140,Y,759.6)','R=(158,Y,759.6)').replace('ZZ_V18_blended_fork_lofts_NOT_A_PART','ZZ_V18_final_junction_lofts_NOT_A_PART')
exec(compile(shape_code,'<clean spaced fork geometry>','exec'))

def shift_all_bodies_world(go,o,dx):
    inv=o.createForAssemblyContext(go).transform2.copy();inv.invert()
    v=V3.create(dx/10,0,0);v.transformBy(inv);m=adsk.core.Matrix3D.create();m.translation=v
    bs=adsk.core.ObjectCollection.create()
    for b in o.component.bRepBodies:bs.add(b)
    inp=o.component.features.moveFeatures.createInput2(bs);inp.defineAsFreeMove(m)
    f=o.component.features.moveFeatures.add(inp);f.name='V18_roll_package_outward_18mm'

report={'roll_center_abs_x_mm':158,'outward_shift_mm':18,'thigh_spacing_mm':260,'pitch_flange':'complete round flange without case-cut fins','fillets':[]}
for go,sg in ((right,1),(left,-1)):
    progress('move roll package and clean adapter '+go.component.name)
    ps=parts(go);o=ps['Q02_CNC_yaw_to_roll_cradle'];orig=TM.copy(o.component.bRepBodies.item(0))
    upper=ix(TM.copy(orig),bx((-400,Y-200,700.3),(400,Y+200,920)))
    bottom=sub(orig,bx((-400,Y-200,700.5),(400,Y+200,920)))
    tx(upper,dx=sg*18);un(bottom,upper)
    floor=rrxy(77,221,Y-43,Y+38,693.5,700.5,8)
    if sg<0:reflect(floor)
    un(bottom,floor)
    for k in range(6):
        ang=math.radians(30+60*k);x=sg*(130+12.5*math.cos(ang));y=Y+12.5*math.sin(ang)
        sub(bottom,cy((x,y,661),(x,y,701),1.7));sub(bottom,cy((x,y,668),(x,y,701),2.8))
    replace(o.component,[('Q02_v18_outward_roll_cradle',bottom)],o.component.description+' Roll center is 18 mm farther outward; yaw output and bearing axes remain unchanged.',silver)
    for n in ('T09_Hip_roll_motor_ENVELOPE_REFERENCE','H01_Hip_roll_117OD_106ID_case'):
        shift_all_bodies_world(go,ps[n],sg*18)
    c=ps['Q03_CNC_roll_to_pitch_fork'].component;b=TM.copy(fork)
    if sg<0:reflect(b)
    replace(c,[('Q03_v18_clean_full_flange_blended_fork',b)],
        'V18 complete 12 mm pitch output flange, 40 mm flat-ended arms, broad native lofted roots, and flat 50 mm roll openings. Roll package moved outward 18 mm to avoid thin cut fins. Gearbox/output/bearing details remain provisional.',silver)
    target=c.bRepBodies.item(0)
    try:
        pred=lambda e:e.faces.count==2 and any(adsk.core.NurbsSurface.cast(f.geometry) for f in e.faces) and any(adsk.core.Plane.cast(f.geometry) for f in e.faces) and e.length*10>4
        f=fillet_edges(c,target,1.5,pred,'V18_clean_junction_edge_fillets')
        report['fillets'].append({'leg':go.component.name,'success':bool(f)})
    except Exception as e:report['fillets'].append({'leg':go.component.name,'success':False,'error':str(e)})
    assert sum(not s.isVoid for s in c.bRepBodies.item(0).shells)==1
construction.isLightBulbOn=False
(OUT/'clean_junction_spacing.json').write_text(json.dumps(report,indent=2));result=report
