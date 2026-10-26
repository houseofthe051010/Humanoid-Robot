import json,time
out=ROOT/'v12';runs=[]
for name in ['check_bilateral.py','audit_mirror.py','export_bilateral.py']:
 (out/'progress.json').write_text(json.dumps({'stage':name,'time':time.time()}))
 scope={'ROOT':ROOT,'app':app,'adsk':adsk,'result':None};exec(compile((out/name).read_text(),name,'exec'),scope)
 r=scope['result'];runs.append(name)
 if name=='check_bilateral.py':
  assert r['neutral_pair_separated'],r
  for side,leg in r['legs'].items():
   assert not leg['invalid_joints']and not leg['empty_bodies'],leg
   assert max(p['knee_matrix_error']for p in leg['knee_native_samples'])<1e-6,leg
   assert max(v for p in leg['knee_native_samples']for v in p['attachment_matrix_errors'].values())<1e-6,leg
 if name=='audit_mirror.py':
  assert r['max_mirror_bound_error_mm']<1e-4,r
  assert all(v is not None and v<.01 for x in r['shape_difference_checks']for v in x['bidirectional_difference_mm3']),r
result={'completed':runs,'export':r}
