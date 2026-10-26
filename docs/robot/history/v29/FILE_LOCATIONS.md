# Critical file locations

## Current walking reward repair — October 1, 2026

Authoritative run pointer is `E:/Aditya/robot_sim/physical_v29/training/ACTIVE_RUN.json`.
The r6 measured-step chain replaces the stationary walking incentive and starts
from r4's passed standing actor. See `docs/robot/TRAINING_REWARD_REPAIR_20261001.md`.
Read live state/gates before claiming progress; old dated pointers below are
historical. No Git commit/push.

## Current physical robot v29 — CAD September 30 / training October 1, 2026

Read `C:/Users/rshan/Documents/GitHub/Humanoid-Robot/docs/robot/BUILD_REPORT.md`, `BOM.csv`, `SIMULATION.md` and `EXPORTS.md`. Saved source **Humanoid_complete_v29_revised**, version 2, `urn:adsk.wipprod:dm.lineage:WTKBF_3ORCqcrKBaU4opCw`, includes corrected hand/wrist mesh placement. Current independently reopened full F3D: `E:/Aditya/robot_sim/outputs/shin_cad_20260912/v29/wrist_review_20260930/Humanoid_complete_v29_wrists_aligned.f3d`. Original version1/checkpoints/release remain preserved. The old STEP omits mesh hands and is geometry-only.

Current height1600.2 mm; +30 mm thigh rails, −20 mm torso, 275/250 mm arms, dual-shaft RDS51160 elbows using authorized RDS51150 size proxy, and continuous hip-output clearance in structural waist holders. Native clean tree:42 rigid/mechanism groups,372 occurrences,1537 visible BReps/eight meshes,47 constraints including23 anatomical revolutes. Actual saved ranges/frame map are `v29/native_joint_map_saved.json`; do not substitute construction-time ranges where save/reopen differences were measured.

Current isolated package: **`E:/Aditya/robot_sim/physical_v29`**. URDF `assets/humanoid_physical_v29.urdf`, USD and all configuration layers, current `assets/actuator_limits.json` and `hardware_actuators.py`; null pending file is historical. Profile `eff95_elbow7_20260930` uses95% added transmission/linkage efficiency,7 N·m/45 RPM elbow and120 RPM shoulder pitch. All23 strict movement/FK/reset checks and all23 larger GUI preview axes pass. Evidence: `validation/eff95_elbow7_20260930` and `_visual`. GUI command: `test_joints.py --device cpu --hardware_actuators --visual_fast --seconds_per_joint 2.5 --repeat` using the existing Isaac Python. Corrected hand visual STLs are synchronized. Actual masses, loaded/thermal duty and contact dynamics remain unqualified. See current local report and `docs/robot/TRAINING.md`: a separate free-base stand/walk/run chain started October 1; no learned stage is claimed passed at this handoff. Older22-axis assets and older Downloads handoff remain separate/history.

Documentation/BOM/skill changes are local only; no Git commit or push.

## Current physical-v29 locomotion and mass estimate — October 1, 2026

Entry point: `E:/Aditya/robot_sim/physical_v29/training/README.md`. Read `ACTIVE_RUN.json`, then the live state it indicates; active handoff run is `runs/locomotion_20261001_r2`. Frozen source, config hashes, 150-update training blocks, separate nominal/push gates, checkpoint rollback and 300 MiB GPU reserve are documented there. 8,192 environments was the measured fastest count. This dated pointer is not proof of current process liveness.

Weight basis: `training/MASS_ESTIMATE.md`, `mass_estimate.json`, `mass_by_link.csv`; local report copies are `docs/robot/MASS_ESTIMATE.md` and `MASS_BASIS.csv`. Conservative 34.46 kg includes battery and 640 g/hand; official 400 g complete-hand value gives 33.98 kg. The 24 kg movement-fixture proxies and old 38 kg training robot are separate. Contact/mass asset is `training/assets/robot_training.urdf`, not the original full-visual movement asset. Review `training/RESEARCH.md`, `research/sources.json` and the preserved old GIF/video samples for the policy research and limitations.

## Historical physical robot v27 — September 30, 2026

Current report/BOM: `C:/Users/rshan/Documents/GitHub/Humanoid-Robot/docs/robot/BUILD_REPORT.md` and `BOM.csv`. Casing detail/inventory: `CASING_DESIGN.md`, `CASING_INVENTORY.csv` in that folder. Working Fusion document **Humanoid_complete_v27**, complete/unmodified saved version 3 (`urn:adsk.wipprod:dm.lineage:cNq9ppTGSpuNdIKGufBJ0w`). Construction, exact native captures, static/sample checks and release: `E:/Aditya/robot_sim/outputs/shin_cad_20260912/v27`.

The 43 new cosmetic solids preserve the v26 skeleton, original 1,785 BRep signatures, eight meshes, 367 placements, 333 joints and all 23 anatomical values. Current inventory totals 1,828 BRep signatures, eight meshes and 410 occurrences. Full-cover static fit and ten targeted hip-cap samples pass at recorded scope; continuous workspace, final attachments, printer fit, strength and added mass/dynamics remain unqualified. Full F3Z file/dependency integrity passes; native standalone package reimport was not performed. See `docs/robot/EXPORTS.md` for each file's actual qualification. Documentation remains local, no Git commit/push.

## Historical mechanical checkpoint v26 — September 30, 2026

Authoritative current physical report: `C:/Users/rshan/Documents/GitHub/Humanoid-Robot/docs/robot/BUILD_REPORT.md`. Whole-robot BOM: `C:/Users/rshan/Documents/GitHub/Humanoid-Robot/docs/robot/BOM.csv`; hand/source evaluation: `C:/Users/rshan/Documents/GitHub/Humanoid-Robot/docs/robot/HAND_OPTIONS.md`. The clean report consolidates the older leg, waist, torso, head and arm records; the dated entries below are historical.

Working full Fusion document **Humanoid_complete_v26**. Construction and validation directory: `E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26`. Current exported files and their scopes are indexed in `C:/Users/rshan/Documents/GitHub/Humanoid-Robot/docs/robot/EXPORTS.md`. Inspect `saved_release.json`, `saved_source_comparison26.json`, `full_f3z_integrity_audit.json` and the relevant `release26_reopen_*.json` for their separate save, source comparison, package-integrity and module-reopen verdicts. Previous verified upper/waist v25 compact archives are preserved in `E:/Aditya/robot_sim/outputs/shin_cad_20260912/v25/deliverables`. Earlier full standalone local F3D archives have legacy external-reference metadata; the current full backup uses F3Z with its declared dependency.

Current physical nominal height **1590.2 mm**. Shoulder centre spacing394 mm; upper arm260 mm and forearm240 mm. Head pitch axis lowered18 mm and head/camera12 mm from v25; actual servo size retained. Full-scale AmazingHand source uses eight SCS0009 microservos per hand, three fingers plus thumb, with no Fusion finger joints. MG90 board conversions are not proven mechanical substitutes. The intended body hierarchy has23 axes, including hip pitch/roll/yaw on each leg and backward knee flexion. Use measured native-joint reports rather than the separate old Isaac pitch-axis convention.

