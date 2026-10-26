# Compact differential wrists v34

Verified 2026-10-23T17:00:54.607348+00:00. Current saved Fusion document: **Humanoid_compact_wrists_v34_release**, version **3**, `urn:adsk.wipprod:dm.lineage:hcNjF0evQJSGkyUjzb6yow`. The preserved v33 source is unchanged.

[Full native Fusion archive](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist34/deliverables/native/Humanoid_compact_wrists_v34.f3d) · [Right wrist STEP](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist34/deliverables/native/W34_R_compact_differential_wrist.step) · [Left wrist STEP](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist34/deliverables/native/W34_L_compact_differential_wrist.step) · [Native drive preview](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist34/wrist34_native_drive_layout.png) · [Whole robot](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist34/robot_compact_wrists_v34.png).

## Requested changes

The user's photo/request asked to remove one spur gear from each side, use 17–18 teeth with a larger module, and shorten the pitch-axis-to-hand lever. Both wrists are revised. The right and left hand meshes, their size, mirrored three-M2.5/42mm-PCD mounting pattern and original neutral mounting planes are retained.

| Measurement per wrist | Previous v33 | Current v34 |
| --- | ---: | ---: |
| Short-path idlers | 1 | 0 |
| Long-path idlers | 3 | 2 |
| Spur meshes, short / long | 2 / 4 | 1 / 3 |
| Spur teeth / module | 24 / 1 | 18 / 1.5 |
| Spur pitch / outside diameter | 24 / 26 mm | 27 / 30 mm |
| Spur face width | 5 mm | 5 mm |
| Servo output stations from pitch axis | 48 / 96 mm | 27 / 81 mm |
| Servo stagger / case gap | 48 / 2.6 mm | 54 / 8.6 mm |
| Pitch axis to hand mounting plane | 54 mm | 37.5 mm |
| Cassette length | 145 mm | 126 mm |
| Hand mounting plane to proximal cassette end | 193 mm | 157.5 mm |
| Roll bearings | Two 608, 8×22×7 mm | Two 688, 8×16×5 mm |

The hand lever is **16.5mm / 30.6% shorter**. The hand-plane-to-cassette-end distance is **35.5mm / 18.4% shorter**. The pitch axis moves 16.5mm toward the hand while the hand mounting plane stays fixed. The cassette itself is 19mm shorter. Servo cases remain exact copies of the existing head-type STS3215 CAD. Two removable clamp straps and sleeved M3 idler axles remain per wrist.

Only the spur stages change tooth count/module. The three proven-clearance prototype mitres per wrist remain **24T/module1** to avoid enlarging the differential envelope. Module1.5 makes thicker spur teeth, but both paths remain **1:1**: no increase in gear torque multiplication is claimed. Printed tooth strength, payload and thermal capability are untested. A shorter mounting-plane lever does not by itself establish a proportional reduction in the whole hand's loaded moment.

