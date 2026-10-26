# Physical v29 Isaac Lab handoff

Package: `E:/Aditya/robot_sim/physical_v29`. This is the current 1.6002 m / 23-axis physical robot export, separate from the older 1.524 m / 22-axis training asset.

## What passed

`validation/joint_validation.json` records all 23 body joints passing. The test checks measured command tracking, non-commanded motion, all 24 link poses against frame-derived FK and return to the saved neutral pose. Commands use up to 12° in each legal direction, or 65% of the available range when smaller. Elbow flexion is negative; knee flexion is positive/backward. Hands and wrists stay static.

The final test was rerun after replacing export ranges with values read from the independently reopened native archive. Saved ankle-mechanism limits showed small differences from construction-time values; diagnostics retain both rather than relaxing an equality comparator.

## Exact command

```powershell
& 'E:\Aditya
obot_sim\env_isaaclab\Scripts\python.exe' 'E:\Aditya
obot_sim\physical_v29	est_joints.py' --headless --device cpu --force_convert
```

Runtime used: Isaac Lab 0.54.4, Isaac Sim 5.1.0.0, CPU physics. The test writes the report and stdout before shutdown. On this machine toolkit cleanup can hang after all tests finish; owned test processes were stopped only after the completed passing report, with cleanup evidence preserved. Do not treat a running shutdown process as ongoing test work.

## Fixture versus hardware

The root is fixed, gravity disabled and no ground/contact dynamics are tested. Positive 1 kg/link proxy masses and box-derived inertias permit movement testing. Test drives use 800 stiffness / 40 damping, 1000 N·m test effort and 10 rad/s test velocity. These are fixture values, **not robot mass, rated actuator limits or a torque recommendation**. Collision boxes are provisional; current conversion/contact behavior is not contact-qualified.

All 23 entries in `assets/actuator_limits_pending.json` have null effort/velocity/continuous torque fields. Configure those from the real hardware after this handoff. No walking, falls, load/impact test or PPO training was started. Actual mass/inertia, useful collision shapes, torque-speed/thermal curves, differential motor-output mapping and hardware control are further steps.

URDF has 24 links / 23 revolutes / 140 colored visual meshes. CAD front −Y maps to Isaac +X. Six-degree resting shoulder abduction is baked into geometry, so q=0 is the saved pose. Actual tilted physical hip axes are retained. Native ankle/waist closed mechanisms stay in the F3D; the URDF uses anatomical output joints and attaches motor/rod visuals to mounting links. It does not simulate those passive closures or assign a fixed differential ratio.

## Files

- `assets/humanoid_physical_v29.urdf`: current tree, meshes and geometric ranges.
- `assets/meshes/`: all 140 visual meshes; keep beside URDF.
- `assets/usd/humanoid_physical_v29.usd`: Isaac asset entry point; keep the full `configuration/` directory alongside it.
- `assets/export_metadata.json`: measured CAD frames, coordinate map, source hash, proxy assumptions and passive-mechanism scope.
- `assets/actuator_limits_pending.json`: hardware settings awaiting user input.
- `test_joints.py`: reproducible fixture; `--force_convert` updates USD from URDF.
- `validation/joint_validation.json` and `validation/validation_stdout.log`: final measured results.

See [Evidence](EVIDENCE.md) and [Exports](EXPORTS.md) for hash-bound native validation. Re-run the appropriate import/joint check if axes, origins or link ownership change; dynamics/contact tests become necessary when real masses and actuator limits are installed.