Documentation/BOM cleanup is local only, with no Git commit or GitHub push. Physical CAD is not yet a dynamics-qualified replacement for the simplified training asset.

## Historical torso, shoulders and electronics v24 — September 29, 2026

Full robot cloud document: `Humanoid_shoulders_electronics_v24`, saved version 4 (data file `urn:adsk.wipprod:dm.lineage:TIrirgGUQnK1gWkzM1Jnow`). Inspect newer live edits before starting. Verified portable upper assembly: `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v24\deliverables\Torso_shoulders_electronics_v24.f3d`; matching STEP and native preview images are beside it. Record: `docs/lower_leg/TORSO_SHOULDERS_V24.md`; evidence: `docs/lower_leg/evidence/v24`. The full local F3D retains legacy external-reference metadata and cannot reopen as a new local design; it is diagnostic-only under `v24/diagnostic_archives`. Use the full cloud document or verified compact archive.

Continues the user's straight, rearward v23 spine and old waist motor layout; abandoned V-spine work and original cloud source are preserved. Torso attaches through an internal shoulder crossmember and two split oval-spine clamps. 6810 shoulder bearings are 50×65×7 mm. Generic pitch outputs carry perpendicular 80 OD×50 mm roll cylinders at X±197 mm, Y28, Z1325.363431. Each upper arm has a front driven flange and passive rear 6005 bearing on a fixed 25 mm journal. Forks extend 260 mm to the elbow, with nominal 34×10 mm rails. Neck retains 6005 25×47×12 and imported MG996/DS3230 surrogate, adding a 40 mm yaw output flange and head socket. Electronics enclosure above battery: 150×86×93 mm overall; 144×80×87 mm main cavity before screw bosses. Robot height remains1600.2 mm; shoulder height1340.2 mm above foot-floor datum.

Final checks: 100 single-lump solids; zero selected neutral non-fastener intersections; five native revolute direction/reset tests pass using precise bounds and occurrence matrices; 30 sampled pitch/outward-roll poses clear. Independently reopened upper archive contains100 solids and31 valid joints (five revolute). This is packaging/mechanism concept CAD, not load- or manufacturing-qualified. Actuator internals, removable pitch-hub inboard collar, neck coupling/outer-race retention, print splits, actual board standoffs and cable routing remain open.

API lessons: use `preciseBoundingBox` and occurrence matrices for rotation validation; coarse cached `boundingBox` gave false mismatches up to27 mm on curved bodies. Recut holes and output-flange relief after joining tapered fork rails. Keep complete shoulder backing rings and trim the shell mating interface. For `TemporaryBRepManager.deleteFaces(faces, deleteSpecifiedFaces)`, True deletes the listed faces; False keeps them and deletes the others. Compact archive import assigns automatic timestamp part numbers; identify components by preserved names, not semantic partNumber prefixes. AsBuiltJoint does not expose feature-style healthState; check validity and measured motion instead.

## Historical physical waist and battery v21 — September 27, 2026

Native full assembly: `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v21\deliverables\Humanoid_waist_battery_v21.f3d`. Independently reopened smaller assembly: `Waist_battery_v21.f3d` in that directory. Record: `docs/lower_leg/WAIST_BATTERY_V21.md`; price-free BOM: `BOM_V21.csv`; evidence: `docs/lower_leg/evidence/v21`. Preserve newer live edits and the untouched recovered-v19 input in the v21 working directory.

Use casing-free GWK6010-8 motors with exposed fixed **8-M2.5 / 40.5 mm PCD** mounts, inward outputs, retained six-M3 / 25 mm output PCD and 26 mm cranks. Waist is **lower pitch X, upper roll Y**, spine shifted 15 mm rearward. Rod eyes remain 60 mm apart. The 6 mm pin is now 102 mm long with supports moved 4 mm outward each side. The user's **35-degree rod-end tilt assumption supersedes v19's 6.25-degree assumption**; physical rod-end CAD remains a surrogate. Nine native samples pass targeted intersections and closure: pure pitch -30/+20, roll +/-30, combined +/-10 corners. Do not claim a full rectangular combined workspace or load qualification.

Battery is a provisional **140 x 85 x 160 mm** solid, 36 cells in a 6x6 grid plus a 134x77x22 mm BMS/wiring bay; no specific BMS selected. Lower cradle/pad and upper restraint support it on a rotated **18X x 10Y** oval spine extended to the proposed neck base. Retained 0.55 mm wall is not strength-qualified. Editable placement sketches give height **1600.2 mm**, shoulders at 1340.2 mm and 360 mm apart, neck base 1400.2 mm. Upper-body mechanisms are not designed yet. Existing legs/hip gearbox estimates are retained. Full archive exported; smaller waist archive reopened with 32 joints and correct axes/dimensions.

V21 API lessons: replacing bodies while an ungrounded jointed occurrence is being recomputed can insert subsequent bodies in a changed pose even when before/after transforms look neutral. Temporarily grounding the target occurrence during replacement corrected this; restore ground state and revalidate actual world bounds. Build a capsule bore from separate rectangular and cylindrical cuts if a union cutter leaves residual material. A successful Boolean alone is insufficient. Do not delete old linked joint history if it triggers unrelated feature recompute failures; preserve input and create a fresh component group with measured native joints. Keep compact component archives for reopen verification when duplicate full-assembly import is unstable.

## Historical physical hips and waist v19 — September 26, 2026

Native: `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v19\deliverables\Legs_hip_waist_v19.f3d`. Record: `docs/lower_leg/HIP_WAIST_V19.md`; price-free BOM: `BOM_V19.csv`; scripts/checks: `docs/lower_leg/evidence/v19`. Preserved live v18 input: `v19/Input_live_v18_user_edits_preserved.f3d`. Inspect newer live edits before changing the archive.

110OD/106ID aluminum pitch/roll tubes retain estimated 105 mm DJI10018 references. Pitch centers X±46.808 bring the nearest rear tube rims together; tilt remains25°. Roll/yaw centers X±120 (240 mm spacing), with centered dual-sided roll-output yokes and curved separate housing forks. Custom gearboxes remain undesigned. Waist now includes lowered inward-facing GIM6010s (X±63.5, Z995), 26 mm cranks, a raised double-supported6 mm cross-pin, copied ankle M6 rod ends and short M6 rods. Native two-loop waist limits: pitch±20°, roll±5°. User explicitly kept6.25°-limit M6 rod ends instead of additional physical swivels; do not claim±30° travel. An861-pose math grid gives1.036–1.949 per-actuator Jacobian magnitudes and5.674° maximum tilt. Nine native pose checks and archive reopen passed; no load qualification. The output partition moves with each crank. Historical v18 details below are superseded.


## Historical physical hips and waist v18 — September 26, 2026

Native: `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v18\deliverables\Legs_hip_waist_v18.f3d`. Record: `docs/lower_leg/HIP_WAIST_V18.md`; price-free BOM: `BOM_V18.csv`; validation, construction scripts and archive checks: `docs/lower_leg/evidence/v18`. The user's edited v16 source is preserved in `v17/Input_live_v16_user_edits_preserved.f3d`, and the v17 checkpoint also remains available.

