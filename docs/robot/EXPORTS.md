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

Full native F3D is112,145,491bytes;SHA256 `2f8bfc1ccb58a6b4d630d10e472fc7c3bc78cac14912977ad10a93c1323f0fb2`. Twelve printed-body candidates and ten hardware/estimated-reference bodies are separated in14STEP files. See the linked saved_release.json for per-file hashes.

<!-- steadywin36_20261023 -->
## SteadyWin enclosure prototypes v36 — October 23, 2026

Current native source: **Humanoid_SteadyWin_enclosures_v36**, saved version 2. Nine separate mounted cases replace visible XDrives for six 6010 and three non-ankle 7010 motors. Original motors, four excluded ankles and all 83 joints remain. Published GDS68 envelopes are used because the downloaded official motor/cap CAD has no standalone PCB; exact 7010 configuration, board holes, encoder stack and thermal/electrical duty remain unverified. Separate flanges, radial screw mounts, split oval-rail clamps and removable vented lids are modeled. W07/local fixed supports and a 140 mm electronics bay are revised with originals retained hidden.

All 3,096 input solids are preserved; neutral solid clearance, full archive reopen and all 15 STEP roundtrips pass; actual motion finds two unresolved inward-arm/waist-case contacts. Continuous motion, material/mass, strength and manufacture remain unqualified. [CAD, images and evidence](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/REPORT.md). V35 below is historical. Training and the custom FOC PCB remain unchanged.

<!-- xdrive35_20261023 -->
## XDrive controller placements v35 — October 23, 2026

Current native source: **Humanoid_XDrive_mounts_v35**, saved version 3.
Nine linked Mini CAD references: four shoulders, two waist differential motors,
two hip-yaw and one waist-yaw. Per the user's steering, the original mechanics
are retained and fit conflicts remain for the user to adjust. No mount brackets,
case reliefs or electronics-box relocation are retained. All nine placements and
the native reopen pass; 1733 original body bounds
and all 83 joints are preserved. Encoder/thermal-stack fit remains unverified.
The two green screw-terminal assemblies per board are disabled for direct
soldering, with their solids retained hidden. Wire/solder envelopes are not modeled.

[Canonical CAD, previews and evidence](E:/Aditya/robot_sim/outputs/shin_cad_20260912/xdrive35/REPORT.md).
The previous compact wrist v34 is preserved below. Training is unchanged.

<!-- wrist34_20261023 -->
# Current compact wrist v34 exports

[Full native robot, both wrist STEP assemblies and modified forearm parts](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist34/REPORT.md). Saved version 3; independent native and STEP reopen pass. Earlier releases follow.

<!-- wrist33_20261023 -->
# Differential wrist v33 export

[Canonical report, complete F3D and 22 STEP subassemblies](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist33/REPORT.md). Independent native reopen passes. Hardware fit and load remain unqualified.

# CAD exports — v32

Native source: **Humanoid_complete_v32**, saved version 2; `urn:adsk.wipprod:dm.lineage:a2yHyUciTnqbR9_IxjUjHw`.

Full independently reopened archive: `C:/Users/rshan/Downloads/Humanoid_v32_CAD/Humanoid_complete_v32.f3d`.

Six edited component STEP files are in `modified_parts_STEP` alongside it: four perforated shin plates and two split hip collars. STEP collar files contain both front/rear solids. Native previews and verification JSONs are included.

Construction, preserved v31 input and all evidence: `E:/Aditya/robot_sim/outputs/shin_cad_20260912/v32`.

Archive CRC, full Fusion reopen, original placements/joints and targeted cover movement checks passed. This is prototype CAD, not manufacturing or dynamics qualification. Prior v31 remains preserved at its original location. Training remains frozen physical_v29.
