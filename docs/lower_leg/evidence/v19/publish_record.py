from pathlib import Path
import json,shutil
out=Path(__file__).parent;dest=out/'deliverables';repo=Path(r'C:\Users\rshan\Documents\GitHub\Humanoid-Robot')
reopen=json.loads((out/'archive_reopen_verification.json').read_text());fit=json.loads((out/'fit_validation.json').read_text());motion=json.loads((out/'waist_motion_validation.json').read_text())
assert reopen['parametric'] and not fit['hits'] and not fit['geometry_issues'] and not fit['feature_issues'] and motion['max_closure_error_mm']<.05 and not any(p['hits'] for p in motion['poses'])
notes=(out/'REVISION_NOTES.md').read_text().replace('Work in progress until the native export and reopened-archive evidence exist.','Native archive exported and reopened successfully. The preserved input and the prior v18 archive remain available.')
notes=notes.replace('## Design boundaries\n\n## Added waist differential','## Added waist differential')
notes=notes.replace('These are prototype interfaces.','## Design boundaries\n\nThese are prototype interfaces.')
notes+='\n## Verified release checks\n\n'
notes+=f'- Targeted standing hip fit: no remaining reported solid intersections, disconnected bodies, invalid joints or unhealthy features in the checked parts.\n- Native waist: {len(motion["poses"])} sampled poses, including combined corners; maximum closure error {motion["max_closure_error_mm"]:.3g} mm, maximum rod-end tilt {motion["max_rod_end_tilt_deg"]:.4f}°, and no reported intersections in the documented pair set.\n- Archive reopened: all four aluminum sleeves remain 110/106 mm; hip roll and yaw are concentric in X; leg center spacing is {reopen["leg_axis_spacing_mm"]:.3f} mm; neutral spine is vertical and the 6010 output faces point inward.\n- These are sampled CAD and kinematic checks, not a continuous collision proof, manufacturing approval or strength analysis.\n'
(out/'REVISION_NOTES.md').write_text(notes)
docs=repo/'docs/lower_leg';ev=docs/'evidence/v19';ev.mkdir(parents=True,exist_ok=True)
(docs/'HIP_WAIST_V19.md').write_text(notes)
shutil.copy2(dest/'BOM_V19.csv',docs/'BOM_V19.csv')
for name in ('v19_waist_drive.png','v19_complete_revision.png','v19_front_preview.png','v19_isolated_Q02.png','v19_isolated_Q03.png'):
 shutil.copy2(dest/name,docs/name)
for path in out.glob('*.py'):shutil.copy2(path,ev/path.name)
for name in ('fit_validation.json','waist_motion_validation.json','waist_kinematic_report.json','waist_drive_geometry.json','waist_drive_joints.json','6010_output_partition.json','archive_reopen_verification.json','edge_rounds.json','pitch_touch_committed.json','carrier_socket_relief.json','final_geometry_audit.json','export.json'):
 shutil.copy2(out/name,ev/name)
native=str(dest/'Legs_hip_waist_v19.f3d')
route=f'''## Current physical hips and waist v19 — September 26, 2026

Native: `{native}`. Record: `docs/lower_leg/HIP_WAIST_V19.md`; price-free BOM: `BOM_V19.csv`; scripts/checks: `docs/lower_leg/evidence/v19`. Preserved live v18 input: `v19/Input_live_v18_user_edits_preserved.f3d`. Inspect newer live edits before changing the archive.

110OD/106ID aluminum pitch/roll tubes retain estimated 105 mm DJI10018 references. Pitch centers X±46.808 bring the nearest rear tube rims together; tilt remains25°. Roll/yaw centers X±120 (240 mm spacing), with centered dual-sided roll-output yokes and curved separate housing forks. Custom gearboxes remain undesigned. Waist now includes lowered inward-facing GIM6010s (X±63.5, Z995), 26 mm cranks, a raised double-supported6 mm cross-pin, copied ankle M6 rod ends and short M6 rods. Native two-loop waist limits: pitch±20°, roll±5°. User explicitly kept6.25°-limit M6 rod ends instead of additional physical swivels; do not claim±30° travel. An861-pose math grid gives1.036–1.949 per-actuator Jacobian magnitudes and5.674° maximum tilt. Nine native pose checks and archive reopen passed; no load qualification. The output partition moves with each crank. Historical v18 details below are superseded.

'''
paths=[repo/'Learning/HumanoidTraining/FILE_LOCATIONS.md',Path(r'C:\Users\rshan\.codex\skills\humanoid-robot-training\references\fusion-lower-leg-workflow.md'),Path(r'E:\Aditya\robot_sim\docs\lower_leg\BUILD_RECORD.md')]
for path in paths:
 txt=path.read_text(encoding='utf-8-sig');first,rest=txt.split('\n',1)
 if '## Current physical hips and waist v19' not in txt:path.write_text(first+'\n\n'+route+rest.replace('## Current physical hips and waist v18','## Historical physical hips and waist v18').replace('## Current v18 hip shells','## Historical v18 hip shells'),encoding='utf-8')
readme=docs/'README.md';txt=readme.read_text(encoding='utf-8-sig')
if not txt.startswith('# Current physical legs and waist — v19'):
 readme.write_text('# Current physical legs and waist — v19\n\n[V19 compact hips and linked waist](HIP_WAIST_V19.md). [Component BOM](BOM_V19.csv). Touching pitch rear rims,110/106 aluminum sleeves, centered bilateral hip adapters, and a low6010 waist differential with M6 links. Initial waist limits are±20° pitch and±5° roll with the existing rod ends. Prototype geometry; see the record for validation scope and unfinished gearbox work.\n\n![V19 waist](v19_waist_drive.png)\n\n'+txt.replace('# Current physical legs and waist — v18','# Historical physical legs and waist — v18',1),encoding='utf-8')
print(json.dumps({'native':native,'record':str(docs/'HIP_WAIST_V19.md'),'evidence':str(ev)},indent=2))
