"""Publish v13 evidence and active, price-free component BOM after CAD verification."""
import csv,json,shutil
from pathlib import Path
OUT=Path(r'E:\Aditya\robot_sim\outputs\shin_cad_20260912\v13');dest=OUT/'deliverables'
REPO=Path(r'C:\Users\rshan\Documents\GitHub\Humanoid-Robot\docs\lower_leg')
data=json.loads((dest/'cad_inventory.json').read_text());rows=[r for r in data['inventory']if r['side']=='Right_leg' and r['body_count']>0]
fit=json.loads((OUT/'fit_validation.json').read_text());knee=json.loads((OUT/'knee_motion_summary.json').read_text());pair=json.loads((OUT/'bilateral_validation.json').read_text());reopen=json.loads((OUT/'archive_reopen_verification.json').read_text())
fields=['id','cad_component','quantity_per_leg','quantity_pair','quantity_unit','nominal_material','status','description']
with (REPO/'BOM_V13.csv').open('w',newline='',encoding='utf-8')as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for i,r in enumerate(rows,1):
  n=r['name'];status='retained modeled component; ownership not audited'
  if n.startswith(('P','N01','N03','N04_Knee_pillow_block_L','N09','N10')):status='v13 custom/reference interface; manufacturing review pending'
  if n.startswith(('Q','T'))or'REFERENCE'in n:status='provisional layout/reference'
  w.writerow(dict(id=f'V13-{i:03}',cad_component=n,quantity_per_leg=1,quantity_pair=2,quantity_unit='component/assembly group',nominal_material=r['material'],status=status,description=r['description']))
