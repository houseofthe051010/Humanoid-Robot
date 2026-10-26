exec(compile((ROOT/'v21/common.py').read_text(),'<common>','exec'))
o=getpart(wg,'W07_');shape=TM.copy(o.createForAssemblyContext(wg).bRepBodies.item(0));holes=[]
for s,key in ((-1,'W19_'),(1,'W20_')):
 xa,xb=sorted((s*46.5,s*48.1))
 ledge=sub(cy((xa,Y,995),(xb,Y,995),25.3),cy((xa,Y,995),(xb,Y,995),17.3))
 for b in getpart(wg,key).createForAssemblyContext(wg).bRepBodies:
  for f in b.faces:
   c=adsk.core.Cylinder.cast(f.geometry)
   if c and abs(c.radius*10-1.0065)<.001:
    y,z=c.origin.y*10,c.origin.z*10;sub(ledge,cy((xa-1,y,z),(xb+1,y,z),1.4));holes.append([s,y,z])
 un(shape,ledge)
world_replace(wg,o,[('W07_upper_roll_curved_GWK_carriers_stepped_bore',shape)],o.component.description+' Stepped bore 34.6 mm front / 37.3 mm rear supports the small exposed-flange bolt circle while clearing output rotation.',plastic)
rounds=[]
o=getpart(wg,'W05_');b=next(b for b in o.component.bRepBodies if b.name.startswith('W05_'))
try:
 f=fillet_edges(o.component,b,2,lambda e:adsk.core.Line3D.cast(e.geometry) and abs(e.boundingBox.minPoint.z*10-916)<.01 and abs(e.boundingBox.maxPoint.z*10-916)<.01 and e.length*10>5,'V21_pitch_support_root_R2')
 rounds.append({'part':'W05','radius_mm':2,'success':bool(f)})
except Exception as e:rounds.append({'part':'W05','error':str(e)})
(OUT/'carrier_detail.json').write_text(json.dumps({'holes':holes,'rounds':rounds},indent=2));result={'mount_holes':len(holes),'rounds':rounds}
