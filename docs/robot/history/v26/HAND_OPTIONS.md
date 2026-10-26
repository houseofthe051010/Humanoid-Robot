# Selected hand and alternatives

Revision v26 · 2026-09-30. [Current build](../../BUILD_REPORT.md) · [BOM](../../BOM.md).

## Selected CAD reference: Pollen Robotics AmazingHand

[AmazingHand](https://github.com/pollen-robotics/AmazingHand) matches the request for a mostly printed, microservo-driven hand with ordinary small purchased hardware and no extensive CNC. It has **three fingers plus a thumb**, four digits in total, and **eight Feetech SCS0009 servos per hand**. Each digit uses two servos and a parallel linkage to provide curl and side motion. It does not use rope tendons or motors in the forearm. The author describes about 400 g and a build cost below €200; that is the source design's claim, not a current delivered quote or a payload rating.

The official source geometry is assembled at full scale for both sides, using each side's own MJCF transforms and source assets rather than estimating finger positions or mirroring commercial servo geometry. Each assembly has 164 source part instances including eight servos; categories group printed structure, soft shells, servos and hardware. The measured right source pose occupies about **120.6×133.8×169.8 mm**; the left about **118.8×134.1×169.8 mm**. These are pose-dependent envelopes, not unfolded-finger dimensions. Finger joints are omitted from Fusion as requested; the hand is a static packaging reference attached to the moving forearm.

The original wrist uses **three M2.5 holes on a 42 mm pitch circle**. A robot-specific connector adapts this to the forearm's four-M3 pattern at **24×18 mm spacing**, with an 18 mm cable passage. Four top-down M3 screws pass through the forearm bridge's 3 mm-deep, radius 3.2 mm head counterbores into nominal OD4.6×4 mm insert pockets in the adapter. Assemble the original hand to the adapter first, then fasten the adapter from above. Actual screw lengths and printed insert fit remain to verify. The mechanism remains full-size; scaling the imported hand would also scale servo pockets, pivots and fasteners and would require a redesign.

The display/rest pose abducts each shoulder by **6°**. Its hand-envelope separation from the neutral hip envelope is at least **18.89 mm on the right and 19.08 mm on the left along X**. These are conservative axis-aligned envelope gaps at neutral hips, not measured surface-to-surface clearances over every motion. Unabducted construction zero and hip/arm motion still need collision-aware limits.

The imported palm planes are approximately vertical across the robot's width, with normals in the fore/aft direction. An inward-facing palm pose is not established by this import; its final orientation is a wrist/adapter design choice.

Source snapshot: commit `3e8241074df3436a3044ced4881e3bb2133aa725`. [Official CAD](https://github.com/pollen-robotics/AmazingHand/tree/main/cad), [assembly guide](https://github.com/pollen-robotics/AmazingHand/blob/main/docs/AmazingHand_Assembly.pdf), [original repository](https://github.com/pollen-robotics/AmazingHand). Local source, notices and STEP/STL files: `E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/references/AmazingHand`. Mechanical design is **CC BY 4.0**; code is Apache 2.0. Credit Pollen Robotics/AmazingHand and identify robot-specific wrist adaptation and placement when the robot is eventually open-sourced. This task has not published anything.

## What an MG90 conversion changes

Replacing an MG90 controller with a local position loop, current sensing and serial bus is feasible in principle. It does **not** make an MG90 mechanically equivalent to SCS0009: case dimensions, mounting ears, shaft/spline, horn position, gear strength, backlash, motor torque and heating can differ. The imported geometry is built for SCS0009. A replacement needs measured hardware and a modified servo mount/horn; a board swap alone is not a demonstrated fit.

Current limiting can help detect contact and cap motor effort. It is not a calibrated fingertip force sensor. Gear friction, mechanism angle, backlash and contact position change force for a given current. Supply current also differs from motor-armature current during PWM recirculation. For initial grasping, use position control with an experimentally chosen current ceiling; calibrate with a known external load or force sensor if accurate force control is needed.

The original SCS0009 already has a serial interface and reported load/position/temperature features. Compare its total delivered cost against the MG90, new boards, wiring and mechanical adaptation before committing to sixteen conversions. The official project links an [SG90 force-control experiment](https://github.com/joanbox24/AmazingHand-with-sg90-servo-force-control); that repository's Arduino/current-monitor example is not proof that all original CAD fits unmodified SG90 or MG90 hardware.

The arm's 1 kg priority and optional 2 kg target are **arm payload goals**, not demonstrated AmazingHand grip ratings. For a conditional friction-only hold with coefficient 0.5, a 1 kg object requires about 19.6 N total contact-normal force; 2 kg requires about 39.2 N before dynamic allowance. Enveloping the object against the palm changes this load path. Prototype one digit, measure temperatures and grip behavior, then select the final servo family and board.

## Alternatives retained for future comparison

| Design | Why it remains relevant | Reason not selected for this CAD pass |
|---|---|---|
| [TheTechTiger RoboticHand](https://github.com/TheTechTiger/RoboticHand) | Five SG90/MG90-type servos and fishing-line tendons; printed gesture-hand architecture | Published examples do not establish the requested payload or calibrated force control; a human-sized mounting/geometry pass would still be needed |
| [Yale OpenHand Model O](https://github.com/grablab/openhand-hardware) | Popular three-finger underactuated research gripper | Original actuation is not a direct MG90 microservo match |
| [LEAP Hand v2](https://v2.leaphand.com/) | Dexterous low-cost hand project with available control resources | Exact intended microservo/mechanical fit and CAD terms must be checked before replacing the now-imported AmazingHand |

The user's unnamed popular three-finger hand remains unidentified. AmazingHand was selected because its official CAD, microservo architecture, scale and accessible hardware meet the current constraints; its three fingers plus thumb are clearly stated rather than treated as a three-digit gripper.
