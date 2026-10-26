exec(compile((ROOT/'v11/common.py').read_text(),'<common>','exec'))
d.computeAll();adsk.doEvents()
app.userInterface.activeSelections.clear()
dest=OUT/'deliverables';dest.mkdir(exist_ok=True)
for n in ['T04_GWK7010_Hip_yaw_REFERENCE','T05_Hip_crosshead_REFERENCE','T06_Pelvis_HALF_REFERENCE','T07_Hip_pitch_motor_ENVELOPE_REFERENCE','T09_Hip_roll_motor_ENVELOPE_REFERENCE','T10_Thigh_front_fairing_PROVISIONAL','T11_Thigh_rear_fairing_PROVISIONAL','T12_Circular_motor_service_cover_PROVISIONAL']:parts[n].isLightBulbOn=True
parts['T08_Transmission_and_height_REFERENCE_SKETCHES'].isLightBulbOn=False
color(parts['T07_Hip_pitch_motor_ENVELOPE_REFERENCE'].component,'T07_Hip_pitch_motor_ENVELOPE_REFERENCE_finish')
color(parts['T09_Hip_roll_motor_ENVELOPE_REFERENCE'].component,'Hip_roll_reference_teal')
for j in root.asBuiltJoints:j.isLightBulbOn=False
for c in [root]+[o.component for o in root.occurrences]:
 for pl in c.constructionPlanes:pl.isLightBulbOn=False
 for sk in c.sketches:sk.isLightBulbOn=False
vp=app.activeViewport
def view(eye,target,name,ext):
 cam=vp.camera;cam.isSmoothTransition=False;cam.cameraType=adsk.core.CameraTypes.OrthographicCameraType
 cam.eye=pt(eye);cam.target=pt(target);cam.upVector=V3.create(0,0,1);cam.isFitView=False;cam.setExtents(*ext)
 vp.camera=cam;adsk.doEvents();vp.refresh();vp.saveAsImageFile(str(dest/name),1500,1500)
view((-1000,-1000,780),(-12,20,410),'leg_shelled_v11.png',(96,96))
view((-850,-750,760),(-15,23,628),'thigh_shelled_v11.png',(48,48))
view((-1000,23,600),(0,23,620),'thigh_side_v11.png',(46,46))
view((0,-1000,600),(-25,23,640),'thigh_front_v11.png',(48,48))
for n in ['T10_Thigh_front_fairing_PROVISIONAL','T11_Thigh_rear_fairing_PROVISIONAL','T12_Circular_motor_service_cover_PROVISIONAL']:parts[n].isLightBulbOn=False
view((850,900,780),(-20,23,622),'thigh_under_shell_v11.png',(45,45))
for n in ['T10_Thigh_front_fairing_PROVISIONAL','T11_Thigh_rear_fairing_PROVISIONAL','T12_Circular_motor_service_cover_PROVISIONAL']:parts[n].isLightBulbOn=True
view((-1000,-1000,780),(-12,20,410),'leg_shelled_v11.png',(96,96))
result={'images':str(dest)}
