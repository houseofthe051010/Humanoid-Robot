exec(compile((ROOT/'v12/common.py').read_text(),'<common>','exec'))
n='Q03_CNC_roll_to_pitch_fork';c=parts[n].component;Y=23.343134;u=(math.cos(math.radians(25)),0,-math.sin(math.radians(25)))
along=lambda t:(-78+t*u[0],Y,803.6+t*u[2])
cuttemp(c,c.bRepBodies.item(0),TM.createCylinderOrCone(pt(along(-22)),5.05,pt(along(20.02)),5.05),'Finish_pitch_front_face_relief_0p02')
assert c.bRepBodies.count==1 and c.bRepBodies.item(0).volume>0
report=json.loads((OUT/'fit_validation.json').read_text());report['interferences']=[h for h in report['interferences']if not h['a'].startswith(n+'/')and not h['b'].startswith(n+'/')]
tests=0
for bn,o in parts.items():
 if bn==n or not o.isLightBulbOn:continue
 for a in parts[n].bRepBodies:
  for b in o.bRepBodies:
   if not b.isLightBulbOn or not a.boundingBox.intersects(b.boundingBox):continue
   tests+=1;cp=TM.copy(a);ok=TM.booleanOperation(cp,TM.copy(b),adsk.fusion.BooleanTypes.IntersectionBooleanType)
   if ok and cp.volume*1000>.02:report['interferences'].append({'a':n+'/'+a.name,'b':bn+'/'+b.name,'volume_mm3':cp.volume*1000})
for f in c.features:
 if f.healthState!=adsk.fusion.FeatureHealthStates.HealthyFeatureHealthState:report['feature_warnings'].append({'component':n,'feature':f.name,'message':f.errorOrWarningMessage})
report['interface_tests']+=tests;report['final_subtractive_relief']='Q03 front face extended from19.95 to20.02mm; Q03 intersections rechecked after subtractive-only change. Other interface checks unchanged.'
for row in report['inventory']:
 if row['component']==n:row['bodies']=[{'name':b.name,'volume_mm3':b.volume*1000,'bounds':[[v*10 for v in b.boundingBox.minPoint.asArray()],[v*10 for v in b.boundingBox.maxPoint.asArray()]]}for b in parts[n].bRepBodies]
(OUT/'fit_validation.json').write_text(json.dumps(report,indent=2));result={k:v for k,v in report.items()if k!='inventory'}
