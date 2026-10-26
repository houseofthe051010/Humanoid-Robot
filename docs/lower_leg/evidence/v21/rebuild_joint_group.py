exec(compile((ROOT/'v21/common.py').read_text(),'<common>','exec'))
old=wg;records=[]
for o in old.component.occurrences:
 rows=[(b.name,TM.copy(b),b.appearance) for b in o.createForAssemblyContext(old).bRepBodies]
 records.append((o.component.partNumber,o.component.description,rows,o.isLightBulbOn))
old.component.name='ZZ_V21_preserved_prior_waist_history';old.isLightBulbOn=False
wg=root.occurrences.addNewComponent(adsk.core.Matrix3D.create());wc=wg.component;wc.name='Waist_pitch_roll_battery_v21'
parts21={}
for name,desc,rows,visible in records:
 progress('reconstruct healthy native waist: '+name)
 o=newpart(wc,name,desc,'Retained physical/reference part; see component description');parts21[name.split('_')[0]]=o
 for n,b,ap in rows:add(o.component,b,n,ap)
 o.isGroundToParent=name.startswith(('W01_','W02_','W03_','W04_'));o.isLightBulbOn=visible
def pref(k):return parts21[k]
def joint(name,one,two,p,axis='x',kind='revolute',limits=None):
 pi=wc.constructionPlanes.createInput();pi.setByOffset(wc.xYConstructionPlane,adsk.core.ValueInput.createByReal(p[2]/10));pl=wc.constructionPlanes.add(pi);pl.isLightBulbOn=False
 sk=wc.sketches.add(pl);sk.name=name+'_datum';sk.isLightBulbOn=False
 sp=sk.sketchPoints.add(sk.modelToSketchSpace(pt(p)));geom=adsk.fusion.JointGeometry.createByPoint(sp)
 ji=wc.asBuiltJoints.createInput(two,one,geom)
 if kind=='ball':ji.setAsBallJointMotion(adsk.fusion.JointDirections.ZAxisJointDirection,adsk.fusion.JointDirections.XAxisJointDirection)
 else:ji.setAsRevoluteJointMotion({'x':adsk.fusion.JointDirections.XAxisJointDirection,'y':adsk.fusion.JointDirections.YAxisJointDirection,'z':adsk.fusion.JointDirections.ZAxisJointDirection}[axis])
 j=wc.asBuiltJoints.add(ji);j.name=name;j.isLightBulbOn=False
 if limits:
  ll=j.jointMotion.rotationLimits;ll.minimumValue=math.radians(limits[0]);ll.maximumValue=math.radians(limits[1]);ll.isMinimumValueEnabled=True;ll.isMaximumValueEnabled=True
 return j
joint('WJ00_waist_yaw',pref('W01'),pref('W05'),(0,Y,899),axis='z')
joint('WJ01_lower_waist_pitch',pref('W05'),pref('W06'),(0,Y+25,927),axis='x',limits=(-30,30))
joint('WJ02_upper_waist_roll',pref('W06'),pref('W07'),(0,Y+25,954),axis='y',limits=(-30,30))
for i,(a,b) in enumerate((('W07','W08'),('W06','W09'),('W05','W10'),('W07','W11'),('W06','W12'),('W04','W13'),('W04','W14'),('W05','W15'),('W07','W16'),('W05','W17'),('W06','W18'),('W07','W19'),('W07','W20'),('W05','W21'),('W05','W22')),3):rigid(wc,pref(a),pref(b),f'WJ{i:02}_{a}_{b}_retained')
cfg=json.loads((ROOT/'v19/waist_drive_geometry.json').read_text())
for row in cfg['links']:
 side=row['side'];s=-1 if side=='L' else 1
 frame=next(o for o in wc.occurrences if o.component.partNumber=='W27_rod_frame_'+side)
 joint('WJ_drive_'+side,pref(row['motor']),pref(row['crank']),(s*63.5,Y,995),limits=(-60,60))
 joint('WJ_rod_'+side+'_pin',pref(row['crank']),frame,row['A'],limits=(-180,180))
 joint('WJ_rod_'+side+'_tilt',frame,pref(row['rod']),row['A'],axis='y',limits=(-35,35))
 joint('WJ_rod_'+side+'_base',pref('W05'),pref(row['rod']),row['B'],kind='ball')
report={'mount_PCD_mm':40.5,'mount_thread':'8-M2.5','mount_clearance_mm':2.8,'output_PCD_mm':25,'lower_pitch_center_mm':[0,Y+25,927],'upper_roll_center_mm':[0,Y+25,954],'spine_rearward_shift_mm':15,'axis_separation_mm':27,'retained_crank_radius_mm':26,'retained_rod_center_spacing_mm':60,'rod_end_tilt_limit_deg':35,'joint_count':wc.asBuiltJoints.count,'history_note':'Waist component solids copied at the current state; native joints reconstructed. Original waist history preserved in hidden named group and source backup.'}
(OUT/'waist_build.json').write_text(json.dumps(report,indent=2));result=report