Both hip motors are estimated DJI10018 77KV references (105 mm OD) inside separate estimated shells; no GIM10015 is used. Both roll openings are provisional 50 mm, narrow journals removed, forks widened with native lofts/fillets. Roll centers move to X±158 to leave room for complete pitch output flanges; thigh spacing remains260mm. The 7010 fixed mount uses its curved interface and 48 mm PCD small holes, output uses six small holes on 25 mm PCD. Hip yaw motors are 15 mm lower with 6007 bearing envelopes above. Knee pillow blocks/adapters match. Waist is yaw -> lower roll -> upper pitch with a vertical neutral spine and two inward-facing actual GIM6010-8 standard STEP references. Gearboxes and enlarged roll bearing/output interfaces remain to design. Check the live document for later user edits before modifying this saved revision.

## Historical physical legs and waist v15 — September 21, 2026

Native: `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v15\deliverables\Legs_and_waist_v15.f3d`. Repo record: `docs/lower_leg/UPPER_LEG_V15.md`; price-free BOM: `BOM_V15.csv`. Continuous slide-on mounts,110×50 pitch references and central vertical waist yaw with curved casing. Waist is standing-pose reference; encoder packaging needs revision. Older releases below are historical.


## Historical physical leg v14 — September 21, 2026

Native: `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v14\deliverables\Bilateral_legs_v14.f3d`. Record: `docs/lower_leg/UPPER_LEG_V14.md`; BOM: `BOM_V14.csv`. Preserved live input in `v14/Input_live_v13_preserved.f3d`. V14 restores full shin-oval enclosure and lowers knee/upper assembly5 mm; CAD pivotZ430.6 is not a measured ground height. Older releases below are historical.

## Historical physical leg v13 — September 21, 2026

Current paired archive: `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v13\deliverables\Bilateral_legs_v13.f3d`; single source: `Leg_chain_v13_source.f3d` in the same directory. Both contain copied solids and reconstructed native joints. Original live v12 backup: `v13/Input_live_v12_20260921_preserved.f3d`. Repo record: `docs/lower_leg/UPPER_LEG_V13.md`; price-free BOM: `BOM_V13.csv`. Check v13 evidence and preserve newer live edits. All older physical-prototype sections below are historical; Isaac training files remain separate.

## Compact physical leg v11 (September 19, 2026)

Current native:`E:\Aditya\robot_sim\outputs\shin_cad_20260912\v11\deliverables\Leg_compact_shelled_v11.f3d`. Current repo record:`docs/lower_leg/UPPER_LEG_V11.md`. Thigh320 mm;standing hip757.6 mm;knee motor85 mm lower;pitch25°;separate roll/yaw;curved removable shell. Read v11 validation evidence and preserve newer live edits. Earlier v10/v9 locations below are historical.


## Physical leg layout v10 (September 19, 2026)

Current native: `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v10\deliverables\Leg_layout_1600mm_v10.f3d`. Repo record: `docs/lower_leg/UPPER_LEG_V10.md`; open questions: `FUTURE_WORK.md`; upper-leg BOM: `UPPER_LEG_BOM.csv`. Lower-leg baseline remains v9 below. Inspect and preserve any newer live edits. Target height1600.2 mm;thigh400 mm;standing hip837.6 mm. Fit/motion verified, strength unresolved.

## Physical lower-leg CAD v9 (documentation updated September 19, 2026)

This is the physical shin prototype, distinct from the older whole-body Isaac training asset. Latest verified saved release is **v9**; preserve newer live Fusion edits before using that archive as a starting point.

| Need | Location |
|---|---|
| Consolidated construction, design history, parts, calculations and open issues | `E:\Aditya\robot_sim\docs\lower_leg\BUILD_RECORD.md` |
| Price-free current per-leg BOM; unresolved hardware marked | `C:\Users\rshan\Documents\GitHub\Humanoid-Robot\docs\lower_leg\BOM.csv` |
| V9 changes and knee strength screening | Repo `docs/lower_leg/V9_CHANGES.md` and `KNEE_STRENGTH_V9.md` |
| Current native release | `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v9\deliverables\Compact_shin_392mm_v9.f3d` |
| CAD skill's current Fusion bridge and simulation workflow | `C:\Users\rshan\.codex\skills\humanoid-robot-training\references\fusion-lower-leg-workflow.md` |

The September 17 user screenshots show a simplified Static Stress model but no verified solved FEA. Later collar-gap/steel-sleeve concepts are not confirmed implemented. The legacy fixed1.15 ankle ratio is not the current physical shin's configuration-dependent transmission.

Use this index before searching the whole workspace. These are the authoritative or most useful files for CAD, actuator limits, diagnostics, torque tests, training, and visual review.

## Historical reverse-curriculum supine recovery v12 (September 6)

V11 stopped cleanly after 600 PPO iterations. Its floor-escape stage passed at
0.395755 m, but the 10%-assisted rise stage exhausted its budget with an
unassisted mean maximum height of 0.529459 m versus the 0.55 m gate and 0/64
strict stands. V12 preserves every v11 artifact and resumes its best checkpoint
in a new directory. It uses 45-degree -> 65-degree -> 80-degree -> tucked-supine
-> randomized-supine training starts while tapering training-only upward
assistance from 35% to zero. All promotion gates are unassisted.

| Need | Location |
|---|---|
| Exact v12 reward/action/termination configuration | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v12_reverse_curriculum\candidate.py` |
| Reverse schedule, immutable bootstrap, gates and GPU fallback | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v12_reverse_curriculum\chain.py` |
| Design and warnings | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v12_reverse_curriculum\README.md` |
| Active 8,192-environment run | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v12_reverse_20260906_033513\` |
| Authoritative live status | Same run, `state.json` |
| CPU contracts and 64/8,192 smokes | Same run, `contract_tests.log`, `preflight.json`, `p00_smoke64_train`, `p01_smoke64_reload`, `p02_benchmark_8192` |
| GPU trace and promotion evidence | Same run, `gpu.csv`, newest `*_gate.json`, per-evaluation `evaluation.json` and `telemetry.npz` |
| Preserved v11 best bootstrap | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v11_height_first_20260905_232453\01_assist10_rise_0400_8192\candidate.pt` |
| Exact failure/revision/launch report | `C:\Users\rshan\Documents\GitHub\Humanoid-Robot\Learning\HumanoidTraining\GETUP_REVERSE_CURRICULUM_2026-09-06.md` |

Preflight passed 31 CPU contracts, a four-iteration 64-environment train and
reload smoke, and a four-iteration 8,192-environment allocation smoke. Peak
sampled GPU memory was 6,809 MiB with 1,379 MiB free, above the required 512 MiB
reserve. Both discovery reward terms were finite and nonzero in all 8,192
environments. Main training then advanced through at least iteration 8 at 8,192
environments. These are execution checks, not recovery success.

The early reverse and height gates remain discovery-only. Never describe them
as standing. Only the final independent unassisted 2+5-second stable-standing
gate from the requested supine pose family can complete the chain.

## Historical height-first supine recovery v11 (September 5)

