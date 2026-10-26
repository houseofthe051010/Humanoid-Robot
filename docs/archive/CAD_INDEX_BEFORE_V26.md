# Earlier CAD landing page

Historical text preserved on 2026-09-30. [Current whole-robot report](../robot/BUILD_REPORT.md) supersedes its current-state statements.

# CAD

## Current physical legs and waist — v15

See [v15 design record](../lower_leg/UPPER_LEG_V15.md) and [BOM](../lower_leg/BOM_V15.csv). Native: `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v15\deliverables\Legs_and_waist_v15.f3d`.


## Historical physical leg — v14

See [v14 adapter correction](../lower_leg/UPPER_LEG_V14.md) and [BOM](../lower_leg/BOM_V14.csv). Native CAD: `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v14\deliverables\Bilateral_legs_v14.f3d`.

## Historical physical leg prototype — v13

The current physical prototype uses a106ID/110OD aluminum motor tube, approximate8T/16T sprockets and revised knee interfaces. See [v13 record](../lower_leg/UPPER_LEG_V13.md) and [BOM](../lower_leg/BOM_V13.csv). Local native/STEP files: `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v13\deliverables`. Older simulation assets below are separate.

Source CAD and STEP files for the robot are here. The actuator gearbox designs are in [`Actuators/`](../../CAD/Actuators), and the shin, ankle, and feet assembly is in [`Assembly/`](../../CAD/Assembly).

## Historical physical leg prototype — v12

The 1600.2 mm humanoid physical prototype now has paired legs, circular knee-motor/gearbox housing and hip-attachment concepts. See [V12 build record](../lower_leg/UPPER_LEG_V12.md) and [price-free BOM](../lower_leg/BOM_V12.csv). Native CAD and STEP outputs are stored locally in `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v12\deliverables`, separately from the older simulation assets below.

## Simulation models

The realistic 20:1 quadruped used for Isaac Lab training is in [`Simulation/Realistic20/`](../../CAD/Simulation/Realistic20/README.md). That folder contains Fusion-native assemblies, STEP interchange files, URDF and dynamics data for both the 22.8 kg standard robot and the 27.8 kg version carrying a 5 kg payload.

The 1.524 m, 22-DOF humanoid ragdoll is in [`Simulation/Humanoid5ft/`](../../CAD/Simulation/Humanoid5ft/README.md). It is a Fusion-native articulated starting point with 12 leg DOF, a two-axis waist, minimal arms and a two-axis head; actuator mechanisms and their mass are intentionally reserved for the next design stage.

The validated 1.7018 m dry humanoid assembly is in [`Simulation/Humanoid5ft7/`](../../CAD/Simulation/Humanoid5ft7/FUSION_VALIDATION.md). Its 34 native Fusion joints include 22 intended simulation DOF and the passive 1.15:1 ankle-differential linkage; motors and electronics remain intentionally excluded pending selection.
