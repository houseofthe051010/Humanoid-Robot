from pathlib import Path
import json,csv,shutil
OUT=Path(r'E:\Aditya\robot_sim\outputs\shin_cad_20260912\v15')
repo=Path(r'C:\Users\rshan\Documents\GitHub\Humanoid-Robot');rd=repo/'docs/lower_leg';local=Path(r'E:\Aditya\robot_sim\docs\lower_leg')
rows=json.loads((OUT/'inventory.json').read_text())
active=[r for r in rows if r['side'] in ['Right_leg','Waist_layout_v15']]
fields=['id','cad_component','subassembly','quantity_per_leg','quantity_robot_pair','quantity_unit','nominal_material','status','description']
with (rd/'BOM_V15.csv').open('w',newline='',encoding='utf-8')as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for i,r in enumerate(active,1):
  waist=r['side']=='Waist_layout_v15';desc=r['description']
  if r['name'].startswith('R01'):desc='Estimated DJI10018 77KV knee motor,105mm OD and30mm black body. Photo-estimated mounting pattern and other geometry remain unmeasured. Axis CAD Z560. The former5mm rear encoder reservation is occupied by the new V15 sleeve; encoder packaging is unresolved.'
  w.writerow(dict(id=f'V15-{i:03}',cad_component=r['name'],subassembly='waist'if waist else'leg',quantity_per_leg=0 if waist else 1,quantity_robot_pair=1 if waist else 2,quantity_unit='component/assembly group',nominal_material=r['material'],status='modeled inventory; ownership and fabrication not audited',description=desc+' Earlier revision-specific positions in inherited descriptions are historical; see UPPER_LEG_V15.md.'))
notes='''# V15 slide-on motor mounts and waist layout

September 21, 2026. Built from the live v14 native design, preserved as `v15/Input_live_v14_preserved.f3d`. Native archive: `E:\\Aditya\\robot_sim\\outputs\\shin_cad_20260912\\v15\\deliverables\\Legs_and_waist_v15.f3d`. The original timeline, components and 101 native joints per leg are retained.

## Implemented geometry

- **Rear knee-motor mount:** continuous 125 mm oval sleeve with broad curved material spreading into the circular backplate. The passage is 10.2 × 18.2 mm for the existing 10 × 18 mm thigh oval. Outer sleeve section is 18 × 26 mm (nominal 3.9 mm wall before local reliefs). The four motor mounting bores and counterbores remain accessible. Three small phase-wire reliefs were cut. Obsolete enclosed clamp screw pockets were filled.
- **Sprocket side:** continuous 78 mm slide-on sleeve, outer 20 × 28 mm section, with the same oval passage. A curved upper 180° shell joins the top and both sides to the cover. Its loft sections use nominal 6 mm offsets; this is not a certified minimum wall thickness. The lower half of the new bridge remains open. The existing cover, sprocket, 6 mm support-pin reference and its 6.6 mm passage remain. No chain dimensions or chain route were calculated.
- The five former split-cap/support components per leg are hidden, and their M4 clamp hardware is removed. Four external M3 case ties per leg remain. Assembly is by sliding the continuous sleeves over the oval tubes before fitting the end structures. Final axial retention, fits and assembly access still need detailing.
- **Hip-pitch references:** 110 mm outside diameter × 50 mm axial depth, retaining the 25° tilt. The mounting/front face stays fixed; the extra 10 mm extends only behind the old 40 mm envelope. These are unselected motor envelopes, not a new vendor motor specification.
- **Waist yaw:** one duplicate of the existing GWK7010 geometry, centered between the legs at X0/Y23.343134, vertical shaft. Body bottom Z876; output top approximately Z904. This follows the user's explicit yaw-axis clarification.
- **Waist casing:** curved front and rear plastic halves surrounding both pitch envelopes and the waist yaw reference. Nominal section offsets are 5 mm, with 6 mm radial pitch-motor barrels, motor-shaped pockets, a yaw collar, four M4 seam-hole provisions, a 0.4 mm seam and a rear wiring opening. Detached slivers from bracket subtraction were removed; each half is one closed connected solid. No seam fasteners have been modeled or selected.

The 106 mm ID / 110 mm OD aluminum knee housing, knee position CAD Z430.6, motor axis Z560, 260 mm leg spacing, shin adapter enclosure and the previous 5 mm lowering are retained. CAD Z is not a measured ground height.

## Verification and limits

`evidence/v15/validation.json` records targeted intersections against visible neighboring parts, ten sleeve enclosure sections per leg, connected closed solids, native-joint validity and mount following at knee positions 0° and 30°. The waist casing has no measured solid overlap with the standing-pose motor/bracket references; the opposing pitch references and casing seam also do not overlap. `archive_reopen_verification.json` verifies the exported native file and its retained joints after reopening. Images were inspected after cleanup.

The waist group is an independent standing-pose reference, not a fully constrained pelvis or articulated hip assembly. The hip motor references still follow their respective thigh groups. There is no whole-body motion-clearance claim. The new plastic is not strength-, fatigue-, thermal- or print-qualified.

Fusion exited on the first archive-reopen attempt while several earlier designs were loaded. Recovery reopened the saved archive in a fresh Fusion session; the recovery report records its outcome. Existing recovered documents were left available. The cause of the process exit was not diagnosed.

**Encoder packaging changed:** the thicker rear sleeve occupies the former 5 mm encoder reservation behind the DJI hub. The hub itself clears the new mount, but the earlier encoder-space claim no longer applies. Revisit the encoder location before detailing electronics or machining interfaces.

The price-free [BOM_V15.csv](BOM_V15.csv) lists active modeled component/assembly groups for two legs and one waist. Hidden retired caps and construction lofts are excluded. Group quantities are not counts of every individual fastener, and ownership remains unaudited. The original price-free [BOM.csv](BOM.csv) and historical revision records remain available.

## Images

![Continuous sleeves and curved upper connection](mount_front_v15.png)

![Curved waist casing with central yaw reference](waist_v15.png)
'''
(rd/'UPPER_LEG_V15.md').write_text(notes,encoding='utf-8')
e=rd/'evidence/v15';e.mkdir(parents=True,exist_ok=True)
for n in ['validation.json','mount_parameters.json','waist_parameters.json','finish_geometry.json','inventory.json','archive_reopen_verification.json']:shutil.copy2(OUT/n,e/n)
for p in OUT.glob('*.py'):shutil.copy2(p,e/p.name)
for n in ['mount_front_v15.png','mount_rear_v15.png','waist_v15.png','legs_and_waist_v15.png']:
 shutil.copy2(OUT/'deliverables'/n,rd/n);shutil.copy2(OUT/'deliverables'/n,local/n)
