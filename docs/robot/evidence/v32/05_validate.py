exec(compile((ROOT/'v32/common32.py').read_text(),'<common32>','exec'))
exec(compile((OUT/'capture32.py').read_text(),'<capture32>','exec'))
d.activateRootComponent()
before=json.loads((OUT/'prechange_pose32.json').read_text());after=capture(d)
old={x['path']:x for x in before['occurrences']};new={x['path']:x for x in after['occurrences']}
assert old.keys()<=new.keys()
delta=max(abs(x-y) for k in old for x,y in zip(old[k]['transform'],new[k]['transform']))
assert delta<1e-8,delta
assert all(v==after['grounds'][k] for k,v in before['grounds'].items())
journal('validation_snapshot32',after)
assert before['joints'].keys()==after['joints'].keys()
joint_delta=0
for name,b in before['joints'].items():
 a=after['joints'][name]
 for key in ('valid','suppressed','type','one','two','anatomical','enabled'):
  if key in b:assert a[key]==b[key],(name,key,a[key],b[key])
 for key in ('frame','axis','limits'):
  if key in b:joint_delta=max(joint_delta,max(abs(x-y) for x,y in zip(a[key],b[key])))
 if 'angle' in b:joint_delta=max(joint_delta,abs(a['angle']-b['angle']))
assert joint_delta<1e-8,joint_delta
edited={r['part'] for f in ('shin_plates32','hip_collars32') for r in json.loads((OUT/(f+'.json')).read_text())}
hidden={f'C27_{p}_{s}' for p in ('Left','Right') for s in ('shin_rear','shin_rear_upper','calf_blue_mark')}|{f'C28_{p}_ankle_shroud' for p in ('Left','Right')}
unchanged=0
for part in before['parts']:
 if part['part'] in edited|hidden:continue
 key=part['path']+'|'+part['body'];assert key in after['shapes'],key
 assert max(abs(x-y) for a,b in zip(before['shapes'][key],after['shapes'][key]) for x,y in zip(a,b))<1e-7,key
 unchanged+=1
journal('pose_invariants32',dict(pass_=True,original_occurrences_compared=len(old),added_occurrences=list(new.keys()-old.keys()),max_transform_error=delta,joints_preserved=len(after['joints']),body_axes=after['anatomical_count'],unchanged_other_visible_shapes=unchanged,height_mm=after['height_mm']))

def overlap(a,b,bb=None):
 aa=bounds(a);bb=bounds(b) if bb is None else bb
 if any(aa[1][i]<bb[0][i] or bb[1][i]<aa[0][i] for i in range(3)):return 0.
 q=TM.copy(a);ix(q,TM.copy(b));return q.volume*1000
records=[];fail=[];target_cache={}
for side in ('left','right'):
 targets=[]
 for other in root.allOccurrences:
  if not other.isVisible or other.component.name in edited|hidden or other.component.name.startswith('C2'):continue
  if not (other.fullPathName.startswith(side+'_') or other.fullPathName.startswith('mechanism_'+side+'_')):continue
  targets.extend([(other.component.name,b,bounds(b)) for b in other.bRepBodies if b.isVisible])
 target_cache[side]=targets
for name in sorted(edited):
 o=exact(name)
 side='left' if '_Left_' in name else 'right'
 targets=target_cache[side]
 for body in o.bRepBodies:
  for target,b,bb in targets:
   v=overlap(body,b,bb)
   if v>.05:fail.append(dict(part=name,body=body.name,other=target,overlap_mm3=v))
  records.append(dict(part=name,body=body.name,kind='neutral',bodies_compared=len(targets)))
  journal('clearance_progress32',dict(completed=len(records),failures=fail))
# The new collar is fixed to the thigh. Check its yaw sweep relative to the
# upstream roll cradle and motor case; all upstream hip pitch/roll moves are shared.
for prefix in ('Left','Right'):
 o=exact('C28_'+prefix+'_hip_yaw_shroud')
 joint=next(j for j in root.allAsBuiltJoints if j.name==prefix+'_Hip_yaw')
 p=[v*10 for v in joint.transform.translation.asArray()];axis=joint.jointMotion.rotationAxisVector.asArray()
 targets=[b for other in root.allOccurrences if other.isVisible and other.fullPathName.startswith(prefix.lower()+'_hip_roll_link:') for b in other.bRepBodies if b.isVisible]
 for deg in range(-45,46,5):
  shapes=[rotate(TM.copy(b),p,axis,math.radians(deg)) for b in o.bRepBodies]
  worst=max([overlap(a,b) for a in shapes for b in targets]+[0])
  rec=dict(part=o.component.name,kind='hip_yaw_sweep',offset_deg=deg,max_overlap_mm3=worst);records.append(rec)
  if worst>.05:fail.append(rec)
journal('clearance_checks32',dict(all_sampled_clear=not fail,records=records,failures=fail,scope='Neutral new-cover fit against visible ipsilateral mechanism; discrete hip-yaw samples. No full robot collision/strength qualification.'))
assert not fail,fail
result=dict(invariants=True,clearance_records=len(records),failures=fail)