lines=['# V13 active assembly BOM','',f'{len(rows)} active component/assembly groups per leg, mirrored to two legs. No prices. This is modeled inventory, not an audited ownership or order list. A component containing screw heads, shafts and nuts counts as one group, not one physical piece. The inherited lower-leg fastener details remain in [BOM.csv](BOM.csv).','','| ID | CAD component | Per leg | Pair | Nominal material |','|---|---|---:|---:|---|']
for i,r in enumerate(rows,1):lines.append(f"| V13-{i:03} | {r['name']} | 1 | 2 | {r['material']} |")
lines += ['', '## Changed stock and hardware per leg', '', '- Two shin tubes:18×10 stadium,366.6 mm long; two thigh tubes:10×18 stadium,234.8 mm long. Wall0.55 mm is assumed. Confirm measured stock before cutting.', '- P03: one106ID/110OD aluminum tube,45 mm axial length, plus separate P15 rear plate and P05 front cover/bridge. Tube and plates are different parts.', '- P02 drive side: twoM4x20 side screws and two crush sleeves. Opposite side: twoM4x25 side screws and two sleeves.', '- N04 drive side: retained donor bearing/cartridge plus a custom CNC aluminum pedestal. Do not order or manufacture it as the original stock pillow block. N10: twoM4x45 top-entering pedestal screws.', '- P12: eight rail-clamp screw envelopes plus fourM3x60 external case ties with nut envelopes. P14: four estimated M4x12 motor screws. Confirm thread engagement against actual motor bosses.', '- N07: fourM3x60 stack ties/nuts, two6×55.605 mm dowels, twoM3x50 rail bolts/nuts, twoM3x10 set screws. Lengths are nominal layout sizes.', '- N09: one48 mm OD×6.395 mm sprocket standoff. P09: one6 mm diameter×39 mm opposite output support pin; bearing and retention undecided.', '- P07/N03: approximate8T/16T sprockets,7.21 mm face. P13 old four-bolt motor sprocket hardware is hidden/excluded.', '', 'No chain, tensioner, planetary gears, completed output-bearing set or driver electronics are included as finished hardware. Reference hubs/hip motors remain marked provisional. CAD materials are nominal metadata, not validated printed-material properties or mass/inertia data.']
(REPO/'BOM_V13.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
evidence=REPO/'evidence'/'v13';evidence.mkdir(parents=True,exist_ok=True)
for name in ['fit_validation.json','knee_motion_validation.json','knee_motion_summary.json','bilateral_build.json','bilateral_validation.json','archive_reopen_verification.json','housing_parameters.json','knee_parameters.json','source_copy.json','native_source_joints.json']:
 shutil.copy2(OUT/name,evidence/name)
shutil.copy2(dest/'cad_inventory.json',evidence/'cad_inventory.json')
scripts=evidence/'scripts';scripts.mkdir(exist_ok=True)
for p in OUT.glob('*.py'):shutil.copy2(p,scripts/p.name)
for n in ['bilateral_legs_v13.png','drive_layout_v13.png','motor_case_open_v13.png']:shutil.copy2(dest/n,REPO/n)
summary={'new_interface_interferences':len(fit['new_interface_interferences']),'chain_interferences':len(fit['chain_interferences']),'retained_vendor_reference_overlaps':len(fit['retained_vendor_reference_overlaps']),'source_knee':knee,'pair_gap_mm':pair['neutral_sagittal_gap_mm'],'reopen':reopen}
(dest/'release_verification.json').write_text(json.dumps(summary,indent=2))
record=REPO/'UPPER_LEG_V13.md';text=record.read_text(encoding='utf-8')
marker='## Saved release checks'
if marker in text:text=text[:text.index(marker)].rstrip()+'\n'
text+='\n'+marker+'\n\n'
text+=f"- Neutral audit: {fit['pair_body_tests']:,} body-pair checks; {len(fit['new_interface_interferences'])} new interface intersections and {len(fit['chain_interferences'])} chain-envelope intersections. {len(fit['retained_vendor_reference_overlaps'])} inherited donor bearing/set-screw overlaps are separately recorded.\n"
text+=f"- Source knee: {knee['poses']} sampled poses at0°,45°,90°,120°; {knee['collision_poses']} collision poses and {knee['error_poses']} Boolean-error poses. This is sampled clearance, not a continuous sweep or load simulation.\n"
text+=f"- Paired assembly: {pair['legs']['Right']['components']} components and {pair['legs']['Right']['joints']} native joints per leg; no invalid joints or empty visible solids. Reflected body bounds matched. Neutral separation between the two leg assemblies is{pair['neutral_sagittal_gap_mm']:.3f} mm; full hip motion remains unchecked.\n"
text+='- Both native archives were reopened and their joint/body checks repeated. Paired knee attachment following was checked again after import. STEP exports contain visible geometry only.\n'
record.write_text(text,encoding='utf-8')
(dest/'README.md').write_text('''# V13 CAD deliverables

`Leg_chain_v13_source.f3d` is a single-leg solid source with reconstructed native joints. `Bilateral_legs_v13.f3d` is the mirrored paired assembly. Neither archive recovers the original component feature history; the untouched live input is preserved one folder above. `Bilateral_legs_v13.step` contains visible geometry only. `parts/` contains selected provisional component STEP exports, not approved manufacturing drawings.

Implemented:106ID/110OD aluminum tube, lowered motor, raised knee, extended shin rails, approximate8T/16T sprockets and common chain plane. Gearbox depth, chain tensioning, bearings, motor measurement and strength remain open. No impact-load approval is implied.

See `release_verification.json` for measured checks and the repository's `docs/lower_leg/UPPER_LEG_V13.md`, `BOM_V13.csv` and `FUTURE_WORK.md` for dimensions and limitations.
''',encoding='utf-8')
local=Path(r'E:\Aditya\robot_sim\docs\lower_leg')
for n in ['UPPER_LEG_V13.md','BOM_V13.csv','BOM_V13.md','FUTURE_WORK.md']:shutil.copy2(REPO/n,local/n)
for path,heading,body in [
 (REPO/'README.md','# Current physical leg — v13 chain packaging','See [v13 construction record](UPPER_LEG_V13.md), [price-free BOM](BOM_V13.csv), [readable BOM](BOM_V13.md) and [future work](FUTURE_WORK.md).\n\n![V13 paired legs](bilateral_legs_v13.png)'),
 (REPO.parents[1]/'CAD'/'README.md','## Current physical leg prototype — v13','The current physical prototype uses a106ID/110OD aluminum motor tube, approximate8T/16T sprockets and revised knee interfaces. See [v13 record](../docs/lower_leg/UPPER_LEG_V13.md) and [BOM](../docs/lower_leg/BOM_V13.csv). Local native/STEP files: `E:\\Aditya\\robot_sim\\outputs\\shin_cad_20260912\\v13\\deliverables`. Older simulation assets below are separate.'),
 (local/'BUILD_RECORD.md','## V13 paired legs — current','See [V13 construction record](UPPER_LEG_V13.md), [BOM](BOM_V13.csv) and [future work](FUTURE_WORK.md). This revision starts from preserved live v12 right-leg solids. Earlier dated records below are historical.'),
 (REPO.parents[1]/'Learning'/'HumanoidTraining'/'FILE_LOCATIONS.md','## Current physical leg v13 — September 21, 2026','Current paired archive: `E:\\Aditya\\robot_sim\\outputs\\shin_cad_20260912\\v13\\deliverables\\Bilateral_legs_v13.f3d`; single source: `Leg_chain_v13_source.f3d` in the same directory. Both contain copied solids and reconstructed native joints. Original live v12 backup: `v13/Input_live_v12_20260921_preserved.f3d`. Repo record: `docs/lower_leg/UPPER_LEG_V13.md`; price-free BOM: `BOM_V13.csv`. Check v13 evidence and preserve newer live edits. All older physical-prototype sections below are historical; Isaac training files remain separate.')]:
 text=path.read_text(encoding='utf-8')
 if heading not in text:
  text=text.replace('# Current physical leg — v12','## Historical physical leg — v12').replace('## Current physical leg prototype — v12','## Historical physical leg prototype — v12').replace('## V12 paired legs — current','## V12 paired legs — historical')
  if path.name=='README.md'and path.parent==REPO:text=heading+'\n\n'+body+'\n\n'+text
  else:
   first,sep,rest=text.partition('\n');text=first+'\n\n'+heading+'\n\n'+body+'\n'+rest
  path.write_text(text,encoding='utf-8')
print(json.dumps({'bom_rows_per_leg':len(rows),'verification':summary},indent=2))
