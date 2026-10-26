import adsk.core, adsk.fusion, json
out={}
for doc in app.documents:
 if doc.name not in ['Bilateral_legs_v12','Legs_gearbox_hip_v12']: continue
 d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'))
 vals=[]
 for o in d.rootComponent.allOccurrences:
  if not o.component.name.endswith('P07_Motor_output_sprocket_BLANK'): continue
  for b in o.component.bRepBodies:
   ap=b.appearance
   props=[]
   for p in ap.appearanceProperties:
    item={'id':p.id,'name':p.name,'type':p.objectType}
    cp=adsk.core.ColorProperty.cast(p)
    if cp:
     v=cp.value;item['color']=[v.red,v.green,v.blue,v.opacity]
    props.append(item)
   vals.append({'component':o.component.name,'body':b.name,'appearance':ap.name,'properties':props})
 out[doc.name]=vals
(ROOT/'v12'/'appearance_probe.json').write_text(json.dumps(out,indent=2))
result=out
