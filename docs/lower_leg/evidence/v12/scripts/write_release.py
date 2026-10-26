"""Publish measured v12 evidence and a price-free active assembly BOM locally."""
import csv,json,shutil
from pathlib import Path
OUT=Path(r'E:\Aditya\robot_sim\outputs\shin_cad_20260912\v12')
REPO=Path(r'C:\Users\rshan\Documents\GitHub\Humanoid-Robot\docs\lower_leg')
dest=OUT/'deliverables';data=json.loads((dest/'cad_inventory.json').read_text());rows=[r for r in data['inventory']if r['side']=='Right_leg']
fit=json.loads((OUT/'fit_validation.json').read_text());knee=json.loads((OUT/'knee_motion_summary.json').read_text());pair=json.loads((OUT/'bilateral_validation.json').read_text());reopen=json.loads((OUT/'archive_reopen_verification.json').read_text())
fields=['id','cad_component','quantity_per_leg','quantity_pair','quantity_unit','nominal_material','status','description']
with (REPO/'BOM_V12.csv').open('w',newline='',encoding='utf-8')as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for i,r in enumerate(rows,1):
  n=r['name'];ref=any(x in n for x in ['REFERENCE','BLANK','ENVELOPE'])
  status='provisional reference'if ref else('new custom interface; manufacturing review pending'if n.startswith(('P','Q'))else'retained lower-leg CAD component')
  w.writerow(dict(id=f'V12-{i:03}',cad_component=n,quantity_per_leg=1,quantity_pair=2,quantity_unit='component/assembly group',nominal_material=r['material'],status=status,description=r['description']))
