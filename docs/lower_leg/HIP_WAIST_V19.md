# V19 compact hips and centered output supports

Native archive exported and reopened successfully. The preserved input and the prior v18 archive remain available.

## User-directed geometry

- Preserve the live edited v18 input in `Input_live_v18_user_edits_preserved.f3d` and the prior v18 release.
- Narrow complete leg centers from 260 to 240 mm. Recenter each hip roll over its hip yaw, reducing roll-center spacing from 316 to 240 mm.
- Bring pitch centers from X±62 to X±46.808 mm: the nearest rear tube rims touch the robot centerline. Maintain the 25-degree tilt; the nonparallel back faces therefore meet at their rims, rather than becoming coincident faces. Place pitch centers at Z824.6 and roll centers at Z753.6; knee geometry and waist-yaw height remain unchanged.
- Replace the pitch and roll casing sleeves with separate aluminum tube references, 110 mm OD / 106 mm ID / 46 mm axial length. Retain the estimated 105 mm DJI10018 motor geometry inside each. Planetary internals remain undesigned.
- Replace the offset rectangular yaw plate with a centered sculpted bell and two curved output cheeks. Retain the actual GWK7010 six-hole, 25 mm PCD output interface and the existing 35 mm yaw journal / 6007 bearing reservation.
- Separate the housing load path from the roll output: a curved pitch-to-roll fork attaches to both recessed tube endcaps; independent 50 mm output-journal references connect both sides of the roll axis to the leg/yaw support.
- Use paired 61810-sized 50×65×7 mm bearing envelopes at the roll axis. Dimensions come from the [SKF 618 series table](https://cdn.skfmediahub.skf.com/api/public/0901d19680237e2b/pdf_preview_medium/0901d19680237e2b_pdf_preview_medium.pdf). This is a packaging reference, not a selected or load-qualified bearing.
- Taper the rear pitch covers around the smaller central hub and reshape the printed waist around them. Retain a hollow electronics cavity, the corrected stationary waist-yaw mount, vertical neutral spine and inward-facing GIM6010 references.

## Added waist differential

- Move the two inward-facing GIM6010 centers from X±73, Z1040 to X±63.5, Z995 mm: 45 mm lower and 19 mm less center-to-center spacing.
- Raised Ø6 mm steel cross-pin at Y3.343, Z935 mm, supported at both ends of the printed yaw-output base. Pin length is a 94 mm retention envelope; both rod-end centers are at X±30 mm.
- Two 26 mm-radius aluminum cranks follow the actual six small output holes. The stationary carrier follows the separate eight-hole 74 mm PCD interface.
- Copy the same Wixroyd 65720.W0006 M6 female rod-end surrogate used at the ankles. Two M6×1 rods have 69.035 mm eye spacing and approximately 33.035 mm stock length, with 12 mm nominal engagement at each end and thin jam-nut envelopes.
- The G1 EDU specifies ±30° pitch/roll, and the referenced iCub model uses ±30° roll. That is a comparison target, not the travel of this design. The user chose to retain the existing M6 rod ends after being informed of their articulation limit.
- Initial design limits: **±20° pitch, ±5° roll**, subject to the native clearance report. An 861-pose numerical grid gives maximum rod-end tilt 5.674° against the assumed 6.25° hardware limit. Per-actuator motor-angle/joint-angle ratios are 1.036–1.949; neutral pitch is 1.309 and roll 1.257. Two-actuator combined torque must be calculated with the full Jacobian, not a single reduction number.
- Optional physical swivels were not added. These would be tiny two-axis yokes: one hinge rotates about the transverse pin and another perpendicular hinge lets the link lean sideways, relieving the rod end's limited spherical tilt. They need additional room and new clearance checks. The zero-body native joint frames are only mathematical frames and are not these extra fabricated swivels.

Published comparison sources: [Unitree G1](https://www.unitree.com/g1/), [official iCub model](https://github.com/robotology/icub-models/blob/master/iCub_manual/robots/iCubGazeboV2_5_visuomanip/model.urdf).

## Design boundaries

These are prototype interfaces. The custom gearbox, its dual-ended output construction, pitch-output pattern, final bearing fits, axial retention and manufacturing drawings remain unfinished. The detailed raw DJI motor and its mounting pattern remain earlier estimates, not a measured production geared actuator. Standing hip layout references retain their existing rigid native relationships; they are not a completed articulated three-axis hip. No strength, fatigue, chain-clearance or full-travel claim is made.

## Evidence

Construction scripts, source inventory, targeted fit checks, isolated adapter images and reopened native-archive checks are retained in this revision folder. Only report a check as passed after its result file exists.

## Verified release checks

- Targeted standing hip fit: no remaining reported solid intersections, disconnected bodies, invalid joints or unhealthy features in the checked parts.
- Native waist: 9 sampled poses, including combined corners; maximum closure error 2.98e-10 mm, maximum rod-end tilt 5.6677�, and no reported intersections in the documented pair set.
- Archive reopened: all four aluminum sleeves remain 110/106 mm; hip roll and yaw are concentric in X; leg center spacing is 240.000 mm; neutral spine is vertical and the 6010 output faces point inward.
- These are sampled CAD and kinematic checks, not a continuous collision proof, manufacturing approval or strength analysis.
