# Lower-leg v9 revision

Revision date: 2026-09-19. This is a geometry prototype with analytical strength screening, not a tested robot.

## Source and preservation

The live design was named `Shin_PA12CF_7010_392mm_v8`. Its original archive is preserved at `outputs/shin_cad_20260912/v9/Input_live_v8_preserved.f3d`. A live external motor reference prevents importing that archive as a self-contained local file. Every shared component's body count and total solid volume matched the saved v8 release within the recorded tolerance. The new revision therefore uses that native v8 release and copies the extra live motor/reference bodies into the new document. This comparison does not establish identical feature history or simulation studies; the original live document remains intact.

The user-added root body is preserved in hidden `U03_Preserved_live_root_layout`. Earlier GIM and GWK layout references also remain hidden. They are excluded from the build BOM totals and exchange assembly. No simulation result was promoted to a strength qualification.

## Foot plate and plastic sole

- Removed the old hole patterns from the final aluminum and plastic bodies while preserving their outer outlines.
- Eight current pillow mounting positions drive matching diameter5.4 mm holes through both layers. Coordinates are in `outputs/shin_cad_20260912/v9/foot_mounts.json`.
- Roll mounts: X=±20.9, Y=-7.7 and31.0 mm. Heel mounts: X=±41, Y=29.75 and71.55 mm.
- Eight M5x20 screws, with one1 mm washer above the bearing base and one beneath the plastic, clamp the complete stack. Eight M5 nuts sit underneath.
- The sole is10 mm thick with a flat ground surface. This adds4 mm to the former6 mm sole to house the fasteners without raising the toe relative to the heel.
- Bottom nut/socket pockets are11.4 mm diameter and6 mm deep. There is4 mm of plastic above the bottom washer. Nuts occupy Z=-13 to-9 mm, washers Z=-9 to-8, screw tips Z=-13.8 and ground Z=-14 mm. Check actual socket OD; the nut is accessed with a tool rather than trapped in a hex pocket.
- The0.2 mm nominal tip recess is small; measure actual screws before assembly. Printed plastic creep and clamp preload remain physical assembly considerations. The CAD does not establish an allowable bolt torque.

## Narrower shin and knee

“8 mm closer” is implemented as4 mm inward per rail. Centre spacing changed28→20 mm, with rail centres at X=±10,Y=6 mm. The oval outside profile is18×10 mm, leaving2 mm between the two steel rails. Rail length354.6 mm and knee-to-ankle-axis distance392 mm remain unchanged.

The motor carrier, ankle adapter and TPU clip bores follow the rails, as do their cross-hole locations and steel crush sleeves. Motor and ODrive placements remain as in v8. The exterior ankle reliefs from the earlier motion work are retained.

The8 mm middle knee slice has no physical body. Its occurrence is renamed `N00_Knee_joint_datum_NO_PHYSICAL_PART` and retained solely to preserve native joint references. Four aluminum slices form a42 mm stack. The left and right knee bearing/clamp/stub assemblies move inward4 mm each; the left sprocket reference follows its mounting face. Shaft cut length is104 mm instead of112 mm. Stack ties are represented as M3x55 and dowels as diameter6×48 mm; verify stock availability and cutdown needs.

See [knee strength screening](KNEE_STRENGTH_V9.md). At90 lb and5x bodyweight on one leg, even favourable outer-block-face load transfer gives about441 MPa in an8 mm shaft. The shaft has been retained geometrically as requested, not approved for running or jumping.

## DJI10018 77KV motor reconstruction

No verified CAD for the exact DJI motor was found in the bounded search. A different manufacturer's10018 and DJI E5000 drawings are not substitutes for this motor. Reconstruction uses the user's photos and estimated105 mm OD/30 mm black body.

`R01_DJI_10018_77KV_ESTIMATED_REFERENCE` is parked beside the knee, not attached to a designed motor bracket. It includes a black can/front plate, exposed rear stator ring and spokes, four mounting bosses and bores, rear hub, visual copper windings, phase-wire envelopes and uncut prop posts.

Estimated rear projection6 mm plus30 mm body plus24 mm prop-post projection gives60 mm axial extent, excluding wires. Four rear mounting centres are at(±20,±33) mm in the rear face, a40×66 mm rectangle. Bore diameter4.2 mm is only a provisional clearance envelope; no thread specification is claimed. Hub, shaft, boss, winding and post geometry is illustrative. Do not use the generated volume as motor mass/inertia or machine its mating bracket before measurements.

The editable reconstruction inputs are `outputs/shin_cad_20260912/v9/dji_motor_parameters.json`; regenerate using the paired builder in Fusion after obtaining measured values. QDD planetary geometry, ratio, output bearing architecture and knee mount are still to be designed. The old sprocket remains a layout reference pending that decision.

## BOM and assembly organization

The price-free [BOM](BOM.md) and [CSV](BOM.csv) cover one current leg, its knee/thigh interfaces and the planned DJI reference. Purchase ownership is not inferred. Hardware missing from inherited CAD is explicitly listed with unresolved lengths.

Subassemblies can be organized as lower leg, upper leg, complete leg, legs/pelvis, upper body and full robot. Nested components provide structure inside one design. **Separate linked Fusion designs** are the option that gives subassemblies their own version histories. Use shared interface datums and explicit joints at each assembly boundary. The current flat component structure has been retained for this revision; restructuring was deferred as requested. The code can later be split into corresponding builders without changing the mechanical interfaces.

## Validation scope

Final geometric results and archive-reopen evidence are in the v9 deliverables README and JSON records. Static intersection checks distinguish inherited supplier bearing fits and simplified screw/thread overlaps from newly introduced interference. Finite motion samples do not prove continuous collision-free travel or structural safety. The old rejected ankle pitch/roll corner combinations remain rejected; a rectangular joint-limit box must not be treated as the accepted motion envelope.
