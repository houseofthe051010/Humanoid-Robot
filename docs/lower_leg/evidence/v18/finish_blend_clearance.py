exec(compile((ROOT/'v18/common.py').read_text(),'<v18 common>','exec'))
result=[]
for go in (right,left):
    ps=parts(go);o=ps['Q03_CNC_roll_to_pitch_fork'];p=o.createForAssemblyContext(go)
    shape=TM.copy(p.bRepBodies.item(0))
    h=ps['H05_DJI10018_pitch_gearbox_shell_ESTIMATE'].createForAssemblyContext(go)
    for b in h.bRepBodies:sub(shape,TM.copy(b))
    assert shape.isSolid and shape.volume>0 and sum(not s.isVoid for s in shape.shells)==1
    inv=p.transform2.copy();inv.invert();transform(shape,inv)
    replace(o.component,[('Q03_v18_blended_fork_fitted_to_estimated_shell',shape)],o.component.description,silver)
    result.append({'leg':go.component.name,'connected_solid':True,'estimated_shell_retained':True})
(OUT/'blend_clearance.json').write_text(json.dumps(result,indent=2))
