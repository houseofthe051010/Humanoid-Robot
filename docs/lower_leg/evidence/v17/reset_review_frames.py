exec(compile((ROOT/'v17/common.py').read_text(),'<v17 common>','exec'))
wc=wg.component;progress('reset inherited waist occurrence frames before rebuilding joints')
for j in reversed(list(wc.asBuiltJoints)):j.deleteMe()
identity=adsk.core.Matrix3D.create()
for o in wc.occurrences:
    o.isGroundToParent=False;o.createForAssemblyContext(wg).transform2=identity.copy();o.isLightBulbOn=True
    if hasattr(o.component,'isBodiesFolderLightBulbOn'):o.component.isBodiesFolderLightBulbOn=True
    for b in o.component.bRepBodies:b.isLightBulbOn=True
if d.snapshots.hasPendingSnapshot:d.snapshots.add()
adsk.doEvents()
ps={o.component.partNumber:o for o in wc.occurrences}
src=(OUT/'import_6010_and_joints.py').read_text()
exec(compile(src[src.index('def prefix'):src.index('# Remove failed')],'<rebuild corrected joints>','exec'))
adsk.doEvents()
hidden=[]
for b in root.bRepBodies:
    bb=b.boundingBox
    if bb.minPoint.z*10>650 and bb.maxPoint.z*10<800:
        b.isLightBulbOn=False;b.name='ZZ_User_rough_hip_output_sketch_replaced_v17';hidden.append(b.name)
wa=[]
for o in wc.occurrences:
    p=o.createForAssemblyContext(wg)
    wa.append({'part':o.component.partNumber,'transform':list(p.transform2.asArray()),'visible':o.isLightBulbOn,
        'body_visibility':[{'name':b.name,'light':b.isLightBulbOn,'effective':getattr(b,'isVisible',None)} for b in p.bRepBodies]})
hips=[]
for go in (right,left):
    for o in go.component.occurrences:
        if o.component.partNumber.startswith(('Q01','Q02','Q03','T04','T07','T09')) or '_Hip_' in o.component.partNumber:
            p=o.createForAssemblyContext(go)
            hips.append({'leg':go.component.name,'part':o.component.partNumber,'transform':list(p.transform2.asArray())})
report={'waist':wa,'hips':hips,'hidden_replaced_user_reference_bodies':hidden}
(OUT/'frame_audit.json').write_text(json.dumps(report,indent=2));result={'waist_parts':len(wa),'hip_parts':len(hips),'hidden_rough_bodies':hidden}
