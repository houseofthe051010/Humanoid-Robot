exec(compile((ROOT/'v17/common.py').read_text(),'<v17 common>','exec'))
wc=wg.component
assert wc.asBuiltJoints.count==0
progress('import two actual standard GIM6010-8 reference motors')
path=r'C:\Users\rshan\Downloads\Planetary-Reduction-Motor\Planetary Reduction Motor\GIM6010-8\GIM6010-8\GIM6010-8  3D Model-Standard Version.stp'
source=app.importManager.importToNewDocument(app.importManager.createSTEPImportOptions(path));assert source
sd=adsk.fusion.Design.cast(app.activeProduct);sr=sd.rootComponent
src=list(sr.bRepBodies)
for o in sr.allOccurrences:src.extend(list(o.bRepBodies))
assert len(src)>=2
copies=[TM.copy(b) for b in src]
source.close(False);doc.activate()
for number,sg in ((19,-1),(20,1)):
    o=newpart(wc,f'W{number}_GIM6010_8_floating_REFERENCE',
              'Actual imported GIM6010-8 standard-version STEP. Floating reference near the spine; no differential crank, rods, brackets or actuator sizing implemented.','purchased motor reference')
    m=basis((sg*62,Y,1040),(sg,0,0),(0,sg,0),(0,0,1))
    for i,b in enumerate(copies):add(o.component,transform(TM.copy(b),m),f'GIM6010_vendor_solid_{i}',black if i==0 else silver)

# Each through-bolt must follow its own pin, not both axes as one rigid part.
w17=next(o for o in wc.occurrences if o.component.partNumber.startswith('W17_'))
upper=next(b for b in w17.component.bRepBodies if 'pitch' in b.name)
w18=newpart(wc,'W18_M3_upper_pitch_pin_reinforcement_REFERENCE','M3 through reinforcement reference for the upper pitch pin.','steel hardware reference')
add(w18.component,TM.copy(upper),upper.name,upper.appearance)
w17.component.features.removeFeatures.add(upper)
ps={o.component.partNumber:o for o in wc.occurrences}
def prefix(n):return next(o for p,o in ps.items() if p.startswith(n+'_'))
for n,o in ps.items():o.isGroundToParent=n.startswith(('W01_','W02_','W03_','W04_'))
def rev(name,a,b,axis,origin):
    base={'x':wc.yZConstructionPlane,'y':wc.xZConstructionPlane,'z':wc.xYConstructionPlane}[axis];idx={'x':0,'y':1,'z':2}[axis]
    pi=wc.constructionPlanes.createInput();pi.setByOffset(base,adsk.core.ValueInput.createByReal(origin[idx]/10*base.geometry.normal.asArray()[idx]));pl=wc.constructionPlanes.add(pi);pl.isLightBulbOn=False
    sk=wc.sketches.add(pl);sk.name=name+'_axis';sk.isLightBulbOn=False
    tip=list(origin);tip[idx]+=10
    ln=sk.sketchCurves.sketchLines.addByTwoPoints(sk.modelToSketchSpace(pt(origin)),sk.modelToSketchSpace(pt(tip)))
    geom=adsk.fusion.JointGeometry.createByCurve(ln,adsk.fusion.JointKeyPointTypes.StartKeyPoint)
    ji=wc.asBuiltJoints.createInput(prefix(a),prefix(b),geom);ji.setAsRevoluteJointMotion(adsk.fusion.JointDirections.ZAxisJointDirection)
    j=wc.asBuiltJoints.add(ji);j.name=name;j.isLightBulbOn=False
    if axis!='z':
        limits=j.jointMotion.rotationLimits;limits.isMinimumValueEnabled=True;limits.minimumValue=math.radians(-30);limits.isMaximumValueEnabled=True;limits.maximumValue=math.radians(30)
    return j
rev('WJ00_waist_yaw','W01','W05','z',(0,Y,899))
rev('WJ01_lower_waist_roll','W05','W06','y',(0,Y+10,927))
rev('WJ02_upper_waist_pitch','W06','W07','x',(0,Y+10,954))
for i,(a,b) in enumerate((('W07','W08'),('W06','W09'),('W05','W10'),('W07','W11'),('W06','W12'),('W04','W13'),('W04','W14'),('W05','W15'),('W07','W16'),('W05','W17'),('W06','W18'),('W07','W19'),('W07','W20')),3):
    rigid(wc,prefix(a),prefix(b),f'WJ{i:02}_{a}_{b}_retained')

# Remove failed optional rounds, then add local root blends one edge at a time.
cleanup=[]
for go in (right,left,wg):
    for o in go.component.occurrences:
        c=o.component
        for f in reversed(list(c.features.filletFeatures)):
            if f.healthState!=adsk.fusion.FeatureHealthStates.HealthyFeatureHealthState:
                cleanup.append(c.name+'/'+f.name);f.deleteMe()
c5=prefix('W05').component
bb=next(b for b in c5.bRepBodies if b.name.startswith('W05_'))
shape=TM.copy(bb)
yr=Y+10
for lo,hi,center_y in ((yr-24,yr-21,yr-24),(yr+21,yr+24,yr+24)):
    wedge=sub(bx((-12,lo,915.9),(12,hi,919)),cy((-13,center_y,919),(13,center_y,919),3))
    un(shape,wedge)
c5.features.removeFeatures.add(bb)
add(c5,shape,'W05_nylon_base_with_R3_outer_root_blends',plastic)
for o in wc.occurrences:
    if o.component.name.startswith(('W05_','W06_','W07_','W09_','W10_','W11_','W12_','W13_')):
        o.component.partNumber=o.component.name
adsk.doEvents()
axes=[]
for name,want in (('WJ00_waist_yaw',(0,0,1)),('WJ01_lower_waist_roll',(0,1,0)),('WJ02_upper_waist_pitch',(1,0,0))):
    j=wc.asBuiltJoints.itemByName(name);axis=j.createForAssemblyContext(wg).jointMotion.rotationAxisVector.asArray()
    err=max(abs(abs(a)-b) for a,b in zip(axis,want));assert err<1e-6
    axes.append({'name':name,'axis':list(axis),'error':err})
result={'motor_file':path,'reference_bodies_each':len(copies),'waist_joint_count':wc.asBuiltJoints.count,'axes':axes,'failed_optional_fillets_removed':cleanup,
        'hip_layout_joint_counts':{go.component.name:go.component.asBuiltJoints.count for go in (right,left)}}
(OUT/'joints_and_motor_import.json').write_text(json.dumps(result,indent=2))
