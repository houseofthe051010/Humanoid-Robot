from pathlib import Path
import json,csv,shutil
OUT=Path(r'E:\Aditya\robot_sim\outputs\shin_cad_20260912\v14');REPO=Path(r'C:\Users\rshan\Documents\GitHub\Humanoid-Robot\docs\lower_leg');dest=OUT/'deliverables'
rows=[r for r in json.loads((dest/'cad_inventory.json').read_text())if r['side']=='Right_leg']
for r in rows:
 n=r['name']
 if n.startswith('N01'):
  r['description']='Aluminum knee stack slice; pivot CAD Z430.6mm. Existing oval sockets and fastening passages retained. Drive-side outer wall restored on slice1 to fully enclose the shin oval.'
 elif n.startswith(('N','P','Q','R01','T')):r['description']+=' V14: knee and upper assembly translated down5mm together; any V13 absolute-position references above are historical.'
fields=['id','cad_component','quantity_per_leg','quantity_pair','quantity_unit','nominal_material','status','description']
with (REPO/'BOM_V14.csv').open('w',newline='',encoding='utf-8')as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for i,r in enumerate(rows,1):w.writerow(dict(id=f'V14-{i:03}',cad_component=r['name'],quantity_per_leg=1,quantity_pair=2,quantity_unit='component/assembly group',nominal_material=r['material'],status='modeled inventory; ownership and manufacturing qualification not audited',description=r['description']))
text='''# V14 enclosed shin adapter and 5 mm knee lowering

September 21, 2026. The user's final instruction was to retain the v13 changes, fully enclose the shin oval in the aluminum knee adapter, and lower the knee by exactly5 mm. No chain dimensions were calculated or optimized in this revision.

The live `Bilateral_legs_v13` was preserved as `v14/Input_live_v13_preserved.f3d`. V14 imports that complete native archive and adds explicit join/cut/move features, retaining its existing components and joints. It does not replace the user's document or reconstruct the assembly from an older source.

## Changes

- Restored the missing drive-side outer wall in `N01_Aluminum_knee_stack_1`, from canonicalX−12 outward toX−21 in the previously relieved area. The adapter now surrounds the complete oval perimeter through the insertion region. Existing nominal0.1 mm socket clearance and screw/dowel passages remain open. The outside wall is nominal1.9 mm at its thinnest straight boundary; this is geometry, not strength qualification.
- Both shin tubes shorten5 mm at the top: length361.6 mm, Z69–430.6. Their upper cross-bolt holes move fromZ418 to413 to remain aligned with the adapter hardware.
- The knee, thigh and hip assembly moves down5 mm together. Knee pivot CADZ430.6; motor axisZ560. Thigh tube length remains234.8 mm. The upper-leg relative layout, custom bearing pedestal and sprockets are retained.
- Both mirrored legs receive the same changes. The native knee-axis sketch datum moves with the physical pivot.

**Height terminology:**430.6 mm is the pivot's CAD Z coordinate, not a newly measured ground-to-knee distance. The retained foot geometry is not based atZ0. The requested relative5 mm lowering is the controlled change; no foot or ground datum was changed.

## Checks and files

`validation.json` verifies enclosure at four cross-sections for each shin tube on both legs, no tube/adapter solid overlap, the new tube lengths, valid feature health and native knee following at0°/30°. `archive_reopen_verification.json` records reopening the saved native file. These are targeted geometry/joint checks, not chain clearance or strength approval. V13 chain-envelope clearance results must not be applied to the restored adapter wall.

Native file: `E:\\Aditya\\robot_sim\\outputs\\shin_cad_20260912\\v14\\deliverables\\Bilateral_legs_v14.f3d`.

Price-free [BOM_V14.csv](BOM_V14.csv) contains80 modeled component/assembly groups per leg. It is not an audited ownership list. Hardware quantities and unresolved interfaces otherwise carry forward from [BOM_V13.md](BOM_V13.md). The v13 STEP file remains historical; use the v14 native model for this revision.

![Restored adapter wall](enclosed_oval_adapter_v14.png)
'''
(REPO/'UPPER_LEG_V14.md').write_text(text,encoding='utf-8')
evidence=REPO/'evidence'/'v14';evidence.mkdir(parents=True,exist_ok=True)
for n in ['validation.json','edit_result.json','archive_reopen_verification.json']:shutil.copy2(OUT/n,evidence/n)
shutil.copy2(dest/'cad_inventory.json',evidence/'cad_inventory.json')
for p in OUT.glob('*.py'):shutil.copy2(p,evidence/p.name)
shutil.copy2(dest/'enclosed_oval_adapter_v14.png',REPO/'enclosed_oval_adapter_v14.png')
local=Path(r'E:\Aditya\robot_sim\docs\lower_leg')
for n in ['UPPER_LEG_V14.md','BOM_V14.csv']:shutil.copy2(REPO/n,local/n)
for p,heading,body in [
 (REPO/'README.md','# Current physical leg — v14 enclosed adapter','[V14 revision](UPPER_LEG_V14.md) restores full oval enclosure and lowers the knee5 mm. [Current price-free BOM](BOM_V14.csv). V13 remains historical.'),
 (REPO.parents[1]/'CAD'/'README.md','## Current physical leg — v14','See [v14 adapter correction](../docs/lower_leg/UPPER_LEG_V14.md) and [BOM](../docs/lower_leg/BOM_V14.csv). Native CAD: `E:\\Aditya\\robot_sim\\outputs\\shin_cad_20260912\\v14\\deliverables\\Bilateral_legs_v14.f3d`.'),
 (local/'BUILD_RECORD.md','## V14 — current','See [v14 correction](UPPER_LEG_V14.md) and [BOM](BOM_V14.csv). Full oval enclosure restored; knee lowered exactly5 mm from live v13. No chain redesign.'),
 (REPO.parents[1]/'Learning'/'HumanoidTraining'/'FILE_LOCATIONS.md','## Current physical leg v14 — September 21, 2026','Native: `E:\\Aditya\\robot_sim\\outputs\\shin_cad_20260912\\v14\\deliverables\\Bilateral_legs_v14.f3d`. Record: `docs/lower_leg/UPPER_LEG_V14.md`; BOM: `BOM_V14.csv`. Preserved live input in `v14/Input_live_v13_preserved.f3d`. V14 restores full shin-oval enclosure and lowers knee/upper assembly5 mm; CAD pivotZ430.6 is not a measured ground height. Older releases below are historical.')]:
 s=p.read_text(encoding='utf-8')
 if heading not in s:
  s=s.replace('# Current physical leg — v13','# Historical physical leg — v13').replace('## Current physical leg prototype — v13','## Historical physical leg prototype — v13').replace('## V13 paired legs — current','## V13 paired legs — historical').replace('## Current physical leg v13','## Historical physical leg v13')
  if p==REPO/'README.md':s=heading+'\n\n'+body+'\n\n'+s
  else:
   a,_,b=s.partition('\n');s=a+'\n\n'+heading+'\n\n'+body+'\n'+b
  p.write_text(s,encoding='utf-8')
print(json.dumps({'bom':str(REPO/'BOM_V14.csv'),'rows_per_leg':len(rows),'notes':str(REPO/'UPPER_LEG_V14.md')}))
