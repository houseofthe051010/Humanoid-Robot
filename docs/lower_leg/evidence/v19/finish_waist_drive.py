exec(compile((ROOT/'v19/common.py').read_text(),'<common>','exec'))
wc=wg.component;cfg=json.loads((OUT/'waist_drive_geometry.json').read_text())
def prefix(k):return next(o for o in wc.occurrences if o.component.partNumber.startswith(k+'_'))
def joint(name,one,two,point,kind='revolute',axis='x',limits=None):
 pi=wc.constructionPlanes.createInput();pi.setByOffset(wc.xYConstructionPlane,adsk.core.ValueInput.createByReal(point[2]/10));pl=wc.constructionPlanes.add(pi);pl.isLightBulbOn=False
 sk=wc.sketches.add(pl);sk.isLightBulbOn=False;sk.name=name+'_datum'
 sp=sk.sketchPoints.add(sk.modelToSketchSpace(pt(point)));geom=adsk.fusion.JointGeometry.createByPoint(sp)
 ji=wc.asBuiltJoints.createInput(two,one,geom) if kind=='revolute' else wc.asBuiltJoints.createInput(one,two,geom)
 if kind=='ball':ji.setAsBallJointMotion(adsk.fusion.JointDirections.ZAxisJointDirection,adsk.fusion.JointDirections.XAxisJointDirection)
 else:ji.setAsRevoluteJointMotion({'x':adsk.fusion.JointDirections.XAxisJointDirection,'y':adsk.fusion.JointDirections.YAxisJointDirection}[axis])
 j=wc.asBuiltJoints.add(ji);j.name=name;j.isLightBulbOn=False
 if limits:
  ll=j.jointMotion.rotationLimits;ll.minimumValue=math.radians(limits[0]);ll.maximumValue=math.radians(limits[1]);ll.isMinimumValueEnabled=True;ll.isMaximumValueEnabled=True
 return j
progress('attach two native waist linkage loops')
for o in wc.occurrences:
 if o.component.partNumber.startswith(('W21_','W22_','W23_','W24_','W25_','W26_')):
  o.isGroundToParent=False
for row in cfg['links']:
 s=-1 if row['side']=='L' else 1;A=row['A'];B=row['B'];motor=prefix(row['motor']);crank=prefix(row['crank']);rod=prefix(row['rod']);side=row['side']
 joint('WJ_drive_'+side,motor,crank,(s*63.5,Y,995),limits=(-60,60))
 # A two-axis kinematic frame mirrors the ankle modeling approach. This
 # represents the existing rod-end swivel and small spherical tilt; it is
 # NOT the optional additional physical swivel proposed to the user.
 fr=newpart(wc,'W27_rod_frame_'+side,'Zero-body rod-end joint frame, not a fabricated additional swivel.','kinematic frame');fr.isLightBulbOn=False
 joint('WJ_rod_'+side+'_pin',crank,fr,A,limits=(-180,180))
 joint('WJ_rod_'+side+'_tilt',fr,rod,A,axis='y',limits=(-6.25,6.25))
 joint('WJ_rod_'+side+'_base',prefix('W05'),rod,B,kind='ball')
progress('build contoured common spine carrier on actual 6010 stationary patterns')
socket=prefix('W07');shape=TM.copy(socket.createForAssemblyContext(wg).bRepBodies.item(0));holes_report=[]
for side,s in (('L',-1),('R',1)):
 motor=prefix('W19' if s<0 else 'W20').createForAssemblyContext(wg);fx=s*48.5
 xa,xb=sorted((fx-s*3,fx));ringpart=ring((xa,Y,995),(xb,Y,995),43,27.5)
 xa2,xb2=sorted((fx-s*6,fx));un(ringpart,ring((xa2,Y,995),(xb2,Y,995),43,35))
 holes=[]
 for b in motor.bRepBodies:
  for f in b.faces:
   c=adsk.core.Cylinder.cast(f.geometry)
   if c and abs(abs(c.axis.x)-1)<1e-5 and abs(c.radius*10-1.2295)<.003 and abs(math.hypot(c.origin.y*10-Y,c.origin.z*10-995)-37)<.01:
    q=(round(c.origin.y*10,4),round(c.origin.z*10,4))
    if q not in holes:holes.append(q)
 assert len(holes)==8,holes
 for y,z in holes:sub(ringpart,cy((xa2-1,y,z),(xb2+1,y,z),1.7))
 # Rounded, tapered arch spans above the crank sweep and meets the spine socket.
 arch=un(beam_y((s*8,1003),(s*25,1024),6,Y+4,Y+16),beam_y((s*25,1024),(s*47,1030),6,Y+4,Y+16))
 ix(arch,bx((-48.5,Y-60,975),(48.5,Y+60,1050)));un(ringpart,arch)
 for b in motor.bRepBodies:sub(ringpart,TM.copy(b))
 un(shape,ringpart);holes_report.append({'side':side,'stationary_mount_plane_x':fx,'eight_mount_holes_yz':holes})
world_replace(wg,socket,[('W07_spine_socket_with_curved_6010_carrier',shape)],'PA12-CF prototype spine socket with curved paired 6010 carriers. Eight measured M3 stationary holes per motor on 74 mm PCD; output cranks have separate 25 mm PCD interfaces. Carrier thickness 3 mm inner / 6 mm outer with open crank envelope.',plastic)
for b in root.bRepBodies:b.isLightBulbOn=False
d.activateRootComponent();app.userInterface.activeSelections.clear();adsk.doEvents()
(OUT/'waist_drive_joints.json').write_text(json.dumps({'mounts':holes_report,'joint_count':wc.asBuiltJoints.count},indent=2));result={'joints':wc.asBuiltJoints.count,'mounts':holes_report}
