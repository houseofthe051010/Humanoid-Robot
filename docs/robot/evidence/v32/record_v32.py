import csv,json,shutil
from pathlib import Path
out=Path(__file__).parent
repo=Path('C:/Users/rshan/Documents/GitHub/Humanoid-Robot')
docs=repo/'docs/robot';mirror=Path('E:/Aditya/robot_sim/docs/robot')
release=json.loads((out/'saved_release32.json').read_text())
inv=json.loads((out/'final_native_inventory32.json').read_text())
checks={n:json.loads((out/(n+'.json')).read_text()) for n in ('pose_invariants32','mount_contact32','native_cover_motion32','native_compound_motion32','clearance_checks32','native_reopen32','native_archive_integrity32')}
assert checks['pose_invariants32']['pass_'] and checks['native_reopen32']['pass_'] and checks['native_cover_motion32']['pass_'] and checks['clearance_checks32']['all_sampled_clear']
archive=Path(release['archive']);handoff=Path('C:/Users/rshan/Downloads/Humanoid_v32_CAD')
handoff.mkdir(exist_ok=True);shutil.copy2(archive,handoff/archive.name)
shutil.copytree(out/'deliverables/modified_parts_STEP',handoff/'modified_parts_STEP',dirs_exist_ok=True)
(handoff/'previews').mkdir(exist_ok=True)
for p in out.glob('robot_v32*.png'):shutil.copy2(p,handoff/'previews'/p.name)
history=docs/'history/v31';history.mkdir(parents=True,exist_ok=True)
for p in docs.iterdir():
 if p.is_file() and p.suffix in ('.md','.csv'):shutil.copy2(p,history/p.name)
(history/'STATUS.md').write_text('# V31 checkpoint\n\nThe v31 waist and structural mechanism are retained. The user rejected the inherited bulky shin/ankle covers and hip collar; v32 replaces those cosmetic parts with shallow perforated shin plates and compact oval-rail hip collars. V31 remains a recoverable native checkpoint.\n')
evidence=docs/'evidence/v32';evidence.mkdir(parents=True,exist_ok=True)
for p in out.iterdir():
 if p.suffix in ('.json','.py') or p.name.startswith('robot_v32') and p.suffix=='.png':shutil.copy2(p,evidence/p.name)
