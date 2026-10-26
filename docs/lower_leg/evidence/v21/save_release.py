exec(compile((ROOT/'v21/common.py').read_text(),'<common>','exec'))
dest=OUT/'deliverables';dest.mkdir(exist_ok=True)
val=json.loads((OUT/'validation.json').read_text());assert val['pass']
neutral=json.loads((OUT/'waist_neutral_check.json').read_text());assert not neutral['hits'],neutral['hits']
report={'files':[],'retired_groups':[]}
def export(path,opt):
 assert d.exportManager.execute(opt)
 report['files'].append({'path':str(path),'bytes':path.stat().st_size})
# The compact, independently reopenable waist assembly includes native joints,
# the battery and all editable upper-body placement sketches.
p=dest/'Waist_battery_v21.f3d';export(p,d.exportManager.createFusionArchiveExportOptions(str(p),wg.component))
p=dest/'Battery_12S3P_21700_140x85x160.step';export(p,d.exportManager.createSTEPExportOptions(str(p),getpart(wg,'U01_').component))
for o in list(root.occurrences):
 if o.component.name=='ZZ_V21_preserved_prior_waist_history' or 'GWK6010-8 3D Model' in o.component.name:
  name=o.component.name
  try:
   f=root.features.removeFeatures.add(o);f.name='V21_remove_superseded_'+name;report['retired_groups'].append({'name':name,'removed':True})
  except Exception as e:
   o.isLightBulbOn=False;report['retired_groups'].append({'name':name,'removed':False,'error':str(e)})
p=dest/'Humanoid_waist_battery_v21.f3d';export(p,d.exportManager.createFusionArchiveExportOptions(str(p)))
for sk in getpart(wg,'U06_').component.sketches:
 p=dest/(sk.name+'.dxf')
 try:
  assert sk.saveAsDXF(str(p));report['files'].append({'path':str(p),'bytes':p.stat().st_size})
 except Exception as e:report['files'].append({'path':str(p),'error':str(e)})
(OUT/'saved_release.json').write_text(json.dumps(report,indent=2));result=report
