exec(compile((ROOT/'v19/common.py').read_text(),'<common>','exec'))
wc=wg.component;cfg=json.loads((OUT/'waist_drive_geometry.json').read_text());report={'poses':[],'scope':'Native joint closure and targeted moving-body intersections; thread engagements and same-part hardware excluded. Rod-end surrogate requires physical verification.'}
def pref(k):return next(o for o in wc.occurrences if o.component.partNumber.startswith(k+'_'))
def point(k,p):
 q=pt(p);q.transformBy(pref(k).createForAssemblyContext(wg).transform2);return [q.x*10,q.y*10,q.z*10]
def length(a):return math.sqrt(sum(x*x for x in a))
def difference(a,b):return [x-y for x,y in zip(a,b)]
def inter(a,b):
 if not a.boundingBox.intersects(b.boundingBox):return 0
 sh=TM.copy(a);assert TM.booleanOperation(sh,TM.copy(b),BT.IntersectionBooleanType);return sh.volume*1000
def check(a,b,rec):
 for aa in pref(a).createForAssemblyContext(wg).bRepBodies:
  for bb in pref(b).createForAssemblyContext(wg).bRepBodies:
   # Crank pin / inner-ring, shaft / ring, M3 thread engagement is intentional.
   ignored=('inner_ring','spacer','M3_','M6_crank_pin_reference','M6_thin_jam_nut_reference')
   if any(t in aa.name for t in ignored) or any(t in bb.name for t in ignored):continue
   vol=inter(aa,bb)
   if vol>.05:rec['hits'].append({'parts':a+'/'+b,'a':aa.name,'b':bb.name,'mm3':round(vol,4)})
jr=wc.asBuiltJoints.itemByName('WJ01_lower_waist_roll');jp=wc.asBuiltJoints.itemByName('WJ02_upper_waist_pitch')
poses=[(0,0),(-20,0),(20,0),(0,-5),(0,5),(-20,-5),(-20,5),(20,-5),(20,5)]
try:
 for p,r in poses:
  progress('native waist linkage fit '+str((p,r)))
  for repeat in range(3):jr.jointMotion.rotationValue=math.radians(r);jp.jointMotion.rotationValue=math.radians(p);adsk.doEvents()
  rec={'command_pitch_roll_deg':[p,r],'actual_pitch_roll_deg':[math.degrees(jp.jointMotion.rotationValue),math.degrees(jr.jointMotion.rotationValue)],'closure_error_mm':[],'rod_end_tilt_deg':[],'motor_crank_delta_deg':[],'hits':[]}
  for row in cfg['links']:
   A=point(row['rod'],row['A']);B=point(row['rod'],row['B']);ca=point(row['crank'],row['A']);cb=point('W05',row['B'])
   rec['closure_error_mm'].extend([length(difference(A,ca)),length(difference(B,cb))])
   n=difference(A,B);nn=length(n);n=[x/nn for x in n]
   for key in ('W05',row['crank']):
    ax=V3.create(1,0,0);ax.transformBy(pref(key).createForAssemblyContext(wg).transform2);rec['rod_end_tilt_deg'].append(math.degrees(math.asin(min(1,abs(sum(a*b for a,b in zip(n,ax.asArray())))))))
   rec['motor_crank_delta_deg'].append(math.degrees(wc.asBuiltJoints.itemByName('WJ_drive_'+row['side']).jointMotion.rotationValue))
  for a,b in (('W05','W06'),('W05','W07'),('W06','W07'),('W19','W20'),('W19','W05'),('W20','W05'),('W19','W06'),('W20','W06'),('W19','W07'),('W20','W07'),('W23','W07'),('W24','W07'),('W23','W19'),('W24','W20'),('W25','W05'),('W26','W05'),('W25','W06'),('W26','W06'),('W25','W07'),('W26','W07'),('W25','W23'),('W26','W24'),('W25','W19'),('W26','W20'),('W21','W06'),('W21','W07')):check(a,b,rec)
  for a,b in (('W07','W08'),('W07','W16'),('W07','W11'),('W11','W12'),('W06','W09'),('W09','W10'),('W05','W21')):check(a,b,rec)
  report['poses'].append(rec);(OUT/'waist_motion_progress.json').write_text(json.dumps(report,indent=2))
finally:
 for repeat in range(3):jr.jointMotion.rotationValue=0;jp.jointMotion.rotationValue=0;adsk.doEvents()
report['max_closure_error_mm']=max(e for p in report['poses'] for e in p['closure_error_mm'])
report['max_rod_end_tilt_deg']=max(e for p in report['poses'] for e in p['rod_end_tilt_deg'])
report['max_pose_error_deg']=max(abs(a-b) for p in report['poses'] for a,b in zip(p['command_pitch_roll_deg'],p['actual_pitch_roll_deg']))
(OUT/'waist_motion_validation.json').write_text(json.dumps(report,indent=2));result={k:v for k,v in report.items() if k!='poses'};result['hit_poses']=sum(bool(p['hits']) for p in report['poses'])