for n in checks:shutil.copy2(out/(n+'.json'),handoff/(n+'.json'))
text='''# Humanoid robot — current build

**CAD v32 · October 1, 2026 · local documentation only.**

V32 replaces the bulky all-side shin covers with four 2.5 mm perforated front plates. Six existing carrier bores per leg locate the upper attachments; shallow saddles and strap slots secure the lower plates to the existing 18 × 10 mm oval rails. Rear skins, calf accents and ankle cowls are hidden. The carrier, motors, rods and steel rails stay in their original positions.

Both hip-yaw collars now fit the existing oval rails and crossheads. The envelope is 131.6 × 84 × 36.5 mm; the old right collar was about 141.6 × 128 × 53 mm. Each collar has separate front/rear halves, a 0.6 mm seam, 2.5 mm nominal skin and two integral oval clamp pads. The previously missing left collar is restored. Broader thigh panels below the collar and the enlarged continuous v31 waist remain unchanged.

![Native v32](evidence/v32/robot_v32_threequarter.png)

All 439 original occurrence transforms and 65 native joint definitions are preserved. Twelve leg axes and eight paired hip movements were checked in a disposable reopened archive; cover ownership followed correctly. New covers passed the recorded neutral mechanism checks and discrete hip-yaw sweep. Full native export independently reopens. These checks do not qualify strength, fastener preload, print retention or continuous full-body clearance.

Training remains on frozen physical_v29 with the provisional 34.46 kg mass estimate. CAD v32 is not loaded into the active policy. The existing supervisor retains its 300 MiB reserve, 180-second headroom rule and 8192 ceiling; inspect its live monitor before quoting status.

[CAD and STEP parts](EXPORTS.md) · [Casings](CASING_DESIGN.md) · [BOM](BOM.md) · [Evidence](EVIDENCE.md) · [Previous v31](history/v31/STATUS.md).
'''
(docs/'BUILD_REPORT.md').write_text(text,encoding='utf-8')
(docs/'CASING_DESIGN.md').write_text('''# Casings — v32

Use the root **Casings** eye to show/hide the cosmetic parts. Original physical-owner constraints are unchanged. Hidden obsolete parts stay hidden when the root toggle is restored.

![Shin plates](evidence/v32/robot_v32_shin_plates.png)

The shin covers are two front plates per leg, 2.5 mm thick, with rounded outlines and 6.4 mm perforations. Their maximum width is 96 mm and the lower end tapers to 54 mm. Upper plate Z263–384 mm; lower plate Z118–262 mm. Conformal standoffs fit the existing carrier and steel rail surfaces, with M3 clearance bores at X±10 mm relative to each leg and Z244/314/366 mm. Lower locating saddles use 18.6 × 10.6 mm oval clearance; strap slots retain them without drilling the rails. Screw lengths, removable straps, printing material and fatigue/retention require a physical trial.

Sides and rear are open. The old rear shell halves, ankle cowls and two blue calf accents are retained hidden. Existing straight carrier side walls remain structural frame parts.

![Open rear](evidence/v32/robot_v32_open_shin_rear.png)

The hip-yaw collars are 131.6 × 84 × 36.5 mm around the original rails/crossheads, about 34% less depth than the previous 128 mm collar. Each splits into two pieces with a 0.6 mm seam, 2.5 mm nominal skin, 10.6 × 18.6 mm clamp bores and M3 seam bores. The bottom is Z666 mm; the top ends at Z702.5 mm below the moving cradle. Final clamp hardware and fit remain provisional.

![Hip collars](evidence/v32/robot_v32_hip_collars.png)

The four broader thigh skins, v31 continuous waist, hip adapters, shoulders, knee covers, hands and shoes are unchanged. Motor spacings and joint axes are preserved. No mass/contact update was made to training.
''',encoding='utf-8')
(docs/'EXPORTS.md').write_text(f'''# CAD exports — v32

Native source: **{release['document']}**, saved version {release['version']}; `{release['datafile_id']}`.

Full independently reopened archive: `C:/Users/rshan/Downloads/Humanoid_v32_CAD/Humanoid_complete_v32.f3d`.

Six edited component STEP files are in `modified_parts_STEP` alongside it: four perforated shin plates and two split hip collars. STEP collar files contain both front/rear solids. Native previews and verification JSONs are included.

Construction, preserved v31 input and all evidence: `E:/Aditya/robot_sim/outputs/shin_cad_20260912/v32`.

Archive CRC, full Fusion reopen, original placements/joints and targeted cover movement checks passed. This is prototype CAD, not manufacturing or dynamics qualification. Prior v31 remains preserved at its original location. Training remains frozen physical_v29.
''',encoding='utf-8')
with (docs/'BOM.csv').open(newline='',encoding='utf-8-sig') as f:r=csv.DictReader(f);fields=r.fieldnames;rows=list(r)
changes={
 'CAS-05':dict(item='Perforated front shin plates',quantity='4',unit='plate',status='V32 native prototype; fit/retention pending',evidence='v32/shin_plates32.json; native_reopen32.json',notes='2.5 mm front-only plates. Six existing M3 carrier bores per leg; lower open oval saddles and strap slots. Rear skins hidden.'),
 'CAS-08':dict(item='Torso identifier',quantity='1',notes='Two obsolete calf accents are hidden in v32; torso identifier retained.'),
 'CAS-13':dict(quantity='0',status='Hidden by user request in v32',notes='Bulky ankle cowls removed from active display; original frame remains exposed.'),
 'CAS-14':dict(item='Compact split hip-yaw collars',quantity='4',unit='half',status='V32 native prototype; clamp fit/hardware pending',evidence='v32/hip_collars32.json; clearance_checks32.json',notes='Two halves per hip, 131.6 x 84 x 36.5 mm envelope; 2.5 mm skin, .6 mm seam, 10.6 x 18.6 mm oval clamp bores. Original rails/crosshead retained.')}
for row in rows:
 if row['id'] in changes:row.update(changes[row['id']])
