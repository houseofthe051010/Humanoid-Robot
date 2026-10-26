exec(compile((ROOT/'v11/common.py').read_text(),'<common>','exec'))
Y=23.343134;Z=600.
progress('check fitted fairings and shortened layout')
before=next(r for r in json.loads((OUT/'live_inventory.json').read_text()) if r['active'])
preserved=[];changes=[]
for row in before['components']:
 n=row['name']
 if n.startswith(('N06','R01','T0')):continue
 bs=list(parts[n].bRepBodies);err=0
 if len(bs)!=len(row['bodies']):err=1e10
 else:
  for b,old in zip(bs,row['bodies']):
   err=max(err,abs(b.volume*1000-old['volume_mm3']))
   for vals,orig in zip([b.boundingBox.minPoint.asArray(),b.boundingBox.maxPoint.asArray()],old['bounds']):err=max(err,max(abs(x*10-y)for x,y in zip(vals,orig)))
 (preserved if err<1e-5 else changes).append({'component':n,'max_delta':err})
moved_errors=[]
for row in before['components']:
 n=row['name'];dz=-85 if n.startswith(('R01','T01','T02','T03')) else (-118 if n.startswith(('T04','T05')) else None)
 if dz is None:continue
 bs=list(parts[n].bRepBodies);err=0
 if len(bs)!=len(row['bodies']):err=1e10
 else:
  for b,old in zip(bs,row['bodies']):
   err=max(err,abs(b.volume*1000-old['volume_mm3']))
   for vals,orig in zip([b.boundingBox.minPoint.asArray(),b.boundingBox.maxPoint.asArray()],old['bounds']):err=max(err,max(abs(x*10-y-(dz if i==2 else 0))for i,(x,y)in enumerate(zip(vals,orig))))
 if err>1e-5:moved_errors.append({'component':n,'max_delta':err})
warnings=[];inventory=[];empty_bodies=[]
for f in root.features:
 if f.healthState!=adsk.fusion.FeatureHealthStates.HealthyFeatureHealthState:warnings.append({'component':root.name,'feature':f.name,'message':f.errorOrWarningMessage})
for o in root.occurrences:
 c=o.component
 for f in c.features:
  if f.healthState!=adsk.fusion.FeatureHealthStates.HealthyFeatureHealthState:warnings.append({'component':c.name,'feature':f.name,'message':f.errorOrWarningMessage})
 if c.name.startswith(('T0','T1','N06','R01')):
  empty_bodies.extend([c.name+'/'+b.name for b in o.bRepBodies if not b.isSolid or b.volume<=1e-9])
  inventory.append({'component':c.name,'bodies':[{'name':b.name,'solid':b.isSolid,'volume_mm3':b.volume*1000,'bounds':[[x*10 for x in b.boundingBox.minPoint.asArray()],[x*10 for x in b.boundingBox.maxPoint.asArray()]]}for b in o.bRepBodies]})
new=[n for n in parts if n.startswith(('T09','T10','T11','T12'))]
allnames=[n for n in parts if not n.startswith(('U0','K01','GIM','N00','S04','T08'))]
collisions=[];errors=[];tests=0;done=set()
for an in new:
 for bn in allnames:
  if an==bn or tuple(sorted([an,bn]))in done:continue
  done.add(tuple(sorted([an,bn])))
  if not parts[an].boundingBox.intersects(parts[bn].boundingBox):continue
  for a in parts[an].bRepBodies:
   for b in parts[bn].bRepBodies:
    if not a.boundingBox.intersects(b.boundingBox):continue
    tests+=1
    try:
     cp=TM.copy(a);ok=TM.booleanOperation(cp,TM.copy(b),adsk.fusion.BooleanTypes.IntersectionBooleanType)
     if ok and cp.volume*1000>.01:collisions.append({'a':an+'/'+a.name,'b':bn+'/'+b.name,'volume_mm3':cp.volume*1000})
    except Exception as e:errors.append({'a':an,'b':bn,'error':str(e)})
motor=parts['R01_DJI_10018_77KV_ESTIMATED_REFERENCE'];hub=next(b for b in motor.bRepBodies if b.name=='Rear_bearing_hub_EST')
rail=parts['N06_Upper_leg_oval_stub_R'].bRepBodies.item(0)
gap=(rail.boundingBox.minPoint.x-hub.boundingBox.maxPoint.x)*10
keep=TM.createCylinderOrCone(pt((33,Y,Z)),1.4,pt((38,Y,Z)),1.4)
keep_hits=[]
for n in allnames:
 for b in parts[n].bRepBodies:
  if not b.boundingBox.intersects(keep.boundingBox):continue
  cp=TM.copy(b);ok=TM.booleanOperation(cp,TM.copy(keep),adsk.fusion.BooleanTypes.IntersectionBooleanType)
  if ok and cp.volume*1000>.001:keep_hits.append({'component':n,'body':b.name,'volume_mm3':cp.volume*1000})
rail_checks=[{'component':n,'bodies':o.component.bRepBodies.count,'length_mm':(max(b.boundingBox.maxPoint.z for b in o.bRepBodies)-min(b.boundingBox.minPoint.z for b in o.bRepBodies))*10,'volume_mm3':sum(b.volume for b in o.bRepBodies)*1000}for n,o in parts.items()if n.startswith('N06')]
result={'unchanged_lower_leg_components':len(preserved),'unexpected_changes':changes,'moved_component_shape_position_errors':moved_errors,'empty_or_nonsolid_bodies':empty_bodies,'rail_checks':rail_checks,'feature_warnings':warnings,'invalid_joints':[j.name for j in root.asBuiltJoints if not j.isValid],'new_interface_tests':tests,'new_interface_collisions':collisions,'boolean_errors':errors,'encoder_gap_mm':gap,'encoder_keepout_intersections':keep_hits,'inventory':inventory}
(OUT/'layout_validation.json').write_text(json.dumps(result,indent=2))
result={k:v for k,v in result.items() if k!='inventory'}
