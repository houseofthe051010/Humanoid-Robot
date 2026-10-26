import adsk.core,adsk.fusion,json
OUT=ROOT/'v14';dest=OUT/'deliverables';doc=next(x for x in app.documents if x.name=='Bilateral_legs_v14');doc.activate();d=adsk.fusion.Design.cast(app.activeProduct);root=d.rootComponent
vp=app.activeViewport;app.userInterface.activeSelections.clear()
components=[root]+[go.component for go in root.occurrences]+[o.component for go in root.occurrences for o in go.component.occurrences]
for c in components:
 for sk in c.sketches:sk.isLightBulbOn=False
 for a in c.constructionAxes:a.isLightBulbOn=False
 for p in c.constructionPlanes:p.isLightBulbOn=False
 for p in c.constructionPoints:p.isLightBulbOn=False
 for j in c.asBuiltJoints:j.isLightBulbOn=False
def pt(a):return adsk.core.Point3D.create(*(x/10 for x in a))
def view(eye,target,name,extent):
 cam=vp.camera;cam.isSmoothTransition=False;cam.cameraType=adsk.core.CameraTypes.OrthographicCameraType;cam.eye=pt(eye);cam.target=pt(target);cam.upVector=adsk.core.Vector3D.create(0,0,1);cam.isFitView=False;cam.setExtents(extent,extent);vp.camera=cam;adsk.doEvents();vp.refresh();vp.saveAsImageFile(str(dest/name),1400,1400)
left=next(o for o in root.occurrences if o.component.name=='Left_leg');left.isLightBulbOn=False
view((-450,-1100,550),(130,20,423),'enclosed_oval_adapter_v14.png',23)
view((130,-1500,423),(130,20,423),'adapter_front_v14.png',23)
left.isLightBulbOn=True
view((-1050,-1700,1050),(0,20,420),'bilateral_legs_v14.png',110)
path=dest/'Bilateral_legs_v14.f3d';assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(path)))
rows=[]
for go in root.occurrences:
 for o in go.component.occurrences:
  if not o.isLightBulbOn or o.component.bRepBodies.count==0:continue
  c=o.component;a=c.attributes.itemByName('SHIN','material')
  rows.append({'side':go.component.name,'name':c.partNumber,'description':c.description,'material':a.value if a else '', 'body_count':c.bRepBodies.count})
(dest/'cad_inventory.json').write_text(json.dumps(rows,indent=2))
result={'native':str(path),'inventory_rows':len(rows),'preview':str(dest/'enclosed_oval_adapter_v14.png')}