At the user's direction, v11 removes the negative constraints that made waiting
on the floor a local optimum. Discovery rewards only pelvis height and positive
vertical velocity. Training-only body assistance tapers 20% -> 10% -> 0%, with
unassisted height gates at every transition. Only after an unassisted rise does
the positive-only upright/two-foot/quiet refinement begin. The final independent
seven-second standing gate is not part of the PPO reward.

| Need | Location |
|---|---|
| Exact reward/action/termination configuration | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v11_rise_only\candidate.py` |
| Design, warnings, schedule and commands | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v11_rise_only\README.md` |
| Train/evaluate worker | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v11_rise_only\worker.py` |
| 8,192-environment chain and height-only gates | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v11_rise_only\chain.py` |
| Read-only monitor | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v11_rise_only\monitor.py` |
| Completed live Isaac train smoke | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v11_rise_only_smoke_20260905_a\result.json` |
| Completed reload/evaluation smoke | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v11_rise_only_smoke_eval_20260905_b\evaluation.json` |
| Active full run | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v11_height_first_20260905_232453\` |
| Authoritative live status | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v11_height_first_20260905_232453\state.json` |
| Launch stdout/stderr | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v11_height_first_20260905_232453.launcher.stdout.log` and `.stderr.log` |
| Design and launch record | `C:\Users\rshan\Documents\GitHub\Humanoid-Robot\Learning\HumanoidTraining\GETUP_HEIGHT_FIRST_2026-09-05.md` |

Do not describe the first three v11 height passes as standing. Their permissive
return can be maximized by a brief leap, roll, collision, or other unnatural
motion. Only the final unassisted stable-standing gate can complete the chain.

## Historical guarded recovery v4 (September 3, 16:33 EDT)

v3 safely stopped but converged to lying still. v4 first learns the terminal
standing hold, then uses locally calibrated 20% -> 10% -> zero training-only
pelvis assistance. Promotion remains completely unassisted. The 8,192 probe
crossed the 512 MiB reserve, so the current main block selected 6,144
environments. This is launch state, not a claim of recovery success.

| Need | Location |
|---|---|
| Design, calibration evidence, gates and limitations | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v4\README.md` |
| Live supervisor state | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v4_20260903_163352\state.json` |
| Read-only iteration/ETA monitor | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v4\monitor.py` |
| GPU samples and full supervisor output | Current run: `gpu.csv`, `supervisor.stdout.log`, `supervisor.stderr.log` |
| Per-block torque/joint/contact telemetry | Evaluated block folders: `telemetry.npz` and `evaluation.json` |
| Rejected 60% assistance evidence | `E:\Aditya\robot_sim\humanoid_project\logs\getup_v4_smoke_assisted_eval_20260903_1622\evaluation.json` |
| Safe 20% calibration evidence | `E:\Aditya\robot_sim\humanoid_project\logs\getup_v4_source_assist20_eval_20260903_1629\evaluation.json` |

## Historical recovery revision v3 (September 3, 11:50 EDT)

v2 was stopped after its independent tests showed 0/128 successes and all trials
unsafe despite rising higher. All terminal frames in the 400-iteration nominal
trace crossed the non-neighbor penetration limit. v3 reduces exploration noise,
penalizes approaching penetration and violent rising, increases failure cost,
and prevents height-only continuation with >=90% unsafe trials. The hard safety
and strict hold gates are unchanged. Details and limitations are in its README.

- Design/code: `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v3\README.md`, `candidate.py`, `reward_core.py`, `worker.py`, `chain.py`.
- Active state: `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v3_20260903_115042\state.json`.
- Monitor: `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v3\monitor.py`.
- GPU, stage outputs, source hashes and raw evaluations: the same v3 run folder.
- Exact inherited checkpoint: v2 run below, `00_supine_discovery_0200_8192\candidate.pt`; actor mean/normalizer retained, critic/optimizer/noise reset. This contains 400 historical lineage iterations, not 400 new v3 iterations.
- 28 CPU tests passed before launch. Consult live preflight/state for simulator completion; launch is not learning success.
- Launch verified at 12:08 EDT: all scaling/reload checks passed; main v3 had 7/200 updates at 8192 environments, 7596 MiB VRAM. No strict recovery success was established. The README records these as historical launch measurements, not live status.
- Why v2 stopped: its run's `MANUAL_STOP.md` and `00_supine_discovery_0400_g0_s47\telemetry.npz`.

## Historical recovery restart v2 (September 3, 10:32 EDT)

The v1 recovery run below is historical: its first nominal supine evaluation had
0/128 recoveries and its perturbation test crashed on an inference-tensor update.
v2 fixes that update and tests floor-level, bounded progress shaping. Strict
completion gates and the successful locomotion policies are unchanged. Always
read the live state; preflight/training does not establish learned recovery.

| Need | Location |
|---|---|
| v2 design, failure evidence, changes and limitations | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v2\README.md` |
| Current supervisor state, stages and checkpoint lineage | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v2_20260903_103200\state.json` |
| Progress, errors, memory and power samples | Same run: `supervisor.stdout.log`, `supervisor.stderr.log`, `gpu.csv`; per-block `stdout.log` / `stderr.log` |
| Reward implementation and strict hold logic | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v2\reward_core.py` and `candidate.py` |
| Inference-buffer push fix / regression tests | Same experiment: `inference_helpers.py`, `test_revision.py` |
| Read-only iteration/ETA/success monitor | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v2\monitor.py` |
| Source/config hashes, saved-policy reload and scaling evidence | Current run: `source_snapshot`, `input_hashes.json`, `preflight.json`, `smoke64`, `smoke_reload`, `benchmark_*` |
| Per-pose success, joint angles, estimated torque and support traces | Current run's evaluated block directories: `evaluation.json`, `telemetry.npz`, plus `*_gate.json` |

Main continuation retains the v1 200-iteration actor/normalizer but resets the
critic/optimizer on migration because reward values changed. Additional stage
ceilings are 600 supine, 800 four-pose and 400 refinement, with checks every 200.
The 64-env smoke updates are discarded before main continuation. 27 CPU contract
tests passed before launch. Full-size runtime status must be verified separately.

## Historical guarded fine-tuning candidate (2026-09-02)

**September 3 completion and recovery work:** v4 completed at 06:37:33 EDT after 1,800 additional iterations at 8,192 environments. Final 4 m/s command measured approximately 3.961 m/s, with walking retention and speed gates passing in both final test batches. The narrow slip margin and simplified collision/actuator physics remain limitations; this is not a guarantee of natural or hardware-ready motion. Inspect the artifacts below before reusing these figures.

