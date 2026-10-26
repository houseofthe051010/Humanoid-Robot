# Humanoid robot — current build

**CAD v30 · October 1, 2026 · local documentation only.**

The waist now fits the fixed hip-pitch cases with a closed bottom/rear and clear outputs. Broader measured aluminum carriers replace the weak hip pitch/roll and roll/yaw connections. The shoulders blend into the torso and have separate articulated covers. Knee sprockets now have actual ANSI #40 roller tooth arcs. A single **Casings** component controls exterior visibility while covers follow their physical links.

![Current native robot](evidence/v30/robot_v30_threequarter.png)

## Current CAD and completed checks

| Item | Current result |
|---|---|
| Source | Humanoid_complete_v30, saved version 2 |
| Height | 1600.2 mm, nominal 1600.2 mm / 5 ft 3 in |
| Retained proportions | +30 mm thighs, −20 mm torso; 275/250 mm upper-arm/forearm spans |
| Joints | Original 47 preserved; 18 cover-owner rigid constraints added; 23 body axes |
| Casing organization | 65 components under one toggle, 18 physical owners; two obsolete white hip caps hidden |
| Active C27/C28/C30 covers | 57 components; head/hand printed groups are additional |
| Motion clearance | 122 temporary-solid samples passed: hips, waist, shoulder pitch and upper-arm roll |
| Native cover motion | All 23 body axes tested on a disposable reopened copy; covers followed owners, live pose unchanged |
| Final native archive | CRC and independent Fusion reopen passed; 1566 visible shapes, all grounds/frames/ranges matched |

The rough detached user prototype is preserved, hidden under **User_concept_reference**, and retained unchanged in the input archive. Its measurements were not copied into the motor adapters. Original skeleton, drivetrain ratios, wrist alignment, battery/electronics, head/camera and hand mechanisms remain.

## New interfaces

The structural waist has two connected printed halves with 5.5 mm nominal cup walls, case locating bands, output apertures and four M4 seam joints. Four existing vertical yaw-mount positions remain. The pitch-to-roll carriers use a 12 mm pitch coupling, 8 mm roll cheeks and broad curved webs; the roll-to-yaw cradles use 10 mm cheeks and broad webs/platforms. Reinforced fixed roll endcaps and sixteen M4 bolt/nut references complete the modeled carrier attachment.

The 8T/16T knee pair preserves its 2:1 ratio and 159.4 mm centers. The #40 tooth profile uses 12.7 mm pitch, 7.9248 mm rollers and 7.21 mm face width; actual #40H chain width, length/tensioning, material and low-tooth-count behavior still need detailing. [Sprocket evidence](evidence/v30/chain_sprockets30.json).

Clearance and thicker sections do not certify strength. Custom reducer fit, printed material/infill, bolt engagement, bearings, cooling and full combined travel remain prototype qualifications. [Open decisions](OPEN_ITEMS.md).

## Simulation and live training

Training remains on the frozen **physical v29** asset, with its provisional **34.46 kg** mass basis and September 30 actuator assumptions. V30 geometry is not silently inserted into a running policy. V30 mass/inertias/contact export are pending. [Actuator calculations](ACTUATOR_CALCULATIONS.md) · [Mass basis](MASS_ESTIMATE.md).

The r10 supervisor resumes the corrected measured-step chain. Standing has passed prior gates; walking has not yet passed. It increases training environments one tier after three minutes of measured VRAM headroom, up to 8192, with the 300 MiB reserve and automatic fallback. Read `physical_v29/training/ACTIVE_RUN.json` and live state for current counts/progress. [Training and monitoring](TRAINING.md).

## Files

| Reference | Contents |
|---|---|
| [Native CAD / downloads](EXPORTS.md) | Verified v30 F3D, previews, profile DXFs, archived v29 simulation |
| [BOM](BOM.md) / [CSV](BOM.csv) | Parts, new brackets/covers/fastener references and pending purchases |
| [Casings](CASING_DESIGN.md) / [inventory](CASING_INVENTORY.csv) | Toggle, physical ownership, colors and print limitations |
| [Mechanical architecture](MECHANICAL_OVERVIEW.md) | Interfaces, proportions and retained mechanisms |
| [Evidence](EVIDENCE.md) | Exact native, clearance, tooth-profile and training records |
| [Open items](OPEN_ITEMS.md) | Hardware, manufacturing and future simulation decisions |
| [V29 history](history/v29/BUILD_REPORT.md) | Prior release and its separate Isaac movement qualification |

Handoff: `C:/Users/rshan/Downloads/Humanoid_v30_CAD`. No Git commit, push, publication or external experiment logging.
