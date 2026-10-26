exec(compile((ROOT/'v10/common.py').read_text(),'<common>','exec'))
dest=OUT/'deliverables';dest.mkdir(exist_ok=True)
for j in root.asBuiltJoints:j.isLightBulbOn=False
for c in [root]+[o.component for o in root.occurrences]:
 for pl in c.constructionPlanes:pl.isLightBulbOn=False
 for sk in c.sketches:sk.isLightBulbOn=c.name=='T08_Transmission_and_height_REFERENCE_SKETCHES' and sk.name in ['Primary_2p5_to_1_PCD_guides','Final_1_to_1_PCD_guides']
vp=app.activeViewport
def view(eye,target,name,ext):
 cam=vp.camera;cam.isSmoothTransition=False;cam.cameraType=adsk.core.CameraTypes.OrthographicCameraType
 cam.eye=pt(eye);cam.target=pt(target);cam.upVector=V3.create(0,0,1);cam.isFitView=False;cam.setExtents(*ext)
 vp.camera=cam;vp.saveAsImageFile(str(dest/name),1500,1500)
view((1100,950,930),(-15,20,475),'leg_layout_v10.png',(105,105))
view((850,900,880),(0,23,690),'upper_leg_mount_v10.png',(42,42))
view((-800,60,685),(0,23,650),'chain_layout_v10.png',(57,57))
view((750,550,725),(34,23,685),'mount_encoder_detail_v10.png',(19,19))
view((1100,950,930),(-15,20,475),'leg_layout_v10.png',(105,105))
result={'images':str(dest)}