| Need | Location |
|---|---|
| Final v4 checkpoint, native action scale .35 | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_run_v4_20260903_0305\06_speed_4_0600_8192\candidate.pt` |
| Final paired gates | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_run_v4_20260903_0305\06_speed_4_0600_gate.json` |
| Final nominal joint/contact/speed metrics | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_run_v4_20260903_0305\06_speed_4_0600_eval_47\evaluation.json` and `telemetry.npz` |
| Final push evaluation | Same run, `06_speed_4_0600_eval_83\evaluation.json` and `telemetry.npz` |
| Matched GUI playback, preserves saved scale and fixes command | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_run_v4\play.py` (`--speed 4 --real-time`) |
| Reusable lessons added to the robot skill | `C:\Users\rshan\.codex\skills\humanoid-robot-training\references\guarded-locomotion-lessons.md` |
| New recovery design, old reward audit, sources, integration prerequisites | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v1\README.md` |
| Standalone recovery reward/hold prototype | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v1\reward_core.py` |
| Synthetic recovery exploit/regression tests | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v1\test_reward_core.py` |

Recovery v1 is now Isaac-integrated as a separate task/network. Its 64-environment, 64-iteration smoke completed in 167 seconds with a saved checkpoint; this was not a success-qualified recovery policy. Existing production configs and archived walk/run policies are unchanged. Read live supervisor state before quoting main-training status.

| Recovery integration evidence | Location |
|---|---|
| Get-up implementation, reward table and failed-run outcome record | `C:\Users\rshan\Documents\GitHub\Humanoid-Robot\Learning\HumanoidTraining\GETUP_EXPERIMENT_2026-09-03.md` |
| Isolated Isaac rewards, reset control and sensor config | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v1\candidate.py` |
| Exact box/support checks and measured ground contacts | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v1\telemetry.py` |
| Collision-enabled overlay and 34-pair filter audit | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v1\assets\recovery.usda` and `collision_audit.json` |
| 1,280 settled poses, train/held-out labels and acceptance counts | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v1\assets\pose_bank.pt` and `pose_audit.json` |
| Independent 2+5-second hold evaluator | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v1\evaluation.py` |
| Passed small training smoke | `E:\Aditya\robot_sim\humanoid_project\logs\getup_smoke_20260903_0800\result.json` |
| Recovery supervisor, budgets and live status | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v1_20260903_0804\state.json` |
| Stationary-hold feasibility (15/16, not learned get-up success) | `E:\Aditya\robot_sim\humanoid_project\logs\getup_hold_20260903_0801\evaluation.json` and `telemetry.npz` |
| Recovery preflight, GPU samples and per-block joint/contact/torque traces | Same run's `preflight.json`, `gpu.csv`, and evaluation subfolders' `telemetry.npz` / `evaluation.json` |
| Read-only iteration/ETA/success monitor | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v1\monitor.py` |

The supervisor uses 800 supine, 800 four-pose, 400 refinement ceilings, evaluates every 200, and requires actual quiet two-foot standing rather than partial-height reward. Source snapshots and input hashes accompany the run. A failed or stalled gate stops it without promoting the candidate. New floor/reset integration findings are in the experiment README and robot-training skill reference.

**Latest revision: v4 (September 3).** v3 passed balance after 300 iterations (5.73%/6.50% improvement) and 1.8 m/s transition after 200, then stopped because target-stage updates regressed .5 m/s torso tilt. v4 resumes the last passing transition checkpoint, adds a modest low-speed actual-torso cost, and checks existing stage success before applying unnecessary PPO updates. Gates/evaluator thresholds are unchanged. Evidence and rationale: `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_run_v4\README.md`; current state: `E:\Aditya\robot_sim\humanoid_project\logs\guarded_run_v4_20260903_0305\state.json`; supervisor log: `E:\Aditya\robot_sim\humanoid_project\logs\guarded_run_v4_20260903_0305.launcher.log`. Existing `guarded_run_v3\monitor.ps1` command forwards to v4 by default. Always inspect live state; this index is not a live status claim.

**Previous revision: v3.** v2 finished 600 balance iterations but failed the 5% stance-improvement gate (walking retention passed). v3 calibrates a bounded completed-step penalty using two-step means and a stronger linear tail; all evaluator and gate thresholds remain unchanged. Design, evidence, budgets, limitations, and file map: `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_run_v3\README.md`. Archived state: `E:\Aditya\robot_sim\humanoid_project\logs\guarded_run_v3_20260902_2244\state.json`; supervisor log: `E:\Aditya\robot_sim\humanoid_project\logs\guarded_run_v3_20260902_2244.launcher.log`. Older entries below are historical.

**Previous revision: v2.** v1 stopped at its walking-regression gate after 100 iterations; it was not promoted. v2 isolates the walking-only changes before transferring to running. Archived state: `E:\Aditya\robot_sim\humanoid_project\logs\guarded_run_v2_20260902_2103\state.json`; progress log: `E:\Aditya\robot_sim\humanoid_project\logs\guarded_run_v2_20260902_2103.launcher.log`; design and code: `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_run_v2\README.md`. The v1 locations below are retained as historical diagnostics, not current status.

This section supersedes older run-status assumptions below; always read live state before reporting training progress. The original walker and runner remain archived. Experimental outputs are not automatically approved.

| Need | Location |
|---|---|
| Candidate design, reward weights, tests, stage budgets and limitations | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_run_v1\README.md` |
| Isolated candidate rewards / command mixture | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_run_v1\candidate.py` |
| Reset-safe, filtered completed-stance logic | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_run_v1\contact_state.py` |
| Regression / speed-promotion thresholds | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_run_v1\gates.py` |
| Background supervisor | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_run_v1\chain.py` |
| Training/evaluation worker | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_run_v1\worker.py` |
| Active candidate state, checkpoint paths and GPU samples | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_run_v1_20260902_1726\state.json` |
| Supervisor progress log | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_run_v1_20260902_1726.launcher.log` |
| GPU trace and all per-block gate/telemetry files | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_run_v1_20260902_1726\` |
| Physics-rate diagnostic report explaining the limp, target problems, and ankle indexing | `E:\Aditya\robot_sim\humanoid_project\logs\gait_diagnostics_20260902\REPORT.md` |
| Diagnostic joint angles, targets, estimated torque, phases and limits | `E:\Aditya\robot_sim\humanoid_project\logs\gait_diagnostics_20260902\nominal\` (also `randomized` and `waist_clamp_ablation`) |
| Fresh archived-walker/running-model matched comparison | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_run_v1_preflight\runner_baseline\evaluation.json` |
| User-approved walker, native action scale 0.35 | `E:\Aditya\robot_sim\humanoid_project\logs\rsl_rl\humanoid5ft_natural_walk\2026-08-31_17-06-10\model_2098.pt` |
| Previous runner, native action scale 0.45 | `E:\Aditya\robot_sim\humanoid_project\logs\rsl_rl\humanoid5ft_natural_run_from_working_walk\2026-09-01_19-54-34\model_3800.pt` |

Important: current `ImplicitActuatorCfg` torque telemetry is an approximate PD drive torque, not a direct measurement of PhysX motor effort or collision torque. Older tables below use “applied torque” loosely. Do not use a configured ceiling or approximate clipped torque alone as proof of hardware sizing.

The old claim of approximately 3.984 m/s elsewhere belongs to a different checkpoint. The September 2 runner diagnostics measured approximately 3.05 m/s at a 4 m/s command under their nominal conditions; it is not a validated 4 m/s policy. Candidate `result.json` stores its action scale, which must be honored in playback.

## 5 ft custom humanoid

