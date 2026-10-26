exec(compile((ROOT/'v21/common.py').read_text(),'<common>','exec'))
prior=json.loads((OUT/'waist_neutral_check.json').read_text())
lookup={(r['part'],r['body']):r['bounds'] for r in prior['parts']}
rep={'checked_bodies':0,'bounds_differences':[],'unhealthy_features':[]}
for o in wg.component.occurrences:
 for b in o.createForAssemblyContext(wg).bRepBodies:
  key=(o.component.partNumber,b.name);assert key in lookup,key
  old=lookup[key];now=bounds(b)
  err=max(abs(a-b) for aa,bb in zip(old,now) for a,b in zip(aa,bb))
  if err>.01:rep['bounds_differences'].append({'part':key,'error_mm':err})
  rep['checked_bodies']+=1
 for f in o.component.features:
  if int(f.healthState)!=0:rep['unhealthy_features'].append({'name':f.name,'message':f.errorOrWarningMessage})
rep['pass']=not rep['bounds_differences'] and not rep['unhealthy_features']
(OUT/'post_save_validation.json').write_text(json.dumps(rep,indent=2));assert rep['pass'],rep
result=rep
