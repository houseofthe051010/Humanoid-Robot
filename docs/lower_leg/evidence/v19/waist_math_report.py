from waist_kinematics import *
c=(30,-30,8,-10,68,26,np.radians(160))
rows=[]
for p in np.arange(-20,20.01,1):
 for r in np.arange(-5,5.01,.5):
  angles=np.radians([p,r]);pose=solve(c,*angles);j=jac(c,*angles)
  assert pose is not None and j is not None
  rows.append({'pitch':float(p),'roll':float(r),'ratio_min':float(np.min(abs(j))),'ratio_max':float(np.max(abs(j))),'tilt_max':float(max(t for x in pose for t in x['tilts'])),'condition':float(np.linalg.cond(j))})
report={'configuration':list(c),'grid_poses':len(rows),'pitch_range_deg':[-20,20],'roll_range_deg':[-5,5],
 'neutral_jacobian_motor_angle_per_joint_angle':jac(c).tolist(),'reduction_min':min(a['ratio_min'] for a in rows),'reduction_max':max(a['ratio_max'] for a in rows),
 'max_rod_end_tilt_deg':max(a['tilt_max'] for a in rows),'assumed_hardware_tilt_limit_deg':6.25,'maximum_J_condition':max(a['condition'] for a in rows),
 'rod_eye_distance_mm':solve(c)[0]['L'],'rod_stock_length_mm':solve(c)[0]['L']-36,
 'definition':'Each absolute Jacobian entry is motor-angle/joint-angle holding the other waist axis fixed; by virtual work it is that actuator contribution to joint torque. This is not a single ratio for the complete two-motor differential.',
 'reference_target_deg':30,'target_sources':['https://www.unitree.com/g1/','https://github.com/robotology/icub-models/blob/master/iCub_manual/robots/iCubGazeboV2_5_visuomanip/model.urdf'],
 'user_choice':'Retain M6 rod ends and limit roll. Explain optional physical two-axis swivels at delivery; do not install them.'}
(OUT/'waist_kinematic_report.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
