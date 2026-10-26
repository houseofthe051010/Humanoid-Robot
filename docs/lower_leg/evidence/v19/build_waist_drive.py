exec(compile((ROOT/'v19/common.py').read_text(),'<common>','exec'))
wc=wg.component
assert not (OUT/'waist_drive_geometry.json').exists()
def prefix(k):return next(o for o in wc.occurrences if o.component.partNumber.startswith(k+'_'))
def obj(items):
 a=adsk.core.ObjectCollection.create()
 for x in items:a.add(x)
 return a
def frame(origin,x,z):
 xx=V3.create(*x);xx.normalize();zz=V3.create(*z);zz.normalize();yy=zz.crossProduct(xx);yy.normalize()
 return basis(origin,xx.asArray(),yy.asArray(),zz.asArray())
def move_world(o,delta):
 inv=o.createForAssemblyContext(wg).transform2.copy();inv.invert();vv=V3.create(*(v/10 for v in delta));vv.transformBy(inv)
 mm=adsk.core.Matrix3D.create();mm.translation=vv
 inp=o.component.features.moveFeatures.createInput2(obj(list(o.component.bRepBodies)));inp.defineAsFreeMove(mm)
 o.component.features.moveFeatures.add(inp).name='V19_lower_and_narrow_6010_placement'
def beam_x(a,b,r,x0,x1):
 sh=beam_y(a,b,r,x0,x1)
 mm=adsk.core.Matrix3D.create();mm.setWithArray([0,1,0,0,1,0,0,0,0,0,-1,0,0,0,0,1])
 # beam_y uses (a0,y,a1). Permute x/y and preserve z with reflection.
 mm.setCell(2,2,1)
 return transform(sh,mm)
progress('lower waist motors and build raised transverse pin supports')
for n,s in (('W19',-1),('W20',1)):
 o=prefix(n);move_world(o,(s*(63.5-73),0,-45));o.component.description='GIM6010-8 standard vendor reference, inward output. V19 center X +/-63.5, Z995; compact waist differential.'
yr=Y+10
v5=prefix('W05');vendor=next(b for b in v5.createForAssemblyContext(wg).bRepBodies if 'vendor' in b.name.lower());vendorcopy=TM.copy(vendor)
base=un(cy((0,Y,901.5),(0,Y,910),18.5),rrxy(-44,44,Y-27,Y+35,909,916,9))
for ya,yb in ((yr-21,yr-13),(yr+13,yr+21)):
 un(base,bx((-12,ya,913),(12,yb,927)),cy((0,ya,927),(0,yb,927),12))
sub(base,cy((0,yr-23,927),(0,yr+23,927),5.05))
pin_y=yr-30;pin_z=935
for xa,xb in ((-43,-36),(36,43)):
 un(base,bx((xa,pin_y-7,913),(xb,pin_y+7,pin_z)),cy((xa,pin_y,pin_z),(xb,pin_y,pin_z),7))
sub(base,cy((-45,pin_y,pin_z),(45,pin_y,pin_z),3.1))
sub(base,vendorcopy);sub(base,cy((0,Y,901),(0,Y,911),7.3))
for k in range(6):
 a=math.radians(30+60*k);x,y=12.5*math.cos(a),Y+12.5*math.sin(a)
 sub(base,cy((x,y,901),(x,y,917),1.7));sub(base,cy((x,y,906.5),(x,y,917),2.9))
world_replace(wg,v5,[('GWK7010_vendor_output_MOVING',TM.copy(vendor)),('W05_raised_cross_pin_double_supported_base',base)],'PA12-CF prototype output base with actual six-hole 7010 interface and elevated X-axis 6 mm steel pin, supported by both outer ears.',plastic)
v5.component.bRepBodies.item(0).appearance=black
try:
 b=v5.component.bRepBodies.item(1)
 fillet_edges(v5.component,b,2,lambda e:adsk.core.Line3D.cast(e.geometry) and abs(e.boundingBox.minPoint.z*10-916)<.01 and abs(e.boundingBox.maxPoint.z*10-916)<.01 and e.length*10>5,'V19_base_ear_root_R2')
