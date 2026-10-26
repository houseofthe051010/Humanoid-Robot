# Humanoid robot — current physical build

**v29 · CAD September 30 / training October 1, 2026 · local documentation only.**

The thighs are 30 mm longer, the torso is 20 mm shorter, and the supported arms now use **275 mm upper arms / 250 mm forearms**. Double-shaft servo elbows replace the generic elbow package. The structural waist holders have continuous relief around both hip motor outputs. The complete native CAD archive independently reopens, and the exported **23-axis URDF/USD passed the Isaac Lab movement test**.

![Current native robot](evidence/v29/revised_threequarter.png)

## Current dimensions and packaging

| Feature | Current geometry |
|---|---|
| Standing height | **1600.2 mm / 1.6002 m / 5 ft 3 in**, from original sole to head |
| Thigh change | +30 mm in four straight oval rails below the raised knee motor; nominal rail length 264.8 mm |
| Lower leg | Existing knee output, shin, ankle mechanism, sole and shoes retained |
| Torso change | −20 mm relative to the raised pelvis; spine top shortened accordingly |
| Shoulder height above sole / roll-center spacing | 1350.2 mm / 394 mm |
| Upper-arm / forearm pivot lengths | 275 / 250 mm, measured on both sides |
| Battery envelope | 140×85×160 mm; unchanged shape, moved with upper assembly |
| Electronics reservation | 150×86×93 mm overall; existing host/converter enclosure retained |
| Elbow actuator | User-selected RDS51160 24 V double-shaft servo; **RDS51150 CAD proxy** |
| Proxy servo case | 65×30×48 mm; exact 160 kg variant and horn/spline fit unverified |
| Waist output relief | Conservative full-turn envelopes, 3 mm radial/axial allowance, flange relief |

The pelvis/hip and knee motor region moves up 30 mm while the knee output and lower leg stay in place. Shoulders and head move up 10 mm after shortening the torso. This changes the knee chain center distance: chain length/tensioning remains to detail. No internal gear ratio was changed.

## Native assembly and elbows

Saved Fusion source **Humanoid_complete_v29_revised**, version 2, wrist alignment corrected, lineage `urn:adsk.wipprod:dm.lineage:WTKBF_3ORCqcrKBaU4opCw`. The live input was preserved first as **Humanoid_complete_v29**, version 1. V28 and earlier releases remain history.

The clean revised assembly has **42 rigid-link/mechanism groups, 372 occurrences, 1537 visible BRep shapes and eight hand meshes**. All child parts are grounded to their appropriate rigid parent. **47 native constraints** include 41 revolutes and six ball closures; **23 revolutes are anatomical body axes**. Native ankle/waist motor and rod closures are retained. Supplier-reference metadata is localized; the reopened full archive has no external referenced occurrences.

Each elbow servo case fixes to the upper-arm cradle, with its transverse shaft on the physical elbow axis. Both outputs carry the forearm U fork. The servo replaces the old generic elbow motor, separate 25 mm shaft, four elbow 6005 bearings and floating cosmetic cheeks. The provisional horns have six M3 positions on 36 mm PCD; actual 160 kg hardware must determine their final spline/bore fit. Existing wrist connectors and rigid hand references remain.

## Completed checks

| Check | Result and scope |
|---|---|
| Dimensions | PASS: both arm spans, rail extension and 1600.2 mm height |
| Waist clearance | PASS: both holders are connected solids, with zero intersections against conservative full-turn hip-output/flange envelopes |
| New elbow packaging | PASS: 20 transient-copy samples, both sides 0° to −135° in 15° steps, new output fork/horns against fixed servo case |
| Full F3D integrity and native reopen | PASS: CRC-valid archive, all 1545 visible shapes matched exported mesh-source bounds within 2.84e-14 mm; joint frames, axes, grounds and neutral pose checked |
| URDF/USD import | PASS: 24 links, 23 body revolutes, 140 colored visual meshes; hands/wrists static |
| Original Isaac Lab joint test | PASS: every body joint tracked legal sample commands, other axes stayed near neutral, all 24 link poses matched frame-derived FK, then returned to neutral |
| Current 95% actuator test | PASS: all 23 axes tracked/reset, FK matched, no invalid transmission samples;7 N·m/45 RPM elbow and 120 RPM shoulder pitch. Fixed base, no gravity/contacts, proxy inertia. |
| Wrist alignment correction | PASS: both hand assemblies aligned; six adapter hole axes match, 1537 solid parts and 47 joints unchanged; corrected full F3D independently reopens. |

