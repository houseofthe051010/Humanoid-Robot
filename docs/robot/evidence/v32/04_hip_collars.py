exec(compile((ROOT/'v32/common32.py').read_text(),'<common32>','exec'))
d.activateRootComponent()
report=[];white=exact('C27_Right_thigh_front').component.bRepBodies.item(0).appearance
outer=loft_round_xy([(666,65.8,Y-42,Y+42,12),(715,65.8,Y-42,Y+42,12)],'V32_fitted_hip_collar_outer')
inner=loft_round_xy([(665,63.3,Y-39.5,Y+39.5,9.5),(716,63.3,Y-39.5,Y+39.5,9.5)],'V32_fitted_hip_collar_inner')
ring=sub(outer,inner)
for x in (-51,51):
 # Two halves clamp the existing 10 x 18 mm oval. No steel drilling.
 saddle=bx((x-12.8,Y-13,667),(x+12.8,Y+13,675))
 bore=un(cy((x,Y-4,666),(x,Y-4,676),5.3),cy((x,Y+4,666),(x,Y+4,676),5.3),bx((x-5.3,Y-4,666),(x+5.3,Y+4,676)))
 sub(saddle,bore)
 # Connect the clamp to the nearby side wall with a broad eight-mm tab.
 x0,x1=(x,65.8) if x>0 else (-65.8,x)
 un(saddle,bx((x0,Y-13,667),(x1,Y+13,675)))
 sub(saddle,bore);sub(saddle,cy((0,Y,666),(0,Y,676),40));un(ring,saddle)
 hx=math.copysign(61,x)
 sub(ring,cy((hx,Y-44,671),(hx,Y+44,671),1.7))
parts=[]
for side in (-1,1):
 prefix='Left' if side<0 else 'Right';name='C28_'+prefix+'_hip_yaw_shroud'
 m=M3.create();m.translation=V3.create(side*12,0,0)
 world=transform(TM.copy(ring),m)
 overlaps=[]
 for o in root.allOccurrences:
  if not o.isVisible or not o.fullPathName.startswith(prefix.lower()+'_thigh:'):continue
  for b in o.bRepBodies:
   bb=bounds(b)
   if bb[1][2]<666 or bb[0][2]>715:continue
   overlap=TM.copy(world);ix(overlap,TM.copy(b))
   if overlap.volume*1000>.05:overlaps.append(dict(part=o.component.name,body=b.name,volume_mm3=overlap.volume*1000))
 assert not overlaps,(prefix,overlaps)
 front=ix(TM.copy(world),bx((-400,-200,660),(400,Y-.3,730)))
 rear=ix(TM.copy(world),bx((-400,Y+.3,660),(400,200,730)))
 assert front.lumps.count==1 and rear.lumps.count==1
 existing=[o for o in root.allOccurrences if o.component.name==name]
 if existing:
  o=existing[0];before=[bounds(b) for b in o.bRepBodies]
  replace_world(o,[(name+'_V32_front',front),(name+'_V32_rear',rear)])
 else:
  owner=exact('Covers_'+prefix.lower()+'_thigh');native=owner.component.occurrences.addNewComponent(M3.create())
  native.component.name=name;native.isGroundToParent=True
  native.component.attributes.add('Robot','physical_owner',prefix.lower()+'_thigh')
  o=native.createForAssemblyContext(owner);before=None
  replace_world(o,[(name+'_V32_front',front),(name+'_V32_rear',rear)])
 for b in o.component.bRepBodies:b.appearance=white
 o.component.description='V32 close fitting 2.5 mm hip-yaw collar around actual oval rails and crosshead; split front/rear with .6 mm seam. Two integrated oval clamp pads and M3 bores. Final screws/inserts and clamp preload require prototype fit.'
 report.append(dict(part=name,previous_bounds_mm=before,bounds_mm=bounds(world),width_mm=131.6,depth_mm=84,wall_mm=2.5,split_seam_mm=.6,clamp_bore_mm=[10.6,18.6],neutral_intersections=overlaps,volume_mm3=(front.volume+rear.volume)*1000))
d.activateRootComponent();exact('Casings').isLightBulbOn=True
journal('hip_collars32',report)
save_view('hip_collars32',(0,23,716),(1250,-2600,1280),500)
result=report
