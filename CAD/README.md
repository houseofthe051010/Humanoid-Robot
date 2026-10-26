# CAD locations

## Current physical robot — v29

[Build report](../docs/robot/BUILD_REPORT.md) · [Casing design](../docs/robot/CASING_DESIGN.md) · [BOM](../docs/robot/BOM.md) · [Evidence](../docs/robot/EVIDENCE.md).

Working full Fusion document **Humanoid_complete_v29_revised**, complete/unmodified saved version 1, lineage `urn:adsk.wipprod:dm.lineage:WTKBF_3ORCqcrKBaU4opCw`. Construction/checks: `E:/Aditya/robot_sim/outputs/shin_cad_20260912/v29`. Height1600.2 mm; +30 mm thighs, −20 mm torso, 275/250 mm arms, double-shaft servo elbows and full-turn hip-output waist relief. The current clean tree has42 groups/47 native constraints/23 body axes. Manufacturing, full combined clearance and strength remain separate qualifications.

Current complete portable native file: [Humanoid_complete_v29_revised.f3d](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v29/deliverables/Humanoid_complete_v29_revised.f3d). Archive CRC and independent native reopen both pass; all1545 visible shapes, saved frames/axes/grounds/neutral and no external referenced occurrence are verified. Matching STEP is geometry only and omits mesh hands. The [export index](../docs/robot/EXPORTS.md) records exact qualification. V28 and earlier packages remain preserved history.

## Preserved mechanics and source designs

The [v26 mechanical checkpoint](../docs/robot/history/v26/BUILD_REPORT.md), [v26 export index](../docs/robot/history/v26/EXPORTS.md) and saved Fusion source remain intact. Earlier verified v25 upper and waist compact archives remain under `E:/Aditya/robot_sim/outputs/shin_cad_20260912/v25/deliverables`.

[Dated physical revisions](../docs/lower_leg/README.md), [Assembly](Assembly/), [Actuators](Actuators/README.md) and the [earlier CAD index](../docs/archive/CAD_INDEX_BEFORE_V26.md) retain source context. Historical full standalone F3D imports have legacy external-reference limitations; the current full backup uses F3Z with its dependencies.

## Separate simulation assets

Current physical export: `E:/Aditya/robot_sim/physical_v29`, 24 links/23 body revolutes, full visual mesh/USD layers. All23 joint movement/FK/reset tests passed. Hardware effort/velocity values are still null; proxy masses/drives and non-contact fixture values do not qualify locomotion or payload. [Simulation handoff](../docs/robot/SIMULATION.md).

The [1.524 m / 22-DOF robot](Simulation/Humanoid5ft/README.md), [5ft7 validation](Simulation/Humanoid5ft7/FUSION_VALIDATION.md) and [Realistic20 quadruped](Simulation/Realistic20/README.md) are separate assets. Their masses, axes and policies do not automatically describe the physical CAD. [Training file locations](../Learning/HumanoidTraining/FILE_LOCATIONS.md).