except Exception:pass
progress('reuse ankle M6 rod-end supplier solids')
path=str(ROOT/'v8/sources/Wixroyd_65720/65720.W0006.step')
sd=app.importManager.importToNewDocument(app.importManager.createSTEPImportOptions(path));assert sd
sr=adsk.fusion.Design.cast(app.activeProduct).rootComponent
sb=list(sr.bRepBodies)+[b for o in sr.allOccurrences for b in o.bRepBodies]
ball=TM.copy(min(sb,key=lambda b:b.volume));housing=TM.copy(max(sb,key=lambda b:b.volume))
sd.close(False);doc.activate()
shaft=newpart(wc,'W21_6mm_transverse_base_pin','6 mm steel shaft, 94 mm overall reference with end retention. Two rod-end inner rings at X +/-30; printed supports X36..43 each side. Not load-qualified.','steel reference')
add(shaft.component,cy((-47,pin_y,pin_z),(47,pin_y,pin_z),3),'6mm_double_supported_pin',silver)
for s in (-1,1):add(shaft.component,transform(TM.copy(ball),frame((s*30,pin_y,pin_z),(0,0,1),(1,0,0))),'Copied_ankle_M6_inner_ring_'+str(s),silver)
rigid(wc,v5,shaft,'WJ21_base_pin_retained')
sp=newpart(wc,'W22_Base_pin_spacers_retention','Axial spacers contact only rod-end inner-ring faces, 0.2 mm end floats. Retention heads/nuts are reference envelopes.','steel / polymer reference')
for a,b in ((-35.8,-34.5),(-25.5,25.5),(34.5,35.8)):
 add(sp.component,ring((a,pin_y,pin_z),(b,pin_y,pin_z),4.25,3.1),'Pin_inner_ring_spacer',silver)
