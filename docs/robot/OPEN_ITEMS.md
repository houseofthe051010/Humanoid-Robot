<!-- steadywin36_20261023 -->
## SteadyWin enclosure prototypes v36 — October 23, 2026

Current native source: **Humanoid_SteadyWin_enclosures_v36**, saved version 2. Nine separate mounted cases replace visible XDrives for six 6010 and three non-ankle 7010 motors. Original motors, four excluded ankles and all 83 joints remain. Published GDS68 envelopes are used because the downloaded official motor/cap CAD has no standalone PCB; exact 7010 configuration, board holes, encoder stack and thermal/electrical duty remain unverified. Separate flanges, radial screw mounts, split oval-rail clamps and removable vented lids are modeled. W07/local fixed supports and a 140 mm electronics bay are revised with originals retained hidden.

All 3,096 input solids are preserved; neutral solid clearance, full archive reopen and all 15 STEP roundtrips pass; actual motion finds two unresolved inward-arm/waist-case contacts. Continuous motion, material/mass, strength and manufacture remain unqualified. [CAD, images and evidence](E:/Aditya/robot_sim/outputs/shin_cad_20260912/steadywin36/REPORT.md). V35 below is historical. Training and the custom FOC PCB remain unchanged.

# V32 remaining work

Select and fit-test longer carrier screws, two lower plate retention straps per leg and two M3 hip collar seam screws per side. Check printed saddle/oval tolerance, clamp preload, panel vibration, continuous travel and strength. Broad thigh skins are unchanged. No measured mass or training asset migration is included.

# Decisions remaining after v31

Current CAD packaging, casing ownership, sampled interface motion and native archive checks pass. These open items concern actual hardware/manufacture and a future simulation migration.

1. Confirm exact custom hip reducer registers/output patterns; current adapters retain provisional existing interfaces. Qualify CNC alloy, web sections, bolt engagement, bearing fits and loaded torque.
2. Select structural waist polymer, infill, print orientation and inserts/reinforcement; verify case clamp preload and load paths at actual motor loads. Nominal wall and connected solids alone do not prove strength.
3. Select #40H chain length, tensioner, guards, hardened sprocket material and actual side-plate clearance. Review the retained small 8T drive sprocket's engagement/chordal behavior before manufacture.
4. Detail shoulder pod retention and panel seams/tool access. Verify all combined body/cable travel; current tests cover selected single-axis and combined hip interfaces.
5. Qualify exact motor variants, loaded torque-speed/thermal duty, RDS51160 dimensions/horns and the user's elbow operating assumptions. Finish internal/custom planetary/cycloidal transmissions.
6. Regenerate v31 mass/inertia/contact/URDF only as a separate reviewed migration. Training currently uses frozen v29 and its provisional 34.46kg estimate; new bracket/cover volume changes are not yet included.
7. Finish battery/BMS, regulators, wiring, host/FOC controls, cooling and electrical regeneration provisions. Electronics volume is reserved; selected boards/ports are not finalized.
8. Retain original AmazingHand mechanics unless an MG90 redesign is explicitly qualified. Current-sense boards do not establish mechanical equivalence. Confirm future palm orientation or powered wrists separately.

Questions for later: exact custom hip output register/PCD and CNC material; structural waist print material; actual #40H chain/tensioner choice; final shoulder-cover retention. No current user response is needed to inspect the delivered CAD or keep the training chain running.
