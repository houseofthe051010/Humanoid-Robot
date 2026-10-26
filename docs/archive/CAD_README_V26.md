# CAD locations

## Current physical robot — v26

[Current build report](../robot/BUILD_REPORT.md) · [Whole-robot BOM](../robot/BOM.md) · [Hand source](../robot/HAND_OPTIONS.md).

Working full Fusion document: **Humanoid_complete_v26**, completed saved version 4. Local construction, checks and exports: `E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26`. The [evidence index](../robot/EVIDENCE.md) separates saved-source, module-reopen, package-integrity and concept-part file checks. The v26 pass lowers and splits the head, integrates full-size microservo hands and wrists, applies material-role colors and validates the 23 body-axis hierarchy. Manufacturing and full swept-motion limits remain outside this completed CAD pass.

Full assembly reference-package backup: [Humanoid_complete_v26_full_20260930.f3z](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/Humanoid_complete_v26_full_20260930.f3z). Package integrity and included dependency resolution pass; native standalone package reimport was not performed. [Local export index](../robot/EXPORTS.md) lists the individual concept parts and their qualifications.

Preserved verified v25 upper archive: `E:/Aditya/robot_sim/outputs/shin_cad_20260912/v25/deliverables/Torso_arms_vision_v25.f3d`. Preserved waist/spine: `E:/Aditya/robot_sim/outputs/shin_cad_20260912/v25/deliverables/Waist_rearward_spine_v25.f3d`. Earlier full local archives have legacy external-reference metadata; use saved full Fusion sources or independently verified compact archives.

## Physical history and source designs

[Dated physical revisions](../lower_leg/README.md) retain the legs/hips/waist/torso history. [Assembly](../../CAD/Assembly) contains earlier prototype sources; [Actuators](../../CAD/Actuators/README.md) contains custom planetary/cycloidal experiments. The [previous CAD landing page](CAD_INDEX_BEFORE_V26.md) is preserved for source context.

## Separate simulation assets

The [1.524 m, 22-DOF humanoid](../../CAD/Simulation/Humanoid5ft/README.md), [5ft7 Fusion validation record](../../CAD/Simulation/Humanoid5ft7/FUSION_VALIDATION.md) and [Realistic20 quadruped](../../CAD/Simulation/Realistic20/README.md) are separate historical/simulation designs. Their masses, joint conventions and training policies do not automatically apply to the current physical CAD. Exact pipeline and checkpoint locations remain in [FILE_LOCATIONS](../../Learning/HumanoidTraining/FILE_LOCATIONS.md).
