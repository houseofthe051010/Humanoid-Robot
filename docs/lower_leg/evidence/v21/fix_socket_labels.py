exec(compile((ROOT/'v21/common.py').read_text(),'<common>','exec'))
o=getpart(wg,'W07_');shape=TM.copy(o.createForAssemblyContext(wg).bRepBodies.item(0))
# Re-cut after joining the carrier arches; their roots crossed the earlier bore.
sub(shape,tx(rotoval(981,1040,5.15,4),dy=15))
for z in (993,1004):sub(shape,cy((0,Y+25-16,z),(0,Y+25+16,z),2.15))
world_replace(wg,o,[('W07_upper_roll_GWK_carrier_finished_spine_bore',shape)],o.component.description+' Final continuous oval bore after all arch unions.',plastic)
guide=getpart(wg,'U06_').component
for sk in guide.sketches:
 for t in sk.sketchTexts:
  t.isVerticalFlip=True;t.height=1.4 if '360 mm' not in t.text else 1.1
# Add the formerly omitted socket/spine pair to the neutral and support checks.
s=(OUT/'check_waist.py').read_text().replace("pairs=[('W05','W06')","pairs=[('W07','W08'),('W05','W06')")
exec(compile(s,'<neutral final fit>','exec'))
