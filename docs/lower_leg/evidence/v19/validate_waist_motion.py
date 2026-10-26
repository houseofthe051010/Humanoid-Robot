exec(compile((ROOT/'v19/common.py').read_text(),'<v19 common>','exec'))
report={'poses':[],'scope':'nine inherited waist poses; new waist skin plus inherited waist parts and hip stationary envelopes; not full hip travel'}
wa={o.component.partNumber.split('_')[0]:o.createForAssemblyContext(wg) for o in wg.component.occurrences}
js=[wg.component.asBuiltJoints.itemByName(n) for n in ('WJ00_waist_yaw','WJ01_lower_waist_roll','WJ02_upper_waist_pitch')]
def overlap(a,b):
    if not a.boundingBox.intersects(b.boundingBox):return 0
    shape=TM.copy(a);assert TM.booleanOperation(shape,TM.copy(b),BT.IntersectionBooleanType);return shape.volume*1000
def check(a,b,hits):
    for aa in wa[a].bRepBodies:
        for bb in wa[b].bRepBodies:
            v=overlap(aa,bb)
            if v>.03:hits.append({'pair':a+'/'+b,'mm3':v})
try:
    for vals in ((0,0,0),(25,0,0),(-25,0,0),(0,25,0),(0,-25,0),(0,0,25),(0,0,-25),(15,15,15),(0,15,-15)):
        for j,a in zip(js,vals):j.jointMotion.rotationValue=math.radians(a)
        adsk.doEvents();hits=[]
        for a,b in (('W01','W04'),('W01','W05'),('W02','W04'),('W03','W04'),('W02','W05'),('W03','W05'),('W04','W05'),
                    ('W05','W06'),('W06','W07'),('W07','W08'),('W06','W09'),('W09','W10'),('W07','W11'),('W11','W12'),('W19','W20')):check(a,b,hits)
        report['poses'].append({'yaw_roll_pitch_deg':vals,'hits':hits})
finally:
    for j in js:j.jointMotion.rotationValue=0
    adsk.doEvents()
(OUT/'waist_motion_validation.json').write_text(json.dumps(report,indent=2));result={'poses':len(report['poses']),'hit_poses':sum(bool(x['hits']) for x in report['poses'])}
