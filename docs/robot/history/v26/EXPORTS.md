# Local CAD and concept-part exports

Revision v26 · 2026-09-30. [Build report](../../BUILD_REPORT.md) · [BOM](../../BOM.md). These files were saved locally; this list is not a manufacturing release.

## Full assembly backup

[Humanoid_complete_v26_full_20260930.f3z](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/Humanoid_complete_v26_full_20260930.f3z) is the native F3Z package including source version 4 and the historical GWK motor dependency. File/dependency integrity passes; native standalone package reimport was not performed. The saved Fusion source was separately reopened and compared successfully.

SHA256: `9d5d89d043512a0696d6240498c41fe8d3abd092fe7d17f7198c8a6da5f02c48`.

## Compact native modules

| Module | File | Qualification |
|---|---|---|
| upper | [Upper_body_hands_head_v26.f3d](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/Upper_body_hands_head_v26.f3d) | Native reopen comparison PASS |

Only the upper-body compact module was exported and qualified in this pass; separate waist/spine and leg modules were not exported. Its already-native-imported snapshot passes the strict comparison against the current source assembly-context placements.

## Individual concept parts

Native STEP and millimetre STL exports are available for fit trials. Filenames retain the native component history; the files come from the current v26 model. Check tolerances, cable routes, fastener access and material/strength before manufacture. The two forearm forks have an unresolved metal-versus-polymer material choice.

| Component | STEP | STL, mm |
|---|---|---|
| N01 Oval spine 6005 servo adapter | [N01_Oval_spine_6005_servo_adapter.step](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/N01_Oval_spine_6005_servo_adapter.step) | [N01_Oval_spine_6005_servo_adapter.stl](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/N01_Oval_spine_6005_servo_adapter.stl) |
| H01 Defined vision head v25 | [H01_Defined_vision_head_v25.step](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/H01_Defined_vision_head_v25.step) | [H01_Defined_vision_head_v25.stl](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/H01_Defined_vision_head_v25.stl) |
| N25 dual side head pitch yoke | [N25_dual_side_head_pitch_yoke.step](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/N25_dual_side_head_pitch_yoke.step) | [N25_dual_side_head_pitch_yoke.stl](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/N25_dual_side_head_pitch_yoke.stl) |
| H25 camera visor bezel | [H25_camera_visor_bezel.step](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/H25_camera_visor_bezel.step) | [H25_camera_visor_bezel.stl](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/H25_camera_visor_bezel.stl) |
| A25 R forearm fork to wrist | [A25_R_forearm_fork_to_wrist.step](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/A25_R_forearm_fork_to_wrist.step) | [A25_R_forearm_fork_to_wrist.stl](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/A25_R_forearm_fork_to_wrist.stl) |
| A25 L forearm fork to wrist | [A25_L_forearm_fork_to_wrist.step](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/A25_L_forearm_fork_to_wrist.step) | [A25_L_forearm_fork_to_wrist.stl](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/A25_L_forearm_fork_to_wrist.stl) |
| H26 removable rear head shell | [H26_removable_rear_head_shell.step](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/H26_removable_rear_head_shell.step) | [H26_removable_rear_head_shell.stl](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/H26_removable_rear_head_shell.stl) |
| N26 pitch servo removable clamp | [N26_pitch_servo_removable_clamp.step](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/N26_pitch_servo_removable_clamp.step) | [N26_pitch_servo_removable_clamp.stl](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/N26_pitch_servo_removable_clamp.stl) |
| Hand26 R forearm wrist adapter | [Hand26_R_forearm_wrist_adapter.step](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/Hand26_R_forearm_wrist_adapter.step) | [Hand26_R_forearm_wrist_adapter.stl](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/Hand26_R_forearm_wrist_adapter.stl) |
| Hand26 L forearm wrist adapter | [Hand26_L_forearm_wrist_adapter.step](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/Hand26_L_forearm_wrist_adapter.step) | [Hand26_L_forearm_wrist_adapter.stl](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/Hand26_L_forearm_wrist_adapter.stl) |

The independent file review passes all ten pairs: binary STL structure, finite coordinates/normals, exact-welded watertight topology, consistent winding, positive volume and one connected surface per part; STEP solid structure and millimetre geometry contexts also pass. No mesh repair was applied. The source-volume check establishes unit scale, not exact surface retention. **Coordinates retain assembly placement; arrange and orient the parts in a slicer before printing.** Native STEP reimport, self-intersection, support/orientation, shrinkage, fastener fit, material and strength remain outside this file review.

The original hand part STEP/STL files remain under the attributed AmazingHand source directory. Failed full standalone F3D import is retained in the evidence as diagnostic history; use the F3Z backup for the full assembly.