lines=['# V12 active assembly BOM','',f'{len(rows)} component/assembly groups per leg; two legs. No prices. This lists modeled parts, not an audited ownership or purchase record. Quantities refer to the named component/group, not its separate CAD body count. See the historical [detailed lower-leg BOM](BOM.csv) for retained fastener groups. New hardware groups are clarified below.','','| ID | Component | Per leg | Pair | Nominal material |','|---|---|---:|---:|---|']
for i,r in enumerate(rows,1):lines.append(f"| V12-{i:03} | {r['name']} | 1 | 2 | {r['material']} |")
lines+=['','New hardware groups per leg: each P02 side group contains two M4x25 side screws and two crush sleeves (four screws/four sleeves total); P12 contains eight clamp screws and eight cover screws; P13 contains four recessed low-profile M4 screw envelopes; P14 contains four M4x12 motor screws. These are nominal CAD sizes, pending measured engagement and hardware selection. P01 bearing-seat fasteners and Q01–Q03 final fastening/access are not a completed purchase specification.','','P09 is one 6 mm support pin, 31 mm long in this layout. N06_L/R are each 246.8 mm of 18x10 oval tube; wall thickness of 0.55 mm remains assumed. Existing joint shafts are retained 8 mm parts; see their lower-leg BOM and strength record.','','Printed part material labels are assumptions. CAD appearances and nominal material metadata do not constitute validated PA-CF structural properties or a qualified mass model.']
(REPO/'BOM_V12.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
evidence=REPO/'evidence'/'v12';evidence.mkdir(exist_ok=True)
for name in ['fit_validation.json','knee_motion_validation.json','knee_motion_summary.json','bilateral_build.json','bilateral_validation.json','mirror_geometry_audit.json','axis_repair.json','archive_reopen_verification.json','appearance_finish.json','motor_case_parameters.json','hip_parameters.json']:
 shutil.copy2(OUT/name,evidence/name)
shutil.copy2(dest/'cad_inventory.json',evidence/'cad_inventory.json')
scriptdir=evidence/'scripts';scriptdir.mkdir(exist_ok=True)
for p in OUT.glob('*.py'):shutil.copy2(p,scriptdir/p.name)
for name in ['bilateral_legs_v12.png','motor_and_hip_v12.png','motor_case_open_v12.png']:
 shutil.copy2(dest/name,REPO/name)
localdocs=Path(r'E:\Aditya\robot_sim\docs\lower_leg');localdocs.mkdir(exist_ok=True)
for name in ['UPPER_LEG_V12.md','BOM_V12.csv','BOM_V12.md','FUTURE_WORK.md']:
 shutil.copy2(REPO/name,localdocs/name)
record=localdocs/'BUILD_RECORD.md';text=record.read_text(encoding='utf-8')
if '## V12 paired legs — current' not in text:
 text=text.replace('## V11 compact upper leg — current','## V11 compact upper leg — historical',1).replace('## V10 upper-leg layout — current','## V10 upper-leg layout — historical',1)
 text=text.replace('# Lower-leg build record','# Lower-leg build record\n\n## V12 paired legs — current\n\nSee [V12 construction and revision](UPPER_LEG_V12.md), [active price-free BOM](BOM_V12.csv), and [future work](FUTURE_WORK.md). Native source and paired assembly are in `E:\\Aditya\\robot_sim\\outputs\\shin_cad_20260912\\v12\\deliverables`. V12 starts from user-edited live v11, preserves rail/motor placement, replaces the rejected fairings with the functional circular case and adds the mirrored leg. All dated records below are historical and must not override v12 geometry.\n',1)
 record.write_text(text,encoding='utf-8')
cadreadme=REPO.parents[1]/'CAD'/'README.md';text=cadreadme.read_text(encoding='utf-8')
if '## Current physical leg prototype — v12' not in text:
 text=text.replace('## Simulation models','## Current physical leg prototype — v12\n\nThe 1600.2 mm humanoid physical prototype now has paired legs, circular knee-motor/gearbox housing and hip-attachment concepts. See [V12 build record](../docs/lower_leg/UPPER_LEG_V12.md) and [price-free BOM](../docs/lower_leg/BOM_V12.csv). Native CAD and STEP outputs are stored locally in `E:\\Aditya\\robot_sim\\outputs\\shin_cad_20260912\\v12\\deliverables`, separately from the older simulation assets below.\n\n## Simulation models',1)
 cadreadme.write_text(text,encoding='utf-8')
readme=REPO/'README.md';old=readme.read_text(encoding='utf-8')
if not old.startswith('# Current physical leg — v12'):
 old=old.replace('# Current physical leg — v11 compact, shelled upper leg','## Historical v11 compact, shelled upper leg',1)
 lead='''# Current physical leg — v12 paired legs and gearbox housing

V12 preserves the user's live v11 changes and adds fitted knee rail seats, a circular motor/gearbox case with 33 mm reserved depth, opposite-rail support, output/sprocket references and CNC hip-attachment concepts. The left and right leg groups use a provisional 260 mm centre spacing. The rejected cosmetic fairings are excluded from the active assembly.

See [revision and construction record](UPPER_LEG_V12.md), [price-free active BOM](BOM_V12.csv), [readable BOM](BOM_V12.md), and [future work](FUTURE_WORK.md). Native CAD, STEP and separate custom-part exports are in `E:\\Aditya\\robot_sim\\outputs\\shin_cad_20260912\\v12\\deliverables`.

![V12 paired legs](bilateral_legs_v12.png)

'''
 readme.write_text(lead+old,encoding='utf-8')
summary={'interface_interferences':fit['interferences'],'feature_warnings':fit['feature_warnings'],'unexpected_source_changes':fit['unexpected_changes'],'source_knee':knee,'pair_gap_mm':pair['neutral_sagittal_gap_mm'],'reopen':reopen}
(dest/'release_verification.json').write_text(json.dumps(summary,indent=2))
(dest/'README.md').write_text('''# V12 CAD deliverables

`Leg_gearbox_hip_v12_parametric.f3d` preserves editable source history. `Bilateral_legs_v12.f3d` contains Right_leg and Left_leg copied components with native lower-leg joints. `Bilateral_legs_v12.step` contains active visible geometry. `parts/` contains provisional new custom parts for each handed side.

The case reserves 33 mm for a future gearbox; no internal gears or chain are modeled. The 6 mm outer support pin and hip attachments are references pending bearings, hardware and load qualification. The 260 mm leg-centre spacing is a neutral packaging choice; full hip motion remains unchecked.

Construction documentation and price-free BOM: `C:\\Users\\rshan\\Documents\\GitHub\\Humanoid-Robot\\docs\\lower_leg\\UPPER_LEG_V12.md` and `BOM_V12.csv`. Read `release_verification.json` for actual checks. No impact strength or FEA pass is implied.
''',encoding='utf-8')
print(json.dumps({'bom':str(REPO/'BOM_V12.csv'),'rows_per_leg':len(rows),'pair_gap_mm':pair['neutral_sagittal_gap_mm'],'fit_interferences':len(fit['interferences']),'knee':knee,'reopen':reopen},indent=2))
