exec(compile((ROOT/'v19/common.py').read_text(),'<v19 common>','exec'))
report=[]
for go in (right,left):
    rr={'group':go.component.name,'transform':list(go.transform2.asArray()),'parts':[]}
    for key in ('Q01_CNC_rail_to_yaw_crosshead','Q02_CNC_yaw_to_roll_cradle','Q03_CNC_roll_to_pitch_fork','H01_Hip_roll_117OD_106ID_case',
                'H05_DJI10018_pitch_gearbox_shell_ESTIMATE','H07_Pitch_tube_recessed_endcaps'):
        o=parts(go)[key];p=o.createForAssemblyContext(go)
        rr['parts'].append({'key':key,'native_transform':list(o.transform2.asArray()),'world_transform':list(p.transform2.asArray()),'bodies':[
            {'name':b.name,'bounds':[[10*v for v in q.asArray()] for q in (b.boundingBox.minPoint,b.boundingBox.maxPoint)]} for b in p.bRepBodies]})
    report.append(rr)
(OUT/'frame_measurements.json').write_text(json.dumps(report,indent=2));result=report
