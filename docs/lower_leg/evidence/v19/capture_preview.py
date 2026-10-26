exec(compile((ROOT/'v19/common.py').read_text(),'<v19 common>','exec'))
dest=OUT/'deliverables';dest.mkdir(exist_ok=True)
vp=app.activeViewport;app.userInterface.activeSelections.clear()
for c in [root]+list(d.allComponents):
    for coll in (c.sketches,c.constructionAxes,c.constructionPlanes,c.constructionPoints,c.asBuiltJoints):
        for x in coll:x.isLightBulbOn=False
def view(eye,target,extent,name):
    cam=vp.camera;cam.isSmoothTransition=False;cam.cameraType=adsk.core.CameraTypes.OrthographicCameraType
    cam.eye=pt(eye);cam.target=pt(target);cam.upVector=V3.create(0,0,1);cam.isFitView=False;cam.setExtents(extent,extent)
    vp.camera=cam;adsk.doEvents();vp.refresh();p=dest/(name+'.png');assert vp.saveAsImageFile(str(p),1600,1600);return str(p)
for go in (right,left,wg):
    go.isLightBulbOn=True
    for o in go.component.occurrences:
        if o.component.partNumber.startswith(('Q0','H05','H06','H07','H08','W0')) or o.component.partNumber=='H01_Hip_roll_117OD_106ID_case':
            o.isLightBulbOn=True;o.createForAssemblyContext(go).isLightBulbOn=True;o.component.isBodiesFolderLightBulbOn=True
for o in root.occurrences:
    if o.component.name.startswith('ZZ_'):o.isLightBulbOn=False
shots=[]
shots.append(view((0,-1100,817),(0,Y,817),47,'v19_front_preview'))
shots.append(view((530,-880,1060),(0,Y,822),58,'v19_overview_preview'))
left.isLightBulbOn=False;wg.isLightBulbOn=False
shots.append(view((380,-440,920),(93,Y,763),31,'v19_right_hip_preview'))
saved={o.component.partNumber:o.isLightBulbOn for o in right.component.occurrences}
for key in ('Q02','Q03'):
    for o in right.component.occurrences:
        o.isLightBulbOn=o.component.partNumber.startswith(key+'_');o.createForAssemblyContext(right).isLightBulbOn=o.isLightBulbOn
    shots.append(view((340,-380,900),(110,Y,758 if key=='Q02' else 794),25,'v19_isolated_'+key))
for o in right.component.occurrences:
    o.isLightBulbOn=saved[o.component.partNumber];o.createForAssemblyContext(right).isLightBulbOn=o.isLightBulbOn
left.isLightBulbOn=True;wg.isLightBulbOn=True
view((530,-880,1060),(0,Y,822),58,'v19_overview_preview')
result={'images':shots}
