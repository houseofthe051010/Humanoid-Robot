# Physical-v29 corrected Unitree adaptation — October 2, 2026

<!-- unitree-nominal-20261002 -->

The current replacement is **r22_unitree_nominal**, reward
`unitree_g1_lifetime_v2`. Read `E:/Aditya/robot_sim/physical_v29/training/ACTIVE_RUN.json`,
its live state/progress, verified worker/supervisor processes and independent
gates for current status. R20 was drained and preserved after 68 full updates;
R21 was preserved after validation, before full standing training. Neither is
active or qualified. R20's replay first breached the waist differential
motor-angle limit at 0.08 seconds, then fell backward without alternating steps.
Its original aggregate reward rates were all negative, allowing early episodes
to avoid future costs.

R22 retains the pinned Unitree RL Lab G1 core bodies and weights, adding the
declared RL Gym nonnegative regular aggregate followed by MJLab H2's -200
physical-termination weight (-4 per 20 ms event). Timeouts are unpenalized.
Per-cause termination telemetry separates motor faults from ordinary falls.
This is an adapted public Unitree design, not unmodified complete G1/H2 or a
commercial pretrained policy. 5,593 core and 149 lifetime CPU checks passed.
Actual new physics/PPO/load/capacity checks are retained in R22's run directory.
Smoke, reward rankings and screenshots do not qualify learned walking.

The original adaptation's expanded reference aliased the nominal pose. A
randomized reset could change that shared origin and every other robot's
reference. The actual-source CPU regression reproduced 0.63665 rad drift after
512 resets; corrected private storage gives zero drift and leaves unreset rows
unchanged. This is a reproduction, not a measurement of old GPU drift. Every
real PPO update now logs/asserts zero nominal drift. Contract is
`physical_v29_history5_unitree_defaultoffset_v2`, still 400/415 actor/critic
dimensions. A fresh actor is used; no moving IK target or standing teacher.
Physical-v29 mass 34.46334 kg, CAD joint frames, motor limits, differential
geometry and collisions are unchanged. CAD v32 stays separate. Do not load
old history4/IK or another robot's policy tensors into this fresh actor.

The chain targets 8192, reserve 300 MiB, fallback, and a 180-second continuous
healthy-live-PPO ramp at checkpoint boundaries. Host RAM recycling preserves
actor/critic/Adam/LR; the allocation leak itself remains unresolved. Keep one
Isaac/CUDA worker only. No training stereo/render camera is instantiated.
Stages: stand; walk 0.35/0.65/1.0; run 1.5/2.0/2.5, with 0.15 retention. Promotion
requires independent current/prior nominal and pushed 20-second gates. The
running cadence/flight extension is declared, not commercial Unitree weights.
Every later learned candidate needs visual review before a human-gait claim.

Report: `E:/Aditya/robot_sim/physical_v29/training/UNITREE_NOMINAL_REPAIR_20261002.md`.
Source/weight comparison: `training/UNITREE_REWARD_PORT_20261002.md`.
Frame review: `training/diagnostics/unitree_port_20261002/frame-review.html`.
The review contains 280 scripted screenshots, 80 learned-r20 replay screenshots,
and 207 explicitly labeled CPU smoke reconstructions (567 frames across 15 cases), with synchronized angles,
contacts, failure causes and original H1/G1 rates; 47 official GIF frames were
inspected too. None of the failed candidates matches the reference gait.
Local-only documentation/source changes; no Git commit or push.

Dated handoff 2026-10-02T17:50:31.581981+00:00: verified live full
stand PPO at 8192 environments, with 17
saved full updates and current worker iteration 12. Free VRAM
1269 MiB; available host RAM 4419 MiB.
Frozen worker/environment/reward files match the tested workspace. This is
runtime evidence, not a behavioral qualification. Inspect fresh active status.
Current nominal-pose drift: 0.0 rad.
The first host-RAM recycle saved 17 full updates and resumed at 8192. Actual
continuation Adam counters advanced420 to440 after the next PPO update;
actor/contract/reward/asset provenance is retained in
`training/diagnostics/unitree_termination_20261002/optimizer_resume_r22.json`.

[Full repair report](TRAINING_UNITREE_NOMINAL_20261002.md).


## Historical record before the nominal-reference repair

# Physical-v29 Unitree G1 training — October 2, 2026

<!-- unitree-port-20261002 -->

The current replacement is **r20_unitree_g1**. Read
`E:/Aditya/robot_sim/physical_v29/training/ACTIVE_RUN.json`, its live `state.json`,
verified worker/supervisor command lines, fresh progress and independent gates.
R19 was drained and preserved without qualifying walking. R20 starts a fresh
five-frame, nominal-position-offset policy using pinned Unitree RL Lab G1
reward bodies/weights and PPO settings. Old CAD-IK moving action references,
discovery bonuses and the standing teacher are absent. H1 RL Lab, older RL Gym
H1/G1 and public MJLab H2 tasks were compared separately, not blended.

The reward version is `unitree_g1_port_v1`; action/observation contract is
`physical_v29_history5_unitree_defaultoffset_v1`. Actor/critic dimensions are
400/415. Original G1 walking phase parameters remain; requested running uses
an explicitly documented cadence/flight extension. Robot dimensions and
entity mappings are adapted; saved physical v29 mass, axes, actuator limits,
collisions and CAD are unchanged. CAD v32 remains a separate release.

5,589 CPU assertions, actual physics/PPO/load checks and fresh capacity
benchmarks passed. At 8192 the short benchmark measured 11,674 env steps/s and
1533 MiB minimum sampled free VRAM. 280 real scripted probe screenshots, all
47 official reference GIF frames, and 50 learned-smoke CPU reconstruction
frames were reviewed. The four-update candidate failed standing/walking;
scripted motions are not a learned gait. No walking/style success is claimed.

Target 8192, reserve 300 MiB, automatic fallback and 180-second healthy-live-PPO
ramp remain. RAM recycling preserves checkpoints/Adam/LR, but the underlying
allocation leak is unresolved. Stages: stand, walk 0.35/0.65/1.0, run
1.5/2.0/2.5 m/s; 0.15 remains a retention command. Promotion requires current
and prior nominal/pushed physical gates, never reward or smoke alone. No camera
is instantiated in training and no second Isaac/CUDA worker may overlap it.
Do not load old history-4/IK or another robot's pretrained tensors into R20.

Full report: [Unitree rewards, tests and visual review](TRAINING_UNITREE_PORT_20261002.md).
Authoritative evidence and live status are in the workspace training folder.
The dated report is not proof of process liveness or completion. Local only;
no Git commit/push. Old training documents are preserved in the workspace's
diagnostic documentation backup and existing repository history directories.
