exec(compile((ROOT/'v17/common.py').read_text(),'<v17 common>','exec'))
assert not any(o.component.partNumber=='H01_Hip_roll_117OD_106ID_case' for o in right.component.occurrences)
cc=next(o.component for o in root.occurrences if o.component.name=='ZZ_V17_motor_interface_construction')
template=cc.bRepBodies.itemByName('Exact_star_mount_template_896p8_902p8')
assert template
u=(math.cos(math.radians(25)),0,-math.sin(math.radians(25)))
v=(0,1,0);w=(math.sin(math.radians(25)),0,math.cos(math.radians(25)))
P=(-68,Y,798.6);R=(10,Y,759.6)
def along(c,u,t,aa=0,bb=0,vv=v,ww=w):return tuple(c[i]+t*u[i]+aa*vv[i]+bb*ww[i] for i in range(3))
def axial(c,u,a,b,r):return cy(along(c,u,a),along(c,u,b),r)
def place(b,sg):
    tx(b,dx=130)
    return b if sg==1 else reflect(b)
def hpart(group,ps,n,bodies,desc,mat='6061 CNC prototype',ap=silver,anchor='Q02_CNC_yaw_to_roll_cradle'):
    o=newpart(group.component,n,desc,mat)
    for label,b in bodies:add(o.component,b,label,ap)
    rigid(group.component,ps[anchor],o,n+'_layout_reference');return o
def outer_case(c,axis):return axial(c,axis,-26,20,58.5)
def case_tube(c,axis):return sub(outer_case(c,axis),axial(c,axis,-27,21,53))
def endplates(c,axis,vv,ww):
    rear=axial(c,axis,-34,-26,58.5);front=axial(c,axis,20,28,58.5)
    sub(rear,axial(c,axis,-35,-25,17));sub(rear,axial(c,axis,-34.1,-27,26))
    sub(front,axial(c,axis,19,29,20.2));sub(front,axial(c,axis,21,28.1,26))
    for a in (-20,20):
        for b in (-33,33):
            sub(rear,cy(along(c,axis,-35,a,b,vv,ww),along(c,axis,-25,a,b,vv,ww),2.2))
    for k in range(6):
        angle=math.radians(30+60*k);a,b=55.5*math.cos(angle),55.5*math.sin(angle)
        for plate,lo,hi in ((rear,-35,-25),(front,19,29)):
            sub(plate,cy(along(c,axis,lo,a,b,vv,ww),along(c,axis,hi,a,b,vv,ww),1.7))
    return rear,front
def bearing(c,axis,a,b,ri,ro):return sub(axial(c,axis,a,b,ro),axial(c,axis,a-.1,b+.1,ri))
def source_motor(c,axis,vv,ww):
    # Original knee reference coordinates, transformed by a proper rigid rotation.
    m=basis(c,tuple(-x for x in axis),tuple(-x for x in vv),ww)
    return [(b.name,transform(tx(TM.copy(b),dx=-141,dy=-Y,dz=-560),m),b.appearance)
            for b in rp['R01_DJI_10018_77KV_ESTIMATED_REFERENCE'].component.bRepBodies]

progress('prepare lowered hip yaw and separate 6007 bearing support')
cross=tx(ix(TM.copy(template),cy((0,Y,896),(0,Y,904),38)),dz=-239.2)
mount_holes=[(24*math.cos(math.radians(22.5+45*k)),Y+24*math.sin(math.radians(22.5+45*k))) for k in range(8)]
for x,y in mount_holes:sub(cross,cy((x,y,657),(x,y,665),1.7))
for x in (-51,51):
    un(cross,rrxy(x-12,x+12,Y-18,Y+18,647,688,4))
    un(cross,rrxy(min(x,0)-3,max(x,0)+3,Y-11,Y+11,680.5,688,4))
    sub(cross,oval(x,Y,646,689,5.1,4))
    for z in (659,677):sub(cross,cy((x-13,Y,z),(x+13,Y,z),2.15))
for angle in (45,135,225,315):
    x,y=33*math.cos(math.radians(angle)),Y+33*math.sin(math.radians(angle))
    un(cross,cy((x,y,662),(x,y,678),5))
seat=cy((0,Y,672.5),(0,Y,688.5),38)
sub(seat,cy((0,Y,671),(0,Y,690),23));sub(seat,cy((0,Y,674.5),(0,Y,690),31))
un(cross,seat)
sub(cross,cy((0,Y,674.5),(0,Y,690),31))
retainer=bearing((0,Y,0),(0,0,1),688.5,691.5,23,38)
for angle in (45,135,225,315):
    x,y=34.5*math.cos(math.radians(angle)),Y+34.5*math.sin(math.radians(angle))
    sub(cross,cy((x,y,678),(x,y,692),1.7));sub(retainer,cy((x,y,688),(x,y,692),1.7))