for a,b in ((-47,-43),(43,47)):add(sp.component,ring((a,pin_y,pin_z),(b,pin_y,pin_z),5,3),'M6_pin_retainer_reference',silver)
rigid(wc,v5,sp,'WJ22_pin_spacers_retained')
report={'motor_centers_mm':[],'pin_center_yz_mm':[pin_y,pin_z],'pin_diameter_mm':6,'pin_length_mm':94,'links':[],'crank_radius_mm':26,'limits_deg':{'pitch':[-20,20],'roll':[-5,5]},'rod_end_assumed_tilt_limit_deg':6.25}
angle=math.radians(160);cr=26
for side,s,num,rodnum,motorid in (('L',-1,23,25,'W19'),('R',1,24,26,'W20')):
 progress('build '+side+' 6010 measured-output crank and short M6 tie rod')
 motor=prefix(motorid);proxy=motor.createForAssemblyContext(wg);mc=(s*63.5,Y,995)
 outface=next(f for b in proxy.bRepBodies for f in b.faces if adsk.core.Plane.cast(f.geometry) and abs(f.area*100-550.6975627)<.1)
 fx=outface.geometry.origin.x*10;A=(s*30,Y+cr*math.cos(angle),995+cr*math.sin(angle));B=(s*30,pin_y,pin_z)
 lo,hi=sorted((fx,fx-s*6));arm=un(cy((lo,Y,995),(hi,Y,995),17),beam_x((Y,995),(A[1],A[2]),7,lo,hi))
 # Clear the actual output's locating features; preserve its six small M3 holes.
 for b in proxy.bRepBodies:sub(arm,TM.copy(b))
 sub(arm,cy((lo-1,Y,995),(hi+1,Y,995),7.5))
 holes=[]
 for b in proxy.bRepBodies:
  for f in b.faces:
   c=adsk.core.Cylinder.cast(f.geometry)
   if c and abs(abs(c.axis.x)-1)<1e-5 and abs(c.radius*10-1.2295)<.003 and abs(math.hypot(c.origin.y*10-Y,c.origin.z*10-995)-12.5)<.01:
    q=(round(c.origin.y*10,5),round(c.origin.z*10,5))
    if q not in holes:holes.append(q)
 assert len(holes)==6,holes
 for y,z in holes:sub(arm,cy((lo-1,y,z),(hi+1,y,z),1.7))
 sub(arm,cy((lo-1,A[1],A[2]),(hi+1,A[1],A[2]),3.1))
 crank=newpart(wc,f'W{num}_6010_crank_{side}','26 mm center-distance crank, 6 mm aluminum with actual six M3 output hole locations, 6 mm rod-end pin and spacers.','6061 aluminum prototype')
 add(crank.component,arm,'6010_contoured_26mm_crank',silver)
 add(crank.component,transform(TM.copy(ball),frame(A,(0,0,-1),(1,0,0))),'Copied_ankle_upper_inner_ring',silver)
 # Crank pin and short spacer to the spherical inner ring.
 x0,x1=sorted((A[0]-s*6,fx));add(crank.component,cy((x0,A[1],A[2]),(x1,A[1],A[2]),3),'M6_crank_pin_reference',silver)
 sa,sb=sorted((A[0]+s*4.5,fx-s*6));add(crank.component,ring((sa,A[1],A[2]),(sb,A[1],A[2]),3.75,3.1),'Crank_inner_ring_spacer',silver)
 for y,z in holes:
  x0,x1=sorted((fx+s*4,fx-s*6));add(crank.component,cy((x0,y,z),(x1,y,z),1.45),'Output_M3_reference',silver)
 L=math.sqrt(sum((a-b)**2 for a,b in zip(A,B)));uv=[(a-b)/L for a,b in zip(A,B)]
 rod=newpart(wc,f'W{rodnum}_M6_waist_tie_rod_{side}',f'M6x1 RH, {L-36:.3f} mm threaded stock and 12 mm nominal engagement at each end; two copies of the ankle Wixroyd surrogate rod-end housing. Confirm purchased hardware.','steel reference')
 core=add(rod.component,cy((0,0,18),(0,0,L-18),3),'M6x1_threaded_rod',silver)
 face=next(f for f in core.faces if adsk.core.Cylinder.cast(f.geometry))
 ti=rod.component.features.threadFeatures.createInput(face,rod.component.features.threadFeatures.createThreadInfo(False,'ISO Metric profile','M6x1','6g'));ti.isFullLength=True;ti.isModeled=True
 rod.component.features.threadFeatures.add(ti).name='Ankle_matching_physical_M6x1_thread'
 # Canonical Z along the link and canonical X along the pin.
 ey=V3.create(*uv).crossProduct(V3.create(1,0,0));ey.normalize();m=basis(B,(1,0,0),ey.asArray(),uv)
 mi=rod.component.features.moveFeatures.createInput2(obj(list(rod.component.bRepBodies)));mi.defineAsFreeMove(m);rod.component.features.moveFeatures.add(mi)
 add(rod.component,transform(TM.copy(housing),frame(B,uv,(1,0,0))),'Copied_ankle_lower_M6_housing',silver)
 add(rod.component,transform(TM.copy(housing),frame(A,[-v for v in uv],(1,0,0))),'Copied_ankle_upper_M6_housing',silver)
 for a,b in ((30,32.5),(L-32.5,L-30)):
  # Thin jam-nut envelopes, internally bored; final wrench/access check remains.
  nut=ring((0,0,a),(0,0,b),5.77,3.05);add(rod.component,transform(nut,m),'M6_thin_jam_nut_reference',silver)
 report['motor_centers_mm'].append(mc);report['links'].append({'side':side,'motor':motorid,'crank':f'W{num}','rod':f'W{rodnum}','A':A,'B':B,'center_distance_mm':L,'stock_length_mm':L-36,'neutral_crank_deg':160,'motor_output_plane_x_mm':fx,'output_holes_yz_mm':holes})
for key,lim in (('WJ01_lower_waist_roll',5),('WJ02_upper_waist_pitch',20)):
 limits=wc.asBuiltJoints.itemByName(key).jointMotion.rotationLimits;limits.minimumValue=math.radians(-lim);limits.maximumValue=math.radians(lim);limits.isMinimumValueEnabled=True;limits.isMaximumValueEnabled=True
(OUT/'waist_drive_geometry.json').write_text(json.dumps(report,indent=2));result=report
