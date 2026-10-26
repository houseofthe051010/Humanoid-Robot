# Physical-v29 training alongside CAD v30

Current active pointer: `E:/Aditya/robot_sim/physical_v29/training/ACTIVE_RUN.json`. R10 is the local measured-step stand/walk/run continuation; standing has a passed prior, walking is still unqualified. Keep live state/gate evidence separate from dated notes.

The chain uses checkpoint blocks with a 25-update minimum and measured timing sufficient for the three-minute ramp window, independent nominal/push and prior-command retention gates, an 18-hour ceiling, and a 300MiB VRAM guard. It raises environments one tier after three continuous minutes of enough live training headroom, up to 8192; startup/evaluation memory cannot qualify. Memory fallback remains automatic.

- [Automatic capacity and terminal monitor](TRAINING_AUTOMATIC_VRAM_20261001.md)
- [Reward repair and normalizer migration](TRAINING_REWARD_REPAIR_20261001.md)
- [Provisional frozen-v29 mass](MASS_ESTIMATE.md)
- [Actuator/linkage assumptions](ACTUATOR_CALCULATIONS.md)
- [Research and source snapshots](E:/Aditya/robot_sim/physical_v29/training/RESEARCH.md)
- [Prior training notes](history/v29/TRAINING.md)

CAD v30 is not silently inserted into an active policy. No camera is instantiated. This is reference-guided residual PPO with CAD IK gait guidance, not a proven AMP/human-motion/commercial policy. Videos/rewards alone cannot promote a stage. Current runtime tests prove execution and capacity logic; they do not establish learned walking, get-up or backflips.

All changes, checkpoints, evidence and documentation are local. No Git commit/push or cloud experiment logger.
