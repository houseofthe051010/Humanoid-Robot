exec(compile((ROOT/'v15/common.py').read_text(),'<common>','exec'))
fixes=[]
for go,sg in groups():
 ps={o.component.partNumber:o.component for o in go.component.occurrences}
 c=ps['P15_Separate_motor_backplate_and_rail_saddles'];b=TM.copy(c.bRepBodies.item(0))
 # Old clamp screw blind pockets became sealed voids after the sleeve union.
 fs=[f for s in b.shells if s.isVoid for f in s.faces]
 if fs:assert TM.deleteFaces(fs,True)
 for dy in [-3,0,3]:sub(b,place(cy((36,Y+dy,524),(43,Y+dy,496),1.85),sg))
 assert b.isSolid and sum(not s.isVoid for s in b.shells)==1
 replace(c,b,'V15_rear_slide_sleeve_with_phase_wire_channels')
 fixes.append({'part':c.name,'filled_obsolete_internal_pocket_faces':len(fs),'wire_channels':3,'shells':b.shells.count})
 c=ps['P05_Gearbox_front_cover'];b=TM.copy(c.bRepBodies.item(0))
 # Remove the old rectangular bridge lip above the curved end section.
 sub(b,place(bx((-12,Y-16,619),(-7,Y+16,639)),sg))
 assert b.isSolid and sum(not s.isVoid for s in b.shells)==1
 replace(c,b,'V15_upper_half_cradle_slide_sleeve_finished')
wg=next(o for o in root.occurrences if o.component.name=='Waist_layout_v15')
for o in wg.component.occurrences:
 c=o.component
 if not c.name.startswith(('W02','W03')):continue
 b=TM.copy(c.bRepBodies.item(0));ss=list(b.shells);main=max(ss,key=lambda s:s.faces.count)
 # Retain the continuous shell and remove detached slivers left by fork cuts.
 assert TM.deleteFaces(list(main.faces),False)
 assert b.isSolid and b.shells.count==1 and b.volume>0
 replace(c,b,c.name+'_continuous')
 fixes.append({'part':c.name,'shells_before':len(ss),'shells_after':b.shells.count,'volume_mm3':b.volume*1000})
(OUT/'finish_geometry.json').write_text(json.dumps(fixes,indent=2));result=fixes