The Isaac test is a **fixed-base, gravity-free movement fixture**, using proxy masses/inertias and test drives, without contact dynamics. It verifies the exported joint tree, directions and movement; it does not certify walking, strength, payload or collision-free full travel. Maximum tracking error was **0.0069°**; maximum link-position difference from FK was **0.0188 mm**.

After native saving/reopening, 12 ankle-mechanism angular ranges differed slightly from construction-time values, at most 0.04720°. The release URDF uses the **actual reopened native range values**, and was retested after that update. Original diagnostics remain preserved; exact preservation of the earlier numeric ranges is not claimed.

## Where work stops

**September 30 actuator assumptions are configured.** [Current calculations](ACTUATOR_CALCULATIONS.md) record the selected torque/RPM inputs, source constants and saved-CAD ankle/waist Jacobians. Use `physical_v29/assets/actuator_limits.json` with `hardware_actuators.make_actuators()`; the null pending file is historical. Current profile uses 95% added-transmission efficiency, 7 N·m sustained elbow at 45 RPM and 120 RPM shoulder pitch. A provisional component estimate is 34.46 kg including the battery, or 33.98 kg with the published complete-hand mass. A separate free-base contact asset passed physics preflight, and the 8,192-environment stand/walk/run chain started October 1. Learned standing and gait gates remain pending at this handoff. Actual masses, measured thermal/loaded duty and full native contact remain unqualified. The older 22-axis model stays separate. See [weight details](MASS_ESTIMATE.md) and [current training](TRAINING.md).

Printed structural capacity, actual material densities/inertias, collision geometry, full combined travel, chain selection, wiring and exact servo fit remain prototype work. The active C27/C28 exterior contains **53 parts: 51 cosmetic pieces and two structural waist halves**. The left hip-yaw collar was absent from active source geometry; the inventory records one active right collar rather than assuming a pair.

Current user actuator configuration: [Current actuator calculations](ACTUATOR_CALCULATIONS.md).

## Files and report map

| Reference | Contents |
|---|---|
| [Native CAD / export index](EXPORTS.md) | Full F3D, geometry-only STEP, URDF/USD package and qualification |
| [BOM](BOM.md) / [CSV](BOM.csv) | Current actuator/bearing/structure/casing/electronics quantities and pending hardware |
| [Mechanical architecture](MECHANICAL_OVERVIEW.md) | Link ownership and interfaces |
| [Casings](CASING_DESIGN.md) / [inventory](CASING_INVENTORY.csv) | Current shapes, ownership, colors and qualification |
| [Simulation handoff](SIMULATION.md) | Current actuator configuration and original movement-fixture evidence |
| [Mass estimate](MASS_ESTIMATE.md) / [part basis](MASS_BASIS.csv) | Provisional total, limb mass, materials and allowances |
| [Current training](TRAINING.md) | Physical v29 stand/walk/run chain, primary research and live-status pointers |
| [Evidence](EVIDENCE.md) | Completed native/Isaac tests, hashes and source |
| [Open items](OPEN_ITEMS.md) | Hardware and detailing decisions for later |
| [Hand design](HAND_OPTIONS.md) / [torque notes](TORQUE_NOTES.md) | Source/licensing and earlier planning evidence |
| [v28 history](history/v28/BUILD_REPORT.md) | Previous saved design; earlier checks are historical |

Handoff: [Humanoid_v29_CAD](C:/Users/rshan/Downloads/Humanoid_v29_CAD). Source/evidence: `E:/Aditya/robot_sim/outputs/shin_cad_20260912/v29`. Simulation: `E:/Aditya/robot_sim/physical_v29`.

Documentation, BOM and repository changes are **local only**. No Git commit, push or GitHub publication was performed.
