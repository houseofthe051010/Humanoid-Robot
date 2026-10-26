exec(compile((ROOT/'v13/common.py').read_text(),'<common>','exec'))
silver=ap('aluminum')
# Trim the drive-side saddle axially so both the chain and the 16T tooth tips clear.
c=parts['P01_Knee_side_rail_seat_L'].component;a=TM.copy(c.bRepBodies.item(0));sub(a,bx((-36,Y-50,440),(0,Y+50,510)))
emit(c.name,a,'38mm-wide CNC drive-side saddle, inner faceX-36 leaves1.395mm to sprocket. Two M4x20 side screws; two top-entering M4x45 pedestal screws.','6061-T6 nominal',silver)
c=parts['P02_Knee_rail_screws_and_sleeves_L'].component;bs=[(b.name,TM.copy(b))for b in c.bRepBodies if not b.name.startswith('M4x25_side_screw')]
for z in [465,481]:bs.append(('M4x20_side_screw',cy((-60,Y,z),(-40,Y,z),2)))
emit(c.name,bs,'Two M4x20 nominal side screws and retained crush sleeves; verify measured engagement.','steel reference',silver)
hw=[]
for dy in [-15,15]:hw += [('M4x45_pedestal_screw',cy((-43,Y+dy,444.2),(-43,Y+dy,489.2),2)),('M4_pedestal_head',cy((-43,Y+dy,489.2),(-43,Y+dy,493.2),3.5))]
emit('N10_Drive_side_pedestal_hardware',hw,'Two top-entering M4x45 pedestal screws; nominal6mm engagement. Thread fit/strength and assembly access pending.','steel reference',silver)
a=un(cy((-7.5,Y,Z),(-4.5,Y,Z),16),cy((CHAIN_X-FACE/2,Y,Z),(-4.5,Y,Z),8));sub(a,cy((CHAIN_X-FACE/2-1,Y,Z),(CHAIN_X-FACE/2+8,Y,Z),3.1))
emit('P06_Gearbox_output_REFERENCE',a,'16mm output shaft with3mm flange,0.5mm axial gaps to cover and motor boss; bearing/carrier/coupling undefined.','aluminum reference',silver)
for n in ['P07_Motor_output_sprocket_BLANK','N03_Sprocket_blank_LAYOUT']:
 c=parts[n].component;c.description=c.description.replace('X-24','X-31').replace('X=-24','X=-31')
result={'sprocket_to_saddle_axial_gap_mm':1.395,'pedestal_screws':'M4x45 top entry','shaft_bearing_vendor_reference_intersection':'retained baseline, not fitted bearing validation'}
