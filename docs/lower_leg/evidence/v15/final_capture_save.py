exec(compile((ROOT/'v15/inspect_capture.py').read_text(),'<capture>','exec'))
r=json.loads((OUT/'validation.json').read_text())
for go,sg in groups():
 c=next(o.component for o in go.component.occurrences if o.component.partNumber=='P05_Gearbox_front_cover');b=c.bRepBodies.item(0)
 for row in r['legs'][go.component.name]['changed_bodies']:
  if row['part']==c.partNumber:row.update(solid=b.isSolid,shells=b.shells.count,volume=b.volume*1000)
 # Final lip removal is confined to the case-side end, remote from sleeve.
 for z in [550,570,590,610,625]:
  ring=sub(oval(-51,z,z+.1,5.7),oval(-51,z-.1,z+.2,5.2));place(ring,sg);sub(ring,TM.copy(b));assert ring.volume*1000<.001
 assert b.isSolid and b.shells.count==1
r['final_lip_cleanup']='Removed only case-side rectangular bridge remnants at canonicalX -12..-7 andZ619..639. Single closed shell and all front sleeve sections rechecked. Removing this material cannot introduce new overlaps; component identities and native joints retained.'
(OUT/'validation.json').write_text(json.dumps(r,indent=2))
exec(compile((ROOT/'v15/save_native.py').read_text(),'<save>','exec'))
