exec(compile((ROOT/'v21/common.py').read_text(),'<common>','exec'))
def rearoval(z0,z1,r=5,flat=4):return tx(rotoval(z0,z1,r,flat),dy=15)
assert not any(o.component.partNumber.startswith('U01_') for o in wg.component.occurrences),'Already built'
ni=json.loads((OUT/'neutral_inventory.json').read_text())
ground=min(ni['ground']);height=1600.2;spine_top=ground+1400.2;yr=Y+25
report={'ground_z_mm':ground,'height_mm':height,'shoulder_height_mm':1340.2,'shoulder_spacing_mm':360,'neck_base_height_mm':1400.2,'head_bottom_height_mm':1420.2,'head_width_mm':150,'head_height_mm':180,'upper_arm_mm':260,'forearm_mm':240,'hand_envelope_mm':150,'spine_z_mm':[982,spine_top],'spine_section_xy_mm':[18,10],'spine_wall_mm':0.55,'battery_envelope_xyz_mm':[140,85,160],'battery_bounds_mm':[[-70,yr-100,1056],[70,yr-15,1216]],'battery_arrangement':'36 cells, 6 across X by 6 up Z; cell axes Y. 22.5 mm pitch. 134.05 x 70.15 x 134.05 raw cell envelope. Remaining space is provisional insulation, enclosure, busbar and BMS/wiring allowance.','BMS_bay_mm':[134,77,22],'material_status':'Prototype packaging, not strength-qualified. Battery is a solid envelope, not a cell/wiring design.'}
progress('rotate and extend spine with matching socket')
sp=getpart(wg,'W08_');socket=getpart(wg,'W07_');hardware=getpart(wg,'W16_')
tube=rearoval(982,spine_top);sub(tube,rearoval(981,spine_top+1,4.45,4))
for z in (993,1004,1067,1085,1192,1210):sub(tube,cy((0,yr-8,z),(0,yr+8,z),2.15))
world_replace(wg,sp,[('W08_spine_90deg_extended',tube)],'18X x 10Y oval spine rotated 90 degrees around its vertical centerline and extended to the proposed neck base. Retains provisional 0.55 mm wall; battery support requires structural verification.',silver)
progress('add rectangular battery envelope and spine-mounted cradle')
bat=newpart(wg.component,'U01_Battery_12S3P_21700_ENVELOPE','Provisional 36-cell pack including dedicated BMS and wiring bay. 140 X 85 Y 160 Z mm; not an electrical design.','Battery package envelope')
bbody=add(bat.component,bx(*report['battery_bounds_mm']),'Battery_pack_140x85x160_BMS_included',black)
tray=newpart(wg.component,'U02_Battery_lower_cradle','Prototype spine sleeve, bottom shelf and strap slots; cross-bolted to spine. Strength and printed fit not qualified.','PA12-CF provisional')
shape=un(rrxy(-75,75,yr-105,yr+14,1048,1054,8),rearoval(1048,1100,10,4))
# Retaining edges outside the pack plus slots for a strap around the pack.
un(shape,bx((-75,yr-100,1053),(-71,yr-16,1068)),bx((71,yr-100,1053),(75,yr-16,1068)),bx((-71,yr-105,1053),(71,yr-101,1068)))
sub(shape,rearoval(1047,1101,5.15,4))
for x in (-68,68):sub(shape,rrxy(x-2,x+2,yr-66,yr-36,1047,1055,1.5))
for z in (1067,1085):sub(shape,cy((0,yr-16,z),(0,yr+16,z),2.15))
add(tray.component,shape,'Spine_battery_lower_cradle',plastic)
pad=newpart(wg.component,'U03_Battery_bottom_pad_REFERENCE','2 mm nominal isolation pad under battery.','Elastomer reference')
add(pad.component,bx((-70,yr-100,1054),(70,yr-15,1056)),'Battery_bottom_pad_2mm',plastic)
upper=newpart(wg.component,'U04_Battery_upper_restraint','Spine-mounted upper crossbar and strap guide. Strap not modeled.','PA12-CF provisional')
shape=un(rearoval(1180,1222,10,4),rrxy(-75,75,yr-15,yr-7,1190,1216,3))
sub(shape,rearoval(1179,1223,5.15,4))
for x in (-68,68):sub(shape,bx((x-2,yr-16,1194),(x+2,yr-6,1212)))
for z in (1192,1210):
 sub(shape,cy((0,yr-16,z),(0,yr+16,z),2.15))
 sub(shape,cy((0,yr-16,z),(0,yr-10,z),3.75))
add(upper.component,shape,'Spine_battery_upper_strap_support',plastic)
bolts=newpart(wg.component,'U05_Battery_cradle_M4_REFERENCES','Four M4 transverse bolts with nominal internal crush sleeves; length and fits provisional.','Steel hardware references')
for z in (1067,1085,1192,1210):
 add(bolts.component,un(cy((0,yr-10,z),(0,yr+10,z),2),cy((0,yr-13,z),(0,yr-10,z),3.5),cy((0,yr+10,z),(0,yr+13,z),3.5)),f'M4_cradle_crossbolt_{z}',silver)
 sleeve=sub(cy((0,yr-4.4,z),(0,yr+4.4,z),3),cy((0,yr-4.5,z),(0,yr+4.5,z),2.15))
 add(bolts.component,sleeve,f'Crush_sleeve_reference_{z}',silver)
for o in (bat,tray,pad,upper,bolts):rigid(wg.component,sp,o,'U_joint_'+o.component.partNumber)
(OUT/'upper_layout.json').write_text(json.dumps(report,indent=2));result=report
