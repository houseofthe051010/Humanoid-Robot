# V12 — paired legs, circular gearbox case and hip interfaces

September 20, 2026. This revision starts from the **live user-edited v11**, preserved as `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v12\Input_live_v11_user_edits_preserved.f3d`. It does not regenerate the older saved v11 over those edits.

## Geometry retained from the user

Coordinates are millimetres: X across the legs, Y fore/aft, Z up. The single-leg source knee axis is `(0,23.343134,423.6)`.

- Thigh rail centres X±51: **102 mm spacing**. Actual rail bounds are 10 mm across X and 18 mm across Y. They run Z438.2–685, **246.8 mm** long. Wall thickness remains the earlier unmeasured 0.55 mm assumption.
- The DJI motor is **8 mm farther right and 10 mm lower** than the saved v11, with axis Z590. The estimated rear hub ends at X41 and the adjacent rail begins at X46: **5 mm nominal encoder space**.
- Yaw reference body starts at Z656.8. Roll is the user's revised **100×36 mm** envelope centred at `(0,26.343134,758.6)`. Pitch is **100×40 mm**, centred at `(-78,23.343134,803.6)`, tilted **25°**. These envelopes are not selected, measured hip actuators.
- Lower-leg, foot and ankle geometry is retained. The source's slight ankle pose and native joint graph are inspected separately from the new upper-leg interfaces.

## New construction

**Knee rail seats:** two CNC aluminum side saddles follow the 18×10 oval profile. Two M4 side screws per rail pass through matching rail holes into the block; internal crush sleeves are represented. The seats also contain the bearing-holder M5 clearance/head-access holes. Tapped thread envelopes, stock grade and engagement require manufacturing review.

**Motor and gearbox housing:** 124 mm outside diameter, 108 mm inside diameter (**8 mm radial wall**), with an 8 mm circular rear mounting plate larger than the 105 mm estimated motor. The motor mounting pattern is still the estimated 40×66 mm four-hole pattern. The rear-hub opening retains the encoder space; the wire exit follows the present wire envelopes.

The housing reserves **33 mm axial gearbox space**, X−28 to X5, ahead of the motor body. It contains **no sun, planets, ring gear teeth or completed carrier**. Existing prop posts remain reference geometry; the 33 mm reservation is not proof that the usable cavity fits a selected gearbox. Confirm which rotor features can be removed when the actual motor arrives.

A bridge from the top of the case clamps the opposite oval rail. Separate split caps permit assembly; the removable 7 mm cover has a bridge clearance notch and eight M4 positions. The housing therefore connects to both thigh rails. This change does not by itself establish torque or impact capacity.

**Output:** a separate flange and 16 mm shaft envelope connect to a 70×6 mm orange sprocket blank through a four-hole flange. Recessed screw heads avoid the adjacent rail. A **6 mm support pin** continues to the opposite rail and its split support block. There are no sprocket teeth or chain yet. The shaft coupling, output bearing, outer bearing seat, retention and support-block section remain open design work. The pin is a support reference, not a verified torque shaft.

**Hip interfaces:** Q01 is a CNC rail-to-yaw crosshead, with two slotted oval sockets and an annulus around the yaw output. Q02 is a yaw-output-to-roll cradle. Q03 is a curved, opposed-cheek roll-to-pitch bracket with a 25° flange and motor relief. They replace the rough user sketch solids as dimensional concepts. Motor mounting patterns, bearing support, tool access, fastener retention and a practical machining/split plan still need actual motor data.

The rejected front/rear fairings and old motor mount are hidden historical geometry in the parametric source. They are excluded from the active STEP/BOM. Intermediate fitting attempts are retained hidden with `ZZ_v12_fit_pass1_` names in the source only.

## Left/right layout

The bilateral assembly uses separate **Right_leg** and **Left_leg** component groups. The left geometry is reflected across the sagittal plane, with each leg shifted 130 mm from it: **260 mm between knee/yaw/leg centrelines**.

This is an initial packaging choice for the 1600.2 mm robot, not a proven biomechanical optimum. The pitch motors point inward. Their static inward X bounds give approximately **25.49 mm clearance** between the two leg envelopes. Their motor centres are consequently 104 mm apart; do not confuse that with the 260 mm leg spacing. Full hip range, pelvis structure, gait stance width and cable sweeps may change this choice.

The paired model uses copied solid geometry with reconstructed native lower-leg joints; the original feature history remains in the separately delivered single-leg parametric file. The paired assembly itself uses a parametric timeline for joints. Its joint zero is the source's current pose; travel limits are offset by the recorded source angle so the same physical endpoints are retained. The passive rod-end pin swivels are continuous; their full-turn stops are disabled to avoid an artificial stop at the local angle-frame wrap. Hip references remain attached to the thigh for layout inspection. This is not a complete articulated hip or an Isaac asset. Mirrored purchased-component geometry is a packaging reference; order normal vendor parts and verify their mounting orientation, connectors and handed features.

## Deliverables and evidence

Working directory: `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v12`.

- `deliverables/Leg_gearbox_hip_v12_parametric.f3d`: source with native feature history and original lower-leg joints.
- `deliverables/Bilateral_legs_v12.f3d`: paired assembly.
- `deliverables/Bilateral_legs_v12.step`: visible geometry exchange.
- `deliverables/parts/`: new custom component STEP files, provisional.
- `fit_validation.json`: source preservation, solid/feature checks and interface interference checks.
- `knee_motion_validation.json` and `knee_motion_summary.json`: sampled source knee articulation.
- `bilateral_build.json` and `bilateral_validation.json`: mirror geometry, native joints, spacing and paired checks.
- `archive_reopen_verification.json`: exported native readback.
- [BOM_V12.csv](BOM_V12.csv): active CAD component BOM, quantities per leg and for the pair, no prices. Hardware groups are assembly-level rows; the historical detailed lower-leg BOM remains [BOM.csv](BOM.csv). Ownership has not been audited.

Validation results: 227 selected interface checks found no solid intersections; 74 retained components had no unexpected geometry changes. The single-leg knee was checked at seven poses from 0° to 120° with no detected collisions in that test. Both paired knees were checked at 0°, 45° and 90°, and again at 30° after reopening the archive; the new motor and hip attachments followed correctly. Each leg has 97 valid native joints. All 527 active mirrored body bounds match their reflected source bounds; targeted Boolean comparisons confirmed the fitted rail seats, circular case and hip fork mirror exactly. Both native archives reopened without invalid joints. The history-bearing source retains 2,206 timeline entries.

Read the actual evidence files for scope and outcomes. The interference checks cover selected interfaces, and finite motion samples are not continuous collision or stress tests. Existing 8 mm shaft impact conclusions in [SHAFT_STRENGTH_8MM.md](SHAFT_STRENGTH_8MM.md) remain in force; this revision does not implement or validate the proposed 9 mm bearing-centre-to-block-edge redesign.
