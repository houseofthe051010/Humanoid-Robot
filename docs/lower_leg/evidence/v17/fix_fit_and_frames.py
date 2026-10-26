exec(compile((ROOT/'v17/common.py').read_text(),'<v17 common>','exec'))
report=[]
wa={o.component.partNumber.split('_')[0]:o for o in wg.component.occurrences}
progress('align physical gimbal geometry with the new native joint frames')
o=wa['W06'];c=o.component
assert not c.attributes.itemByName('V17','frame_baked')
m=o.createForAssemblyContext(wg).transform2.copy();m.invert()
replace(c,[(b.name+'_frame_corrected',transform(TM.copy(b),m)) for b in list(c.bRepBodies)],c.description,plastic)
c.attributes.add('V17','frame_baked','inverse occurrence rest transform')

# The inherited right upper-leg frame has a small nonzero transform. Bring new
# bearing/case references into that same frame without changing the user's leg.
ps=parts(right);frame=ps['Q02_CNC_yaw_to_roll_cradle'].createForAssemblyContext(right).transform2
for n in ('H01_Hip_roll_117OD_106ID_case','H02_Hip_pitch_roll_bearing_REFERENCES','H03_Hip_yaw_6007_bearing_REFERENCE','H04_Hip_yaw_bearing_retainer'):
    c=ps[n].component
    assert not c.attributes.itemByName('V17','frame_baked')
    replace(c,[(b.name,transform(TM.copy(b),frame)) for b in list(c.bRepBodies)],c.description)
    c.attributes.add('V17','frame_baked','inherited right upper-leg frame')
adsk.doEvents()

def world_replace(go,o,shape,label):
    inv=o.createForAssemblyContext(go).transform2.copy();inv.invert()
    c=o.component;replace(c,[(label,transform(shape,inv))],c.description)
def trim(go,target,cutters,label):
    o=parts(go)[target];p=o.createForAssemblyContext(go);shape=TM.copy(p.bRepBodies.item(0));before=shape.volume*1000
    for tool in cutters:
        if shape.boundingBox.intersects(tool.boundingBox):sub(shape,TM.copy(tool))
    after=shape.volume*1000;assert shape.isSolid and after>0
    world_replace(go,o,shape,label);report.append({'target':go.component.name+'/'+target,'trim_mm3':before-after})

progress('finish bearing seats and remove cradle-to-sleeve intersections')
for go in (right,left):
    ps={n:o.createForAssemblyContext(go) for n,o in parts(go).items()}
    case=list(ps['H01_Hip_roll_117OD_106ID_case'].bRepBodies)
    bearings=[b for b in ps['H02_Hip_pitch_roll_bearing_REFERENCES'].bRepBodies if b.name.startswith('roll')]
    trim(go,'Q02_CNC_yaw_to_roll_cradle',case+bearings,'Q02_v17_finished_saddle_and_seats')
    trim(go,'Q03_CNC_roll_to_pitch_fork',case,'Q03_v17_full_center_fork_clearanced')
    trim(go,'Q01_CNC_rail_to_yaw_crosshead',list(ps['H03_Hip_yaw_6007_bearing_REFERENCE'].bRepBodies),'Q01_v17_finished_6007_seat')

progress('finish shell relief against actual assembled output positions')
for key in ('W02','W03'):
    o=wa[key];shape=TM.copy(o.createForAssemblyContext(wg).bRepBodies.item(0));before=shape.volume*1000
    for go in (right,left):
        ps={n:o.createForAssemblyContext(go) for n,o in parts(go).items()}
        cutters=list(ps['Q03_CNC_roll_to_pitch_fork'].bRepBodies)
        cutters += [b for b in ps['T07_Hip_pitch_motor_ENVELOPE_REFERENCE'].bRepBodies if b.name.startswith(('Mount_boss','Rear_bearing_hub'))]
        for b in cutters:
            if shape.boundingBox.intersects(b.boundingBox):sub(shape,TM.copy(b))
    world_replace(wg,o,shape,key+'_v17_final_output_clearance')
    report.append({'target':key,'trim_mm3':before-shape.volume*1000})

for o in wg.component.occurrences:
    o.isLightBulbOn=True;o.createForAssemblyContext(wg).isLightBulbOn=True
    if hasattr(o.component,'isBodiesFolderLightBulbOn'):o.component.isBodiesFolderLightBulbOn=True
    for b in o.component.bRepBodies:b.isLightBulbOn=True
for o in root.occurrences:
    if o.component.name.startswith('ZZ_'):o.isLightBulbOn=False
adsk.doEvents();app.activeViewport.refresh()
(OUT/'fit_corrections.json').write_text(json.dumps(report,indent=2));result=report
