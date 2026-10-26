exec(compile((ROOT/'v21/common.py').read_text(),'<common>','exec'))
cfg=json.loads((OUT/'upper_layout.json').read_text());g=cfg['ground_z_mm']
dest=OUT/'deliverables';dest.mkdir(exist_ok=True)
d.activateRootComponent();vp=app.activeViewport;app.userInterface.activeSelections.clear()
for c in [root]+list(d.allComponents):
 for coll in (c.sketches,c.constructionAxes,c.constructionPlanes,c.constructionPoints,c.asBuiltJoints):
  for x in coll:x.isLightBulbOn=False
for go in (right,left,wg):go.isLightBulbOn=True
for o in root.occurrences:
 if o.component.name.startswith('ZZ_') or 'GWK6010-8 3D Model' in o.component.name:o.isLightBulbOn=False
for o in wg.component.occurrences:
 if o.component.partNumber.startswith(('U','W19','W20')):
  o.isLightBulbOn=True;o.createForAssemblyContext(wg).isLightBulbOn=True;o.component.isBodiesFolderLightBulbOn=True
guide=getpart(wg,'U06_').component
guide.isSketchesFolderLightBulbOn=True
def view(eye,target,extent,name):
 cam=vp.camera;cam.isSmoothTransition=False;cam.cameraType=adsk.core.CameraTypes.OrthographicCameraType
 cam.eye=pt(eye);cam.target=pt(target);cam.upVector=V3.create(0,0,1);cam.isFitView=False;cam.setExtents(extent,extent)
 vp.camera=cam;adsk.doEvents();vp.refresh();p=dest/(name+'.png');assert vp.saveAsImageFile(str(p),1800,1800);return str(p)
images=[]
images.append(view((500,-800,1310),(0,Y,1130),62,'v21_battery_spine'))
for s in guide.sketches:s.isLightBulbOn=s.name.startswith(('U20','U21'))
images.append(view((0,-2000,g+810),(0,Y,g+810),185,'v21_full_height_layout'))
for s in guide.sketches:s.isLightBulbOn=s.name.startswith('U20')
images.append(view((1000,-1800,g+1200),(0,Y,g+820),180,'v21_overview'))
for s in guide.sketches:s.isLightBulbOn=s.name.startswith(('U20','U21'))
view((0,-2000,g+810),(0,Y,g+810),185,'v21_full_height_layout')
result={'images':images}
