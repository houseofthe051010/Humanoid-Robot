from pathlib import Path
import json,shutil

out=Path(__file__).parent
repo=Path(r'C:\Users\rshan\Documents\GitHub\Humanoid-Robot\docs\lower_leg')
v=json.loads((out/'validation.json').read_text())
r=json.loads((out/'archive_reopen_verification.json').read_text())
assert not v['static_interferences'] and not any(p['interferences'] for p in v['waist_poses'])
assert not v['geometry_issues'] and not v['feature_issues'] and not v['invalid_joints']
assert r['spine_bound_error_mm']<.01 and len(r['inward_6010_outputs'])==2
for version in ('v17','v18'):
    source=out.parent/version
    evidence=repo/'evidence'/version;evidence.mkdir(parents=True,exist_ok=True)
    for p in source.glob('*.py'):shutil.copy2(p,evidence/p.name)
    for p in source.glob('*.json'):shutil.copy2(p,evidence/p.name)
    notes=(source/'REVISION_NOTES.md').read_text()
    if version=='v17':
        notes='> Historical checkpoint. [V18](HIP_WAIST_V18.md) supersedes its exposed hip references, roll opening/journal arrangement and 6010 orientation.\n\n'+notes
    else:
        notes+='\nThe final native archive reopened successfully with the expected joints, vertical neutral spine and both measured 6010 output normals pointing inward.\n'
    (repo/('HIP_WAIST_'+version.upper()+'.md')).write_text(notes,encoding='utf-8')
    bom=source/'deliverables'/('BOM_'+version.upper()+'.csv')
    if bom.exists():shutil.copy2(bom,repo/bom.name)
    for name in (f'{version}_overall_hips_and_waist.png',f'{version}_right_hip_open_interfaces.png',f'{version}_correct_scalloped_7010_mount.png',f'{version}_estimated_shell_cutaway.png',f'{version}_blended_fork_isolated.png'):
        p=source/'deliverables'/name
        if p.exists():shutil.copy2(p,repo/name)
print('Published v18 design record, historical v17 record, price-free BOMs, images and evidence.')
