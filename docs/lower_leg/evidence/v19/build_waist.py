exec(compile((ROOT/'v19/common.py').read_text(),'<v19 common>','exec'))
co=next(o for o in root.occurrences if o.component.name=='ZZ_V19_construction');cc=co.component
src=(OUT/'build_geometry.py').read_text();exec(compile(src[src.index('def loft_z'):src.index('def save')],'<loft helpers>','exec'))
progress('build compact waist loft and curved tube saddles')
rows=[(778,0,Y,19,28),(794,0,Y,32,41),(823,0,Y,65,57),(852,0,Y,71,59),(879,0,Y,53,47),(896.8,0,Y,47,44)]
outer=loft_z(rows,'V19_compact_waist_outer')
innerrows=[(z,x,y,a-5,b-5) for z,x,y,a,b in rows]
innerrows[0]=(777,0,Y,14,23);innerrows[-1]=(897.8,0,Y,42,39)
sub(outer,loft_z(innerrows,'V19_electronics_cavity'))
for s in (1,-1):
    collar=pcyl(-24,18,59)
    if s<0:reflect(collar)
    un(outer,collar)
# Exact curved envelopes, rather than broad flat end cuts, bring the hips inward.
for s in (1,-1):
    envelope=un(cone(pp(-34.2),pp(-26),28.1,55.05),pcyl(-26,20,55.05),pcyl(20,28,57.1))
    un(envelope,pcyl(-42,-33,26.2),pcyl(28,65,35))
    if s<0:reflect(envelope)
    sub(outer,envelope)
    # Keep printed material clear of roll cases, both output cheeks and fork.
    rtool=rcyl(-48,42,63.8)
    if s<0:reflect(rtool)
    sub(outer,rtool)
sub(outer,cy((0,Y,875.8),(0,Y,904),39.05))
sub(outer,bx((-200,Y-150,896.8),(200,Y+150,950)))
for deg in (45,135,225,315):
    x,y=43*math.cos(math.radians(deg)),Y+43*math.sin(math.radians(deg))
    un(outer,cy((x,y,887.5),(x,y,896.8),5.8));sub(outer,cy((x,y,887),(x,y,898),2.3))
seams=[]
for s in (-1,1):
    for t,b in ((-8,58),(-8,-58)):
        p=pp(t,0,b);x=s*p[0];z=p[2]
        un(outer,cy((x,Y-9,z),(x,Y+9,z),5));sub(outer,cy((x,Y-10,z),(x,Y+10,z),2.2));seams.append([x,z])
slot=beam_y((-10,865),(10,865),5,Y+35,Y+80);sub(outer,slot)
report={'skin_section_offset_mm':5,'pitch_saddle_outer_radius_mm':59,'tube_radius_mm':55,'shells':[],'seam_bolt_centers_xz_mm':seams}
for name,cutter in (('W02_compact_waist_front',bx((-200,Y-150,750),(200,Y-.2,910))),('W03_compact_waist_rear',bx((-200,Y+.2,750),(200,Y+150,910)))):
    shape=ix(TM.copy(outer),cutter)
    add(cc,shape,name,plastic)
    key='W02_Waist_front_shell' if name.startswith('W02') else 'W03_Waist_rear_shell'
    world_replace(wg,wp[key],[(name+'_touching_pitch_layout',TM.copy(shape))],
                  'V19 curved hollow PA12-CF skin closely follows the touching pitch actuator backs. Motor tubes remain separate 110/106 aluminum.',plastic)
    report['shells'].append({'name':name,'volume_mm3':shape.volume*1000,'outer_shells':sum(not s.isVoid for s in shape.shells)})
co.isLightBulbOn=False
(OUT/'waist_build.json').write_text(json.dumps(report,indent=2));result=report
