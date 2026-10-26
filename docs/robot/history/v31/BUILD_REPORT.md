# Humanoid robot — current build

**CAD v31 · October 1, 2026 · local documentation only.**

V31 replaces the user-rejected v30 motor cups with an enlarged continuous pelvis enclosure. It covers both fixed hip-pitch cases and ends 0.9 mm behind their output faces, with closing rims around those openings. The underside is closed. Hip adapters have broad planar hoods, rounded contours and solid external roll faces. Straight side walls join each pair of ankle motor rings. Existing motor positions, shoulders, sprockets and Casings organization are retained.

![Native v31](evidence/v31/robot_v31_threequarter.png)

| Check | Result |
|---|---|
| Source | Humanoid_complete_v31, saved version 2 |
| Height | 1600.2 mm |
| Original placements | All 439 occurrence transforms unchanged; maximum error 0.0 |
| Joints | 65 original definitions/frames/ranges preserved; 23 body axes |
| Native movement | 23 single-axis tests and 8 paired hip pitch/roll tests on a disposable archive |
| Solid clearance | 183 discrete hip/waist samples passed, including combined pitch/roll |
| Native release | CRC and independent Fusion reopen passed |

The exact unsaved user input is preserved in `v31/Input_live_v30_user_edits_preserved.f3d`. Detached user sketches/prototypes remain hidden references. No motor spacing, joint zero or drivetrain ratio was changed.

The enclosure uses nominal 5 mm skins and a 5 mm closed underside. Output rims are 3 mm deep. Hip carriers retain 8 mm flanks and a 12 mm pitch coupling; the moving U cradles use 10 mm cheeks with 5 mm solid external caps over blind internal recesses. The carriers use larger rounded profiles and 1.5 mm outside edge fillets. Ankle side walls are 4.2 mm thick. These are prototype geometries: CNC setups, final tool radii, alloy, fasteners, custom reducers, print fit and structural loads remain unqualified.

Training remains on frozen **physical v29**, with its provisional 34.46 kg mass basis. The active supervisor targets up to 8192 environments, using 300 MiB reserve and 180 continuous seconds of training headroom before a ramp. New CAD volume is not silently introduced into the running policy. Walking has not been certified by these CAD checks.

[Native CAD and STEP parts](EXPORTS.md) · [BOM](BOM.md) · [Casings](CASING_DESIGN.md) · [Evidence](EVIDENCE.md) · [Open work](OPEN_ITEMS.md) · [Rejected v30 history](history/v30/STATUS.md).