yaw_bearing=bearing((0,Y,0),(0,0,1),674.5,688.5,17.5,31)

progress('prepare full-center roll supports and curved yaw cradle')
rear,front=endplates(R,(0,1,0),(1,0,0),(0,0,1))
cradle=un(cy((0,Y,662.3),(0,Y,673),18),cy((0,Y,672),(0,Y,689.5),17.45),cy((0,Y,689),(0,Y,697),22),rrxy(-53,73,Y-43,Y+38,693.5,700.5,8))
for plate in (rear,front):un(cradle,plate)
for lo,hi in ((Y-34,Y-26),(Y+20,Y+28)):
    un(cradle,bx((-25,lo,697),(45,hi,718)))
# Broad concave R8 transitions between the floor and both end supports.
for lo,hi,center_y in ((Y-26,Y-18,Y-18),(Y+12,Y+20,Y+12)):
    fillet=sub(bx((-25,lo,700.4),(45,hi,708.5)),cy((-26,center_y,708.5),(46,center_y,708.5),8))
    un(cradle,fillet)
sub(cradle,axial(R,(0,1,0),-26,20,53))
sub(cradle,cy((0,Y,661),(0,Y,673),7.3))
out_holes=[(12.5*math.cos(math.radians(30+60*k)),Y+12.5*math.sin(math.radians(30+60*k))) for k in range(6)]
for x,y in out_holes:
    sub(cradle,cy((x,y,661),(x,y,701),1.7))
    sub(cradle,cy((x,y,668),(x,y,701),2.8))

progress('prepare paired roll arms and pitch output coupling')
pc=along(P,u,34)
fork=axial(P,u,30,38,42)
un(fork,axial(P,u,20,31,19.95))
sub(fork,axial(P,u,19,39,8))
for yy0,yy1,jn0,jn1 in ((Y-44,Y-36,Y-36,Y-27),(Y+30,Y+38,Y+20,Y+31)):
    un(fork,beam_y((R[0],R[2]),(pc[0],pc[2]),14,yy0,yy1),cy((R[0],yy0,R[2]),(R[0],yy1,R[2]),25))
    journal=cy((R[0],jn0,R[2]),(R[0],jn1,R[2]),19.95)
    sub(journal,cy((R[0],jn0-.1,R[2]),(R[0],jn1+.1,R[2]),16.5 if yy0<Y else 8))
    un(fork,journal)
    sub(fork,cy((R[0],yy0-1,R[2]),(R[0],yy1+1,R[2]),16.5 if yy0<Y else 8))
for k in range(4):
    az=math.radians(45+90*k);a,b=15*math.cos(az),15*math.sin(az)
    sub(fork,cy(along(P,u,19,a,b),along(P,u,39,a,b),2.2))
    x,z=R[0]+15*math.cos(az),R[2]+15*math.sin(az)
    sub(fork,cy((x,Y+19,z),(x,Y+39,z),2.2))
# Keep the motor cavity intact where the tilted flange approaches its neighbor.
sub(fork,axial(R,(0,1,0),-26,20,53))
sub(fork,un(case_tube(R,(0,1,0)),TM.copy(rear),TM.copy(front)))
rolltube=case_tube(R,(0,1,0))
pr,pf=endplates(P,u,v,w);pitchcase=un(case_tube(P,u),pr,pf)

report={'yaw_lowering_mm':15,'yaw_bearing_mm':[35,62,14],
        'roll_center_right_mm':[140,Y,759.6],'pitch_center_right_mm':[62,Y,798.6],
        'hip_case_OD_ID_mm':[117,106],'pitch_tilt_deg':25,'motor':'copied knee DJI10018 reference',
        'pitch_roll_bearing_reservations_mm':[40,52,7],'parts':[],'fillets':[]}
