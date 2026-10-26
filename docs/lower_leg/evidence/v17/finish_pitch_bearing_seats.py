exec(compile((ROOT/'v17/common.py').read_text(),'<v17 common>','exec'))
tools_world=[]
for go in (right,left):
    o=parts(go)['H02_Hip_pitch_roll_bearing_REFERENCES'].createForAssemblyContext(go)
    tools_world.extend([b for b in o.bRepBodies if b.name.startswith('pitch')])
report=[]
for key in ('W02_Waist_front_shell','W03_Waist_rear_shell'):
    o=wp[key];p=o.createForAssemblyContext(wg);shape=TM.copy(p.bRepBodies.item(0));before=shape.volume*1000
    for b in tools_world:
        if shape.boundingBox.intersects(b.boundingBox):sub(shape,TM.copy(b))
    inv=p.transform2.copy();inv.invert();transform(shape,inv)
    replace(o.component,[(key+'_v17_finished_bearing_seats',shape)],o.component.description,plastic)
    report.append({'part':key,'trim_mm3':before-shape.volume*1000})
wg.isLightBulbOn=True
for o in wg.component.occurrences:o.isLightBulbOn=True;o.createForAssemblyContext(wg).isLightBulbOn=True
(OUT/'pitch_bearing_seat_finish.json').write_text(json.dumps(report,indent=2));result=report
