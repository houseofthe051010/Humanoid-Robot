import adsk.core,adsk.fusion,json
OUT=ROOT/'v19';path=OUT/'deliverables'/'Legs_hip_waist_v19.f3d'
assert path.exists() and path.stat().st_size>1_000_000
working=next(x for x in app.documents if x.name=='Legs_hip_waist_v19')
working.close(False);adsk.doEvents()
doc=app.importManager.importToNewDocument(app.importManager.createFusionArchiveImportOptions(str(path)));assert doc
doc.name='Legs_hip_waist_v19'
d=adsk.fusion.Design.cast(app.activeProduct);root=d.rootComponent
report={'archive':str(path),'parametric':d.designType==adsk.fusion.DesignTypes.ParametricDesignType,'groups':{},'tube_dimensions':[],'hip_alignment':[]}
for go in root.occurrences:
    if go.component.name not in ('Right_leg','Left_leg','Waist_roll_pitch_v19'):continue
    c=go.component;ps={o.component.partNumber:o.createForAssemblyContext(go) for o in c.occurrences}
    report['groups'][c.name]={'parts':c.occurrences.count,'joints':c.asBuiltJoints.count,'invalid_joints':[j.name for j in c.asBuiltJoints if not j.isValid]}
    assert not report['groups'][c.name]['invalid_joints']
    if go.component.name=='Waist_roll_pitch_v19':
        spine=next(o for n,o in ps.items() if n.startswith('W08_'))
        bb=spine.bRepBodies.item(0).boundingBox;got=list(bb.minPoint.asArray())+list(bb.maxPoint.asArray())
        exp=[-.5,2.4343134,98.2,.5,4.2343134,109.1]
        report['spine_bound_error_mm']=max(abs(a-b)*10 for a,b in zip(got,exp));assert report['spine_bound_error_mm']<.01
        report['inward_6010_outputs']=[]
        for n,sg in (('W23',-1),('W24',1)):
            o=next(o for k,o in ps.items() if k.startswith(n+'_'))
            face=next(f for b in o.bRepBodies for f in b.faces if adsk.core.Plane.cast(f.geometry) and abs(f.area*100-550.69756)<.1)
            plane=adsk.core.Plane.cast(face.geometry);assert sg*plane.normal.x<-.99
            assert abs(abs(plane.origin.x*10)-45)<.05
            report['inward_6010_outputs'].append({'part':n,'normal':list(plane.normal.asArray()),'output_x_mm':plane.origin.x*10})
        report['waist_joint_limits_deg']={}
        import math
        for name,limit in (('WJ01_lower_waist_roll',5),('WJ02_upper_waist_pitch',20)):
            lim=c.asBuiltJoints.itemByName(name).jointMotion.rotationLimits
            vals=[math.degrees(lim.minimumValue),math.degrees(lim.maximumValue)]
            assert abs(vals[0]+limit)<1e-5 and abs(vals[1]-limit)<1e-5
            report['waist_joint_limits_deg'][name]=vals
    else:
        tubes=[o for n,o in ps.items() if n.startswith(('H01_Hip_roll_','H05_DJI10018_pitch_'))]
        assert len(tubes)==2
        for o in tubes:
            radii=sorted(set(round(adsk.core.Cylinder.cast(f.geometry).radius*10,4) for b in o.bRepBodies for f in b.faces if adsk.core.Cylinder.cast(f.geometry)))
            assert radii==[53,55],radii
            report['tube_dimensions'].append({'group':c.name,'part':o.component.partNumber,'ID_mm':106,'OD_mm':110,'wall_mm':2})
        roll=next(o for n,o in ps.items() if n.startswith('H01_Hip_roll_'))
        rollface=next(adsk.core.Cylinder.cast(f.geometry) for b in roll.bRepBodies for f in b.faces if adsk.core.Cylinder.cast(f.geometry) and abs(adsk.core.Cylinder.cast(f.geometry).radius-5.5)<1e-5)
        yaw=ps['T04_GWK7010_Hip_yaw_REFERENCE']
        yawface=next(adsk.core.Cylinder.cast(f.geometry) for b in yaw.bRepBodies for f in b.faces if adsk.core.Cylinder.cast(f.geometry) and abs(adsk.core.Cylinder.cast(f.geometry).radius-3.9)<1e-4)
        err=abs(rollface.origin.x-yawface.origin.x)*10
        assert err<.01,err
        report['hip_alignment'].append({'group':c.name,'roll_axis_x_mm':rollface.origin.x*10,'yaw_axis_x_mm':yawface.origin.x*10,'x_error_mm':err})
assert report['parametric'] and len(report['groups'])==3
report['leg_axis_spacing_mm']=abs(report['hip_alignment'][0]['yaw_axis_x_mm']-report['hip_alignment'][1]['yaw_axis_x_mm'])
assert abs(report['leg_axis_spacing_mm']-240)<.01
(OUT/'archive_reopen_verification.json').write_text(json.dumps(report,indent=2));result=report
