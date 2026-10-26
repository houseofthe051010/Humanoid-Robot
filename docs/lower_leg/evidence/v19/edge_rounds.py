exec(compile((ROOT/'v19/common.py').read_text(),'<v19 common>','exec'))
report=[]
for go in (right,left):
    for key in ('Q02_CNC_yaw_to_roll_cradle','Q03_CNC_roll_to_pitch_fork','H06_Roll_tube_recessed_endcaps','H07_Pitch_tube_recessed_endcaps'):
        c=parts(go)[key].component
        for index in range(c.bRepBodies.count):
            b=c.bRepBodies.item(index)
            # Round the exposed flange rims. Bearing and tube-register edges
            # are excluded, keeping their nominal cylindrical seat sizes.
            candidates=[]
            for e in b.edges:
                geom=adsk.core.Circle3D.cast(e.geometry)
                if geom and e.faces.count==2 and min(abs(geom.radius*10-r) for r in (30,33,57))<.001 and e.length*10>25:
                    if any(adsk.core.Plane.cast(f.geometry) for f in e.faces):candidates.append(e)
            success=False;errors=[]
            for radius in (.6,.3):
                try:
                    if not candidates:break
                    es=adsk.core.ObjectCollection.create()
                    for e in candidates:es.add(e)
                    inp=c.features.filletFeatures.createInput();inp.addConstantRadiusEdgeSet(es,adsk.core.ValueInput.createByReal(radius/10),False)
                    f=c.features.filletFeatures.add(inp);f.name='V19_exposed_rim_edge_rounds';success=True;break
                except Exception as e:errors.append(str(e))
            report.append({'part':go.component.name+'/'+key,'body':b.name,'candidates':len(candidates),'success':success,'errors':errors})
for key in ('W02_Waist_front_shell','W03_Waist_rear_shell'):
    c=wp[key].component;b=c.bRepBodies.item(0)
    candidates=[e for e in b.edges if e.faces.count==2 and any(adsk.core.NurbsSurface.cast(f.geometry) for f in e.faces) and any(adsk.core.Cylinder.cast(f.geometry) for f in e.faces) and e.length*10>20]
    ok=0
    for e in sorted(candidates,key=lambda ee:ee.length,reverse=True)[:4]:
        if not e.isValid:continue
        for r in (1.5,.7):
            try:
                es=adsk.core.ObjectCollection.create();es.add(e);inp=c.features.filletFeatures.createInput()
                inp.addConstantRadiusEdgeSet(es,adsk.core.ValueInput.createByReal(r/10),False)
                f=c.features.filletFeatures.add(inp);f.name='V19_waist_saddle_blend';ok+=1;break
            except:pass
    report.append({'part':key,'saddle_blends':ok})
(OUT/'edge_rounds.json').write_text(json.dumps(report,indent=2));result=report
