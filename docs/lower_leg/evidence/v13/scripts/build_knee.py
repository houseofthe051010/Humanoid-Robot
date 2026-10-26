exec(compile((ROOT/'v13/common.py').read_text(),'<v13common>','exec'))
progress('raised knee pivot and curved chain-side relief')
silver=ap('aluminum');orange=ap('orange')
tiepos=[(yy,K+zz)for yy in [18.5,36]for zz in [-15,15]]
dowelpos=[(36,K+zz)for zz in [-8,8]]
for n in [1,2,4,5]:
 name='N01_Aluminum_knee_stack_'+str(n);b=TM.copy(parts[name].component.bRepBodies.item(0));bb=b.boundingBox;x0=bb.minPoint.x*10;x1=bb.maxPoint.x*10
 bounds=bx((x0,-1,393.6),(x1,44,441.6))
 # Close original shaft, stack-tie, registration, rail-bolt and set-screw passages before recutting.
 for yy,zz,rr in [(Y,423.6,4.1)]+[(yy,zz,1.8)for yy in [18.5,36]for zz in [404,437]]+[(36,zz,3.2)for zz in [414,430]]:
  un(b,ix(cy((x0,yy,zz),(x1,yy,zz),rr),TM.copy(bounds)))
 for xx in [-10,10]:
  if x0-2<xx<x1+2:un(b,ix(cy((xx,-1,406),(xx,44,406),1.8),TM.copy(bounds)))
 for xx in [-5,5]:
  if x0<xx<x1:un(b,ix(cy((xx,27.343134,423.6),(xx,38,423.6),1.8),TM.copy(bounds)))
 un(b,cy((x0,Y,K),(x1,Y,K),24))
 # Preserve the oval sockets, extending their upper ends with the shin tubes.
 for xx in [-10,10]:sub(b,shinoval(xx,392,435.65,5.1))
 sub(b,cy((x0-1,Y,K),(x1+1,Y,K),4.05))
 for yy,zz in tiepos:sub(b,cy((x0-1,yy,zz),(x1+1,yy,zz),1.65))
 for yy,zz in dowelpos:sub(b,cy((x0-1,yy,zz),(x1+1,yy,zz),3.05))
 for xx in [-10,10]:sub(b,cy((xx,-2,418),(xx,50,418),1.65))
 for xx in [-5,5]:sub(b,cy((xx,27.343134,K),(xx,38,K),1.5))
 # Remove only the outer skin beyond the24.8mm load-transfer boss on the chain side.
 # Inner face X-12 is1mm beyond the22mm-wide chain allowance at X-24.
 cut=sub(bx((-22,-60,390),(-12,100,480)),cy((-23,Y,K),(-11,Y,K),24.8))
 sub(b,cut)
 emit(name,b,'V13 raised shaft axis Z435.6 (+12mm), R24 crown, extended shin sockets, revised tie/dowel pattern and chain-side relief toX-12 outside R24.8. Recheck CNC stock and strength.','6061-T6 nominal',silver)
for name in ['N02_Knee_shaft_8mm','N04_Knee_pillow_block_L','N04_Knee_pillow_block_R','P01_Knee_side_rail_seat_L','P01_Knee_side_rail_seat_R','P02_Knee_rail_screws_and_sleeves_L','P02_Knee_rail_screws_and_sleeves_R']:
 shift(name,12)
 parts[name].component.description+=' V13 knee pivot/support raised12mm.'
progress('shin extension and revised thigh rail lower ends')
for side,x in [('L',-10),('R',10)]:
 a=sub(shinoval(x,69,K,5),shinoval(x,68,K+1,4.45))
 sub(a,cy((x,-1,418),(x,13,418),1.65))
 emit('S05_Continuous_oval_steel_rail_'+side,a,'Continuous18x10 stadium steel tube,0.55mm assumed wall,366.6mm long,12mm longer for raised knee; knee cross-bolt passage atZ418.','steel, grade and wall unverified')
