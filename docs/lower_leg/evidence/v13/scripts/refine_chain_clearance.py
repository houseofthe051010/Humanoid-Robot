exec(compile((ROOT/'v13/common.py').read_text(),'<common>','exec'))
silver=ap('aluminum');orange=ap('orange')
progress('chain plane, output and knee standoff')
# Change only bodies constructed at the original draft chain plane.
for n in ['P07_Motor_output_sprocket_BLANK','N03_Sprocket_blank_LAYOUT','V13_Chain_clearance_ENVELOPE']:
 c=parts[n].component;bs=[(b.name,trans(TM.copy(b),dx=-7))for b in c.bRepBodies];emit(n,bs)
parts['V13_Chain_clearance_ENVELOPE'].isLightBulbOn=False
x0=CHAIN_X-FACE/2;x1=CHAIN_X+FACE/2
a=un(cy((-8.5,Y,Z),(-4.5,Y,Z),16),cy((x0,Y,Z),(-4.5,Y,Z),8));sub(a,cy((x0-1,Y,Z),(x0+8,Y,Z),3.1))
emit('P06_Gearbox_output_REFERENCE',a,'16mm output shaft and32mm flange reference.0.5mm axial clearance to estimated motor central boss. Carrier/bearing/coupling pending.','aluminum reference',silver)
a=sub(cy((x1,Y,Z),(-19,Y,Z),9.5),cy((x1-1,Y,Z),(-18,Y,Z),8))
emit('P08_Sprocket_output_flange',a,'19mm OD compact8T hub; provisional keyed/coupled interface and retention.','aluminum reference',silver)
emit('P09_Opposite_output_support_pin_6mm',cy((-67,Y,Z),(-28,Y,Z),3),'6mm support pin,39mm long in revised chain plane. Bearing/retention pending.','steel reference',silver)
# Rebuild only stack tie shanks/heads and dowels for the7mm outward sprocket shift.
c=parts['N07_Knee_stack_fasteners'].component;bs=[]
for b in c.bRepBodies:
 if b.name.startswith(('M3x50_stack_tie','Recessed_M3_head','6mm_stack_dowel')):continue
 bs.append((b.name,TM.copy(b)))
for yy in [18.5,36]:
 for zz in [K-15,K+15]:
  bs += [('M3x60_stack_tie',cy((x0+3,yy,zz),(x0+63,yy,zz),1.5)),('Recessed_M3_head',cy((x0,yy,zz),(x0+3,yy,zz),2.75))]
for zz in [K-8,K+8]:bs.append(('6mm_stack_dowel',cy((x0,36,zz),(21,36,zz),3)))
emit(c.name,bs,'Four recessed M3x60 stack ties/nuts, two6x55.605 nominal dowels, two M3x50 rail bolts/nuts and two M3x10 set screws.','steel reference',silver)
a=sub(cy((x1,Y,K),(-21,Y,K),24),cy((x1-1,Y,K),(-20,Y,K),4.1))
for yy in [18.5,36]:
 for zz in [K-15,K+15]:sub(a,cy((x1-1,yy,zz),(-20,yy,zz),1.65))
for zz in [K-8,K+8]:sub(a,cy((x1-1,36,zz),(-20,36,zz),3.05))
emit('N09_Knee_sprocket_standoff_hub',a,'48mm OD x6.395mm sprocket standoff, fourM3 ties and two6mm registrations. Keeps chain planeX-31 clear of shin tubes. Provisional load path.','6061-T6 nominal',silver)
progress('compact drive-side CNC bearing pedestal and rail saddle')
c=parts['N04_Knee_pillow_block_L'].component;kept=[(b.name,TM.copy(b),b.appearance)for b in c.bRepBodies if not b.name.startswith('608ZZ Standing bearing')]
yy=Y+0.00000170585;zz=K+.10000181328
a=cy((-49.5,yy,zz),(-36.5,yy,zz),17.5)
ix(a,bx((-50,Y-30,K-18),(-36,Y+30,450.2)))
un(a,bx((-49.5,Y-19,443.6),(-36.5,Y+19,450.2)))
sub(a,cy((-50,yy,zz),(-36,yy,zz),12.9))
for dy in [-15,15]:sub(a,cy((-43,Y+dy,443.5),(-43,Y+dy,451),2.2))
emit(c.name,[(n,b)for n,b,ap0 in kept]+[('CUSTOM_CNC_compact_cartridge_pedestal',a)],'V13 custom aluminum pedestal replaces stock standing casting on drive side ONLY; retained bearing/cartridge solids and bearing centre.25.8mm through-seat follows unverified donor cartridge envelope. Bearing fit, shoulders and retention require design.','608 bearing/cartridge + custom aluminum pedestal',silver)
for b,old in zip(list(c.bRepBodies)[:-1],kept):b.appearance=old[2]
a=rrxy(-51,-33,Y-19,Y+19,450.2,489.2,3);sub(a,oval(-51,449,491,5.05))
for dy in [-15,15]:sub(a,cy((-43,Y+dy,450),(-43,Y+dy,490),2.2))
for z in [465,481]:sub(a,cy((-52,Y,z),(-32,Y,z),2))
emit('P01_Knee_side_rail_seat_L',a,'Narrow38mm-wide CNC drive-side saddle for chain clearance. Two side M4 screws; two bottom-entering M4 pedestal screws atY+/-15. Right saddle unchanged.','6061-T6 nominal',silver)
hw=[]
for dy in [-15,15]:hw += [('M4x18_pedestal_screw',cy((-43,Y+dy,443.6),(-43,Y+dy,461.6),2)),('M4_pedestal_head',cy((-43,Y+dy,439.6),(-43,Y+dy,443.6),3.5))]
emit('N10_Drive_side_pedestal_hardware',hw,'Two M4x18 nominal bottom-entering screws for custom pedestal to rail saddle; final thread engagement and tool access pending.','steel reference',silver)
for filename in ['housing_parameters.json','knee_parameters.json']:
 v=json.loads((OUT/filename).read_text());v['chain_plane_x_mm']=CHAIN_X;v['driver_move_from_released_v12_mm']=10;v['custom_drive_side_pedestal']=True;(OUT/filename).write_text(json.dumps(v,indent=2))
result={'chain_plane_x':CHAIN_X,'custom_pedestal':'Left drive side, bearing centre unchanged','standoff_mm':6.395}
