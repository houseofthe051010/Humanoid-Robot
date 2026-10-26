exec(compile((ROOT/'v10/common.py').read_text(),'<common>','exec'))
progress('validate upper-leg solids, contacts and unchanged lower leg')
before=next(r for r in json.loads((OUT/'live_inventory.json').read_text()) if r['active'])
preserved=[];changes=[]
for row in before['components']:
 n=row['name']
 if n.startswith(('N06','R01')):continue
 oc=parts[n];bs=list(oc.bRepBodies)
 err=0
 if len(bs)!=len(row['bodies']):err=1e10
 else:
  for b,old in zip(bs,row['bodies']):
   err=max(err,abs(b.volume*1000-old['volume_mm3']))
   for vals,orig in zip([b.boundingBox.minPoint.asArray(),b.boundingBox.maxPoint.asArray()],old['bounds']):err=max(err,max(abs(x*10-y)for x,y in zip(vals,orig)))
 (preserved if err<1e-5 else changes).append({'component':n,'max_delta':err})
newnames=[n for n in parts if n.startswith(('T0','R01','N06'))]
inventory=[];warnings=[]
for o in root.occurrences:
 c=o.component
 for f in c.features:
  if int(f.healthState)!=0:warnings.append({'component':c.name,'feature':f.name,'health':int(f.healthState),'message':f.errorOrWarningMessage})
 if c.name in newnames:
  inventory.append({'component':c.name,'bodies':[{'name':b.name,'solid':b.isSolid,'volume_mm3':b.volume*1000,'bounds':[[x*10 for x in b.boundingBox.minPoint.asArray()],[x*10 for x in b.boundingBox.maxPoint.asArray()]]}for b in o.bRepBodies]})
physical=[n for n in parts if n.startswith(('N06','T01','T02','T03','R01'))]
collisions=[];errors=[];tests=0
for i,an in enumerate(physical):
 for bn in physical[i+1:]:
  if not parts[an].boundingBox.intersects(parts[bn].boundingBox):continue
  for a in parts[an].bRepBodies:
   for b in parts[bn].bRepBodies:
    if not a.boundingBox.intersects(b.boundingBox):continue
    tests+=1
    try:
     cp=TM.copy(a);ok=TM.booleanOperation(cp,TM.copy(b),adsk.fusion.BooleanTypes.IntersectionBooleanType)
     if ok and cp.volume*1000>.01:collisions.append({'a':an+'/'+a.name,'b':bn+'/'+b.name,'volume_mm3':cp.volume*1000})
    except Exception as e:errors.append(str(e))
motor=parts['R01_DJI_10018_77KV_ESTIMATED_REFERENCE']
hub=next(b for b in motor.bRepBodies if b.name=='Rear_bearing_hub_EST')
rail=parts['N06_Upper_leg_oval_stub_R'].bRepBodies.item(0)
gap=(rail.boundingBox.minPoint.x-hub.boundingBox.maxPoint.x)*10
keep=TM.createCylinderOrCone(pt((33,23.343134,685)),1.4,pt((38,23.343134,685)),1.4)
keep_hits=[]
for n in physical:
 for b in parts[n].bRepBodies:
  if not b.boundingBox.intersects(keep.boundingBox):continue
  cp=TM.copy(b);ok=TM.booleanOperation(cp,TM.copy(keep),adsk.fusion.BooleanTypes.IntersectionBooleanType)
  if ok and cp.volume*1000>.001:keep_hits.append({'component':n,'body':b.name,'volume_mm3':cp.volume*1000})
result={'unchanged_input_components':len(preserved),'unexpected_changes':changes,'feature_warnings':warnings,'invalid_joints':[j.name for j in root.asBuiltJoints if not j.isValid],'interface_collision_tests':tests,'interface_collisions':collisions,'boolean_errors':errors,'encoder_axial_gap_mm':gap,'encoder_keepout_dia_mm':28,'encoder_keepout_intersections':keep_hits,'inventory':inventory}
(OUT/'layout_validation.json').write_text(json.dumps(result,indent=2))
result={k:v for k,v in result.items() if k!='inventory'}
