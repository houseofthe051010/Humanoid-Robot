exec(compile((ROOT/'v19/common.py').read_text(),'<common>','exec'))
report={'waist_geometry_issues':[],'waist_feature_issues':[],'waist_invalid_joints':[],'pitch_rear_rim_x_mm':[]}
for o in wg.component.occurrences:
 if not o.component.partNumber.startswith(('W05_','W07_','W21_','W22_','W23_','W24_','W25_','W26_')):continue
 for b in o.component.bRepBodies:
  if 'vendor' in b.name.lower():continue
  n=sum(not s.isVoid for s in b.shells)
  if not b.isSolid or b.volume<=0 or n!=1:report['waist_geometry_issues'].append({'part':o.component.partNumber,'body':b.name,'shells':n})
 for f in o.component.features:
  if f.healthState!=adsk.fusion.FeatureHealthStates.HealthyFeatureHealthState:report['waist_feature_issues'].append({'part':o.component.partNumber,'feature':f.name,'message':f.errorOrWarningMessage})
report['waist_invalid_joints']=[j.name for j in wg.component.asBuiltJoints if not j.isValid]
for go,s in ((right,1),(left,-1)):
 o=parts(go)['H05_DJI10018_pitch_gearbox_shell_ESTIMATE'].createForAssemblyContext(go);bb=o.bRepBodies.item(0).boundingBox
 closest=bb.minPoint.x*10 if s>0 else bb.maxPoint.x*10
 report['pitch_rear_rim_x_mm'].append(closest)
assert not report['waist_geometry_issues'] and not report['waist_feature_issues'] and not report['waist_invalid_joints'],report
assert max(abs(x) for x in report['pitch_rear_rim_x_mm'])<.02,report
(OUT/'final_geometry_audit.json').write_text(json.dumps(report,indent=2));result=report
