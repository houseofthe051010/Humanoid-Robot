# SteadyWin controller enclosures — CAD v36

Recorded 2026-10-23T23:36:01.905875+00:00. Saved native source **Humanoid_SteadyWin_enclosures_v36**, version 2; `urn:adsk.wipprod:dm.lineage:L5mGVY-GSc6xk-57pUTA2A`.

Nine separate mechanically fastened controller-enclosure prototypes replace the visible rectangular XDrive placements: four shoulders, two waist differential motors, two hip-yaw motors and waist yaw. The original six GWK6010 and seven GWK7010 motors remain. All four ankle controllers are excluded. The user's oversized shoulder concept and previous XDrive geometry are preserved hidden, with the complete unsaved input archived before editing.

**Neutral packaging is checked; full inward arm clearance is unresolved.** Of 21 actual native samples, 19 are clear. Left inward roll -20 degrees and right inward roll +21 degrees contact their waist cases and the conservative driver envelopes. Left -15/right +15 and right outward -60 are clear, including the board envelopes. No original motor positions, arm geometry or joint limits were changed to conceal this conflict. This is a prototype release, not a claim that all nine installations are mechanically qualified through full travel. The envelope is deliberately fuller than a real populated PCB; its collision does not prove the real hardware cannot fit. Actual component geometry/encoder spacing must be verified before further compacting these two packages. [Exact contact attribution](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/inward_arm_attribution.json), [motion review](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/motion_review.json).

- [Complete native Fusion archive](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/deliverables/Humanoid_SteadyWin_enclosures_v36.f3d)
- [Individual enclosure/lid/clamp and modified-support STEP sets](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/deliverables/print_parts_STEP)
- [Official downloaded motor/cap CAD](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/sources/GIM6010_8_official.stp)
- [Published GDS68 drawing](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/sources/GDS68_drawing.png) · [Source audit](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/RESEARCH.md) · [File hashes](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/sources/manifest.json)

![Complete robot](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/robot_steadywin_v36.png)
![Both shoulders](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/both_shoulders_steadywin_v36.png)
![Shoulder enclosure](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/left_shoulder_steadywin_v36.png)
![Waist enclosures](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/waist_steadywin_v36.png)
![Hip-yaw clamp enclosure](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/left_hip_steadywin_v36.png)
![Waist-yaw enclosure](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/waist_yaw_steadywin_v36.png)
![Lid removed: published driver envelope](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/waist_driver_envelope_cutaway_v36.png)

## What is installed

| Location | Qty | Physical attachment |
|---|---:|---|
| Shoulder pitch | 2 | Separate rear annular flanges on six existing M4 carrier axes per side; original structural carriers and nuts retained |
| Shoulder roll | 2 | Four radial M3 screws per case; local service recess/bores in separate variants of the original fixed housing |
| Waist differential | 2 | Eight measured factory M2.5 axes per motor; 2.3 mm flange, local matching recesses in the printed W07 carrier |
| Hip yaw | 2 | Two split oval-rail clamps per case; original CNC crossheads retained, four M3x20 bolts and nuts per case |
| Waist yaw | 1 | Two countersunk M3 screws into added ribs, local clearance bores in the printed fixed mount |

The nominal cup has a 60 mm outside diameter, 2.4 mm side wall, removable 62 mm vented lid and cable opening. Most lids use four M2 screws; waist yaw uses two opposed screws and the necessary hip-hardware relief openings. Motor cage/flange dimensions differ by installation. The central shaft/magnet, motor bearings and outputs are not relocated or cut. The electronics bay is narrowed from 150 to 140 mm outside width, retaining its existing attachment centers. Hidden originals remain recoverable.

The GDS68-shaped body is **a published dimensional envelope, not detailed supplier PCB CAD**. The official downloadable STEP has a simplified motor and removable 57 mm driver cap, without PCB internals. The manual drawing supplies 47.040 x 47.003 x 8.651 mm dimensions. A clipped-square envelope and provisional PCB pilots are clearly labelled. Exact board outline/hole coordinates, connector/wire clearance, encoder gap/axis, hardware screw engagement and thermal contact need physical measurement. No inaccessible semiconductor geometry was invented.

The manufacturer explicitly lists the 6010 family for GDS68; an exact current GWK7010 firmware/hardware match remains unverified. Conflicting voltage descriptions do not qualify 12S full charge. These are packaging candidates, not procurement/electrical/current/thermal approval. No custom FOC PCB, motor limits or training assets were changed.

## Verification

