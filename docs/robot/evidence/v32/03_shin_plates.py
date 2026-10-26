exec(compile((ROOT/'v32/common32.py').read_text(),'<common32>','exec'))
exec(compile((ROOT/'v32/plate_helpers32.py').read_text(),'<plate_helpers>','exec'))
d.activateRootComponent();cc=exact('V30_construction_reference').component
report=[]
for side in (-1,1):
 prefix='Left' if side<0 else 'Right';xc=side*120
 for upper in (False,True):
  name='C27_'+prefix+'_shin_front'+('_upper' if upper else '')
  if upper:
   contour=[(-48,263),(48,263),(48,350),(37,378),(24,384),(-24,384),(-37,378),(-48,350)]
   mounts=[(dx,z) for dx in (-10,10) for z in (314,366)]
  else:
   contour=[(-27,118),(27,118),(32,180),(48,222),(48,262),(-48,262),(-48,222),(-32,180)]
   mounts=[(dx,244) for dx in (-10,10)]
  body=polygon_plate([(xc+x,z) for x,z in contour],-7.5,2.5,name+'_R8_outline',radius=8)
  # Small mounting pads meet the existing carrier face at Y=-4 mm.
  for dx,z in mounts:
   un(body,cy((xc+dx,-5.1,z),(xc+dx,-4,z),5))
   sub(body,cy((xc+dx,-9,z),(xc+dx,-3,z),1.7))
  if not upper:
   # Shallow open saddles locate on the unchanged 18 x 10 mm oval rails.
   # Removable straps pass through the flanking slots; no new holes in steel.
   for z in (134,182):
    for dx in (-10,10):
     saddle=bx((xc+dx-11.5,-5.1,z-5),(xc+dx+11.5,9,z+5))
     bore=un(cy((xc+dx-4,6,z-6),(xc+dx-4,6,z+6),5.3),cy((xc+dx+4,6,z-6),(xc+dx+4,6,z+6),5.3),bx((xc+dx-4,.7,z-6),(xc+dx+4,11.3,z+6)))
     sub(saddle,bore);sub(saddle,bx((xc+dx-9.3,6,z-6),(xc+dx+9.3,15,z+6)))
     un(body,saddle)
    for dx in (-23.5,23.5):
     sub(body,bx((xc+dx-1.5,-9,z-3),(xc+dx+1.5,0,z+3)))
  # Rounded perforations; continuous border and solid mounting islands.
  holes=[]
  for row,z in enumerate(range(277 if upper else 130,375 if upper else 255,12)):
   if not upper and min(abs(z-a) for a in (134,182,244))<9:continue
   width=(38 if z<355 else 23) if upper else (18 if z<177 else 29 if z<217 else 38)
   for col in range(-4,5):
    dx=col*10+(5 if row%2 else 0)
    if abs(dx)>width:continue
    if any(math.hypot(dx-mx,z-mz)<8 for mx,mz in mounts):continue
    sub(body,cy((xc+dx,-8,z),(xc+dx,-4.5,z),3.2));holes.append([xc+dx,z])
  assert body.isSolid and body.lumps.count==1,(name,body.lumps.count)
  o=exact(name);oldvol=sum(b.volume for b in o.bRepBodies)*1000
  replace_world(o,[(name+'_V32_shallow_perforated_plate',body)],'V32 2.5 mm front-only perforated plate. Existing carrier M3 bores; lower plate has open oval-rail saddles and strap slots. Sides/rear remain open. Strap and screw length/retention require prototype fit.')
  report.append(dict(part=name,bounds_mm=bounds(body),volume_mm3=body.volume*1000,previous_volume_mm3=oldvol,perforations=len(holes),mounts_xz=[[xc+dx,z] for dx,z in mounts],thickness_mm=2.5,carrier_pad_gap_mm=0))
 for suffix in ('shin_rear','shin_rear_upper','calf_blue_mark'):
  o=exact('C27_'+prefix+'_'+suffix);o.isLightBulbOn=False;o.component.description+=' Superseded by V32 front-only perforated plate; retained hidden for history.'
 o=exact('C28_'+prefix+'_ankle_shroud');o.isLightBulbOn=False;o.component.description+=' V32: bulky all-side ankle shroud removed from active design; structural frame exposed.'
d.activateRootComponent();exact('Casings').isLightBulbOn=True
journal('shin_plates32',report)
save_view('shin_plates32',(0,20,260),(1450,-3100,1050),510)
result=report
