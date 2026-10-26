exec(compile((ROOT/'v17/common.py').read_text(),'<v17 common>','exec'))
report=[]
for go,center in ((right,130),(left,-130)):
    ps=parts(go);progress('restore matching knee '+go.component.name)
    for base in ('N04_Knee_pillow_block_','P01_Knee_side_rail_seat_','P02_Knee_rail_screws_and_sleeves_'):
        donor=ps[base+'R'].component;target=ps[base+'L'].component
        copies=[(b.name,reflect(TM.copy(b),center)) for b in donor.bRepBodies]
        replace(target,copies,'V17 mirror of opposite stock part. Full original bearing/saddle geometry restored; chain clearance intentionally not changed or checked.')
        report.append({'group':go.component.name,'target':base+'L','donor':base+'R','bodies':len(copies)})
    hw=ps['N10_Drive_side_pedestal_hardware'].component
    rows=[]
    for sx in (-43,43):
        x=center+sx
        for yy in (-20.9,20.9):
            b=un(cy((x,Y+yy,439.2),(x,Y+yy,480.2),2.5),cy((x,Y+yy,480.2),(x,Y+yy,484.2),4.25))
            rows.append(('V17_M5_knee_bearing_mount_REFERENCE',b))
    replace(hw,rows,'Four nominal M5 top-entry screws for matching knee saddles and original pillow blocks. Thread and length reference only.',silver)
(OUT/'knee_restoration.json').write_text(json.dumps(report,indent=2));result=report
