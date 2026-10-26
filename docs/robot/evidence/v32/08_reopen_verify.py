exec(compile((ROOT/'v32/common32.py').read_text(),'<common32>','exec'))
exec(compile((OUT/'capture32.py').read_text(),'<capture32>','exec'))
baseline=json.loads((OUT/'final_native_inventory32.json').read_text());source=doc;opened=None
archive=OUT/'deliverables/Humanoid_complete_v32.f3d'
try:
 opened=app.importManager.importToNewDocument(app.importManager.createFusionArchiveImportOptions(str(archive)));assert opened
 rd=adsk.fusion.Design.cast(opened.products.itemByProductType('DesignProductType'));actual=capture(rd)
 assert baseline['shapes'].keys()==actual['shapes'].keys()
 bound_error=max(abs(x-y) for k in baseline['shapes'] for a,b in zip(baseline['shapes'][k],actual['shapes'][k]) for x,y in zip(a,b))
 assert bound_error<.003,bound_error
 assert baseline['grounds']==actual['grounds']
 assert baseline['joints'].keys()==actual['joints'].keys()
 joint_error=0.;limit_differences=[]
 for name,a in baseline['joints'].items():
  b=actual['joints'][name];assert b['valid'] and not b['suppressed'] and a['type']==b['type']
  assert a['one']==b['one'] and a['two']==b['two']
  joint_error=max(joint_error,max(abs(x-y) for x,y in zip(a['frame'],b['frame'])))
  if a['type']==1:
   joint_error=max(joint_error,abs(math.atan2(math.sin(a['angle']-b['angle']),math.cos(a['angle']-b['angle']))),max(abs(x-y) for x,y in zip(a['axis'],b['axis'])))
   assert a['enabled']==b['enabled']
   if max(abs(x-y) for x,y in zip(a['limits'],b['limits']))>1e-7:limit_differences.append(dict(name=name,before=a['limits'],after=b['limits']))
 assert joint_error<1e-5,joint_error
 assert not limit_differences,limit_differences
 assert actual['anatomical_count']==23 and actual['visible_meshes']==8 and actual['external_referenced_occurrences']==0
 report=dict(pass_=True,archive=str(archive),visible_shapes=len(actual['shapes']),native_joints=len(actual['joints']),body_axes=actual['anatomical_count'],all_parent_grounds_match=True,max_bounds_error_mm=bound_error,max_joint_error=joint_error,exact_ranges_match=True,epoch=time.time())
 journal('native_reopen32',report);result=report
finally:
 if opened:opened.close(False)
 source.activate()
