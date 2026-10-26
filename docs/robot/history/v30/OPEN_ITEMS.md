# Decisions remaining after v30

Current CAD packaging, casing ownership, sampled interface motion and native archive checks pass. These open items concern actual hardware/manufacture and a future simulation migration.

1. Confirm exact custom hip reducer registers/output patterns; current adapters retain provisional existing interfaces. Qualify CNC alloy, web sections, bolt engagement, bearing fits and loaded torque.
2. Select structural waist polymer, infill, print orientation and inserts/reinforcement; verify case clamp preload and load paths at actual motor loads. Nominal wall and connected solids alone do not prove strength.
3. Select #40H chain length, tensioner, guards, hardened sprocket material and actual side-plate clearance. Review the retained small 8T drive sprocket's engagement/chordal behavior before manufacture.
4. Detail shoulder pod retention and panel seams/tool access. Verify all combined body/cable travel; current tests cover selected single-axis interfaces.
5. Qualify exact motor variants, loaded torque-speed/thermal duty, RDS51160 dimensions/horns and the user's elbow operating assumptions. Finish internal/custom planetary/cycloidal transmissions.
6. Regenerate v30 mass/inertia/contact/URDF only as a separate reviewed migration. Training currently uses frozen v29 and its provisional 34.46kg estimate; new bracket/cover volume changes are not yet included.
7. Finish battery/BMS, regulators, wiring, host/FOC controls, cooling and electrical regeneration provisions. Electronics volume is reserved; selected boards/ports are not finalized.
8. Retain original AmazingHand mechanics unless an MG90 redesign is explicitly qualified. Current-sense boards do not establish mechanical equivalence. Confirm future palm orientation or powered wrists separately.

Questions for later: exact custom hip output register/PCD and CNC material; structural waist print material; actual #40H chain/tensioner choice; final shoulder-cover retention. No current user response is needed to inspect the delivered CAD or keep the training chain running.
