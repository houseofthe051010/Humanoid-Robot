exec(compile((ROOT/'v21/common.py').read_text(),'<common>','exec'))
names={'W06_':'W06_PA12CF_pitch_to_roll_bridge','W09_':'W09_lower_pitch_bushings','W10_':'W10_lower_pitch_pin','W11_':'W11_upper_roll_bushings','W12_':'W12_upper_roll_pin','W17_':'W17_M3_lower_pitch_pin_reinforcement_REFERENCE','W18_':'W18_M3_upper_roll_pin_reinforcement_REFERENCE','W08_':'W08_spine_18X10Y_extended_REFERENCE'}
for p,n in names.items():
 o=getpart(wg,p);o.component.name=n;o.component.partNumber=n
for o in wg.component.occurrences:
 for b in o.component.bRepBodies:b.isLightBulbOn=True
# Axis-only travel based on successful final native pose checks. Combined
# reachable workspace is coupled, not the full rectangular product of limits.
check=json.loads((OUT/'waist_motion_validation.json').read_text())
assert check['max_closure_error_mm']<.01 and check['max_pose_error_deg']<.01
assert not any(p['hits'] for p in check['poses'])
for n,lo,hi in [('WJ01_lower_waist_pitch',-30,20),('WJ02_upper_waist_roll',-30,30)]:
 j=wg.component.asBuiltJoints.itemByName(n);ll=j.jointMotion.rotationLimits;ll.minimumValue=math.radians(lo);ll.maximumValue=math.radians(hi);ll.isMinimumValueEnabled=True;ll.isMaximumValueEnabled=True
wg.component.description='V21 casing-free GWK differential, lower pitch / upper roll, spine rearward 15 mm, 12S3P battery packaging and upper-body placement study. Tested pure-axis pitch -30/+20 and roll +/-30 degrees; combined +/-10 only. Coupled linkage workspace, not a rectangular full-range guarantee. No strength certification.'
cfg=json.loads((OUT/'upper_layout.json').read_text());cfg['native_tested_pitch_deg']=[-30,20];cfg['native_tested_roll_deg']=[-30,30];cfg['native_tested_combined_pitch_roll_deg']=[-10,10]
(OUT/'upper_layout.json').write_text(json.dumps(cfg,indent=2));result={'names_updated':list(names.values()),'native_limits':{'pitch':[-30,20],'roll':[-30,30]}}
