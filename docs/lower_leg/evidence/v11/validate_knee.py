ROOT=ROOT/'v11'
import adsk.core,adsk.fusion,math,json
doc=next(d for d in app.documents if d.name=='Leg_compact_shelled_v11');doc.activate()
d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'));root=d.rootComponent;tm=adsk.fusion.TemporaryBRepManager.get()
ocs={o.component.name:o for o in root.occurrences};j=root.asBuiltJoints.itemByName('Knee_pitch');p=adsk.core.Point3D.create(0,2.3343134,42.36)
moving=[n for n in ocs if n.startswith(('N04','N05','N06','N08','T0','T1','R01'))]
cache=[(n,b.name,tm.copy(b)) for n,o in ocs.items() if not n.startswith(('K01','U0','GIM','N00','T08','S04')) for b in o.component.bRepBodies]
out=[]
try:
    for angle in range(0,121,10):
        j.jointMotion.rotationValue=math.radians(angle);adsk.doEvents()
        m=ocs['N04_Knee_pillow_block_L'].transform2
        q=p.copy();q.transformBy(m);center_error=q.distanceTo(p)*10
        expected=adsk.core.Matrix3D.create();expected.setToRotation(math.radians(angle),adsk.core.Vector3D.create(1,0,0),p)
        transform_error=max(abs(a-b) for a,b in zip(m.asArray(),expected.asArray()))
        collisions=[];errors=[];tests=0;bodies=[]
        for name,bn,b in cache:
            cp=tm.copy(b)
            if name in moving:tm.transform(cp,m)
            bodies.append((name,bn,cp,cp.boundingBox))
        for i,(an,ab,a,abox) in enumerate(bodies):
            for bn,bb,b,bbox in bodies[i+1:]:
                if (an in moving)==(bn in moving) or not abox.intersects(bbox):continue
                pair=an+'/'+ab+'|'+bn+'/'+bb
                if 'N02_Knee_shaft_8mm' in pair and 'N04_' in pair and ('Inner & Outer Ring' in pair or 'Set Screw' in pair):continue
                tests+=1
                try:
                    cp=tm.copy(a);ok=tm.booleanOperation(cp,tm.copy(b),adsk.fusion.BooleanTypes.IntersectionBooleanType)
                    if ok and cp.volume*1000>.05:collisions.append({'a':an+'/'+ab,'b':bn+'/'+bb,'volume_mm3':cp.volume*1000})
                except Exception as e:errors.append(str(e))
        out.append({'command_deg':angle,'measured_deg':math.degrees(j.jointMotion.rotationValue),'axis_point_error_mm':center_error,'matrix_error':transform_error,'tested_pairs':tests,'collisions':collisions,'errors':errors})
        (ROOT/'knee_motion_validation.json').write_text(json.dumps(out,indent=2))
    j.jointMotion.rotationValue=math.radians(75);adsk.doEvents()
    vp=app.activeViewport;cam=vp.camera;cam.isSmoothTransition=False;cam.isFitView=True;cam.eye=adsk.core.Point3D.create(-75,95,85);cam.target=adsk.core.Point3D.create(0,0,35);cam.upVector=adsk.core.Vector3D.create(0,0,1);vp.camera=cam;vp.saveAsImageFile(str(ROOT/'knee_native_75deg.png'),1800,1400)
finally:j.jointMotion.rotationValue=0;adsk.doEvents()
result={'poses':len(out),'collision_poses':sum(bool(x['collisions']) for x in out),'error_poses':sum(bool(x['errors']) for x in out),'max_axis_error_mm':max(x['axis_point_error_mm'] for x in out),'max_matrix_error':max(x['matrix_error'] for x in out)}
(ROOT/'knee_motion_summary.json').write_text(json.dumps(result,indent=2))