for side,x in [('L',-51),('R',51)]:
 a=sub(oval(x,450.2,685,5),oval(x,449.2,686,4.45))
 for z in [465,481]:sub(a,cy((x-6,Y,z),(x+6,Y,z),2.2))
 if side=='L':sub(a,cy((x-6,Y,Z),(x+6,Y,Z),3.3))
 emit('N06_Upper_leg_oval_stub_'+side,a,'18Yx10X oval tube,0.55mm assumed wall,234.8mm long; lower end raised12mm while hip height stays fixed. New side-screw and output-pin passages.','steel, grade and wall unverified')
progress('approximate16T knee sprocket and matched fasteners')
x0=CHAIN_X-FACE/2;x1=CHAIN_X+FACE/2
a=sub(cy((x0,Y,K),(x1,Y,K),71.37/2),cy((x0-1,Y,K),(x1+1,Y,K),4.1))
for i in range(16):
 t=2*math.pi*i/16;yy=Y+32.55*math.cos(t);zz=K+32.55*math.sin(t)
 sub(a,cy((x0-1,yy,zz),(x1+1,yy,zz),3.96))
for yy,zz in tiepos:
 sub(a,cy((x0-1,yy,zz),(x1+1,yy,zz),1.65));sub(a,cy((x0-1,yy,zz),(x0+3.1,yy,zz),2.95))
for yy,zz in dowelpos:sub(a,cy((x0-1,yy,zz),(x1+1,yy,zz),3.05))
emit('N03_Sprocket_blank_LAYOUT',a,'Approximate16T #40 sprocket:12.7pitch,65.10PD,71.37OD,7.21face. Common chain planeX-24. Revised four recessed M3 ties and two6mm dowels. Roller-pocket teeth are visualization only.','sprocket material undecided',orange)
hw=[]
for yy,zz in tiepos:
 hw += [('M3x50_stack_tie',cy((x0+3,yy,zz),(x0+53,yy,zz),1.5)),('Recessed_M3_head',cy((x0,yy,zz),(x0+3,yy,zz),2.75)),('M3_stack_nut_envelope',sub(cy((21,yy,zz),(23.4,yy,zz),2.9),cy((20,yy,zz),(24,yy,zz),1.55)))]
for yy,zz in dowelpos:hw.append(('6mm_stack_dowel',cy((x0,yy,zz),(21,yy,zz),3)))
for xx in [-10,10]:
 hw += [('M3x50_rail_crossbolt',cy((xx,-1,418),(xx,49,418),1.5)),('M3_rail_head',cy((xx,-4,418),(xx,-1,418),2.75)),('M3_rail_nut_envelope',sub(cy((xx,44,418),(xx,46.4,418),2.9),cy((xx,43,418),(xx,47,418),1.55)))]
for xx in [-5,5]:hw.append(('M3x10_shaft_set_screw',cy((xx,27.343134,K),(xx,37.343134,K),1.5)))
emit('N07_Knee_stack_fasteners',hw,'Four recessed M3x50 stack ties/nuts, two6mm dowels48.605mm nominal, two M3x50 rail cross-bolts/nuts and two M3x10 shaft-set-screw envelopes. New pattern; verify stock and engagement.','steel reference',silver)
(OUT/'knee_parameters.json').write_text(json.dumps({'pivot_z_mm':K,'pivot_raise_mm':12,'shin_tube_length_mm':366.6,'thigh_tube_length_mm':234.8,'hip_height_changed':False,'chain_plane_x_mm':CHAIN_X,'driven_teeth':16,'PD_mm':65.1,'OD_mm':71.37,'face_mm':FACE,'chain_side_clearance_x_mm':-12,'crown_radius_mm':24,'tie_pattern_yz_mm':tiepos,'dowel_pattern_yz_mm':dowelpos,'strength_validated':False},indent=2))
result={'knee_z':K,'shin_length':366.6,'thigh_length':234.8,'sprocket':'16T,71.37OD,7.21face'}
