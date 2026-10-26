exec(compile((ROOT/'v17/common.py').read_text(),'<v17 common>','exec'))
report={'static_interferences':[],'waist_poses':[],'geometry_issues':[],'feature_issues':[],
        'knee_symmetry':[],'joint_counts':{},'scope':'targeted structural pairs and sampled waist motion; excludes gearbox internals, removed prop-feature assumption, threads and chain clearance'}
def overlap(a,b):
    if not a.boundingBox.intersects(b.boundingBox):return 0
    cp=TM.copy(a)
    assert TM.booleanOperation(cp,TM.copy(b),BT.IntersectionBooleanType)
    return cp.volume*1000
def pair(a,b,label,out):
    for ba in a.bRepBodies:
        if not ba.isLightBulbOn:continue
        for bb in b.bRepBodies:
            if not bb.isLightBulbOn:continue
            vol=overlap(ba,bb)
            if vol>.025:out.append({'pair':label,'a':ba.name,'b':bb.name,'mm3':round(vol,4)})
wa={o.component.partNumber.split('_')[0]:o.createForAssemblyContext(wg) for o in wg.component.occurrences}
progress('check hip interfaces and casing outputs')
for go in (right,left):
    ps={o.component.partNumber:o.createForAssemblyContext(go) for o in go.component.occurrences}
    tests=[
      ('T04_GWK7010_Hip_yaw_REFERENCE','Q01_CNC_rail_to_yaw_crosshead'),
      ('Q01_CNC_rail_to_yaw_crosshead','Q02_CNC_yaw_to_roll_cradle'),
      ('Q01_CNC_rail_to_yaw_crosshead','H03_Hip_yaw_6007_bearing_REFERENCE'),
      ('Q02_CNC_yaw_to_roll_cradle','H03_Hip_yaw_6007_bearing_REFERENCE'),
      ('Q02_CNC_yaw_to_roll_cradle','H04_Hip_yaw_bearing_retainer'),
      ('Q02_CNC_yaw_to_roll_cradle','Q03_CNC_roll_to_pitch_fork'),
      ('Q02_CNC_yaw_to_roll_cradle','H01_Hip_roll_117OD_106ID_case'),
      ('Q03_CNC_roll_to_pitch_fork','H01_Hip_roll_117OD_106ID_case'),
      ('Q03_CNC_roll_to_pitch_fork','H02_Hip_pitch_roll_bearing_REFERENCES'),
      ('Q02_CNC_yaw_to_roll_cradle','H02_Hip_pitch_roll_bearing_REFERENCES'),
      ('T09_Hip_roll_motor_ENVELOPE_REFERENCE','Q02_CNC_yaw_to_roll_cradle'),
      ('T09_Hip_roll_motor_ENVELOPE_REFERENCE','Q03_CNC_roll_to_pitch_fork'),
      ('T09_Hip_roll_motor_ENVELOPE_REFERENCE','H01_Hip_roll_117OD_106ID_case'),
      ('T09_Hip_roll_motor_ENVELOPE_REFERENCE','H02_Hip_pitch_roll_bearing_REFERENCES'),
      ('T07_Hip_pitch_motor_ENVELOPE_REFERENCE','Q03_CNC_roll_to_pitch_fork'),
      ('T07_Hip_pitch_motor_ENVELOPE_REFERENCE','H02_Hip_pitch_roll_bearing_REFERENCES'),
      ('N04_Knee_pillow_block_L','P01_Knee_side_rail_seat_L'),
      ('N04_Knee_pillow_block_R','P01_Knee_side_rail_seat_R')]
    for a,b in tests:pair(ps[a],ps[b],go.component.name+'/'+a+'/'+b,report['static_interferences'])
    for shell in ('W02','W03'):
        for n in ('T07_Hip_pitch_motor_ENVELOPE_REFERENCE','T09_Hip_roll_motor_ENVELOPE_REFERENCE',
                  'Q02_CNC_yaw_to_roll_cradle','Q03_CNC_roll_to_pitch_fork','H02_Hip_pitch_roll_bearing_REFERENCES'):
            pair(wa[shell],ps[n],shell+'/'+go.component.name+'/'+n,report['static_interferences'])
    for base in ('N04_Knee_pillow_block_','P01_Knee_side_rail_seat_','P02_Knee_rail_screws_and_sleeves_'):
        vols=[sum(b.volume for b in ps[base+side].bRepBodies)*1000 for side in ('L','R')]
        report['knee_symmetry'].append({'leg':go.component.name,'part':base,'volume_difference_mm3':abs(vols[0]-vols[1])})
    report['joint_counts'][go.component.name]=go.component.asBuiltJoints.count

progress('sample waist yaw roll pitch motion')
names=('WJ00_waist_yaw','WJ01_lower_waist_roll','WJ02_upper_waist_pitch')
js=[wg.component.asBuiltJoints.itemByName(n) for n in names]
assert all(js)
pairs=[('W01','W04'),('W01','W05'),('W02','W03'),('W02','W04'),('W03','W04'),
       ('W04','W05'),('W05','W06'),('W06','W07'),('W07','W08'),
       ('W06','W09'),('W09','W10'),('W07','W11'),('W11','W12'),
       ('W19','W20'),('W19','W08'),('W20','W08'),('W19','W02'),('W20','W03')]
try:
    for yaw,roll,pitch in ((0,0,0),(25,0,0),(-25,0,0),(0,25,0),(0,-25,0),(0,0,25),(0,0,-25),(15,15,15),(0,15,-15)):
        for j,a in zip(js,(yaw,roll,pitch)):j.jointMotion.rotationValue=math.radians(a)
        adsk.doEvents();hits=[]
        for a,b in pairs:pair(wa[a],wa[b],a+'/'+b,hits)
        report['waist_poses'].append({'yaw':yaw,'roll':roll,'pitch':pitch,'interferences':hits})
finally:
    for j in js:j.jointMotion.rotationValue=0
    adsk.doEvents()

progress('audit edited solids and feature health')
for go in (right,left,wg):
    for o in go.component.occurrences:
        c=o.component;part=c.partNumber
        if go!=wg and not (part.startswith(('Q01','Q02','Q03','T04','T07','T09','N04','P01','P02','N10')) or '_Hip_' in part):continue
        for b in c.bRepBodies:
            shells=sum(not s.isVoid for s in b.shells)
            if not b.isSolid or b.volume<=0 or shells!=1:
                report['geometry_issues'].append({'part':c.name,'body':b.name,'solid':b.isSolid,'volume_mm3':b.volume*1000,'outer_shells':shells})
        for f in c.features:
            if f.healthState!=adsk.fusion.FeatureHealthStates.HealthyFeatureHealthState:
                report['feature_issues'].append({'part':c.name,'feature':f.name,'message':f.errorOrWarningMessage})
report['joint_counts']['Waist']=wg.component.asBuiltJoints.count
report['invalid_joints']=[go.component.name+'/'+j.name for go in (right,left,wg) for j in go.component.asBuiltJoints if not j.isValid]
(OUT/'validation.json').write_text(json.dumps(report,indent=2))
result={'static_hits':len(report['static_interferences']),'waist_pose_hits':sum(bool(r['interferences']) for r in report['waist_poses']),
        'geometry_issues':len(report['geometry_issues']),'feature_issues':len(report['feature_issues']),
        'joint_counts':report['joint_counts'],'invalid_joints':report['invalid_joints']}
