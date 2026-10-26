exec(compile((ROOT/'v32/common32.py').read_text(),'<common32>','exec'))
d.activateRootComponent();report=[]
for prefix,xc in (('Left',-120),('Right',120)):
 frames=[TM.copy(b) for n in (prefix+'_S06_Dual_7010_motor_carrier',prefix+'_S05_Continuous_oval_steel_rail_L',prefix+'_S05_Continuous_oval_steel_rail_R',prefix+'_H01_Steel_crush_sleeves') for b in exact(n).bRepBodies]
 for upper in (False,True):
  name='C27_'+prefix+'_shin_front'+('_upper' if upper else '');o=exact(name);body=TM.copy(o.bRepBodies.item(0))
  zs=(314,366) if upper else (244,)
  for dx in (-10,10):
   for z in zs:
    support=cy((xc+dx,-5.1,z),(xc+dx,3,z),5)
    for frame in frames:sub(support,TM.copy(frame))
    un(body,support);sub(body,cy((xc+dx,-9,z),(xc+dx,4,z),1.7))
  if not upper:
   # Cut both bores AFTER uniting both saddles, so the adjacent saddle does
   # not refill the tip of the first oval bore.
   for z in (134,182):
    for dx in (-10,10):
     bore=un(cy((xc+dx-4,6,z-6),(xc+dx-4,6,z+6),5.3),cy((xc+dx+4,6,z-6),(xc+dx+4,6,z+6),5.3),bx((xc+dx-4,.7,z-6),(xc+dx+4,11.3,z+6)))
     sub(body,bore);sub(body,bx((xc+dx-9.3,6,z-6),(xc+dx+9.3,15,z+6)))
  if body.lumps.count>1:
   pieces=sorted(separate_lumps(body),key=lambda q:q.volume,reverse=True)
   journal(name+'_trim_fragments32',dict(all_lumps=[dict(bounds=bounds(p),volume_mm3=p.volume*1000) for p in pieces]))
   assert pieces[0].volume>body.volume*.95 and all(p.volume*1000<150 for p in pieces[1:]),(name,[p.volume*1000 for p in pieces])
   body=pieces[0]
  assert body.lumps.count==1,(name,body.lumps.count)
  replace_world(o,[(name+'_V32_perforated_plate_fitted',body)],'V32 front-only perforated plate, 2.5 mm face. Six unchanged frame bores per leg with conformal standoffs fitted to carrier/steel rails. Lower open saddle bores recut after union; removable strap slots. Final screws/strap retention require physical fit.')
  report.append(dict(part=name,bounds_mm=bounds(body),volume_mm3=body.volume*1000,conformal_mount_support=True))
outer=loft_round_xy([(666,65.8,Y-42,Y+42,12),(702.5,65.8,Y-42,Y+42,12)],'V32_compact_collar_standoff_boundary')
for prefix,xc in (('Left',-120),('Right',120)):
 o=exact('C28_'+prefix+'_hip_yaw_shroud');m=M3.create();m.translation=V3.create(xc/10,0,0);boundary=transform(TM.copy(outer),m);rows=[]
 for front,b in zip((True,False),o.bRepBodies):
  body=TM.copy(b);ix(body,bx((-400,-200,660),(400,200,702.5)))
  for dx in (-61,61):
   support=cy((xc+dx,Y-43,671),(xc+dx,Y+43,671),3.8);ix(support,TM.copy(boundary))
   ix(support,bx((-400,-200,660),(400,Y-.3,710)) if front else bx((-400,Y+.3,660),(400,200,710)))
   un(body,support);sub(body,cy((xc+dx,Y-44,671),(xc+dx,Y+44,671),1.7))
  assert body.lumps.count==1,(o.component.name,body.lumps.count)
  rows.append((o.component.name+'_V32_'+('front' if front else 'rear')+'_clear',body))
 replace_world(o,rows,'V32 compact 131.6 x 84 x 36.5 mm split hip-yaw collar around oval rails/crosshead. Ends at Z702.5 below upstream moving cradle. 2.5 mm skin, oval clamp pads and internally supported M3 seam bores; final hardware/fit qualification pending.')
 report.append(dict(part=o.component.name,top_z_mm=702.5,height_mm=36.5,volume_mm3=sum(s.volume*1000 for _,s in rows),internally_supported_seam_bores=True))
for f in ('shin_plates32','hip_collars32'):
 data=json.loads((OUT/(f+'.json')).read_text())
 for row in data:
  change=next(r for r in report if r['part']==row['part']);row.update(change);row.pop('carrier_pad_gap_mm',None)
  if f=='hip_collars32':row['bounds_mm'][1][2]=702.5
 journal(f,data)
journal('fit_repairs32',report)
d.activateRootComponent();save_view('repaired_leg_covers32',(0,20,460),(1400,-3100,1250),950)
result=report
