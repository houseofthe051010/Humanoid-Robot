# Nine XDrive Mini placements — v35

**Final scope: add the nine controller references; retain the existing mechanics.**
The user will adjust the mechanics later. No printed bracket or fit clearance is claimed.
The two green screw-terminal assemblies on each board are disabled for the user's
planned direct soldering. All 17 terminal solids per board are retained hidden for
reversible re-enabling; signal connectors, PCB, capacitors and rear plates remain.
Wires, solder joints and strain relief are not yet modeled.

Saved Fusion source: **Humanoid_XDrive_mounts_v35**, version 3.
Data ID: `urn:adsk.wipprod:dm.lineage:od_ADwCPRXWIEDsXKhBmvg`.

- [Full native robot](E:/Aditya/robot_sim/outputs/shin_cad_20260912/xdrive35/deliverables/Humanoid_XDrive_placements_v35.f3d)
- [Controller reference STEP](E:/Aditya/robot_sim/outputs/shin_cad_20260912/xdrive35/deliverables/MKS_XDrive_Mini_supplied_reference.step)
- [All nine controllers and their motors](E:/Aditya/robot_sim/outputs/shin_cad_20260912/xdrive35/nine_xdrives_and_motors.png)
- [Shoulder placement view](E:/Aditya/robot_sim/outputs/shin_cad_20260912/xdrive35/shoulder_xdrives_placement.png)
- [Waist placement view](E:/Aditya/robot_sim/outputs/shin_cad_20260912/xdrive35/waist_xdrives_placement.png)
- [Complete robot](E:/Aditya/robot_sim/outputs/shin_cad_20260912/xdrive35/robot_xdrive_v35_final.png)

| Location | Quantity | Motor |
|---|---:|---|
| Left/right shoulder pitch | 2 | GWK6010 |
| Left/right shoulder roll | 2 | GWK6010 |
| Two waist differential motors | 2 | GWK6010 |
| Left/right hip yaw | 2 | GWK7010 |
| Waist yaw | 1 | GWK7010 |
| **Total** | **9** | |

The nine instances share one editable controller definition. Their nominal encoder
center datums are radially centered over the existing 6 mm magnet axes. The provisional
PCB reference plane is 6 mm behind each motor rear datum; the supplied rear
plate's closest face is 1.5 mm behind it. **These are CAD placement dimensions,
not a verified magnetic air gap.** Actual encoder package and thermal-stack
dimensions remain unverified.

## Verification and deliberate remaining clashes

- All nine actual PCB solids match their expected frames after recompute.
- The saved native archive independently reopens with nine controller instances,
  145 bodies per instance (144 supplied solids plus one hidden axis datum),
  all 83 original native joints valid, and 1733
  original body bounds unchanged. Missing original bodies: 0.
- All 17 disabled screw-terminal bodies per board remain off after native reopen.
- Every experimental enclosure move, housing relief and case opening was undone
  after the user's steering. The original electronics box, bearings, shafts,
  covers, motor locations, wrists and hands remain. The proposed bracket
  generator was never executed.
- Nearby intersections are intentionally retained: shoulder pitch/electronics
  box, shoulder roll/housing and rear support region, waist controllers/covers,
  hip-yaw controllers/knee-drive cover, and waist-yaw controller/hip hardware.
  This is a placement layout, not an interference-free assembly.
- The center rear-plate opening and the encoder/PCB are different features.
  Enlarging a cover opening does not resolve all of the board/component clashes.

The isolated preview hides surrounding parts for visibility; they are retained
in the native robot. The source STEP's rear encoder and semiconductor/thermal
details are incomplete. No electrical, thermal, strength or manufacturing
qualification is claimed.

## Sources and preserved experiments

[Source audit](E:/Aditya/robot_sim/outputs/shin_cad_20260912/xdrive35/SOURCE_AND_SCOPE.md), [original mechanics restoration](E:/Aditya/robot_sim/outputs/shin_cad_20260912/xdrive35/user_scope_restoration.json),
[placement proof](E:/Aditya/robot_sim/outputs/shin_cad_20260912/xdrive35/placement_verification.json), [native reopen proof](E:/Aditya/robot_sim/outputs/shin_cad_20260912/xdrive35/independent_native_reopen.json),
[saved archive/hash receipt](E:/Aditya/robot_sim/outputs/shin_cad_20260912/xdrive35/saved_release.json), [144-body source reconciliation](E:/Aditya/robot_sim/outputs/shin_cad_20260912/xdrive35/source_body_reconciliation.json).

The unusable seven-surface user-library import is preserved. The replacement
is Aleksandr's supplied [XDrive STEP](https://hackaday.io/project/204985-mks-xdrive-mini-guide-set-up-tuning-arduino),
checked against [Makerbase's Mini drawings](https://makerbase3d.com/product/makerbase-xdrive-mini-high-precision-brushless-servo-motor-controller-based-on-odrive3-6-with-as5047p-on-board/).
Its outline/hole-spacing differences and incomplete detail are documented in
the source audit. Earlier packaging trials, failed API calls and the reversed
mechanical edits remain separate evidence, not final design changes.

Full native SHA256: `2b6782a34a4d1a720b8ef5445fd38056aeb2a28862c2d13ead7fa941f49946fb` (102,494,268 bytes).
Recorded UTC: 2026-10-23T18:15:13.549004+00:00. Training and the custom FOC PCB are unchanged.
