# Current completed evidence — v29

Evidence below is from completed native jobs and the final Isaac run. Source scripts/raw diagnostics are under `E:/Aditya/robot_sim/outputs/shin_cad_20260912/v29`; final simulation results are under `E:/Aditya/robot_sim/physical_v29/validation`.

| Record | Finding |
|---|---|
| [Saved session](evidence/v29/saved_session.json) | Saved original live input as v29 checkpoint; revised source version 1 complete/unmodified before export |
| [Final saved-source handoff](evidence/v29/final_native_handoff29.json) | Saved cloud source reopened, matches released geometry/joint map, complete/unmodified; console/data panes hidden |
| [Automation shutdown](evidence/v29/automation_shutdown29.json) | Temporary watcher stopped; workbench run and startup switches verified off in Fusion |
| [Native release](evidence/v29/native_release.json) | Full F3D and geometry STEP exported successfully; STEP excludes mesh hands |
| [Archive integrity](evidence/v29/native_archive_integrity.json) | 750 ZIP entries, all payload CRCs valid, stable 178,961,497-byte archive |
| [Actual archive reopen](evidence/v29/native_archive_reopen.json) | 42 groups / 372 occurrences / 47 native constraints / 1545 visible shapes, correct bounds/axes/frames/neutral and no external referenced occurrences |
| [Saved native joint map](evidence/v29/native_joint_map_saved.json) | Actual reopened angular values used for final URDF; 12 small saved range differences retained in diagnostic record |
| [Final native inventory](evidence/v29/final_native_inventory.json) | Actual owners, grounds, source names, appearances, bounds and material placeholders |
| [Geometry validation](evidence/v29/geometry_validation.json) | Measured bilateral 275/250 mm arms and 20 elbow fork/horn-versus-case samples pass |
| [Waist clearance](evidence/v29/waist_output_clearance.json) | Both connected holders clear conservative continuous full-turn output/flange cutter envelopes with 3 mm allowance |
| [Elbow geometry](evidence/v29/elbow_build.json) | User-selected 160 kg actuator represented by authorized 150 kg CAD reference; floating old elbow parts removed |
| [Isaac joint measurements](evidence/v29/isaac_joint_validation.json) | All 23 body joints PASS with commanded/measured angles, other-joint motion, all-link FK comparisons and neutral reset |
| [Isaac stdout](evidence/v29/isaac_validation_stdout.log) | Actual USD conversion/runtime and per-joint PASS lines |
| [Export metadata](evidence/v29/export_metadata.json) | 23 DOF / 24 links / 140 visual meshes, coordinate transform, proxy dynamics and differential abstraction |
| [Pending hardware limits](evidence/v29/actuator_limits_pending.json) | All hardware effort/velocity/continuous torque fields null |

F3D SHA-256: `3e809affb85bda0ab33a346bd533cbb598c48e21c97178491a401ce42dda0461`. Native exact mesh-source bounds comparison has maximum difference 2.84e-14 mm across 1545 shapes. This is a strict same-coordinate comparison, not a loosened tolerance or a test of an earlier source.

Native views are actual Fusion captures. The archive import initially exposed an audit enum/default document-name issue and small saved range differences; raw failed audit attempts are retained in the working evidence folder. The final verification reads the actual opened archive and passes geometry/axis/ground checks, explicitly reporting range differences. The final Isaac test was rerun against that saved joint map. A full STEP native reimport was not performed.

Movement testing uses fixed-root/gravity-free test dynamics, with no contact qualification. Selected new elbow samples and conservative hip-output envelopes do not establish every whole-body pose, cable path, printed strength or real torque capability. Previous v28/v26 evidence stays under history and is not relabeled as a test of modified v29 geometry.

## Wrist alignment and current actuator update

Corrected native archive: `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v29\wrist_review_20260930\Humanoid_complete_v29_wrists_aligned.f3d`; SHA256 `0095c89563b39f3d77763b9020fb3f7a003e4b052af5c0803e19ff69580d552a`. Native reopen passed 1545 visible shapes, 47 joint frames/states/ranges and all parent grounds. Originals remain hidden and the before archive is preserved. Live source version 2. Evidence and reviewed image: `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v29\wrist_review_20260930`.

Active95% actuator/strict movement evidence: `E:\Aditya\robot_sim\physical_v29\validation\eff95_elbow7_20260930`. Fast GUI preview evidence: `E:\Aditya\robot_sim\physical_v29\validation\eff95_elbow7_20260930_visual`. The simulation visual meshes match the corrected hands; all joint frames and actuator settings are preserved. The older downloaded handoff remains historical unless refreshed.
