import adsk.core,adsk.fusion,json
OUT=ROOT/'v12';dest=OUT/'deliverables';dest.mkdir(exist_ok=True)
doc=next(x for x in app.documents if x.name=='Bilateral_legs_v12');doc.activate();d=adsk.fusion.Design.cast(app.activeProduct);root=d.rootComponent
app.userInterface.activeSelections.clear();vp=app.activeViewport
# A full-turn passive pin is physically continuous. Avoid an artificial stop at
# the +/-180deg wrap introduced by the copied joint's local angle reference.
report=json.loads((OUT/'bilateral_validation.json').read_text())
for go in root.occurrences:
 side=go.component.name.removesuffix('_leg')
 for name in ['Rod_A_pin_swivel','Rod_B_pin_swivel']:
  j=go.component.asBuiltJoints.itemByName(side+'_'+name);r=j.jointMotion.rotationLimits;r.isMinimumValueEnabled=False;r.isMaximumValueEnabled=False
  report['legs'][side]['pose_angle_rebases'][name]['continuous_full_turn_pin']=True
(OUT/'bilateral_validation.json').write_text(json.dumps(report,indent=2))
pt=lambda a:adsk.core.Point3D.create(*(x/10 for x in a))
def view(eye,target,name,extent):
 cam=vp.camera;cam.isSmoothTransition=False;cam.cameraType=adsk.core.CameraTypes.OrthographicCameraType;cam.eye=pt(eye);cam.target=pt(target);cam.upVector=adsk.core.Vector3D.create(0,0,1);cam.isFitView=False;cam.setExtents(extent,extent);vp.camera=cam;adsk.doEvents();vp.refresh();vp.saveAsImageFile(str(dest/name),1600,1600)
for go in root.occurrences:
 for j in go.component.asBuiltJoints:j.isLightBulbOn=False
 for p in go.component.constructionPoints:p.isLightBulbOn=False
 for a in go.component.constructionAxes:a.isLightBulbOn=False
view((-1050,-1700,1050),(0,20,420),'bilateral_legs_v12.png',110)
view((0,-1500,530),(0,20,420),'bilateral_front_v12.png',105)
left=next(o for o in root.occurrences if o.component.name=='Left_leg');left.isLightBulbOn=False
view((-800,-1100,880),(130,23,645),'motor_and_hip_v12.png',53)
view((850,850,860),(130,23,645),'rear_rail_mounts_v12.png',53)
right=next(o for o in root.occurrences if o.component.name=='Right_leg');hidden=[]
for o in right.component.occurrences:
 if o.component.partNumber.startswith(('P03','P05')):o.isLightBulbOn=False;hidden.append(o)
view((-700,-950,720),(130,23,590),'motor_case_open_v12.png',37)
for o in hidden:o.isLightBulbOn=True
left.isLightBulbOn=True
view((-1050,-1700,1050),(0,20,420),'bilateral_legs_v12.png',110)
assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(dest/'Bilateral_legs_v12.f3d')))
result={'preview':str(dest/'bilateral_legs_v12.png')}