Eighteen teeth is the conservative integer choice around the standard 20° full-depth spur undercut threshold; KHK discusses the commonly quoted 17-tooth threshold and the importance of strength/contact ratio. That is a spur-gear reference, not a universal minimum for bevels. [KHK primary technical note](https://khkgears.us/media/e5hdctid/gear-solutions_khk_addendum-modification-and-undercut.pdf). Bearing nominal envelopes are checked against [NSK's primary catalogue](https://www.nsk.com/content/dam/nsk/common/catalogs/ctrgPdf/bearings/e1258f.pdf); this does not qualify our bearing seats, retention or loaded life. The compact roll bearings have 7mm centre spacing; no equivalence to the old bearing load capacity is claimed.

## Native kinematics and fit

Removing one idler flips the motor sign on each path. With outward input coordinates, `a=pitch-roll`, `b=-pitch-roll`, and motor angles are `-a`, `-b`. Therefore `pitch=(motorB-motorA)/2` and `roll=(motorA+motorB)/2`. The CAD-only [pose driver](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist34/pose.py) coordinates eight native revolutes per wrist. It does not send physical servo commands or run a Fusion gear-contact solver.

The original 65 native joints remain; their types, owners and validity are checked. There are 18 new joints: 16 revolute and two rigid attachments, for **83 total**. The selected limits remain pitch ±35° and roll ±60°. The cassette is trimmed to the original forearm skins with sampled 0.5mm offsets; only new service ports and required rail/crossbar relief are added. Old static wrist adapters/shrouds are hidden in this revision.

## Verification

| Check | Result / scope |
| --- | --- |
| Native neutral audit | 72 visible BRep solids; zero inter-group overlaps above 0.02mm³; connected solids and valid joints |
| Neutral installed placement | Six case/input/output checks transformed back into the intended wrist frame, maximum bounds error 1e-07mm |
| Native driven motion | 12 poses across both wrists; independent pitch/roll matrix prediction agrees within 1e-5; case/fixed geometry remains stationary |
| Actual-forearm solid sweeps | 18 selected combined/end poses, no overlaps above 0.02mm³ against cassette, servo cases, original rails and skins |
| New spur mesh | 52 rigid-solid pair samples across one 20° tooth period, maximum overlap 0mm³; ideal transverse contact ratio 1.530 |
| Independent full F3D reopen | 28 wrist/hand components and all 83 joints agree; zero errors |
| Independent native STEP reopen | Both wrist exports contain 29 valid solids with matching bounds and relative volume error below 1e-5 |
| Visual inspection | Full robot, isolated wrist, gear cutaway and combined pitch20°/roll30° native snapshots inspected |

Evidence: [native audit](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist34/native_audit.json), [placement checks](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist34/native_neutral_placement_checks.json), [native motion](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist34/native_motion.json), [forearm sweep](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist34/native_forearm_sweep.json), [spur samples](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist34/spur_mesh_period.json), [native reopen](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist34/native_reopen.json), [STEP reopen](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist34/native_step_reopen.json), [release hashes](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist34/saved_release.json).

Mesh-hand collision and continuous whole-body clearance remain unqualified; the solid sweeps do not certify mesh-hand contact. There is no physical load, fatigue, print-fit, backlash, wear or motor test. The 14mm-PCD/four-M2 horn adapter still needs comparison with the purchased horn. The CAD shaft/hubs and sleeved M3 supports remain prototypes. No simulator, controller, training, native motor caps or automation was changed.

## Preservation and repaired failures

The source v33 archive SHA256 remains `cf5748627bc2cd0a25889c2285a6cd00b0ef7349d01aeef0e8b994660b7d2b23`. The final native build branches from its preserved v32 version-4 baseline (`b4daf3668369bab5d09dff0d70217aaa0ffd90e54c7262b05e958fd4f56c4085`) and incorporates the new wrist geometry derived from v33. Recompute normalizes historical cached assembly poses to the authored neutral pose; cached pre-recompute matrices are preserved in `native_clean_open.json`, not claimed bitwise invariant.

The user's original Fusion process had already exited when restart was attempted. Available recovery files were copied. A later task-created rebuild that removed old v33 components exhausted RAM and became unresponsive; Escape cancellation timed out. That owned session was stopped, evidence retained, and the final build used the preserved pre-wrist baseline with nine rigid links per wrist. This avoids redundant per-part constraints and old-wrist component deletion. Native preparation subsequently completed with about 11.8GiB available host memory.

Initial neutral interference in the compact ring/strap was reproduced and repaired. An initial absolute 0.01mm³ STEP volume threshold was unsuitable for numerical reintegration of 34,806mm³ servo cases; valid-solid topology, bounds and a relative 1e-5 volume threshold are used, with initial failures preserved. Maximum standalone part discrepancy was 2.51ppm.

Visual review then exposed a native placement fault: Fusion reset transient imported occurrence transforms to identity when recomputing. The first angle-only motion checks were insufficient. Those reports and archive are preserved in `first_native_attempt`; they are superseded. The final body geometry is explicitly baked into the authored world frame, hand meshes stay in their correct world placement, and six independent neutral placement checks, actual forearm collision checks, motion tests and new renders all pass before export. Datum bodies were excluded from the placement transform.

The temporary recovery add-in startup setting was restored. The workbench is stopped after final inventory with a harmless inventory request queued. Fusion and the computer remain on. Earlier v33, recovery files, standalone geometry, interrupted build and pre-placement evidence are retained. No commit or push was made.

## Artifact identity

Full native archive: `285,271,607` bytes; SHA256 **`1f3c045dc28e415f9e0beeede2f95bc4431cc776fec50e7418913c6d1f6c23e3`**; ZIP CRC error `None`. Saved document version 3 and identity are recorded above. `deliverables/native` is canonical. Other STEP files are standalone local-frame construction evidence; the canonical native STEP assemblies use the robot's authored world frame. STEP does not preserve the full native hand meshes or joints.

![Native compact drive layout](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist34/wrist34_native_drive_layout.png)

![Native combined pose](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist34/wrist34_native_pitch20_roll30.png)
