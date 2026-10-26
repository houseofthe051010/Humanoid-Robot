exec(compile((ROOT/'v19/common.py').read_text(),'<common>','exec'))
o=getpart(wg,'W07_');ppp=o.createForAssemblyContext(wg);sh=TM.copy(ppp.bRepBodies.item(0))
before=sh.volume*1000;old=TM.copy(sh)
sub(sh,oval(0,Y+10,981,1012,5.15,4))
for z in (993,1004):
 sub(sh,cy((-18,Y+10,z),(18,Y+10,z),2.15))
 sub(sh,cy((-18,Y+10,z),(-10.8,Y+10,z),3.75))
 sub(sh,cy((10.8,Y+10,z),(18,Y+10,z),3.75))
after=sh.volume*1000
world_replace(wg,o,[('W07_6010_carrier_clear_spine_and_crossbolts',sh)],o.component.description+' Spine bore and retention-head access are re-cut after carrier union.',plastic)
result={'carrier_bore_and_head_relief_volume_mm3':before-after};(OUT/'carrier_socket_relief.json').write_text(json.dumps(result,indent=2))
exec(compile((OUT/'validate_new_drive.py').read_text(),'<complete waist adjacent-parts check>','exec'))
