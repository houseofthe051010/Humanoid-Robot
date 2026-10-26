exec(compile((ROOT/'v19/common.py').read_text(),'<v19 common>','exec'))
cc=next(o.component for o in root.occurrences if o.component.name=='ZZ_V19_construction')
assert not root.attributes.itemByName('V19','layout_committed')
sourceknee=rp['R01_DJI_10018_77KV_ESTIMATED_REFERENCE']
report={'groups':[],'parts':[]}
for go,sg in ((right,1),(left,-1)):
    ps=parts(go);frame=ps['Q02_CNC_yaw_to_roll_cradle'].createForAssemblyContext(go).transform2.copy()
    def place(b):
        if sg<0:reflect(b)
        return transform(b,frame)
    # Move each complete existing leg, preserving its native internal joints.
    go.isGrounded=False
    mat=go.transform2.copy();mat.translation=V3.create(-sg,0,0);go.transform2=mat
    if d.snapshots.hasPendingSnapshot:d.snapshots.add()
    go.isGrounded=True
    def install(key,templates,description,ap=silver,material='6061 aluminum prototype'):
        o=ps.get(key)
        if o is None:
            o=newpart(go.component,key,description,material);ps[key]=o
            rigid(go.component,ps['Q03_CNC_roll_to_pitch_fork'],o,key+'_standing_layout')
        rows=[(n,place(TM.copy(cc.bRepBodies.itemByName(n)))) for n in templates]
        world_replace(go,o,rows,description,ap);o.component.attributes.add('SHIN','material',material)
        o.isLightBulbOn=True;o.createForAssemblyContext(go).isLightBulbOn=True
        o.component.isBodiesFolderLightBulbOn=True
        report['parts'].append({'group':go.component.name,'part':key,'bodies':len(rows)})
        return o
    install('Q02_CNC_yaw_to_roll_cradle',['Q02_centered_dual_output_yoke'],
            'V19 centered yaw-output adapter with sculpted bell and two curved, hollow roll-output cheeks. Nominal 50 mm roll journals, paired output flange provisions, 35 mm yaw-bearing journal and actual six-hole 7010 output pattern. Dual-ended roll gearbox internals remain to design.')
    install('Q03_CNC_roll_to_pitch_fork',['Q03_curved_pitch_to_tube_fork'],
            'V19 compact pitch output coupling with paired lofted side webs attaching to stationary recessed roll-tube endcaps. The center roll output is mechanically separate from these housing supports. Prototype output bolt pattern.')
    install('H01_Hip_roll_117OD_106ID_case',['H01_roll_110OD_106ID_tube'],
            'V19 aluminum roll actuator tube: 110 mm OD, 106 mm ID, 46 mm axial length. Existing DJI10018 reference retained inside; gearbox internals not designed.')
    ps['H01_Hip_roll_117OD_106ID_case'].component.name=go.component.name+'_H01_roll_aluminum_tube_110OD_106ID'
    install('H05_DJI10018_pitch_gearbox_shell_ESTIMATE',['H05_pitch_110OD_106ID_tube'],
            'V19 aluminum pitch actuator tube: 110 mm OD, 106 mm ID, 46 mm axial length. Separate curved rear and front endcaps; estimated gearbox reservation retained.')
    install('H06_Roll_tube_recessed_endcaps',['H06_roll_endcap_-1','H06_roll_endcap_1'],
            'Separate aluminum endcaps with 3 mm annular tube registers, 65 mm bearing seats, 50.4 mm through apertures and three housing-fork bolts per side. Four external M3 tie-bolt bosses avoid the 2 mm tube wall.')
    install('H07_Pitch_tube_recessed_endcaps',['H07_pitch_conical_rear_endcap','H07_pitch_front_endcap'],
            'Separate aluminum pitch caps. Compact conical back follows the small rear hub, replacing the wasteful broad rear shoulder. Motor 40x66 pattern remains inherited estimate.')
    for key,c0,axis,vv,ww in (('T07_Hip_pitch_motor_ENVELOPE_REFERENCE',(PX,Y,PZ),u,(0,1,0),w),
                            ('T09_Hip_roll_motor_ENVELOPE_REFERENCE',(RX,Y,RZ),(0,1,0),(1,0,0),(0,0,-1))):
        m=basis(c0,tuple(-x for x in axis),tuple(-x for x in vv),ww)
        rows=[];apps=[]
        for b in sourceknee.component.bRepBodies:
            shape=transform(tx(TM.copy(b),dx=-141,dy=-Y,dz=-560),m);rows.append((b.name,place(shape)));apps.append(b.appearance)
        world_replace(go,ps[key],rows,'Estimated 105 mm DJI10018 reference retained inside V19 aluminum tube. Prop fittings and phase wire visuals retained hidden; gearbox not modeled.',black)
        for b,ap in zip(ps[key].component.bRepBodies,apps):
            b.appearance=ap
            if b.name.startswith(('Prop_','Phase_wire')):b.isLightBulbOn=False
    # Rebuild the bearing references at the new centers rather than moving the
    # inherited right-leg frame twice.
    rows=[]
    for a,b in ((-34,-27),(21,28)):rows.append(('Pitch_40x52x7_'+str(a),place(sub(pcyl(a,b,26),pcyl(a-.01,b+.01,20)))))
    world_replace(go,ps['H02_Hip_pitch_roll_bearing_REFERENCES'],rows,'Two retained pitch 40x52x7 bearing envelope references.',silver)
    rb=newpart(go.component,'H08_Roll_61810_bearing_references','Paired 61810 dimension references 50x65x7. Nominal fits only; no load or life rating assigned.','bearing steel reference')
    for a,b in ((-36,-29),(23,30)):
        shape=place(sub(rcyl(a,b,32.5),rcyl(a-.01,b+.01,25)))
        inv=rb.createForAssemblyContext(go).transform2.copy();inv.invert();add(rb.component,transform(shape,inv),'Roll_50x65x7_'+str(a),silver)
    rigid(go.component,ps['Q03_CNC_roll_to_pitch_fork'],rb,'H08_roll_bearing_layout')
    report['groups'].append({'name':go.component.name,'translation_x_mm':-sg*10,'joints':go.component.asBuiltJoints.count})
for key,name in (('W02_Waist_front_shell','W02_compact_waist_front'),('W03_Waist_rear_shell','W03_compact_waist_rear')):
    world_replace(wg,wp[key],[(name,TM.copy(cc.bRepBodies.itemByName(name)))],
        'V19 compact curved PA12-CF waist skin with contoured pitch-tube saddles, open outputs and hollow central electronics cavity. Front/rear halves preserve 0.4 mm seam.',plastic)
wg.component.name='Waist_roll_pitch_v19'
root.attributes.add('V19','layout_committed','true')
for o in root.occurrences:
    if o.component.name.startswith('ZZ_'):o.isLightBulbOn=False
(OUT/'layout_commit.json').write_text(json.dumps(report,indent=2));result=report