| Need | Location | Notes |
|---|---|---|
| Main Isaac actuator values | `E:\Aditya\robot_sim\humanoid_project\humanoid_cfg.py` | Torque, velocity, PD gains, armature, initial pose, collision settings |
| Actuator metadata export | `E:\Aditya\robot_sim\humanoid_project\assets\urdf\humanoid_5ft_actuators.json` | Per-joint values derived from the Fusion/export workflow |
| Mass and inertia metadata | `E:\Aditya\robot_sim\humanoid_project\assets\urdf\humanoid_5ft_dynamics.json` | Link mass, center of mass, inertia |
| Prepared URDF | `E:\Aditya\robot_sim\humanoid_project\assets\urdf\humanoid_5ft_isaac.urdf` | Asset currently imported into Isaac |
| Converted USD | `E:\Aditya\robot_sim\humanoid_project\assets\usd\humanoid_5ft.usd` | Root USD; supporting layers are in `configuration/` |
| Fusion-native design | `C:\Users\rshan\Documents\GitHub\Humanoid-Robot\CAD\Simulation\Humanoid5ft\humanoid_5ft_ragdoll.f3d` | Best file for continued Fusion editing |
| Fusion builder | `C:\Users\rshan\Documents\GitHub\Humanoid-Robot\CAD\Simulation\Humanoid5ft\FusionHumanoid5ftBuilder\FusionHumanoid5ftBuilder.py` | Regenerates geometry, components, joints, and exports |
| Raw CAD dynamics | `C:\Users\rshan\Documents\GitHub\Humanoid-Robot\CAD\Simulation\Humanoid5ft\humanoid_5ft_ragdoll_dynamics.json` | CAD-side mass/inertia record |
| Task and reward config | `E:\Aditya\robot_sim\humanoid_project\source\humanoid_tasks\curriculum\env_cfg.py` | Task registrations, command ranges, reward weights, events, terminations, curricula |
| Custom reward/state logic | `E:\Aditya\robot_sim\humanoid_project\source\humanoid_tasks\curriculum\skill_mdp.py` | Gated velocity, get-up state machine, differential envelope, saturation, clearance |
| PPO config | `E:\Aditya\robot_sim\humanoid_project\source\humanoid_tasks\curriculum\agents\rsl_rl_cfg.py` | Network/runner/algorithm settings |
| Joint GUI validator | `E:\Aditya\robot_sim\humanoid_project\scripts\test_all_joints.py` | Moves all 22 joints individually and prints command/measured/error |
| Joint validator launcher | `E:\Aditya\robot_sim\humanoid_project\test_all_joints.ps1` | PowerShell wrapper |
| Checkpoint evaluator | `E:\Aditya\robot_sim\humanoid_project\evaluate_policy.py` | Commanded behavior tests and hard metrics |
| Checkpoint validator | `E:\Aditya\robot_sim\humanoid_project\validate_checkpoint.py` | Load/schema sanity checks |
| Stand/walk/run chain | `E:\Aditya\robot_sim\humanoid_project\train_full_curriculum.ps1` | 8,192→6,144→4,096 fallback, preflight, gates, state files |
| Corrected natural-motion retraining chain | `E:\Aditya\robot_sim\humanoid_project\retrain_natural_curriculum.ps1` | Starts from scratch; corrected-axis stand→walk→run→4 m/s→get-up chain |
| Corrected retraining plan | `C:\Users\rshan\Documents\GitHub\Humanoid-Robot\Learning\HumanoidTraining\RETRAINING_PLAN.md` | Iterations, reward changes, promotion gates, and future command |
| Natural gait retraining record | `C:\Users\rshan\Documents\GitHub\Humanoid-Robot\Learning\HumanoidTraining\GAIT_RETRAINING_2026-08-31.md` | Sloppy-gait diagnosis, new walk/run rewards, hard gait gates, and overnight chain |
| Asset coordinate converter and axis guard | `E:\Aditya\robot_sim\humanoid_project\prepare_asset.py` | Converts Fusion coordinates and rejects leg pitch axes other than Isaac +Y |
| Latest asset axis audit | `E:\Aditya\robot_sim\humanoid_project\assets\urdf\asset_prepare_status.json` | Records all prepared joint axes and the required leg-pitch convention |
| Sprint/get-up chain | `E:\Aditya\robot_sim\humanoid_project\train_sprint_then_getup.ps1` | 4 m/s, discovery, refinement, GPU telemetry |
| Review recorder | `E:\Aditya\robot_sim\humanoid_project\scripts\rsl_rl\record_humanoid_review.py` | Produces MP4 and telemetry CSV |
| Dashboard builder | `E:\Aditya\robot_sim\humanoid_project\scripts\build_humanoid_review.py` | Produces synchronized HTML torque/power viewer |
| Live review viewer | `C:\Users\rshan\Documents\GitHub\Humanoid-Robot\docs\macondo-journal\reviews\humanoid5ft\index.html` | Stand, walk, 4 m/s sprint, get-up video with 22-joint telemetry |
| Archived local viewer | `C:\Users\rshan\Documents\GitHub\Humanoid-Robot\Code\Firmware\Learning\Humanoid5ft\review\index.html` | Private local copy |

### Humanoid diagnostic data

| Data | Location |
|---|---|
| Completed stand/walk/run chain state | `E:\Aditya\robot_sim\humanoid_project\logs\background\humanoid_full_chain_20260830_094949.state.json` |
| Stand/walk/run GPU trace | `E:\Aditya\robot_sim\humanoid_project\logs\background\humanoid_full_chain_20260830_094949.vram.csv` |
| Completed sprint/get-up state | `E:\Aditya\robot_sim\humanoid_project\logs\background\sprint_getup_20260830_200827.state.json` |
| Sprint/get-up GPU trace | `E:\Aditya\robot_sim\humanoid_project\logs\background\sprint_getup_20260830_200827.gpu.csv` |
| Standing train log | `E:\Aditya\robot_sim\humanoid_project\logs\background\stand_8192_train_20260830_091050.stdout.log` |
| Walking train log | `E:\Aditya\robot_sim\humanoid_project\logs\background\walk_8192_train_20260830_094949.stdout.log` |
| 2.5 m/s train log | `E:\Aditya\robot_sim\humanoid_project\logs\background\run_fast_8192_train_20260830_094949.stdout.log` |
| 4 m/s train log | `E:\Aditya\robot_sim\humanoid_project\logs\background\sprint4_8192_train_20260830_163227.stdout.log` |
| Get-up discovery log | `E:\Aditya\robot_sim\humanoid_project\logs\background\getup_discovery_8192_train_20260830_200827.stdout.log` |
| Get-up refinement log | `E:\Aditya\robot_sim\humanoid_project\logs\background\getup_refine_8192_train_20260830_200827.stdout.log` |
| 4 m/s behavioral gate | `E:\Aditya\robot_sim\humanoid_project\logs\background\sprint4_gate_run_4_20260830_163227.json` |
| Standing telemetry | `C:\Users\rshan\Documents\GitHub\Humanoid-Robot\docs\macondo-journal\reviews\humanoid5ft\stand\telemetry.csv` |
| Walking telemetry | `C:\Users\rshan\Documents\GitHub\Humanoid-Robot\docs\macondo-journal\reviews\humanoid5ft\walk\telemetry.csv` |
| Sprint telemetry | `C:\Users\rshan\Documents\GitHub\Humanoid-Robot\docs\macondo-journal\reviews\humanoid5ft\sprint\telemetry.csv` |
| Get-up telemetry | `C:\Users\rshan\Documents\GitHub\Humanoid-Robot\docs\macondo-journal\reviews\humanoid5ft\getup\telemetry.csv` |

