# v27 outer casings

Saved physical CAD revision v27, Fusion version 3, adds **43 cosmetic solids** while retaining the original mechanism and 23 body-axis settings. This is a cosmetic design/fit release, not a manufacturing or full-motion release. [Build report](BUILD_REPORT.md) · [BOM](BOM.md).

![Actual native casing overview](evidence/v27/handoff_iso.png)

## Shape, palette and assembly

Tapered pale limb shells and a split chest establish a continuous exterior, with open dark joint breaks and three restrained blue/teal identifiers. The original head, stereo camera, hands, actuators, spine and supported limb skeleton are retained. The original torso skin is hidden and preserved in favor of the new 12-piece covering.

Pale RGB 213/223/230; graphite RGB 70/84/95; blue accent RGB 26/139/165. Hip-roll front caps are pale; pelvis and knee/ankle guards are graphite. Colors indicate casing roles, not certified polymer or structural material.

| Casing group | Actual solids | Native dimensions / splits |
|---|---:|---|
| torso | 12 | Largest observed per-piece native axis dimensions 150.8×77.7×193.5 mm. Three horizontal bands, front/rear and left/right; largest width 150.75 mm and band height 193.5 mm. |
| upper arm | 4 | Largest observed per-piece native axis dimensions 78.2×49.7×172.0 mm. |
| forearm | 4 | Largest observed per-piece native axis dimensions 94.0×32.7×178.0 mm. |
| thigh | 4 | Largest observed per-piece native axis dimensions 137.2×68.1×166.0 mm. Final Z 473–639 mm trim and service opening checked directly on both sides. |
| shin | 8 | Largest observed per-piece native axis dimensions 121.6×66.0×137.8 mm. Front/rear panels split near Z 262 mm into upper/lower; maximum piece height 137.75 mm. |
| hip caps | 2 | Largest observed per-piece native axis dimensions 116.9×5.6×116.9 mm. |
| pelvis | 2 | Largest observed per-piece native axis dimensions 114.8×12.5×119.0 mm. |
| joint guards | 4 | Largest observed per-piece native axis dimensions 120.2×11.0×81.7 mm. |
| marks | 3 | Largest observed per-piece native axis dimensions 68.0×1.6×50.0 mm. |

Exact dimensions are in the [actual after-capture inventory](CASING_INVENTORY.csv). Earlier torso panels reached 302 mm width; the new left/right splits address that axis size. This does not certify a selected printer, orientation, support, brim allowance, shrinkage, insert fit or panel joining. Nominal skins use 2.5 mm profile offsets; no continuous minimum-normal wall guarantee is inferred from that parameter.

## Actual native evidence

- Original preservation PASS: 1,785 body signatures, eight hand meshes, 367 original placements, 333 original joint configurations and all 23 anatomical values. Exactly 43 bodies/occurrences added; no joints added. Native identity/token resolution and both placement domains were compared; no token drift was recorded.
- Static fit PASS for 43 final panels, merged from 109 exact selected batches and 934 original-body candidate comparisons. All inputs cover the exact final geometry; the four upper torso skins use final02 after new-only screw-head pockets. Earlier failed attempts remain history.
- The geometric intersection tolerance is 0.01 mm³. These are static-rest original-BRep checks, not a continuous sweep, minimum-distance guarantee, new-new panel collision certificate or print-strength test.
- The separate file-only mesh-box check considers 344 cover/hand-mesh pairs; four gross transformed hand-box overlaps were inconclusive. Exact retained source-STL vertices clear the same-side thigh skins by 13.30 mm right / 13.50 mm left along X. Source bounds match native bounds within 0.00002 mm; triangle counts differ slightly, so native vertex identity is not claimed.
- [Preservation record](evidence/v27/casing_preservation_final_result.json) · [Full static coverage and hashes](evidence/v27/static_fit_aggregate27.json) · [Actual native after capture](evidence/v27/casing_after_final.json).

## Printing, interfaces and remaining qualification

Covers remain cosmetic and follow individual rigid links. No original mounting hole, shaft, bearing, actuator or differential constraint was changed. Splits and six torso ventilation openings are modeled; final retaining lips/fasteners, service access, actual minimum walls and physical print fits need a prototype. Fastener quantities and polymer purchase mass remain unselected.

Added solid geometric volume is 2414.0 cm³. No mass is assigned until polymer density and print settings are selected. Added skin mass changes dynamics despite preserving the skeleton; the older Isaac torque table is not a new casing-loaded simulation.

All ten calibrated hip-pitch cap samples pass at −45°, −30°, 0°, +30°, +45° per side, after new-only pelvis relief. These use temporary copies against the two fixed new pelvis skins and original W02/W03/W04; they do not establish a full swept workspace. Raw native02 failures remain history.

The native v27 source is saved complete/unmodified as version 3. The full 219,727,989-byte F3Z package passes independent CRC/hash/member/dependency checks; native package reimport was not performed. [Export index](EXPORTS.md) records compact casing and individual STEP/STL qualification separately. Preserved v26 manufacturing files remain available for the unchanged head, wrists and forearms.

[Current casing BOM rows](BOM.csv). All prices are blank. Documentation remains local; no Git commit/push or publication was performed.

## Evidence limits

The original signature measurements use Fusion's default LowCalculationAccuracy for physical properties, separately from precise bounds. They do not qualify mass/inertia, strength or exact BRep equality. Mesh-box broad-phase results and source-vertex checks are static rest evidence. All original native geometry and joints remain preserved; the new skins still need physical retaining hardware and fit trials.

All 43 casing source parts retain Fusion's default **Steel physical-material placeholder**, despite their intended cosmetic-polymer role and pale/graphite/blue appearances. That placeholder is not a chosen material; native mass or inertia computed from it must not be used as the printed robot's mass model. Choose the actual polymer/density and print construction before a new dynamics/torque evaluation.

## Visual-reference provenance

[Saved reference review](evidence/v27/design_reference_notes.md) records the observed limb segmentation, dark joint breaks and quiet pale-shell palette, with [official image URLs and hashes](evidence/v27/references/visual_reference_manifest.json). These were styling references, not copied robot profiles, measured clearances or source geometry. All casing dimensions were set from this robot's preserved native mechanism.
