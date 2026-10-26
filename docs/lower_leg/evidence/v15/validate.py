exec(compile((ROOT/'v15/common.py').read_text(),'<common>','exec'))
report={'chain_analysis_performed':False,'legs':{},'waist':{}}
def overlap(a,b):
 if not a.boundingBox.intersects(b.boundingBox):return 0
 t=TM.copy(a);ix(t,TM.copy(b));return t.volume*1000
for go,sgn in groups():
 side=go.component.name;g=go.component
 parts={o.component.partNumber:o.createForAssemblyContext(go)for o in g.occurrences if o.isLightBulbOn}
 changes=[n for n in parts if n.startswith(('P05','P15','T07'))]
 hits=[];counts=0
 for n in changes:
  for m,o in parts.items():
   if n==m:continue
   for a in parts[n].bRepBodies:
    for b in o.bRepBodies:
     if not a.boundingBox.intersects(b.boundingBox):continue
     v=overlap(a,b);counts+=1
     if v>.01:hits.append({'a':n,'b':m,'body':b.name,'volume_mm3':v})
 probes=[]
 for pre,x,zvals,r in [('P15',51,[500,520,580,610,622],5.7),('P05',-51,[550,570,590,610,625],5.7)]:
  body=next(o for n,o in parts.items()if n.startswith(pre)).bRepBodies.item(0)
  for z in zvals:
   ring=sub(oval(x,z,z+.1,r),oval(x,z-.1,z+.2,5.2));place(ring,sgn);sub(ring,TM.copy(body));probes.append({'part':pre,'z':z,'missing_enclosure_mm3':ring.volume*1000})
 j=g.asBuiltJoints.itemByName(side.removesuffix('_leg')+'_Knee_pitch').createForAssemblyContext(go);motion=[]
 try:
  for angle in [0,30]:
   j.jointMotion.rotationValue=math.radians(angle);adsk.doEvents();m=parts['N04_Knee_pillow_block_L'].transform2
   errs={n:max(abs(a-b)for a,b in zip(m.asArray(),parts[n].transform2.asArray()))for n in changes}
   motion.append({'angle':angle,'follow_errors':errs})
 finally:j.jointMotion.rotationValue=0;adsk.doEvents()
 report['legs'][side]={'target_intersections_tested':counts,'overlaps':hits,'slide_enclosure':probes,'native_joint_count':g.asBuiltJoints.count,'invalid_joints':[j.name for j in g.asBuiltJoints if not j.isValid],'knee_motion':motion,'changed_bodies':[{'part':n,'solid':b.isSolid,'shells':b.shells.count,'volume':b.volume*1000}for n in changes for b in parts[n].bRepBodies]}
wg=next(o for o in root.occurrences if o.component.name=='Waist_layout_v15')
wp={o.component.name:o.createForAssemblyContext(wg)for o in wg.component.occurrences}
shells=[o for n,o in wp.items()if n.startswith(('W02','W03'))]
targets=[(n,b)for n,o in wp.items()if n.startswith('W01')for b in o.bRepBodies]
for go,sg in groups():
 for o in go.component.occurrences:
  if o.isLightBulbOn:
   for b in o.createForAssemblyContext(go).bRepBodies:targets.append((go.component.name+'/'+o.component.partNumber,b))
hits=[]
for o in shells:
 for a in o.bRepBodies:
  for n,b in targets:
   v=overlap(a,b)
   if v>.01:hits.append({'shell':o.component.name,'part':n,'body':b.name,'volume_mm3':v})
report['waist']={'overlaps':hits,'shells':[{'name':o.component.name,'solid':b.isSolid,'shell_count':b.shells.count,'volume_mm3':b.volume*1000}for o in shells for b in o.bRepBodies],'seam_overlap_mm3':sum(overlap(a,b)for a in shells[0].bRepBodies for b in shells[1].bRepBodies)}
pitch=[next(o for o in go.component.occurrences if o.component.partNumber.startswith('T07')).createForAssemblyContext(go).bRepBodies.item(0)for go,sg in groups()]
report['opposing_pitch_motor_overlap_mm3']=overlap(*pitch)
report['feature_issues']=[{'component':c.name,'feature':f.name,'message':f.errorOrWarningMessage}for c in d.allComponents for f in c.features if f.healthState!=adsk.fusion.FeatureHealthStates.HealthyFeatureHealthState]
(OUT/'validation.json').write_text(json.dumps(report,indent=2))
assert not report['feature_issues'] and not report['waist']['overlaps']
assert report['waist']['seam_overlap_mm3']<.001 and report['opposing_pitch_motor_overlap_mm3']<.001
assert all(s['shell_count']==1 and s['solid'] for s in report['waist']['shells'])
for r in report['legs'].values():
 assert not r['overlaps'] and not r['invalid_joints']
 assert max(p['missing_enclosure_mm3']for p in r['slide_enclosure'])<.001
 assert all(b['solid'] and b['shells']==1 and b['volume']>0 for b in r['changed_bodies'])
 assert all(max(m['follow_errors'].values())<1e-6 for m in r['knee_motion'])
result=report
