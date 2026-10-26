# Current verification evidence — v28

[Build report](BUILD_REPORT.md) · [Hashes and copied source paths](../../evidence/v28/evidence_manifest28.json).

All claims below refer to completed final records. Raw failed and superseded iterations remain in the local v28 construction folder; the invalid empty-target waist result and the out-of-limit initial left-shoulder probe are not accepted evidence.

| Evidence | What it establishes |
|---|---|
| [Preservation](../../evidence/v28/casing_preservation_final_result.json) | Original 1,828 body signatures, eight meshes, 410 placements/grounds, 333 configurations and 23 anatomical values preserved; 27 declared new bodies/occurrences, no new joints |
| [Before](../../evidence/v28/casing_before.json) / [after](../../evidence/v28/casing_after_final.json) | Hash-bound native identity/path, native property signatures, geometry counts, joint and two-domain placement captures |
| [Visibility](../../evidence/v28/active_casing_visibility28.json) | 58 active C27/C28 pieces, 12 hidden prototypes; old structural holders retained hidden, both replacements visible |
| [Static summary](../../evidence/v28/static_fit_final_summary28.json) / per-part final02 records | 25 active new pieces, 867 selected BRep comparisons, zero intersections over 0.01 mm³, including new-part pairs |
| [Final rim subset](../../evidence/v28/shoe_rim_ground_refinement28.json) / per-rim final03 records | The final rim geometry only shrinks; no added volume, and selected static candidates were rechecked |
| [Left elbow](../../evidence/v28/Left_elbow_continuous_clearance28.json) / [right elbow](../../evidence/v28/Right_elbow_continuous_clearance28.json) | Conservative continuous axial/radial proof against nine selected moving parts per side through −135° to 0°; no cover bridge across bending |
| Left/right knee and hip-yaw final motion records | Five selected poses per side for each guard/collar |
| Left/right shoulder cuff final motion records | Six mirrored in-limit samples per side, with 35 actual fixed torso/frame/carrier targets |
| [Neck collar](../../evidence/v28/neck_collar_head_motion_final28.json) | Thirteen pitch samples, 33 moving actual head/camera shell solids |
| Left/right ankle final probes | Fifteen measured-axis pitch/roll combinations per foot against 93 fixed-neighbor BRePs |
| [Shoe contact](../../evidence/v28/shoe_ground_margin28.json) | Nine orientations per foot, 36 casing/sole minimum-height comparisons; final minimum margin 0.794 mm |
| [Waist bends](../../evidence/v28/waist_torso_motion28.json) / [hip caps](../../evidence/v28/hip_caps_waist_motion28.json) | Nine selected bends with 13 actual torso solids and ten selected hip-cap samples against the two new waist holders |
| Waist build records / [torso relief](../../evidence/v28/torso_hem_refinement28.json) | Complete original holder interfaces included, one connected body per half; conservative hem relief without skeleton edits |
| [Native casing reopen](../../evidence/v28/casings_reopen28.json) | Independent native F3D reopen of 58 connected solids; strict same-root-frame bounds/volume/topology and colors |
| [Saved handoff](../../evidence/v28/final_native_handoff28.json) / [shutdown](../../evidence/v28/final_automation_shutdown28.json) | Saved v2 complete/unmodified, 437 occurrences and 23 axes, no pending snapshot; console hidden, watcher disabled, Fusion left open |
| [Full package integrity](../../evidence/v28/full_archive_integrity28.json) | Full F3Z CRC, nested members, root v2 and GWK dependency v1; no native full-package reimport |

Default Fusion physical-property integration is approximate and can change with rotated coordinate domains. Source preservation compares signatures consistently; export compares the unchanged temporary source geometry in the same root frame. [Root-frame diagnostic](../../evidence/v28/export_root_frame_diagnostic28.json) records exact matching copy volume/topology after an orientation-dependent proxy mismatch. No strict comparison tolerance was loosened.

Calibrated physical shaft/bore faces determine motion frames. The approximate 0.1 mm inherited stock bearing-center offsets were left unchanged. These are local geometric checks, not mass/inertia, strength, thermal, cable-sweep, impact, continuous whole-body or print qualification. The earlier [v27 evidence](../v27/EVIDENCE.md) and [v26 evidence](../v26/EVIDENCE.md) remain distinct historical baselines.