- All 3,096 original input solids retain their bounds and volume, with all 469 original occurrence poses preserved; all 83 joints remain valid.
- The nine installed groups are grounded to their appropriate stator-owning rigid links. The recorded neutral audit finds zero new case/board/fastener collisions against visible surrounding non-fastener solids, above its 0.03 mm³ reporting threshold. Thread engagement and intentional source hardware interfaces are excluded explicitly.
- 21 actual native single-axis samples reach their bounded requested angles and preserve case ownership: 19 clear and 2 inward-arm conflicts. The requested right +60-degree sample correctly clamps to the retained +21-degree native limit; it is not a +60-degree motion pass. A separate right -60-degree sample passes. Neutral returns with maximum matrix error 2.74e-12. Continuous full-body clearance is unqualified.
- The independent full F3D reopen checks 3,096 original solids, 129 new/modified-group bodies and all 83 joint states/axes/ranges. The archive CRC is clean.
- All 15 STEP sets independently reimport with 28 expected connected solids and measured bounds/volumes. These separate files contain the intended parts, without hidden controller references or hardware.
- Native complete/detail/cutaway images were visually inspected. No strength, print retention, preload, thermal, electrical or dynamics qualification is implied. Legacy CAD materials are generic Steel proxies; appearances identify planned polymer, and CAD mass/inertia is not a physical build estimate.

## Preserved failures and corrections

The initial combined carrier/case prototype was replaced with separate additions, retaining original CNC crossheads. Disconnected prototype offcuts were quantified/removed before installation. Native clearance checks exposed waist flange/carrier overlap, small right-rail offsets and waist-yaw hardware interference; those were repaired locally with originals retained. Filling the waist-yaw unused screw holes also filled bearing relief and was rejected/restored. One tangent Boolean failed before any affected replacement was committed; its receipt is retained. Initial motion tests called `computeAll`, which reset driven angles to zero; those three samples are **not** motion evidence. That test was cooperatively shortened, its neutral reset passed, and the corrected direct-drive test asserts actual reached angles. Browser/skill-fetch/download failures are recorded in RESEARCH.md. Earlier rejected geometry and failed receipts remain in this directory.

Four initial STEP comparisons exceeded a fixed 0.1 mm³ threshold when using Fusion's low-accuracy volume estimates, despite matching bounds. The installed Autodesk API documents a default +/-1% physical-property calculation margin. The affected parts were checked with both directional solid differences: empty results in both directions. A controlled 1 mm³ sliver is detected by the same check, while the worst actual file gives valid zero-face/zero-lump/zero-volume differences. The first failed numeric review is retained; no CAD shape or locomotion gate was changed. [Geometric equivalence](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/step_geometric_equivalence.json), [metrology evidence](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/difference_metrology.json), [initial numeric review](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/step_roundtrip_default_volume.json).

## Exact evidence

[Preservation](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/preservation_and_parts.json), [mounts](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/physical_mounts.json), [local corrections](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/clearance_corrections.json), [lid relief](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/waist_yaw_lid_correction.json), [clamp fasteners](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/hip_clamp_fasteners.json), [neutral clearance](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/native_clearance.json), [actual motion](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/verified_motion_samples.json), [neutral reset](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/verified_motion_reset.json), [native reopen](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/independent_reopen.json), [STEP roundtrip](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/step_roundtrip.json), [saved release/hashes](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/saved_release.json).

Full native SHA256: `cd19c3318afe919a04f1024fbd1974c7fc8df03a1ad58747503a2c1ec5a3e112`. The v35 user-input archive SHA256 is `a0f74e690de0f15a12846c351fe62d36be6360889bef231cfdc2ef29f5ee9e31`.

Training remains stopped under the user's October 10 instruction. No automation or simulator is started. Custom circular FOC PCB0255 retains SHA256 `d6136915f8c79c7ba11bcbf8f39d75439624b727fdfe39c7c402193b874154fc`. Computer and saved Fusion model remain on/open. No commit or push is made.


Final handoff: saved cloud version 2 reopened, unmodified, nine parent-grounded cases, 83 valid joints and 16 retained mesh bodies. All old XDrive instances are hidden. The bridge holds only the read-only handoff request and its watcher is stopped. [Handoff receipt](final_handoff.json). [FOC chronological record](E:/Aditya/robot_sim/foc_controller/logs/0267-steadywin-driver-enclosure-cad-v36-with-measured-inward-arm-fit-limits.txt).

CPU-only history refresh completed: 41 preserved physical runs, 37 CAD archive groups, zero differing frozen hashes and no read warnings; eight historical missing manifests remain documented. Delivery hashes verify the full native archive and all 15 STEP files. The report's 31 local links and the updated BOM IDs/counts pass validation.
