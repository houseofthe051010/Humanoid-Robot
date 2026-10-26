# Current exports — v29

Saved Fusion source: **Humanoid_complete_v29_revised**, version 1, `urn:adsk.wipprod:dm.lineage:WTKBF_3ORCqcrKBaU4opCw`. Preserved live-input checkpoint: **Humanoid_complete_v29**, version 1, `urn:adsk.wipprod:dm.lineage:rJYaX75CRoKLryXt6Q5RNQ`. The old v28 release remains intact.

| File | Bytes | Qualification |
|---|---:|---|
| [Humanoid_complete_v29_revised.f3d](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v29/deliverables/Humanoid_complete_v29_revised.f3d) | 178,961,497 | Full native reopen and CRC PASS |
| [Humanoid_complete_v29_revised.step](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v29/deliverables/Humanoid_complete_v29_revised.step) | 129,597,512 | Geometry only; mesh hands omitted; not STEP-reimported |
| [humanoid_physical_v29.urdf](E:/Aditya/robot_sim/physical_v29/assets/humanoid_physical_v29.urdf) | 74,449 | Actual Isaac conversion and all 23 movement tests PASS |
| [humanoid_physical_v29.usd](E:/Aditya/robot_sim/physical_v29/assets/usd/humanoid_physical_v29.usd) | 1,469 | Actual Isaac conversion and all 23 movement tests PASS |

The full F3D is portable/localized, independently reopened with all 1545 visible shapes, 47 native constraints, exact saved frames/bounds and eight hand meshes. No external referenced occurrence remains. CRC/hash and native reopen are separate completed checks. [File hashes](evidence/v29/release_files.json).

STEP took approximately 13 minutes and finished successfully after appearing stalled. It carries geometry/placement, omits mesh hands and is not a native joint/color/print qualification. No STEP reimport was performed. The native archive is the complete CAD handoff.

URDF must remain alongside its full `meshes/` directory. USD must retain its `configuration/` layers; the small top-level USD file is only an entry point. The handoff includes the complete `physical_v29` package, test script, metadata and final validation outputs. Mass/inertia remain test proxies. September 30 user actuator assumptions are configured in the workspace package; use the active `actuator_limits.json` and custom coupled actuator from [Actuator calculations](ACTUATOR_CALCULATIONS.md). Earlier downloaded packages retain original fixture settings unless updated.

The [Downloads handoff](C:/Users/rshan/Downloads/Humanoid_v29_CAD) contains CAD, the complete simulation package, previews and the current report/BOM. Source construction/diagnostics: `E:/Aditya/robot_sim/outputs/shin_cad_20260912/v29`. Documentation and packages remain local; no Git commit/push/publication occurred.

## Wrist alignment and current actuator update

Corrected native archive: `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v29\wrist_review_20260930\Humanoid_complete_v29_wrists_aligned.f3d`; SHA256 `0095c89563b39f3d77763b9020fb3f7a003e4b052af5c0803e19ff69580d552a`. Native reopen passed 1545 visible shapes, 47 joint frames/states/ranges and all parent grounds. Originals remain hidden and the before archive is preserved. Live source version 2. Evidence and reviewed image: `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v29\wrist_review_20260930`.

Active95% actuator/strict movement evidence: `E:\Aditya\robot_sim\physical_v29\validation\eff95_elbow7_20260930`. Fast GUI preview evidence: `E:\Aditya\robot_sim\physical_v29\validation\eff95_elbow7_20260930_visual`. The simulation visual meshes match the corrected hands; all joint frames and actuator settings are preserved. The older downloaded handoff remains historical unless refreshed.
