# Local saved CAD and exports — v28

[Build report](BUILD_REPORT.md) · [Evidence](EVIDENCE.md) · [Downloads handoff](C:/Users/rshan/Downloads/Humanoid_v28_CAD).

## Saved full source

`Humanoid_complete_v28`, Fusion version **2**, `urn:adsk.wipprod:dm.lineage:MsQkWo2RS0WYAsfp69Rfzw`, is complete/unmodified. Native final counts are 1,855 BRePs, eight meshes, 437 occurrences and 333 constraints including 23 body axes. Camera changes and export documents did not alter saved geometry or source pose. Both new structural waist halves are visible; original W02/W03 and rejected prototype covers stay preserved hidden.

## Full dependency package

[Humanoid_complete_v28_full_20260930.f3z](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v28/deliverables/Humanoid_complete_v28_full_20260930.f3z) is **226,078,397 bytes**. SHA-256: `3c67d291f4acf5c94ed3753206ac4a2726dfaf0d4d072501ab0889e2bd3d772f`. The F3Z includes saved root version 2 plus the linked GWK6010 motor source version 1. Outer/nested CRC, declared members, graph root and dependency IDs pass. **Native complete-package reimport was not performed.** Package integrity and source native handoff are separate evidence; do not call the complete package independently reopened.

## Portable casing set

| File | Bytes | Qualification |
|---|---:|---|
| [Active_casings_v28.f3d](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v28/deliverables/Active_casings_v28.f3d) | 7,052,851 | Independent native reopen PASS, 58 active connected solids |
| [Active_casings_v28.step](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v28/deliverables/Active_casings_v28.step) | 7,029,918 | 58-part geometry only; joints/colors are not a STEP guarantee |


These isolated source copies contain only the 58 active C27/C28 casing and waist replacement bodies, already placed at the saved robot pose. They exclude the frame, motors, original head, hand meshes, old source holders and 12 rejected prototypes. The F3D uses independent identity component placements with geometry already in root coordinates; it is not a standalone articulated robot.

[Changed_parts_STEP](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v28/deliverables/Changed_parts_STEP) contains 25 individual active C28 part exports. CAD source remains millimetre-scale. STEP exports succeeded and have recorded hashes; their geometry was not independently reimported as STEP. Use the independently verified native F3D as the portable geometry reference.

[Export manifest](../../evidence/v28/casing_exports28_manifest.json) records source paths, root bounds, root-frame volume/topology, palette and material intent. [File hashes](../../evidence/v28/casing_export_files28.json) bind all 27 casing export files. [Native reopen](../../evidence/v28/casings_reopen28.json) confirms 58 one-connected solids, strict same-frame bounds/volume/topology, colors and placeholder material names. The integration coordinate-domain issue is documented, not resolved by loosening tolerances.

No new STL set is supplied as print-qualified. Final cosmetic retention, structural polymer and printer settings need detailing; STEP or F3D can be used to prepare a prototype after that review. Native Steel physical-material placeholders must not be treated as a printed mass model.

## Retained checkpoints

V27 and v26 source/archive folders and documentation remain untouched as history. Preserved v26 head, wrist and forearm manufacturing trials remain in [v26 export index](../v26/EXPORTS.md). They are not automatically qualified with the new external skins or changed mass. Earlier incomplete or diagnostic full F3D/STL files remain historical and are not the current handoff.

Native previews are actual Fusion API renders; there is no generated-image substitute for geometry. The handoff includes whole-body front/rear/side/isometric views and feet/elbow/waist closeups. Local documentation and exports were not committed or pushed to GitHub. Temporary automation is stopped and startup reset to false.
