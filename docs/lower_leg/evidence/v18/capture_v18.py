exec(compile((ROOT/'v18/common.py').read_text(),'<v17 common>','exec'))
dest=OUT/'deliverables';dest.mkdir(exist_ok=True)
vp=app.activeViewport;app.userInterface.activeSelections.clear()
for c in [root]+list(d.allComponents):
    for coll in (c.sketches,c.constructionAxes,c.constructionPlanes,c.constructionPoints,c.asBuiltJoints):
        for x in coll:x.isLightBulbOn=False
def view(eye,target,extent,name):
    cam=vp.camera;cam.isSmoothTransition=False;cam.cameraType=adsk.core.CameraTypes.OrthographicCameraType
    cam.eye=pt(eye);cam.target=pt(target);cam.upVector=V3.create(0,0,1);cam.isFitView=False;cam.setExtents(extent,extent)
    vp.camera=cam;adsk.doEvents();vp.refresh();path=dest/(name+'.png')
    assert vp.saveAsImageFile(str(path),1600,1600)
    return str(path)
ps={o.component.partNumber.split('_')[0]:o for o in wg.component.occurrences}
for go in (right,left):
    for o in go.component.occurrences:
        if o.component.partNumber.startswith('H05_') or o.component.partNumber=='H01_Hip_roll_117OD_106ID_case':
            o.isLightBulbOn=True;o.createForAssemblyContext(go).isLightBulbOn=True
            o.component.isBodiesFolderLightBulbOn=True
            for b in o.component.bRepBodies:b.isLightBulbOn=True
for o in wg.component.occurrences:
    o.isLightBulbOn=True
    o.createForAssemblyContext(wg).isLightBulbOn=True
    if hasattr(o.component,'isBodiesFolderLightBulbOn'):o.component.isBodiesFolderLightBulbOn=True
    for b in o.component.bRepBodies:b.isLightBulbOn=True
old={o.fullPathName:o.isLightBulbOn for o in root.allOccurrences}
shots=[]
try:
    right.isLightBulbOn=True;left.isLightBulbOn=True;wg.isLightBulbOn=True
    shots.append(view((630,-930,1100),(0,Y,825),70,'v18_overall_hips_and_waist'))
    shots.append(view((380,-600,1050),(0,Y,961),39,'v18_waist_and_6010_references'))
    right.isLightBulbOn=False;left.isLightBulbOn=False
    for key in ('W19','W20'):
        ps[key].isLightBulbOn=False;ps[key].createForAssemblyContext(wg).isLightBulbOn=False
    shots.append(view((180,-280,1090),(0,Y,933),20,'v18_short_roll_pitch_gimbal'))
    for key,o in ps.items():
        o.isLightBulbOn=key in ('W01','W04','W13','W14')
        o.createForAssemblyContext(wg).isLightBulbOn=key in ('W01','W04','W13','W14')
    shots.append(view((110,-140,1170),(0,Y,899),14,'v18_correct_scalloped_7010_mount'))
    wg.isLightBulbOn=False;right.isLightBulbOn=True
    shots.append(view((470,-470,950),(113,Y,764),34,'v18_right_hip_open_interfaces'))
    shots.append(view((435,490,900),(113,Y,767),32,'v18_right_hip_opposite_support'))
    saved_right={o.component.partNumber:o.isLightBulbOn for o in right.component.occurrences}
    for o in right.component.occurrences:
        o.isLightBulbOn=o.component.partNumber=='Q03_CNC_roll_to_pitch_fork'
        o.createForAssemblyContext(right).isLightBulbOn=o.isLightBulbOn
    shots.append(view((330,-370,960),(112,Y,783),22,'v18_blended_fork_isolated'))
    for o in right.component.occurrences:
        o.isLightBulbOn=saved_right[o.component.partNumber]
        o.createForAssemblyContext(right).isLightBulbOn=o.isLightBulbOn
    h5=rp['H05_DJI10018_pitch_gearbox_shell_ESTIMATE']
    hidden_half=next(b for b in h5.component.bRepBodies if b.name.startswith('W02'))
    hidden_half.isLightBulbOn=False
    rp['H01_Hip_roll_117OD_106ID_case'].isLightBulbOn=False
    rp['H01_Hip_roll_117OD_106ID_case'].createForAssemblyContext(right).isLightBulbOn=False
    shots.append(view((420,-540,960),(110,Y,785),33,'v18_estimated_shell_cutaway'))
    hidden_half.isLightBulbOn=True
    rp['H01_Hip_roll_117OD_106ID_case'].isLightBulbOn=True
    rp['H01_Hip_roll_117OD_106ID_case'].createForAssemblyContext(right).isLightBulbOn=True
    shots.append(view((270,-390,815),(130,Y,676),19,'v18_hip_yaw_bearing_and_mount'))
    shots.append(view((380,-380,580),(130,Y,442),21,'v18_matched_knee_bearings'))
finally:
    for o in root.allOccurrences:
        if o.fullPathName in old:o.isLightBulbOn=old[o.fullPathName]
    right.isLightBulbOn=True;left.isLightBulbOn=True;wg.isLightBulbOn=True
    for o in wg.component.occurrences:
        o.isLightBulbOn=True;o.createForAssemblyContext(wg).isLightBulbOn=True
    for o in root.occurrences:
        if o.component.name.startswith('ZZ_'):o.isLightBulbOn=False
    view((630,-930,1100),(0,Y,850),66,'v18_final_visible_assembly')
(OUT/'renders.json').write_text(json.dumps(shots,indent=2));result={'renders':shots}
