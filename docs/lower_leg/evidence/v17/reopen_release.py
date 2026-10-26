import adsk.core,adsk.fusion,json,math
OUT=ROOT/'v17';path=OUT/'deliverables'/'Legs_hip_waist_v17.f3d'
assert path.exists() and path.stat().st_size>1_000_000
# Only close this task's generated revision after its native archive exists.
# The user's original v16 document remains open and its archive is preserved.
working=next(x for x in app.documents if x.name=='Legs_hip_waist_v17')
working.close(False);adsk.doEvents()
reopened=app.importManager.importToNewDocument(app.importManager.createFusionArchiveImportOptions(str(path)));assert reopened
reopened.name='Legs_hip_waist_v17'
d=adsk.fusion.Design.cast(app.activeProduct);root=d.rootComponent
report={'archive':str(path),'parametric':d.designType==adsk.fusion.DesignTypes.ParametricDesignType,'groups':{},'waist_axes':[]}
for go in root.occurrences:
    if go.component.name not in ('Right_leg','Left_leg','Waist_roll_pitch_v17'):continue
    c=go.component
    report['groups'][c.name]={'parts':c.occurrences.count,'joints':c.asBuiltJoints.count,
        'invalid_joints':[j.name for j in c.asBuiltJoints if not j.isValid]}
    assert not report['groups'][c.name]['invalid_joints']
    if c.name=='Waist_roll_pitch_v17':
        assert c.asBuiltJoints.count==16 and c.occurrences.count==20
        spine=next(o for o in c.occurrences if o.component.partNumber.startswith('W08_')).createForAssemblyContext(go)
        bb=spine.bRepBodies.item(0).boundingBox
        measured=list(bb.minPoint.asArray())+list(bb.maxPoint.asArray())
        expected=[-.5,(23.343134+1)/10,98.2,.5,(23.343134+19)/10,109.1]
        report['spine_bounds_mm']=[x*10 for x in measured]
        report['spine_bound_error_mm']=max(abs(a-b)*10 for a,b in zip(measured,expected))
        assert report['spine_bound_error_mm']<.01,report['spine_bounds_mm']
        for name,axis in (('WJ00_waist_yaw',(0,0,1)),('WJ01_lower_waist_roll',(0,1,0)),('WJ02_upper_waist_pitch',(1,0,0))):
            j=c.asBuiltJoints.itemByName(name);got=j.createForAssemblyContext(go).jointMotion.rotationAxisVector.asArray()
            assert max(abs(abs(a)-b) for a,b in zip(got,axis))<1e-6
            report['waist_axes'].append({'joint':name,'axis':list(got)})
    else:assert c.asBuiltJoints.count==105
assert report['parametric'] and len(report['groups'])==3
(OUT/'archive_reopen_verification.json').write_text(json.dumps(report,indent=2));result=report
