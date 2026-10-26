exec(compile((ROOT/'v21/common.py').read_text(),'<common>','exec'))
o=getpart(wg,'W05_');rows=[]
for b in o.component.bRepBodies:
 b.appearance=black if 'vendor' in b.name.lower() else plastic
 rows.append({'body':b.name,'bounds':bounds(b)})
b=next(b for b in o.component.bRepBodies if b.name.startswith('W05_'))
f=fillet_edges(o.component,b,2,lambda e:adsk.core.Line3D.cast(e.geometry) and abs(e.boundingBox.minPoint.z*10-916)<.01 and abs(e.boundingBox.maxPoint.z*10-916)<.01 and e.length*10>5,'V21_pin_support_finished_R2_roots')
result={'bodies':rows,'fillet_success':bool(f)}
