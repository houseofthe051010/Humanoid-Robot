<!-- clearance41_20261024 -->
## Clearance repairs and redesigned hip adapters V41 — October 24, 2026

Both yaw-to-hip-roll adapters are redesigned in **Humanoid_clearance_adapter_redesign_v41**, saved Fusion version 2. They use tapered 8 mm cheeks, an 8.5 mm base and R12 primary root blends, with measured local clearance pockets instead of thin right-angle attachments. Both yaw bearing seats and their bearings/retainers are lowered 6.3 mm axially; motor placements and all 83 joints remain unchanged. The right output hub is realigned to its motor axis as explicitly requested; its shape is preserved. The electronics holder is shortened for a 2 mm battery gap, shoulder fasteners are recessed and both inner waist caps/tube tips are trimmed for triangular clearance. The V40 chains are preserved.

Final visible-assembly checks pass 17 hip poses with zero absolute adapter contacts and 15 shoulder/waist poses with no added interference. All 4,175 original bodies remain recoverable; the full F3D and 25 single-solid STEP files independently reopen. This is a CAD prototype: material choice, tolerances, strength, fatigue, fastening, manufacture and continuous whole-body clearance remain unqualified.

[V41 CAD, images and measured checks](E:/Aditya/robot_sim/outputs/shin_cad_20260912/clearance41/REPORT.md). Input live edits and all rejected attempts are preserved. Training stays stopped; computer stays on.


<!-- chains40_20261024 -->
## Straight-run knee chains V40 — October24,2026

Current native source **Humanoid_tensioned_knee_chains_v40**, saved v2. The user-rejected V39 oval layout is replaced with36-pitch ANSI40 chains and complete knee motor/mount assemblies lowered7.83755mm. Both spans are straight;151.56245mm centres,12.7mm pitch,18inner/18outer links and180active solids per knee. No stretched or offset link. Lower knee axes/rails/ankles and83joints retained; adapter overlap remains intentionally for the user's later repair. Native placement/tooth checks, independent fullF3D and two180-body STEP reopen pass. Static geometry only; preload,dynamics,load and manufacture unqualified. [CAD, views and evidence](E:/Aditya/robot_sim/outputs/shin_cad_20260912/chains40/REPORT.md). V38 remains preserved below; V39 is rejected evidence. Training stopped, computer on, unrelated unsaved Fusion work preserved.


<!-- adapter38_20261024 -->
## Refined yaw-to-hip-roll cradles V38 — October 24, 2026

Current source **Humanoid_refined_hip_cradles_v38**, saved version 2. Both Q02 cradles gain editable R8 cheek-to-base root blends and R2 base corners. Original 10 mm cheeks, 8 mm base, 5 mm blind caps and all 39 cylindrical surfaces per part remain; all V37 motors, driver/encoder mounts and 83 joints are retained. Native neutral and 16 sampled hip poses show no added contact; full F3D and two STEP parts independently reopen. The original bodies and all failed probes remain recoverable. This is prototype geometry, with strength/material/fatigue/manufacturing and continuous full-body clearance unqualified.

[Before/after images, CAD and measured checks](E:/Aditya/robot_sim/outputs/shin_cad_20260912/adapter38/REPORT.md). The one-time follow-up is consumed; no ongoing schedule or training restart. Computer remains on. V37 below is preserved history.


<!-- drivers_encoders37_20261024 -->
## Leg drivers and ankle encoders v37 — October23 local /24UTC,2026

Current native source **Humanoid_leg_drivers_encoders_v37**, saved v4. Six additional GDS68 envelope mounts are integrated behind the10018 knee/roll/pitch motors, with reversible axial motor-solid moves8.5/14.5/14mm and attached support/fastener changes. Four visible official Arbite AS5047P boards mount on revised S06 carriers at1mm sensor-face gaps to the unchanged stock ankle magnet CAD. All ankle motors and83native joints remain;3,221original solids are retained. Neutral clearance and independent F3D/14STEP reopen pass.26/28sampled poses have no added moving-group contact; the two crossed-leg30deg poses were already invalid. First sampled cross-leg contact remains11deg in both original/revised geometry. Continuous motion, material/mass/load, exact driver PCB holes,10018 electrical/firmware/thermal and real gearbox/encoder operation remain unqualified.

[CAD, previews, sources and measured checks](E:/Aditya/robot_sim/outputs/shin_cad_20260912/drivers_encoders37/REPORT.md). Q02 yaw-to-hip-roll adapter refinement is explicitly deferred to the same one-time Oct24,01:41local follow-up. Training and custom FOC PCB remain unchanged. Older v36 is preserved below.


<!-- steadywin36_20261023 -->
## SteadyWin enclosure prototypes v36 — October 23, 2026

Current native source: **Humanoid_SteadyWin_enclosures_v36**, saved version 2. Nine separate mounted cases replace visible XDrives for six 6010 and three non-ankle 7010 motors. Original motors, four excluded ankles and all 83 joints remain. Published GDS68 envelopes are used because the downloaded official motor/cap CAD has no standalone PCB; exact 7010 configuration, board holes, encoder stack and thermal/electrical duty remain unverified. Separate flanges, radial screw mounts, split oval-rail clamps and removable vented lids are modeled. W07/local fixed supports and a 140 mm electronics bay are revised with originals retained hidden.

All 3,096 input solids are preserved; neutral solid clearance, full archive reopen and all 15 STEP roundtrips pass; actual motion finds two unresolved inward-arm/waist-case contacts. Continuous motion, material/mass, strength and manufacture remain unqualified. [CAD, images and evidence](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/REPORT.md). V35 below is historical. Training and the custom FOC PCB remain unchanged.

# V32 verification

- [pose_invariants32.json](evidence/v32/pose_invariants32.json)
- [mount_contact32.json](evidence/v32/mount_contact32.json)
- [native_cover_motion32.json](evidence/v32/native_cover_motion32.json)
- [native_compound_motion32.json](evidence/v32/native_compound_motion32.json)
- [clearance_checks32.json](evidence/v32/clearance_checks32.json)
- [native_reopen32.json](evidence/v32/native_reopen32.json)
- [native_archive_integrity32.json](evidence/v32/native_archive_integrity32.json)

Neutral intersections and discrete yaw samples passed. Twelve leg axes and eight paired hip moves verified native ownership on a disposable copy; original live pose untouched. Original439 occurrence transforms and65 joints preserved; one left collar occurrence added. Full archive CRC and independent reopen passed. No full continuous collision, printing, strength or thermal qualification.
