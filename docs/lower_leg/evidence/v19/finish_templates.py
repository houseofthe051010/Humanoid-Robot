exec(compile((ROOT/'v19/common.py').read_text(),'<v19 common>','exec'))
cc=next(o.component for o in root.occurrences if o.component.name=='ZZ_V19_construction')
report=[]
# Restore the pitch bearing journal after the housing-envelope relief operation.
old=cc.bRepBodies.itemByName('Q03_curved_pitch_to_tube_fork');b=TM.copy(old)
un(b,pcyl(20.1,28.6,19.95));sub(b,pcyl(19,36,10))
for k in range(4):
    az=math.radians(45+90*k);a,z=15*math.cos(az),15*math.sin(az)
    sub(b,cy(pp(19,a,z),pp(37,a,z),2.2))
cc.features.removeFeatures.add(old);add(cc,b,'Q03_curved_pitch_to_tube_fork',silver)
# Rounded internal weight-relief pockets retain the bearing boss, perimeter
# register and the upper mounting sector. These are not through-holes.
for side,name in ((-1,'H06_roll_endcap_-1'),(1,'H06_roll_endcap_1')):
    old=cc.bRepBodies.itemByName(name);b=TM.copy(old);before=b.volume*1000
    for ang in (205,250,295,340):
        a=math.radians(ang);x=RX+44*math.cos(a);z=RZ+44*math.sin(a)
        lo,hi=(-31,-22) if side<0 else (16,25)
        sub(b,cy((x,Y+lo,z),(x,Y+hi,z),9))
    cc.features.removeFeatures.add(old);add(cc,b,name,silver)
    report.append({'part':name,'removed_mm3':before-b.volume*1000})
(OUT/'template_finish.json').write_text(json.dumps(report,indent=2));result=report
