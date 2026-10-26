exec(compile((ROOT/'v19/common.py').read_text(),'<v19 common>','exec'))
progress('finish output clearance, thin internal endcap webs and smooth edge blends')
report={'removed_mm3':[],'fillets':[]}
for go,sg in ((right,1),(left,-1)):
    ps=parts(go)
    # Current new bodies use the exact inherited upper-leg frame, with X
    # translation applied once to the complete leg assembly.
    frame=ps['Q02_CNC_yaw_to_roll_cradle'].createForAssemblyContext(go).transform2.copy()
    # Remove the root-group translation from this frame; all tools below are
    # already defined at the final global hip centers.
    tr=frame.translation;tr.x+=sg;frame.translation=tr
    def placed(b):
        if sg<0:reflect(b)
        return transform(b,frame)
    def update(key,modify):
        o=ps[key];rows=[]
        for b in o.createForAssemblyContext(go).bRepBodies:
            shape=TM.copy(b);before=shape.volume*1000;modify(shape,b.name)
            rows.append((b.name,shape));report['removed_mm3'].append({'leg':go.component.name,'part':key,'body':b.name,'delta':before-shape.volume*1000})
        world_replace(go,o,rows,o.component.description,silver)
    def forkcut(b,n):sub(b,placed(rcyl(-48,42,34)))
    update('Q03_CNC_roll_to_pitch_fork',forkcut)
    def rollcapcut(b,n):
        side=-1 if n.endswith('_-1') else 1
        lo,hi=(-31,-23) if side<0 else (17,25)
        pocket=sub(rcyl(lo,hi,52.9),rcyl(lo-.01,hi+.01,35))
        for ang in (85,120,155):
            a=math.radians(ang);x=RX+45*math.cos(a);z=RZ+45*math.sin(a)
            sub(pocket,cy((x,Y+lo-1,z),(x,Y+hi+1,z),7.5))
        sub(b,placed(pocket))
    update('H06_Roll_tube_recessed_endcaps',rollcapcut)
    def pitchcapcut(b,n):
        if 'rear' in n:sub(b,placed(pcyl(-26,-22,50)))
        else:sub(b,placed(sub(pcyl(20,24,52.9),pcyl(19.9,24.1,29))))
    update('H07_Pitch_tube_recessed_endcaps',pitchcapcut)
    for key in ('Q02_CNC_yaw_to_roll_cradle','Q03_CNC_roll_to_pitch_fork','H06_Roll_tube_recessed_endcaps','H07_Pitch_tube_recessed_endcaps'):
        c=ps[key].component
        for b in list(c.bRepBodies):
            try:
                def pred(e):
                    return e.faces.count==2 and any(adsk.core.NurbsSurface.cast(f.geometry) for f in e.faces) and any(adsk.core.Plane.cast(f.geometry) for f in e.faces) and e.length*10>6
                f=fillet_edges(c,b,.8,pred,'V19_smooth_loft_intersection_edges')
                report['fillets'].append({'part':go.component.name+'/'+key,'body':b.name,'success':bool(f)})
            except Exception as e:report['fillets'].append({'part':go.component.name+'/'+key,'success':False,'error':str(e)})
(OUT/'refined_interfaces.json').write_text(json.dumps(report,indent=2));result=report
