import adsk.core,adsk.fusion,json
OUT=ROOT/'v13';dest=OUT/'deliverables'
doc=next(x for x in app.documents if x.name=='Bilateral_legs_v13');doc.activate();d=adsk.fusion.Design.cast(app.activeProduct);root=d.rootComponent
app.userInterface.activeSelections.clear();vp=app.activeViewport
pt=lambda a:adsk.core.Point3D.create(*(x/10 for x in a))
def view(eye,target,name,extent):
 cam=vp.camera;cam.isSmoothTransition=False;cam.cameraType=adsk.core.CameraTypes.OrthographicCameraType;cam.eye=pt(eye);cam.target=pt(target);cam.upVector=adsk.core.Vector3D.create(0,0,1);cam.isFitView=False;cam.setExtents(extent,extent);vp.camera=cam;adsk.doEvents();vp.refresh();vp.saveAsImageFile(str(dest/name),1600,1600)
for go in root.occurrences:
 for j in go.component.asBuiltJoints:j.isLightBulbOn=False
 for s in go.component.sketches:s.isLightBulbOn=False
 for a in go.component.constructionPlanes:a.isLightBulbOn=False
 for o in go.component.occurrences:
  if o.component.partNumber.startswith('V13'):o.isLightBulbOn=False
left=next(o for o in root.occurrences if o.component.name=='Left_leg');left.isLightBulbOn=False
view((-800,-950,750),(130,23,510),'drive_layout_v13.png',43)
view((-1500,23,500),(130,23,500),'sprocket_side_v13.png',40)
right=next(o for o in root.occurrences if o.component.name=='Right_leg');hidden=[]
for o in right.component.occurrences:
 if o.component.partNumber.startswith(('P03','P05')):o.isLightBulbOn=False;hidden.append(o)
view((-700,-950,720),(130,23,565),'motor_case_open_v13.png',35)
for o in hidden:o.isLightBulbOn=True
left.isLightBulbOn=True
view((-1050,-1700,1050),(0,20,420),'bilateral_legs_v13.png',110)
assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(dest/'Bilateral_legs_v13.f3d')))
result={'preview':str(dest/'bilateral_legs_v13.png')}
