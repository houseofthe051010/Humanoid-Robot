exec(compile((ROOT/'v15/common.py').read_text(),'<common>','exec'))
dest=OUT/'deliverables';dest.mkdir(exist_ok=True)
vp=app.activeViewport;app.userInterface.activeSelections.clear()
for c in [root]+list(d.allComponents):
 for coll in [c.sketches,c.constructionAxes,c.constructionPlanes,c.constructionPoints,c.asBuiltJoints]:
  for a in coll:a.isLightBulbOn=False
def view(eye,target,name,extent):
 cam=vp.camera;cam.isSmoothTransition=False;cam.cameraType=adsk.core.CameraTypes.OrthographicCameraType;cam.eye=pt(eye);cam.target=pt(target);cam.upVector=V3.create(0,0,1);cam.isFitView=False;cam.setExtents(extent,extent);vp.camera=cam;adsk.doEvents();vp.refresh();vp.saveAsImageFile(str(dest/name),1400,1400)
left=next(o for o,s in groups()if s==-1);left.isLightBulbOn=False
view((-550,-950,700),(130,Y,560),'mount_front_v15.png',26)
view((750,-950,700),(130,Y,560),'mount_rear_v15.png',26)
left.isLightBulbOn=True
view((-620,-1200,1050),(0,Y,820),'waist_v15.png',42)
view((-1050,-1700,1050),(0,20,450),'legs_and_waist_v15.png',120)
rows=[]
for go in root.occurrences:
 if not go.isLightBulbOn:continue
 for o in go.component.occurrences:
  if not o.isLightBulbOn or o.component.bRepBodies.count==0:continue
  c=o.component;a=c.attributes.itemByName('SHIN','material')
  rows.append({'side':go.component.name,'name':c.partNumber,'description':c.description,'material':a.value if a else '', 'body_count':c.bRepBodies.count,'bodies':[{'name':b.name,'solid':b.isSolid,'shells':b.shells.count,'volume_mm3':b.volume*1000}for b in c.bRepBodies]})
(OUT/'inventory.json').write_text(json.dumps(rows,indent=2))
result={'inventory':str(OUT/'inventory.json'),'renders':4}
