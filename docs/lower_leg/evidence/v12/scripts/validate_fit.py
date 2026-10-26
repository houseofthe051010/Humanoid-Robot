exec(compile((ROOT/'v12/common.py').read_text(),'<common>','exec'))
progress('measure interfaces and check clearances')
before=json.loads((OUT/'live_inventory.json').read_text())[0]
preserved=[];changed=[]
for row in before['components']:
 n=row['name']
 if n.startswith(('N06','T10','T11','T12')):continue
 bs=list(parts[n].bRepBodies);err=0
 if len(bs)!=len(row['bodies']):err=1e10
 else:
  for b,old in zip(bs,row['bodies']):
   err=max(err,abs(b.volume*1000-old['volume_mm3']))
   for vals,orig in zip([b.boundingBox.minPoint.asArray(),b.boundingBox.maxPoint.asArray()],old['bounds']):err=max(err,max(abs(x*10-y)for x,y in zip(vals,orig)))
 (preserved if err<1e-4 else changed).append({'component':n,'max_delta':err})
inventory=[];warnings=[];zero=[]
for c in [root]+[o.component for o in root.occurrences]:
 for f in c.features:
  if f.healthState!=adsk.fusion.FeatureHealthStates.HealthyFeatureHealthState:warnings.append({'component':c.name,'feature':f.name,'message':f.errorOrWarningMessage})
for n,o in parts.items():
 bs=[b for b in o.bRepBodies if b.isLightBulbOn]
 if o.isLightBulbOn:
  inventory.append({'component':n,'description':o.component.description,'grounded':o.isGrounded,'transform':o.transform2.asArray(),'bodies':[{'name':b.name,'volume_mm3':b.volume*1000,'bounds':[[x*10 for x in b.boundingBox.minPoint.asArray()],[x*10 for x in b.boundingBox.maxPoint.asArray()]]}for b in bs]})
  zero.extend(n+'/'+b.name for b in bs if not b.isSolid or b.volume<1e-8)
cache={n:[(b.name,TM.copy(b)) for b in o.bRepBodies if b.isLightBulbOn] for n,o in parts.items()if o.isLightBulbOn}
hits=[];errors=[];tests=0;done=set()
for an in [n for n in cache if n.startswith(('P','Q'))]:
 for bn in cache:
  if an==bn or tuple(sorted([an,bn]))in done:continue
  done.add(tuple(sorted([an,bn])))
  for ab,a in cache[an]:
   for bb,b in cache[bn]:
    if not a.boundingBox.intersects(b.boundingBox):continue
    tests+=1
    try:
     cp=TM.copy(a);ok=TM.booleanOperation(cp,TM.copy(b),adsk.fusion.BooleanTypes.IntersectionBooleanType)
     if ok and cp.volume*1000>.02:hits.append({'a':an+'/'+ab,'b':bn+'/'+bb,'volume_mm3':cp.volume*1000})
    except Exception as e:errors.append({'a':an,'b':bn,'error':str(e)})
joints=[]
for j in root.asBuiltJoints:
 m=j.jointMotion;typ=m.jointType;r={'name':j.name,'one':j.occurrenceOne.component.name,'two':j.occurrenceTwo.component.name,'type':int(typ),'suppressed':j.isSuppressed,'valid':j.isValid}
 if typ!=0:
  r['transform']=j.transform.asArray()
  if typ==1:
   r['axis']=m.rotationAxisVector.asArray();r['value']=m.rotationValue
   r['limits']={'min':m.rotationLimits.minimumValue,'max':m.rotationLimits.maximumValue,'min_on':m.rotationLimits.isMinimumValueEnabled,'max_on':m.rotationLimits.isMaximumValueEnabled}
 joints.append(r)
(OUT/'joint_inventory.json').write_text(json.dumps(joints,indent=2))
result={'unchanged_components':len(preserved),'unexpected_changes':changed,'zero_or_nonsolid':zero,'feature_warnings':warnings,'interface_tests':tests,'interferences':hits,'boolean_errors':errors,'invalid_joints':[r for r in joints if not r['valid']],'inventory':inventory}
(OUT/'fit_validation.json').write_text(json.dumps(result,indent=2));result={k:v for k,v in result.items()if k!='inventory'}
vp=app.activeViewport;cam=vp.camera;cam.isSmoothTransition=False;cam.cameraType=adsk.core.CameraTypes.OrthographicCameraType;cam.eye=pt((-500,800,850));cam.target=pt((0,20,600));cam.upVector=V3.create(0,0,1);cam.setExtents(45,45);vp.camera=cam;vp.refresh();adsk.doEvents()
vp.saveAsImageFile(str(OUT/'single_leg_interfaces.png'),1500,1500)
