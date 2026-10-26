exec(compile((ROOT/'v32/common32.py').read_text(),'<common32>','exec'))
exec(compile((OUT/'capture32.py').read_text(),'<capture32>','exec'))
assert json.loads((OUT/'pose_invariants32.json').read_text())['pass_']
assert json.loads((OUT/'native_cover_motion32.json').read_text())['pass_']
assert json.loads((OUT/'clearance_checks32.json').read_text())['all_sampled_clear']
d.activateRootComponent();exact('Casings').isLightBulbOn=True
root.attributes.add('Robot','revision','v32 shallow perforated shin plates and compact oval-rail hip collars; v31 waist/mechanism and frozen v29 training retained')
photos={}
photos['front']=save_view('robot_v32_front',(0,28,810),(0,-4200,810),1730)
photos['threequarter']=save_view('robot_v32_threequarter',(0,28,810),(2300,-4200,1950),1730)
photos['shin']=save_view('robot_v32_shin_plates',(0,20,250),(1450,-3100,1050),510)
photos['shin_rear']=save_view('robot_v32_open_shin_rear',(0,20,245),(1450,3100,950),510)
photos['hip']=save_view('robot_v32_hip_collars',(0,23,710),(1250,-2600,1280),480)
exact('Casings').isLightBulbOn=False
photos['bare']=save_view('robot_v32_casings_off',(0,28,810),(2300,-4200,1950),1730)
exact('Casings').isLightBulbOn=True
save_view('robot_v32_threequarter',(0,28,810),(2300,-4200,1950),1730)
assert doc.save('V32: thin perforated front shin plates on existing carrier bores and rail saddles; open sides/rear. Compact split hip collars around original oval rails/crosshead. V31 waist and all motor/joint placements retained.')
inventory=capture(d);assert inventory['anatomical_count']==23 and inventory['visible_meshes']==8
journal('final_native_inventory32',inventory)
deliver=OUT/'deliverables';deliver.mkdir(exist_ok=True)
archive=deliver/'Humanoid_complete_v32.f3d';assert not archive.exists()
assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(archive)))
steps=deliver/'modified_parts_STEP';steps.mkdir(exist_ok=True);paths=[]
for f in ('shin_plates32','hip_collars32'):
 for row in json.loads((OUT/(f+'.json')).read_text()):
  name=row['part'];path=steps/(name+'.step')
  assert d.exportManager.execute(d.exportManager.createSTEPExportOptions(str(path),exact(name).component));paths.append(str(path))
result=dict(document=doc.name,datafile_id=doc.dataFile.id,version=doc.dataFile.versionNumber,archive=str(archive),bytes=archive.stat().st_size,photos=photos,step_parts=paths,epoch=time.time(),joints=len(inventory['joints']),body_axes=inventory['anatomical_count'],height_mm=inventory['height_mm'])
journal('saved_release32',result)