for go,sg in ((right,1),(left,-1)):
    ps=parts(go);progress('commit corrected hips '+go.component.name)
    mc=ps['T04_GWK7010_Hip_yaw_REFERENCE'].component
    copies=[(b.name,tx(TM.copy(b),dz=-15)) for b in mc.bRepBodies]
    replace(mc,copies,'V17 vendor 7010 hip yaw lowered 15 mm for separate 6007 structural-bearing reference above output.',black)
    for key,shape,description in (
        ('Q01_CNC_rail_to_yaw_crosshead',cross,'V17 CNC crosshead: exact scalloped 7010 mount / correct 48-PCD holes, full rail sleeves and 6007 outer-race seat. Separate removable top retainer.'),
        ('Q02_CNC_yaw_to_roll_cradle',cradle,'V17 six-hole 25-PCD yaw output coupler, 35 mm bearing journal and curved R8 floor transitions into full annular roll endplates; DJI 40x66 estimated rear pattern and central output/bearing openings.'),
        ('Q03_CNC_roll_to_pitch_fork',fork,'V17 equal full-center roll cheeks with front/rear 40 mm journals and tilted pitch output flange. Both roll support arms reach the axis. Gearbox output interfaces are provisional custom designs.')):
        c=ps[key].component;replace(c,[(key+'_v17',place(TM.copy(shape),sg))],description,silver)
    for key,c0,ax,vv,ww in (
        ('T09_Hip_roll_motor_ENVELOPE_REFERENCE',R,(0,1,0),(1,0,0),(0,0,-1)),
        ('T07_Hip_pitch_motor_ENVELOPE_REFERENCE',P,u,v,w)):
        copies=source_motor(c0,ax,vv,ww);c=ps[key].component
        replace(c,[(name,place(b,sg)) for name,b,ap in copies],
                'V17 duplicate of 105 mm DJI10018 knee reference. Prop posts/pads and wire visuals retained hidden; packaging assumes removable prop features and an unmodeled compact gearbox. Rear four-hole pattern remains estimated 40x66 mm.',black)
        for b,(_,__,ap) in zip(c.bRepBodies,copies):
            b.appearance=ap
            if b.name.startswith(('Prop_','Phase_wire')):b.isLightBulbOn=False
        c.name=('Right_' if sg==1 else 'Left_')+('DJI10018_Hip_roll_REFERENCE' if key.startswith('T09') else 'DJI10018_Hip_pitch_REFERENCE')
    hpart(go,ps,'H01_Hip_roll_117OD_106ID_case', [('H01_roll_tube',place(TM.copy(rolltube),sg))],
          '117 OD /106 ID sleeve around the copied 105 mm DJI10018 reference. Endplates belong to Q02; gearbox internals remain omitted.','PA12-CF prototype',plastic)
    br=[]
    for label,c0,axis in (('roll',R,(0,1,0)),('pitch',P,u)):
        for a,b in ((-34,-27),(21,28)):
            br.append((label+'_40x52x7_reference',place(bearing(c0,axis,a,b,20,26),sg)))
    hpart(go,ps,'H02_Hip_pitch_roll_bearing_REFERENCES',br,
          'Four 61808 / 6808 sized 40x52x7 bearing packaging references. Roll journals connect the two fork cheeks; opposite pitch journal/linkage remains to detail. No load rating selected.')
    hpart(go,ps,'H03_Hip_yaw_6007_bearing_REFERENCE',[('6007_35x62x14_reference',place(TM.copy(yaw_bearing),sg))],
          'Common 6007 35x62x14 ball-bearing envelope supports yaw output journal above lowered motor. Prototype geometry only.',anchor='Q01_CNC_rail_to_yaw_crosshead')
    hpart(go,ps,'H04_Hip_yaw_bearing_retainer',[('Removable_outer_race_retainer',place(TM.copy(retainer),sg))],
          'Separate top retainer permits axial installation of the 6007. Four M3 provisions outside the outer race.',anchor='Q01_CNC_rail_to_yaw_crosshead')
    add(cc,place(TM.copy(pitchcase),sg),go.component.name+'_pitch_case_seed',plastic)
    report['parts'].append(go.component.name)
    for key in ('Q02_CNC_yaw_to_roll_cradle','Q03_CNC_roll_to_pitch_fork'):
        c=ps[key].component;b=c.bRepBodies.item(0)
        try:
            # Broad curved profiles already define the main load paths; these
            # editable small edge rounds remove remaining sharp planar corners.
            f=fillet_edges(c,b,1.2,lambda e:isinstance(e.geometry,adsk.core.Line3D) and e.length*10>5,'V17_CNC_edge_blends')
            report['fillets'].append({'part':go.component.name+'/'+key,'success':bool(f)})
        except Exception as e:report['fillets'].append({'part':go.component.name+'/'+key,'success':False,'error':str(e)})

(OUT/'hip_build.json').write_text(json.dumps(report,indent=2));progress('hips committed; waist skin pending');result=report
