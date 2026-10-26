# Upper-leg layout v10

This revision develops a **1600.2 mm (5 ft 3 in) robot layout** from the live v9 leg, including the user's longer thigh rails and moved DJI motor. The original live document was archived before editing. The lower-leg geometry is retained; the new upper leg is a packaging prototype, not an impact-qualified assembly.

## Placement and height

| Item | Layout dimension |
|---|---|
| Standing ground plane | Z = −14 mm |
| Knee axis | Z = 423.6 mm; 437.6 mm above ground |
| Knee-to-hip pitch reference | **400 mm** |
| Hip pitch reference height | Z = 823.6 mm; **837.6 mm above ground** |
| Height remaining above hip datum | **762.6 mm** to the 1600.2 mm target |
| Thigh rail centers | X = ±43 mm; Y = 23.343134 mm |
| Thigh rails | 18 × 10 mm oval, long direction Y; **351.8 mm** modeled length, Z446.2–798 |
| Knee motor center | Y = 23.343134 mm; Z = 685 mm, **261.4 mm above knee** |
| Hip yaw reference | Vertical axis at X0/Y23.343134; vendor motor rear at Z808.8 mm |
| Hip pitch motor reference | Unselected Ø100 × 40 mm envelope; **10° provisional tilt**, angle/direction undecided |

The 400 mm thigh is close to the existing 392 mm shin axis length and leaves room for the knee motor, an intermediate transmission and the hip references. It is a design choice for packaging, not a derived anthropometric requirement. The hip height is a standing reference; bent knees reduce it. There is no complete 1600.2 mm body yet.

## Motor and printed shell

The estimated DJI10018 77 KV motor remains near the right rail. Its orientation is reversed from the supplied live layout so the **stationary four-hole face faces the right rail**, and the drive/prop side faces the left chain space. This makes a short mounting path possible while preserving the requested side placement. The opposite leg can later be mirrored.

The rear motor plane is X27 mm; the estimated central rear hub reaches X33 mm. The right rail's inner face is X38 mm, leaving **5 mm axial space**. A hidden reference sketch marks a Ø28 mm encoder envelope; an actual encoder, magnet and cable have not been selected.

- `T01_Knee_motor_rail_shell_PROVISIONAL`: 8 mm thick mounting web at X29–37, four Ø4.5 mm clearances on the estimated 40 × 66 mm pattern, Ø42 mm central opening and lower motor-wire exit.
- Two integrated saddle halves grip the right oval rail above and below the encoder region. The two separate `T02` caps make the clamps removable. Their socket has 0.3 mm provisional diametral print clearance; calibrate to the tube and printer.
- Four nominal M4×25 clamp screws and nut envelopes are shown. Four nominal M4×12 motor screws provide only 4 mm of provisional engagement into the estimated bosses. These are **not a final screw purchase specification** until actual threads and depth are measured.
- Motor screw head/tool access passes through the saddle and cap regions. The central encoder space remains open. No holes were added through the thin steel rail for this clamp design.

The shell is deliberately a separate printed component with separate caps. Neither its strength nor the clamp's ability to transmit the final gearbox/chain reaction has been established. See [Future work](FUTURE_WORK.md) before manufacture.

## Transmission references

The visible sketches show the proposed **2.5:1 first chain stage followed by a 1:1 final stage**. No chain links, teeth, gearbox internals, intermediate bearings or output couplings were modeled.

| Reference | Pitch-circle diameter | Center Z |
|---|---|---|
| Knee motor output guide | 40 mm | 685 mm |
| Intermediate primary guide | 100 mm | 577 mm |
| Intermediate secondary guide | 70 mm | 577 mm |
| Knee guide | 70 mm | 423.6 mm |

An alternative Ø80 mm intermediate circle for 2:1 is saved as a hidden sketch. The existing knee blank remains a historical reference, not a designed sprocket. Circle sizes show continuous diameter ratios; real chain pitch and integer tooth counts will change these values.

The two sketch planes are only 6 mm apart (X−30 and X−24). This is an unresolved packaging allowance: real chain widths, hubs, bearings and adjustment may require more spacing. Do not infer a buildable two-chain stack from the circles alone. Encoder placement on the intermediate shaft is recorded as an option, with downstream backlash still to evaluate.

## Hip references

`T04` copies both the stationary region and visible rotating output of the actual GWK7010 reference already used at the ankle, rotated to a vertical yaw axis. It is not a cylinder standing in for the motor. The 40–50 N·m peak remains a user prediction.

`T05` is a rail-top crosshead envelope; `T06` is a half-pelvis block; `T07` is an unselected tilted pitch-motor envelope. These establish occupied space only. Their apparent proximity does not define bearings, bolts, a serial hip mechanism or a structural connection. They are excluded from mass/strength interpretation and rigidly follow the thigh only for layout inspection; no hip DOFs are claimed.

## Files and validation

Working directory: `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v10`.

- Native Fusion: `deliverables\Leg_layout_1600mm_v10.f3d`.
- STEP geometry: `deliverables\Leg_layout_1600mm_v10.step`.
- Printed mount/cap STEP files: `deliverables\upper_leg_parts`.
- Input preservation: `Input_live_v9_preserved.f3d` and `live_inventory.json`.
- Parameters: `layout_parameters.json`; fit and unchanged-component audit: `layout_validation.json`.
- Native knee motion: `knee_motion_validation.json` and `knee_motion_summary.json`.
- Native archive check: `archive_reopen_verification.json`.

Validation passed: 63 input components outside the two thigh rails and DJI motor retained their body counts, volumes and positions. Forty-seven potentially overlapping new interface pairs produced no solid collisions; the Ø28 × 5 mm encoder reservation is clear. Thirteen native knee poses from0° to120° in10° increments produced no detected collisions or calculation errors. The native archive reopened with75 components,72 valid joints and no feature warnings; the new components followed the native knee joint correctly. Finite samples do not establish full continuous-motion clearance, fatigue life or impact strength. The earlier 8 mm knee shaft strength concern remains open. No new FEA, dynamic simulation or physical load test is represented by this revision.

The price-free lower-leg BOM remains [BOM.csv](BOM.csv). New upper-leg items and reference-only parts are listed in [UPPER_LEG_BOM.csv](UPPER_LEG_BOM.csv). Future calculations and unresolved decisions are tracked in [FUTURE_WORK.md](FUTURE_WORK.md).
