exec(compile((ROOT/'v21/common.py').read_text(),'<common>','exec'))
yr=Y+25;o=getpart(wg,'W05_');vendor=next(b for b in o.createForAssemblyContext(wg).bRepBodies if 'vendor' in b.name.lower())
base=un(cy((0,Y,901.5),(0,Y,910),18.5),rrxy(-48,48,Y-27,yr+18,909,916,9))
for xa,xb in ((-21,-13),(13,21)):
 un(base,bx((xa,yr-12,913),(xb,yr+12,927)),cy((xa,yr,927),(xb,yr,927),12))
sub(base,cy((-23,yr,927),(23,yr,927),5.05))
for xa,xb in ((-47,-40),(40,47)):
 un(base,bx((xa,Y-27,913),(xb,Y-13,935)),cy((xa,Y-20,935),(xb,Y-20,935),7))
sub(base,cy((-49,Y-20,935),(49,Y-20,935),3.1))
sub(base,TM.copy(vendor));sub(base,cy((0,Y,901),(0,Y,911),7.3))
for k in range(6):
 a=math.radians(30+60*k);x,y=12.5*math.cos(a),Y+12.5*math.sin(a)
 sub(base,cy((x,y,901),(x,y,917),1.7));sub(base,cy((x,y,906.5),(x,y,917),2.9))
world_replace(wg,o,[('GWK7010_vendor_output_MOVING',TM.copy(vendor)),('W05_lower_pitch_base_with_30deg_rod_clearance',base)],'V21 lower pitch base and raised M6 shaft ears. Supports moved 4 mm outward each side to X40..47, retaining rod-end centers X+/-30. Rounded printed base 96 mm wide.',plastic)
o.component.bRepBodies.item(0).appearance=black
b=o.component.bRepBodies.item(1)
f=fillet_edges(o.component,b,2,lambda e:adsk.core.Line3D.cast(e.geometry) and abs(e.boundingBox.minPoint.z*10-916)<.01 and abs(e.boundingBox.maxPoint.z*10-916)<.01 and e.length*10>5,'V21_widened_pin_support_root_R2')
pin=getpart(wg,'W21_');rows=[]
for b in pin.createForAssemblyContext(wg).bRepBodies:
 rows.append((b.name,cy((-51,Y-20,935),(51,Y-20,935),3) if b.name=='6mm_double_supported_pin' else TM.copy(b)))
world_replace(wg,pin,rows,'6 mm steel shaft reference, 102 mm overall; rod-end centers remain 60 mm apart. Supports X40..47 each side.',silver)
def ring(a,b,ro,ri):return sub(cy(a,b,ro),cy(a,b,ri))
rows=[]
for a,b in ((-39.8,-34.5),(-25.5,25.5),(34.5,39.8)):
 rows.append(('M6_pin_inner_ring_spacer',ring((a,Y-20,935),(b,Y-20,935),4.25,3.1)))
for a,b in ((-51,-47),(47,51)):rows.append(('M6_pin_retainer_reference',ring((a,Y-20,935),(b,Y-20,935),5,3)))
world_replace(wg,getpart(wg,'W22_'),rows,'Spacers and retainers updated to the 102 mm pin and outward-shifted supports. Rod-end centers unchanged.',silver)
cfg=json.loads((OUT/'waist_build.json').read_text());cfg['base_pin_length_mm']=102;cfg['base_pin_support_x_mm']=[[-47,-40],[40,47]];cfg['pin_support_shift_each_mm']=4
(OUT/'waist_build.json').write_text(json.dumps(cfg,indent=2));result={'pin_length_mm':102,'rod_center_spacing_mm':60,'support_shift_each_mm':4,'R2_root_fillets':bool(f)}