for id,item,quantity,unit,notes in (
 ('CAS-22','Removable shin plate retention straps','4','strap','Two per leg through lower plate slots around existing oval rails; width and retention method to fit physically.'),
 ('CAS-23','Hip collar M3 seam closure hardware','4','set','Two per hip; internally supported seam bores. Select screw length and insert/nut retention after prototype fit.'),
 ('CAS-24','Shin plate M3 attachment screws','12','screw','Six per leg using unchanged frame bores and fitted standoffs. Select thread engagement and replacement lengths; do not double-count superseded short screws.')):
 row={k:'' for k in fields};row.update(id=id,category='Casing hardware',item=item,quantity=quantity,unit=unit,status='Interface modeled; hardware selection pending',evidence='v32 native CAD and mount_contact32.json',notes=notes);rows.append(row)
with (docs/'BOM.csv').open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
(docs/'BOM.md').write_text('# Robot BOM — v32\n\nPrototype quantities from current native CAD. Prices omitted; final fit, materials and hardware selection remain open. See BOM.csv for full evidence and notes.\n\n| ID | Item | Quantity | Status |\n|---|---|---|---|\n'+'\n'.join(f"| {r['id']} | {r['item']} | {r['quantity']} {r['unit']} | {r['status']} |" for r in rows)+'\n',encoding='utf-8')
with (docs/'CASING_INVENTORY.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.writer(f);w.writerow(['component','body','owner','bounds_mm','volume_mm3'])
 for p in inv['parts']:
  if p['path'].startswith('Casings:'):w.writerow([p['part'],p['body'],p['owner'],json.dumps(p['bounds_mm']),p['volume_mm3']])
# Full current parts data, keeping the source inventory schema explicit.
with (docs/'CAD_PARTS.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.writer(f);w.writerow(['component','body','owner','kind','bounds_mm','volume_mm3'])
 for p in inv['parts']:w.writerow([p['part'],p['body'],p['owner'],p['kind'],json.dumps(p['bounds_mm']),p['volume_mm3']])
(docs/'EVIDENCE.md').write_text('# V32 verification\n\n'+''.join(f'- [{n}.json](evidence/v32/{n}.json)\n' for n in checks)+'\nNeutral intersections and discrete yaw samples passed. Twelve leg axes and eight paired hip moves verified native ownership on a disposable copy; original live pose untouched. Original439 occurrence transforms and65 joints preserved; one left collar occurrence added. Full archive CRC and independent reopen passed. No full continuous collision, printing, strength or thermal qualification.\n',encoding='utf-8')
for name,heading,body in [
 ('MECHANICAL_OVERVIEW.md','Current v32 covers','V32 changes cosmetic shin plates and hip-yaw collars only. The v31 enlarged waist, adapters and straight ankle holder side walls are retained. All original placements/joints are preserved.'),
 ('OPEN_ITEMS.md','V32 remaining work','Select and fit-test longer carrier screws, two lower plate retention straps per leg and two M3 hip collar seam screws per side. Check printed saddle/oval tolerance, clamp preload, panel vibration, continuous travel and strength. Broad thigh skins are unchanged. No measured mass or training asset migration is included.')]:
 p=docs/name;p.write_text('# '+heading+'\n\n'+body+'\n\n'+p.read_text(encoding='utf-8'),encoding='utf-8')
for p in docs.iterdir():
 if p.is_file() and p.suffix in ('.md','.csv'):shutil.copy2(p,mirror/p.name)
shutil.copytree(evidence,mirror/'evidence/v32',dirs_exist_ok=True)
shutil.copytree(history,mirror/'history/v31',dirs_exist_ok=True)
(handoff/'README.md').write_text('''# Humanoid v32 CAD

Open **Humanoid_complete_v32.f3d** in Fusion. Six edited component STEP files are in `modified_parts_STEP`; hip collar files each contain front/rear halves. Native images are in `previews`.

- Four thin perforated shin front plates; open sides/rear and no ankle cowls.
- Compact split hip-yaw collars around the existing oval rails/crossheads.
- V31 enlarged waist, mechanical frame, motors and all original joints retained.
- Root Casings eye toggles cosmetic parts; old rear shells remain hidden.

![Native v32](previews/robot_v32_threequarter.png)

Included JSON records document unchanged placements, seated mounts, native leg movement, discrete clearances, archive CRC and independent full reopen. Printing, straps, screw lengths, preload and structural strength require physical qualification. Training remains frozen physical_v29.
''',encoding='utf-8')
locations=repo/'Learning/HumanoidTraining/FILE_LOCATIONS.md'
locations.write_text('# Critical file locations\n\n## Current CAD v32 — October 1, 2026\n\nNative source Humanoid_complete_v32. Handoff `C:/Users/rshan/Downloads/Humanoid_v32_CAD`; scripts/evidence `E:/Aditya/robot_sim/outputs/shin_cad_20260912/v32`. Read current docs/robot report/BOM. Thin perforated front shin plates replace bulky wraparound shells; compact split hip-yaw collars fit oval rails. Original mechanism and v31 waist retained; all439 original transforms and65 joint definitions preserved. Native movement, discrete clearance, archive CRC and independent reopen passed. Printing/retention/strength remain provisional. Training stays on frozen physical_v29. Preserve newer live user edits before changing CAD. Local docs only; no commit/push.\n\n'+locations.read_text(encoding='utf-8').replace('# Critical file locations\n','',1).replace('## Current CAD v31','## Previous CAD v31',1),encoding='utf-8')
skill=Path('C:/Users/rshan/.codex/skills/humanoid-robot-training')
(skill/'references/physical-v32-covers.md').write_text('''# Physical v32 — thin leg covers

Current native source Humanoid_complete_v32; verified full F3D and six STEP components at C:/Users/rshan/Downloads/Humanoid_v32_CAD. Evidence/scripts in E:/Aditya/robot_sim/outputs/shin_cad_20260912/v32. Read current docs/robot report/BOM and preserve live edits.

User rejected full wraparound shin casing: frame already exists. Use shallow front-only 2.5 mm perforated plates with open sides/rear, existing six M3 carrier bores, lower open oval saddles and strap slots. Old rear skins/ankle cowls/calf accents stay hidden. User requested smaller hip casing around oval rails: two compact split hip-yaw collars,131.6 x84 x36.5mm,2.5mm skins,.6mm seam and oval clamp pads. Left collar restored. Broader thigh panels unchanged. V31 waist/adapters/structural carrier walls and all original motor placements/joints retained. Training remains frozen physical_v29.

Native tests: all439 original transforms,65 joint definitions,12 leg single-axis cover-follow tests,8 paired hip poses,neutral new-cover mechanism clearance and discrete hip-yaw sweep; archive CRC/full reopen passed. Final screws,strap retention,material,manufacturing and continuous collision/strength remain unqualified.

API lessons: exact tangent motor envelopes can create tiny real overlaps on a slightly tilted right thigh. Keep explicit positive clearance; clamp saddles must clear the central yaw case and collar top must end below the moving cradle. Preserve separate mounted component bodies under the existing Casings owner groups. Use RemoveFeatures for superseded bodies and hide replaced rear shells without moving underlying mechanisms.
''',encoding='utf-8')
p=skill/'SKILL.md';s=p.read_text(encoding='utf-8');s=s.replace('## Start with evidence','## Current physical CAD v32\n\nRead [references/physical-v32-covers.md](references/physical-v32-covers.md) for the latest shallow shin plates and compact oval-rail hip collars. V31 waist and structural mechanism are retained; inherited bulky shin/ankle shells were rejected. Training stays frozen physical_v29.\n\n## Start with evidence',1).replace('Current CAD v31 retains','The retained v31 mechanism keeps');p.write_text(s,encoding='utf-8')
p=skill/'references/fusion-lower-leg-workflow.md';s=p.read_text(encoding='utf-8');s=s.replace('## Current physical CAD v31','## Current physical CAD v32 — October 1, 2026\n\nRead [physical-v32-covers.md](physical-v32-covers.md) and the current local report/BOM. V32 replaces bulky shin/ankle cosmetic shells with thin front plates and tightens the hip-yaw collars around the existing oval rails. V31 waist/structure are retained.\n\n## Previous physical CAD v31',1);p.write_text(s,encoding='utf-8')
(out/'documentation_handoff32.json').write_text(json.dumps(dict(handoff=str(handoff),docs=str(docs),local_only=True,archive=str(archive)),indent=2))
print(json.dumps(dict(handoff=str(handoff),parts=len(inv['parts']),docs=str(docs))))
