# V21 waist, battery and upper-body placement

Updated September 27, 2026. This revision uses the user's recovered live v19 assembly. Its untouched input is preserved in `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v21\Input_recovered_v19_untouched.f3d`.

## Delivered geometry

- Both waist motors are the casing-free GWK6010-8 supplier model, with their output faces inward. The supplier drawing specifies the exposed fixed flange as **8-M2.5 on 40.5 mm PCD**, 4 mm effective thread depth. The new carrier uses 2.8 mm clearance holes, a stepped flange seat and curved support arms. Do not use the previous cased motor's 74 mm mount pattern.
- The existing six-M3 output pattern on 25 mm PCD and 26 mm crank radius are retained. The output geometry is partitioned from the stationary motor and follows the crank. The three larger locating features are not substituted for the output mounting screws.
- Waist order is **yaw -> lower pitch X -> upper roll Y**. Pitch center is (0, 48.343134, 927) mm and roll center is (0, 48.343134, 954) mm. Axis spacing is 27 mm. The spine is 15 mm rearward relative to the previous layout.
- Existing M6 rod ends and the 60 mm lower eye-center spacing are retained. The raised 6 mm base pin is supported at both ends; its new overall reference length is 102 mm. Each printed support moved 4 mm outward for housing clearance at 30-degree roll. Native 2 mm root fillets soften the support junctions.
- The oval spine is rotated 90 degrees to **18 mm across X and 10 mm across Y**, and extended to the proposed neck base. Its retained 0.55 mm wall is provisional, not strength-qualified.
- **Battery U01 is a solid 140 W x 85 D x 160 H mm packaging block**, forward of the spine and above the waist motors. It is supported by a lower cradle, 2 mm pad, upper restraint/strap guide and M4 fastener/crush-sleeve references. No completed electrical pack is implied.
- Three editable native sketches locate the upper body, label heights and show the hidden battery cell/BMS packaging study. Shoulders, arms, neck and head are placement sketches, not fabricated mechanisms.

## Battery packaging assumptions

The provisional 12S3P layout has 36 cylindrical 21700 cells in a 6-across by 6-high grid, with cell axes fore/aft. A 22.5 mm pitch and 21.55 mm diameter by 70.15 mm maximum cell envelope give a raw cell array of 134.05 x 70.15 x 134.05 mm. The enclosing block allows for holders, insulation, enclosure and connections. A **134 x 77 x 22 mm BMS/wiring reservation** sits above the cell grid. This is a compact packaging candidate, not a proof of global optimality. The exact cell, BMS, interconnect layout, fusing, cooling and enclosure remain to be selected before manufacturing. Do not infer mass/inertia from the solid block's default CAD material.

## Proposed dimensions from the neutral sole datum

| Location | Height |
|---|---:|
| Top of head | 1600.2 mm / 5 ft 3 in |
| Neck base | 1400.2 mm |
| Shoulder axes | 1340.2 mm |
| Elbow axes | 1080.2 mm |
| Wrist axes | 840.2 mm |
| Hand envelope bottom | 690.2 mm |

Shoulder centers are 360 mm apart. Upper arm is 260 mm, forearm 240 mm, hand envelope 150 mm. The head envelope is 150 mm wide by 180 mm high. Floor reference is the inherited lowest sole surface at world Z = -14.836568639 mm, not world zero. Unrelated leg/foot geometry was retained from the user's recovered source.

## Verification and limits

Native pure-axis travel checked at **pitch -30/+20 degrees** and **roll +/-30 degrees**. Four combined +/-10-degree corners and neutral were also checked. All nine sampled poses closed the two links and passed the documented targeted solid-intersection checks. These samples do not prove clearance throughout a continuous sweep or the full rectangle of pitch and roll limits. Native limits are set to the tested pure-axis endpoints.

The user explicitly raised the allowable spherical rod-end tilt to **35 degrees**, superseding the earlier 6.25-degree assumption in v19. Maximum calculated tilt in these nine samples is 24.86258 degrees. The reused ankle rod-end CAD is a surrogate, so internal spherical-bearing stop geometry, actual physical clearances and usable articulation under load still require measurement. Physical swivels were not added. A swivel would be a small two-axis yoke with perpendicular pivots to accommodate sideways link lean; the empty native joint-frame components are mathematical frames, not extra fabricated swivels.

Neutral battery-to-waist and battery-support fit checks pass. New custom bodies are positive-volume solids with one outer shell. All checked active component features report healthy. Existing legs retain 109 native joints each. The waist/battery group has 32 native joints. The smaller native waist/battery archive was reopened and checked for intact solids, battery dimensions and pitch/roll axes. The full assembly archive was exported successfully but was not reopened in a duplicate heavy document during this run.

The revised waist components contain copied source solids, new features and reconstructed native joints. Original source feature history remains in the untouched input archive. This is a geometry/kinematics revision; it does not certify printed-part strength, the thin spine, fatigue, bearing fits, torque capacity or battery safety. Custom hip gearboxes remain undesigned estimates.

## Files

All deliverables are under `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v21\deliverables`:

- `Humanoid_waist_battery_v21.f3d`: full assembly.
- `Waist_battery_v21.f3d`: smaller independently reopened waist/battery assembly.
- `Battery_12S3P_21700_140x85x160.step`: solid pack envelope in assembly coordinates.
- Three `U20/U21/U22` DXF files: placement, annotation and battery packaging sketches.
- `v21_battery_spine.png`, `v21_full_height_layout.png`, `v21_overview.png`: native Fusion captures.

Price-free BOM: `BOM_V21.csv`. Evidence: `docs/lower_leg/evidence/v21`; full construction/probe history remains in the working v21 directory. Read the JSON results before quoting a completed check.

Recorded native maximum closure error: 1.18e-12 mm. Reopened archive contains 32 native joints and 91 bodies.