for n in ['UPPER_LEG_V15.md','BOM_V15.csv']:shutil.copy2(rd/n,local/n)
for p,heading,body in [
 (rd/'README.md','# Current physical legs and waist — v15','[V15 slide-on mounts and waist](UPPER_LEG_V15.md). [Current price-free modeled BOM](BOM_V15.csv). Includes central vertical-axis waist yaw and110×50mm hip-pitch envelopes. V14 below is historical.'),
 (repo/'CAD/README.md','## Current physical legs and waist — v15','See [v15 design record](../docs/lower_leg/UPPER_LEG_V15.md) and [BOM](../docs/lower_leg/BOM_V15.csv). Native: `E:\\Aditya\\robot_sim\\outputs\\shin_cad_20260912\\v15\\deliverables\\Legs_and_waist_v15.f3d`.'),
 (repo/'Learning/HumanoidTraining/FILE_LOCATIONS.md','## Current physical legs and waist v15 — September 21, 2026','Native: `E:\\Aditya\\robot_sim\\outputs\\shin_cad_20260912\\v15\\deliverables\\Legs_and_waist_v15.f3d`. Repo record: `docs/lower_leg/UPPER_LEG_V15.md`; price-free BOM: `BOM_V15.csv`. Continuous slide-on mounts,110×50 pitch references and central vertical waist yaw with curved casing. Waist is standing-pose reference; encoder packaging needs revision. Older releases below are historical.'),
 (local/'BUILD_RECORD.md','## V15 — current','[Slide-on mounts and waist](UPPER_LEG_V15.md), [BOM](BOM_V15.csv). Existing lower-leg geometry and native joints retained. Central waist motor is yaw, vertical shaft.')]:
 s=p.read_text(encoding='utf-8')
 if heading not in s:
  s=s.replace('# Current physical leg — v14','# Historical physical leg — v14').replace('## Current physical leg — v14','## Historical physical leg — v14').replace('## Current physical leg v14','## Historical physical leg v14').replace('## V14 — current','## V14 — historical')
  first,sep,rest=s.partition('\n')
  if p==rd/'README.md':s=heading+'\n\n'+body+'\n\n'+s
  else:s=first+'\n\n'+heading+'\n\n'+body+'\n\n'+rest
  p.write_text(s,encoding='utf-8')
p=rd/'FUTURE_WORK.md';s=p.read_text(encoding='utf-8');h='## September 21 — v15 priorities'
if h not in s:
 a,_,b=s.partition('\n');p.write_text(a+'\n\n'+h+'''\n\n- Resolve encoder placement: the new rear slide sleeve occupies the old5mm reservation.
- Select print material/orientation, slide fit, axial retention and actual assembly sequence. Check plastic creep, motor heat, sleeve stress and the curved connections under gearbox reactions.
- Finalize waist yaw support bearings, bolt interfaces and motor/driver cooling. Add proper pelvis/hip joints and validate sweeps before treating the waist as articulated.
- Choose actual110×50 hip-pitch motors and recheck the pockets, wiring, attachment access and tolerances. The current motors are envelopes.
- Detail the waist seam fasteners and fastening bosses, service access and printed tolerances.
- Earlier chain questions remain deferred; the user's current scope explicitly excludes further chain calculations or neighboring bracket redesign.
\n'''+b,encoding='utf-8')
print(json.dumps({'bom_rows':len(active),'leg_groups':sum(r['side']=='Right_leg'for r in active),'waist_groups':sum(r['side']=='Waist_layout_v15'for r in active),'record':str(rd/'UPPER_LEG_V15.md')}))
