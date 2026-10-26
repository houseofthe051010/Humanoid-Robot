exec(compile((ROOT/'v13/common.py').read_text(),'<common>','exec'))
V=adsk.core.ValueInput;OP=adsk.fusion.FeatureOperations
# Reuse only the tested sketch/extrude helpers; no build entrypoint.
src=(ROOT/'v7/build_shin.py').read_text();hs=dict(globals());exec(compile(src[src.index('def pt('):src.index('for n,v,unit,desc')],'<sketch_helpers>','exec'),hs)
name='V13_Chain_clearance_ENVELOPE'
if name not in parts or parts[name].component.bRepBodies.count==0:
 if name in parts:
  parts[name].deleteMe();del parts[name]
 co=root.occurrences.addNewComponent(adsk.core.Matrix3D.create());co.component.name=name;co.component.partNumber=name;parts[name]=co
 c=co.component;c.description='Hidden22mm-wide,12.2mm-high #40H chain swept-envelope reference. Not individual chain links; slack, connector projection and tensioner deferred.';c.attributes.add('SHIN','material','clearance reference, not BOM hardware')
 sk=hs['sketch'](c,'x',CHAIN_X-11,'Chain_envelope_section')
 hs['hull'](sk,'x',CHAIN_X-11,(Y,K),(Y,Z),32.55+6.1,16.595+6.1)
 hs['hull'](sk,'x',CHAIN_X-11,(Y,K),(Y,Z),32.55-6.1,16.595-6.1)
 region=next(p for p in sk.profiles if p.profileLoops.count==2)
 ei=c.features.extrudeFeatures.createInput(region,OP.NewBodyFeatureOperation);ei.setDistanceExtent(False,V.createByReal(2.2));c.features.extrudeFeatures.add(ei).name='Chain_sideplate_and_pin_allowance';sk.isLightBulbOn=False
 co.isLightBulbOn=False
env=TM.copy(parts[name].component.bRepBodies.item(0))
def overlap(a,b):
 aa=a.boundingBox;bb=b.boundingBox
 if any(aa.maxPoint.asArray()[i]<bb.minPoint.asArray()[i]-1e-8 or bb.maxPoint.asArray()[i]<aa.minPoint.asArray()[i]-1e-8 for i in range(3)):return 0.
 z=TM.copy(a);assert TM.booleanOperation(z,TM.copy(b),BT.IntersectionBooleanType)
 return z.volume*1000 if z.isSolid else 0.
report={'chain_envelope_mm':{'width':22,'plate_height':12.2,'centre_distance':Z-K,'plane_x':CHAIN_X},'chain_interferences':[],'interface_interferences':[],'errors':[],'solids':[]}
progress('chain sweep clearance audit')
for n,o in parts.items():
 if not o.isLightBulbOn or n.startswith(('N03','P07','V13')):continue
 for b in o.component.bRepBodies:
  if not b.isLightBulbOn:continue
  try:
   v=overlap(env,b)
   if v>.01:report['chain_interferences'].append({'part':n,'body':b.name,'mm3':v})
  except Exception as e:report['errors'].append({'part':n,'error':str(e)})
progress('motor and knee interface audit')
newnames=[n for n in parts if n.startswith(('P','N01','N02','N03','N04','N06','N09','N10','S05'))and parts[n].isLightBulbOn]
others=[n for n in parts if parts[n].isLightBulbOn and not n.startswith('V13')]
checked=set();tests=0
for n in newnames:
 for m in others:
  pair=tuple(sorted([n,m]))
  if n==m or pair in checked:continue
  checked.add(pair)
  # Retained lower-leg contacts are outside this revision's interface scope.
  if n.startswith('S05')and not m.startswith(('N','P')):continue
  if n.startswith('N06')and not m.startswith(('N','P','Q','R','T')):continue
  for a in parts[n].component.bRepBodies:
   for b in parts[m].component.bRepBodies:
    try:
     v=overlap(a,b);tests+=1
     if v>.05:report['interface_interferences'].append({'one':n,'body1':a.name,'two':m,'body2':b.name,'mm3':v})
    except Exception as e:report['errors'].append({'one':n,'two':m,'error':str(e)})
report['pair_body_tests']=tests
for n,o in parts.items():
 if o.isLightBulbOn:
  for b in o.component.bRepBodies:
   if not b.isSolid or b.volume<=0:report['solids'].append(n+'/'+b.name)
(OUT/'fit_validation.json').write_text(json.dumps(report,indent=2))
assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(OUT/'v13_layout_checkpoint.f3d')))
result={k:v for k,v in report.items()if k not in ['interface_interferences']};result['interface_interference_count']=len(report['interface_interferences'])
