exec(compile((ROOT/'v21/common.py').read_text(),'<common>','exec'))
s=(OUT/'clear_base_pin_supports.py').read_text().split('world_replace(wg,o,')[0]
exec(compile(s,'<base rebuild>','exec'))
rep={'expected':bounds(base),'transforms':[]}
o.isGroundToParent=True
old=list(o.component.bRepBodies)
for q in old:o.component.features.removeFeatures.add(q)
rep['transforms'].append(list(o.transform2.asArray()))
for name,shape in [('GWK7010_vendor_output_MOVING',TM.copy(vendor)),('W05_lower_pitch_base_with_30deg_rod_clearance',base)]:
 rep['transforms'].append(list(o.transform2.asArray()))
 nb=add(o.component,shape,name,black if 'vendor' in name.lower() else plastic)
 rep[name]={'source':bounds(shape),'native':bounds(nb),'transform':list(o.transform2.asArray())}
o.isGroundToParent=False
adsk.doEvents()
rep['final']=[{'name':b.name,'bounds':bounds(b)} for b in o.createForAssemblyContext(wg).bRepBodies]
(OUT/'base_rebuild.json').write_text(json.dumps(rep,indent=2));result=rep