The telemetry CSV files are the best evidence for actual applied torque. `humanoid_cfg.py` and the actuator JSON contain limits; they do not show what a policy actually used.

The checkpoints listed above were trained on the old leg-pitch convention and are diagnostic artifacts only. Do not resume them after the 2026-08-30 corrected-axis rebuild.

## Unitree H1 comparison data

| Need | Location |
|---|---|
| Isaac Lab H1/G1 actuator definitions | `E:\Aditya\robot_sim\IsaacLab\source\isaaclab_assets\isaaclab_assets\robots\unitree.py` |
| H1 analysis script | `E:\Aditya\robot_sim\IsaacLab\scripts\demos\h1_analysis.py` |
| H1 robustness script | `E:\Aditya\robot_sim\IsaacLab\scripts\demos\h1_robustness_test.py` |
| H1 walking dashboard | `E:\Aditya\robot_sim\IsaacLab\logs\h1_robustness\2026-08-27_17-05-32\walking_review.html` |
| H1 test summary | `E:\Aditya\robot_sim\IsaacLab\logs\h1_robustness\2026-08-27_17-05-32\summary.csv` |
| H1 report | `E:\Aditya\robot_sim\IsaacLab\logs\h1_robustness\2026-08-27_17-05-32\suite_report.txt` |
| H1 raw walking data | `E:\Aditya\robot_sim\IsaacLab\logs\h1_robustness\2026-08-27_17-05-32\walking_max_speed\trial_001__0N\samples.csv` |
| H1 torque/speed charts | `E:\Aditya\robot_sim\IsaacLab\logs\h1_robustness\2026-08-27_17-05-32\torque_speed_envelopes\` |
| H1 left-push combined data | `E:\Aditya\robot_sim\IsaacLab\logs\h1_robustness\H1_left_push_sweep_2026-08-27\combined_samples.csv` |

## Unitree G1 comparison data

| Need | Location |
|---|---|
| G1 analysis script | `E:\Aditya\robot_sim\IsaacLab\scripts\demos\g1_analysis.py` |
| G1 robustness script | `E:\Aditya\robot_sim\IsaacLab\scripts\demos\g1_robustness_test.py` |
| G1 walking dashboard | `E:\Aditya\robot_sim\IsaacLab\logs\g1_robustness\2026-08-27_17-10-24\walking_review.html` |
| G1 test summary | `E:\Aditya\robot_sim\IsaacLab\logs\g1_robustness\2026-08-27_17-10-24\summary.csv` |
| G1 report | `E:\Aditya\robot_sim\IsaacLab\logs\g1_robustness\2026-08-27_17-10-24\suite_report.txt` |
| G1 raw walking data | `E:\Aditya\robot_sim\IsaacLab\logs\g1_robustness\2026-08-27_17-10-24\walking_max_speed\trial_001__0N\samples.csv` |
| G1 torque/speed CSVs and charts | `E:\Aditya\robot_sim\IsaacLab\logs\g1_robustness\2026-08-27_17-10-24\torque_speed_envelopes\` |
| G1 fully validated robustness set | `E:\Aditya\robot_sim\IsaacLab\logs\g1_robustness\2026-08-26_08-48-06\` |
| G1 validated joint extrema | `E:\Aditya\robot_sim\IsaacLab\logs\g1_robustness\2026-08-26_08-48-06\joint_extrema_validated.csv` |
| G1 validated master summary | `E:\Aditya\robot_sim\IsaacLab\logs\g1_robustness\2026-08-26_08-48-06\master_summary_validated.csv` |

## Realistic quadruped comparison

| Need | Location |
|---|---|
| Full dashboard | `E:\Aditya\robot_sim\quadruped_project\reviews\realistic20\index.html` |
| Per-skill telemetry | `E:\Aditya\robot_sim\quadruped_project\reviews\realistic20\{stand,walk,run,jump}\telemetry.csv` |
| Realistic actuator implementation | `E:\Aditya\robot_sim\quadruped_project\source\quadruped_tasks\realistic_actuator.py` |
| Archived checkpoints | `E:\Aditya\robot_sim\quadruped_project\firmware\learning\realistic20\checkpoints\` |
| Chain state and failures | `E:\Aditya\robot_sim\quadruped_project\logs\background\` |

The quadruped backflip policy is a reward-exploit example, not a successful reference motion.

## How to answer future torque questions

1. Read the custom robot's limits and reflected inertia from `humanoid_cfg.py` and the actuator JSON.
2. Read actual peak/RMS use from the relevant humanoid telemetry CSV.
3. Compare against the H1/G1 raw walking samples and torque/speed envelopes, accounting for robot mass, limb length, reduction, and task speed.
4. Separate peak torque, continuous torque, speed limit, and thermal feasibility.
5. Recalculate static/get-up moments from the current geometry and mass distribution; do not scale another robot's torque number blindly.
6. Treat a policy touching a configured torque limit as evidence of saturation or reward pressure, not proof that the hardware needs exactly that limit.

## Historical guarded get-up v9

| Need | Location |
|---|---|
| Isolated v9 implementation and README | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v9\` |
| Active September 4 run | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v9_20260904_1540\` |
| Authoritative live status | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v9_20260904_1540\state.json` |
| GPU samples | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v9_20260904_1540\gpu.csv` |
| Reloaded crouch-anchor evaluation | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v9_20260904_1540\p01_anchor_reload_crouch\evaluation.json` |
| 8,192-environment PPO preflight | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v9_20260904_1540\p02_benchmark_8192\result.json` |
| Target-slew physics comparison | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v9_slew_grid_20260904_1515\slew_probe.json` |
| HumanUP reference assets investigated (not accepted as this robot's target motion) | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v9\assets\humanup_reference\` |
| Console monitor | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v9\monitor.py` |

Read `state.json` plus the newest strict `evaluation.json`; do not infer success from GPU activity, training return, or a saved checkpoint alone. v9 uses action contract `limit_aware_slew14_v3`, so older get-up checkpoints are intentionally incompatible.

The v9 run above was rejected at the one-degree gate and is retained as failure evidence. Its reason is recorded in `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v9_20260904_1540\REJECTED.md`.

| Current replacement | Location |
|---|---|
| v10 implementation | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v10\` |
| v10 live run | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v10_20260904_1531\` |
| v10 authoritative status | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v10_20260904_1531\state.json` |
| v10 monitor | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v10\monitor.py` |

v10 action contract is `limit_aware_uniform100_v4`. Its one-degree baseline is validated at 64/64; harder stages are not validated until their own gate files pass.

## Historical guarded 6 m/s continuation v8 (September 5, 2026)

V6 stopped cleanly at 4.5 m/s because both independent batches failed only
torso lean occupancy.  V7's isolated -1.25 torso-weight repair was stopped after
its first gate remained above the unchanged occupancy limit.  V8 resumes v6's
last fully passing 4.0 m/s checkpoint and changes only the high-speed torso
weight to -2.00; the term remains exactly zero through 1 m/s.

| Need | Location |
|---|---|
| V6 terminal failure evidence | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_run_v6_traction6_20260905_0122\state.json` and `01_speed_4.5_0400_gate.json` |
| V7 first-gate evidence and safe stop | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_run_v7_posture6_20260905_0640\MANUAL_STOP.md` |
| V8 implementation and rationale | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_run_v8_posture6\` |
| V8 authoritative live state | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_run_v8_posture6_20260905_0705\state.json` |
| First passing 4.5 m/s gate report | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_run_v8_posture6_20260905_0705\FIRST_GATE_REPORT.md` |
| Passing 4.5 m/s checkpoint, native scale .35 | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_run_v8_posture6_20260905_0705\00_speed_4.5_0200_8192\candidate.pt` |

The 4.5 m/s checkpoint passed both nominal and lateral-kick gates with zero
falls, approximately 4.483 m/s measured speed, and torso excess occupancy about
0.047.  V8 later passed 5.0 m/s and stopped safely at the 5.5 m/s gate after its
600-iteration budget.  Both final 5.5 m/s batches failed archived 1.0 m/s stance
asymmetry and target reachability, so the newest fully passing checkpoint is
`01_speed_5_0400_8192/candidate.pt` with SHA256
`89cb755d856e14d8b158da7c0d765f5ab17576e7774fa860089c3692d9dce61e`.
This is not a 5.5 or 6 m/s success claim.

## Humanoid5ft7 CAD status (September 5, 2026)

The source inventory was verified, but computer-use exposed no native Windows
apps and no `getApp` capability, so Fusion 360 could not be opened or controlled.
No 5ft7 CAD/URDF/USD was fabricated and no 5-foot source was modified.  Exact
blocker and source hashes:
`C:\Users\rshan\Documents\GitHub\Humanoid-Robot\CAD\Simulation\Humanoid5ft7\BLOCKED.md`.
The user later opened Fusion manually, but a helper reset and fresh discovery
still returned no native apps and the direct bind remained unavailable.

## Working locomotion torque-viewer captures (September 5, 2026)

These captures use physics time rather than wall/render time. Each source video
contains exactly 750 control frames at 50 Hz (15.000 simulation seconds). Each
dashboard GIF contains 150 synchronized frames at 10 Hz (15.000 seconds).

| Need | Location |
|---|---|
| Gallery for all three policies | `E:\Aditya\robot_sim\humanoid_project\reviews\working_locomotion_20260905_d\index.html` |
| Approved 1 m/s walking dashboard GIF | `E:\Aditya\robot_sim\humanoid_project\reviews\working_locomotion_20260905_d\walk_1ms\dashboard.gif` |
| Passing 4 m/s running dashboard GIF | `E:\Aditya\robot_sim\humanoid_project\reviews\working_locomotion_20260905_d\run_4ms\dashboard.gif` |
| Passing 5 m/s running dashboard GIF | `E:\Aditya\robot_sim\humanoid_project\reviews\working_locomotion_20260905_d\run_5ms\dashboard.gif` |
| Per-joint torque and velocity data | `E:\Aditya\robot_sim\humanoid_project\reviews\working_locomotion_20260905_d\{walk_1ms,run_4ms,run_5ms}\telemetry.csv` |
| Capture manifests and checkpoint hashes | `E:\Aditya\robot_sim\humanoid_project\reviews\working_locomotion_20260905_d\{walk_1ms,run_4ms,run_5ms}\manifest.json` |
| Physics-time walking recorder | `E:\Aditya\robot_sim\humanoid_project\scripts\rsl_rl\record_humanoid_review.py` |
| Physics-time guarded-run recorder | `E:\Aditya\robot_sim\humanoid_project\scripts\rsl_rl\record_guarded_locomotion_review.py` |
| Dashboard/GIF renderer | `E:\Aditya\robot_sim\humanoid_project\scripts\build_locomotion_dashboard_gifs.py` |

The steady-state measured forward speeds from 2.0 through 15.0 seconds were
0.994 m/s, 4.001 m/s, and 5.009 m/s, respectively; all three captures had zero
falls. Applied torque is Isaac Lab's simulated implicit-drive estimate, not a
direct measurement from physical hardware.

## Historical guarded get-up v13 stable-reverse recovery (September 6, 2026)

The v12 checkpoint learned to reach height briefly, but it did not learn to
remain standing: fresh 12-second evaluations from tilt5 through tilt45 produced
0 strict stands and finished near 0.172 m base height. V13 therefore replaces
the max-height curriculum with a stable-first reverse curriculum. Its positive
rewards are a bounded standing-height band, upward velocity only below the
standing region, uprightness, two-foot support, and quiet standing. Every
promotion gate evaluates unassisted stability; transient height is diagnostic
only and cannot pass a stage.

| Need | Location |
|---|---|
| V13 implementation and rationale | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v13_stable_reverse\` |
| Authoritative live run | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v13_stable_reverse_20260906_062055\` |
| Live status | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v13_stable_reverse_20260906_062055\state.json` |
| GPU samples | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v13_stable_reverse_20260906_062055\gpu.csv` |
| V12 intermediate failure probes | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v12_intermediate_probe_20260906\` |
| Console monitor | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v13_stable_reverse\monitor.py` |

The fresh v13 run passed CPU tests, a 64-environment train/reload smoke, and an
8,192-environment allocation smoke. The sampled preflight peak was 6,862 MiB
with a 512 MiB reserve. A running process or saved checkpoint is not proof of
get-up success; use the latest stable-gate `evaluation.json` and require the
strict stand count and dwell criteria to pass.

## Historical guarded get-up v14 supported-stand recovery (September 6, 2026)

V13 later exhausted its 600-iteration first stage at 0/64 strict stands. Its
final trace exposed timeout-only refinement termination, a run-off-floor fall,
over-permissive upright/quiet shaping, and exploration std 2.30. V14 corrects
those issues, restores the measured 14 rad/s target slew, and starts from a
clean zero-mean controller rather than preserving the failed v13 actor.

| Need | Location |
|---|---|
| V14 code, rationale and commands | `E:\Aditya\robot_sim\humanoid_project\experiments\guarded_getup_v14_supported_stand\` |
| Authoritative live run | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v14_supported_stand_20260906_105955\` |
| Live state and gates | Same run: `state.json` and newest `*_gate.json` |
| GPU history | Same run: `gpu.csv` |
| Clean slew-limited bootstrap | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v14_slew_zero_bootstrap_20260906_1058\candidate.pt` |
| V13 terminal failure evidence | `E:\Aditya\robot_sim\humanoid_project\logs\guarded_getup_v13_stable_reverse_20260906_062055\e007_00_stable_tilt05_0600_g0_nominal\` |

V14 passed 31 CPU tests, 64-environment train/reload tests, and an 8,192-env
allocation smoke with 6,884 MiB sampled peak before starting its first PPO
block. This is execution validation only; recovery succeeds only when an
independent unassisted seven-second stable gate passes.
