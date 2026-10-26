# Inspection evidence — v27

[Build report](BUILD_REPORT.md) · [Casing design](CASING_DESIGN.md). Final current geometry and saved-source evidence are separated from inherited v26 articulation and manufacturing history.

## Original-object preservation

- [Native before capture](evidence/v27/casing_before.json)
- [Final native after capture](evidence/v27/casing_after_final.json)
- [Strict comparison — PASS](evidence/v27/casing_preservation_final_result.json)
- [Comparator and scope](evidence/v27/compare_casing_preservation.py), [native capture](evidence/v27/capture_casing_preservation.py), [24 synthetic behavior tests](evidence/v27/comparator_synthetic_qa.json)

The final comparison retains 1,785 original body signatures, eight meshes, 367 placements, 333 joint configurations and all 23 anatomical values. Exactly 43 bodies/occurrences were added. No joint was added and no token drift was recorded. Volume/area/centroid use the native API's default LowCalculationAccuracy; these are consistent signatures, not exact geometry hashes or accurate mass/inertia measurements. Precise bounds, native token resolution and both root-context and owner-local placements are separate checks.

## Final fit coverage and sampled motion

- [Exact 43-part static aggregation — PASS](evidence/v27/static_fit_aggregate27.json): 109 selected current attempts, 934 original-BRep candidates. Every batch input is hashed and checked against the final after geometry.
- [Selected final attempts](evidence/v27/final_fit_progress27.json): upper torso and pelvis use final02 after new-only screw-head/pelvis relief. Initial rejected trials remain under the local output directory, without suppressing their failures.
- [Ten hip-pitch samples — PASS](evidence/v27/hip_pitch_samples_final_review27.json): temporary-copy cap poses against two fixed new pelvis panels and original W02/W03/W04. Five angles per side; not a full swept workspace.
- [Hand source-vertex separation](evidence/v27/hand_source_vertex_separation27.json): current root matrices applied once; source/native bounds agree within 0.00002 mm, source/native triangle counts differ slightly. Positive source-envelope X gaps 13.30/13.50 mm clear new thigh skins. Gross box overlaps alone were not treated as collisions.

Static BRep checks use a 0.01 mm³ intersection tolerance and preserve original rest/ground/configuration. They do not establish minimum clearance, new-to-new cover separation, continuous motion, cable routing, wall thickness, force or strength.

## Saved source and package

- [Final native handoff — PASS](evidence/v27/final_native_handoff27.json): complete/unmodified v3, 410 placements, 23 axes, no pending snapshot, command panel hidden; source kept open.
- [Native saved source](evidence/v27/native_final_save_status27.json): Humanoid_complete_v27, complete/unmodified version 3.
- [Full F3Z integrity — PASS](evidence/v27/full_archive_integrity27.json): exact size/hash, all outer and nested CRCs, root source version 3 and GWK dependency version 1; native standalone import/reopen was not performed.
- [Evidence file hashes](evidence/v27/evidence_files_sha256.json)
- [Compact casing-only native reopen — PASS](evidence/v27/casings_reopen27.json): all 43 solids, identity placements, palette/bounds/volume/material signatures; source restored unchanged. The archive has no skeleton or joints.
- [Current export index](EXPORTS.md): file existence, file topology and native reopening remain separate qualifications.

## Initial casing mesh export review

The [raw initial STL review](evidence/v27/casing_stl_validation27.json) records 35/43 file reviews passing. Its raw failed rows are retained: native tessellation defects do not erase the successful CAD/source fit or qualify a failed STL. Retessellated/derived files require their own provenance and final topology/scale checks; consult [EXPORTS](EXPORTS.md) for the final recommended files.

## Native previews

![Actual final portrait view](evidence/v27/handoff_iso.png)

[Earlier wide isometric](evidence/v27/release_iso.png).

[Front](evidence/v27/release_front.png) · [Rear](evidence/v27/release_rear.png) · [Side](evidence/v27/release_side.png).

## Retained engineering evidence

The [v26 evidence index](history/v26/EVIDENCE.md) and [build report](history/v26/BUILD_REPORT.md) retain 23 measured axis tests, five paired differential fixtures, final source/rest checks, nine head-clearance samples, hand provenance, material/feature audits, verified upper-module import and ten earlier concept-part STEP/STL reviews. Unchanged joints do not make the newly added covers continuous-motion qualified. Earlier failed full F3D import and raw recovery/placement attempts remain diagnostic history.

All documentation is local only. No Git commit, GitHub push or publication was performed.
