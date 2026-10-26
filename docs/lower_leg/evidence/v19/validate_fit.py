exec(compile((ROOT/'v19/common.py').read_text(),'<v19 common>','exec'))
report={'hits':[],'geometry_issues':[],'feature_issues':[],'joint_counts':{},'centers':[],
        'scope':'targeted standing-pose fit of tube, endcaps, paired output journals, housing forks, motors, waist and yaw bearings; gearbox internals and continuous hip motion not represented'}
def overlap(a,b):
    if not a.boundingBox.intersects(b.boundingBox):return 0
    shape=TM.copy(a)
    assert TM.booleanOperation(shape,TM.copy(b),BT.IntersectionBooleanType)
    return shape.volume*1000
def pair(a,b,label):
    for aa in a.bRepBodies:
        if not aa.isLightBulbOn:continue
        for bb in b.bRepBodies:
            if not bb.isLightBulbOn:continue
            vv=overlap(aa,bb)
            if vv>.03:report['hits'].append({'pair':label,'a':aa.name,'b':bb.name,'mm3':round(vv,4)})
wa={o.component.partNumber.split('_')[0]:o.createForAssemblyContext(wg) for o in wg.component.occurrences}
structural=['Q02_CNC_yaw_to_roll_cradle','Q03_CNC_roll_to_pitch_fork','H01_Hip_roll_117OD_106ID_case','H02_Hip_pitch_roll_bearing_REFERENCES',
            'H05_DJI10018_pitch_gearbox_shell_ESTIMATE','H06_Roll_tube_recessed_endcaps','H07_Pitch_tube_recessed_endcaps','H08_Roll_61810_bearing_references']
for go in (right,left):
    progress('fit '+go.component.name)
    ps={n:o.createForAssemblyContext(go) for n,o in parts(go).items()}
    for i,a in enumerate(structural):
        for b in structural[i+1:]:pair(ps[a],ps[b],go.component.name+'/'+a+'/'+b)
        for b in ('T07_Hip_pitch_motor_ENVELOPE_REFERENCE','T09_Hip_roll_motor_ENVELOPE_REFERENCE'):
            pair(ps[a],ps[b],go.component.name+'/'+a+'/'+b)
        for shell in ('W02','W03'):pair(wa[shell],ps[a],shell+'/'+go.component.name+'/'+a)
    for b in ('Q01_CNC_rail_to_yaw_crosshead','H03_Hip_yaw_6007_bearing_REFERENCE','H04_Hip_yaw_bearing_retainer','T04_GWK7010_Hip_yaw_REFERENCE'):
        pair(ps['Q02_CNC_yaw_to_roll_cradle'],ps[b],go.component.name+'/Q02/'+b)
    for b in ('T07_Hip_pitch_motor_ENVELOPE_REFERENCE','T09_Hip_roll_motor_ENVELOPE_REFERENCE'):
        for shell in ('W01','W02','W03'):pair(wa[shell],ps[b],shell+'/'+go.component.name+'/'+b)
    for key in structural:
        c=parts(go)[key].component
        for b in c.bRepBodies:
            count=sum(not s.isVoid for s in b.shells)
            if not b.isSolid or b.volume<=0 or count!=1:report['geometry_issues'].append({'part':go.component.name+'/'+key,'body':b.name,'shells':count,'volume_mm3':b.volume*1000})
        for f in c.features:
            if f.healthState!=adsk.fusion.FeatureHealthStates.HealthyFeatureHealthState:
                report['feature_issues'].append({'part':go.component.name+'/'+key,'feature':f.name,'message':f.errorOrWarningMessage})
    report['joint_counts'][go.component.name]=go.component.asBuiltJoints.count
for key in ('W02','W03'):
    for b in wa[key].bRepBodies:
        count=sum(not s.isVoid for s in b.shells)
        if not b.isSolid or b.volume<=0 or count!=1:report['geometry_issues'].append({'part':key,'shells':count,'volume_mm3':b.volume*1000})
for a,b in (('W02','W03'),('W02','W01'),('W03','W01'),('W02','W04'),('W03','W04')):pair(wa[a],wa[b],a+'/'+b)
report['invalid_joints']=[go.component.name+'/'+j.name for go in (right,left,wg) for j in go.component.asBuiltJoints if not j.isValid]
(OUT/'fit_validation.json').write_text(json.dumps(report,indent=2))
result={'hits':len(report['hits']),'geometry_issues':report['geometry_issues'],'feature_issues':report['feature_issues'],'joint_counts':report['joint_counts'],'invalid_joints':report['invalid_joints']}
