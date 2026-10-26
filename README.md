# Humanoid Robot

I am building a human-sized humanoid robot, including its mechanical design, motor control and simulation.

## Current physical prototype — v29

The physical CAD is **1.6002 m tall**, with 23 body axes, a three-axis waist, rearward metal spine, battery/electronics packaging, supported arms, microservo hand references and a stereo-camera head. V29 lengthens thighs 30 mm, shortens the torso 20 mm, uses 275/250 mm arms and replaces generic elbows with double-shaft servos. The complete native archive independently reopens, and all 23 body joints passed an Isaac Lab movement test. Hardware limits, actual masses/inertias, contact dynamics and manufacture remain pending.

The detailed build documents and screenshots are retained locally under `docs/`, which is excluded from the online repository.

| Start here | Contents |
|---|---|
| [Forge journal](JOURNAL.md) | Repo journal imported by Forge; Main entries only |
| [CAD locations](CAD/README.md) | Saved native source and local artifact locations |
| [Firmware](firmware/) | Controller firmware and host utilities |

`Learning/HumanoidTraining` indexes the separate local Isaac pipeline. Firmware and host utilities are in [firmware](firmware/), with [Schematics](Schematics/README.md) and [custom gearboxes](CAD/Actuators/README.md).

The local `docs/archive/LOWER_LEG_GRANT.md` and root [bom.csv](bom.csv) retain the earlier lower-leg $761.45 scope; they are not a whole-humanoid budget. The local `docs/robot/history/v26/BUILD_REPORT.md` preserves the v26 mechanism checkpoint.

Documentation updated 2026-09-30. Local only; no Git commit, GitHub push or publication.
