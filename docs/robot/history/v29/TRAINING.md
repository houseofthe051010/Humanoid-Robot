# Current physical v29 locomotion — October 1, 2026

## Current reward repair — October 1, 2026

The active chain is `runs/locomotion_20261001_r6_measured_steps`. It fixes the
observed stationary walking incentive and starts from r4's verified standing
actor, with a fresh critic/optimizer for the changed reward. It revalidates
standing, then trains 0.15/0.35/0.65/1.0 m/s walking and 1.5/2.0/2.5 m/s running.
Actual forward progress, unloaded swing and ordered forward lift/land events
replace planted-foot gait credit. Existing gate thresholds remain; all prior
commands must pass nominal and pushed retention tests.

28 reward/reference/normalization/capacity tests and the 14 gate/three logging tests passed. Replaying
the saved bobbing rollout removed 96.43% of its positive locomotion credit.
This does not establish learned walking. R5 completed physics/PPO/reload execution checks
and capacity benchmarks with identical frozen training code. R6 reuses this
recorded evidence and revalidates the standing policy. R5's 8192 benchmark
dipped to 243 MiB free; R6 correctly selects 6144 with the 300 MiB reserve.
Unused command/phase input scales inherited from standing are repaired in a
checkpoint copy; all physical-input statistics and network weights remain.
All 256 CPU standing-input trials produced exactly identical outputs.
The run requests 8192
environments, preserves the 300 MiB reserve and fallback, uses 25-update blocks
and a 12-hour ceiling. Read `ACTIVE_RUN.json` and the live state for progress.
Details/evidence: [reward repair](TRAINING_REWARD_REPAIR_20261001.md).

The following earlier restart entries are historical. All changes are local;
no Git commit/push or external logger.

## Historical r4 restart: user requested 8,192 environments

The active run is `runs/locomotion_20261001_r4_8192`, starting at **8,192
environments** as requested. It resumed from r3's latest `model_50.pt`, with
verified provenance metadata restored; actor/critic tensors are unchanged and
the original periodic save is preserved. The r3 process tree was stopped only
after that checkpoint was recovered. Its evidence and superseded state remain.

Current training blocks are **25 PPO updates**. Shorter worker lifetimes reduce
the accumulated memory growth observed in the previous sustained 8,192 run
and check behavior more frequently. The 300 MiB guard, memory fallback,
hardware limits and independent stand/walk/run/retention gates remain active.
Neither switching the environment count nor recovering a save qualifies
standing. The current restart has a 16-hour ceiling. Use `ACTIVE_RUN.json` and
its live state for progress. Earlier count/block settings below are history.

The current 23-axis robot has started a new free-base Isaac Lab stand/walk/run
chain. Standing PPO updates were observed advancing at **8,192 environments**.
No learned standing or locomotion stage is claimed passed at this handoff.

The authoritative entry point is
`E:/Aditya/robot_sim/physical_v29/training/README.md`. Read
`training/ACTIVE_RUN.json` and its indicated live `state.json` for progress;
this dated report is not a live status display. Active run at handoff:
`training/runs/locomotion_20261001_r2`.

## October 1 restart after the status check

The r2 chain stopped after a Windows reader temporarily blocked renaming
`progress.tmp` onto `progress.json`. It had completed a 150-update training
block, failed the independent nominal standing gate, and then advanced 58
updates into the next block. This is a logging failure, not a policy promotion.

The status writer now retries transient sharing violations for up to five
seconds. Three tests passed, including a real held Windows read handle and a
permanent-lock case that preserves the old file and reports failure. The
supervisor uses the same writer; the helper is included in each frozen source
snapshot. No dynamics, rewards, actuator limits or gates were changed.

The latest periodic `model_50.pt` was recovered from the interrupted block.
Its missing provenance metadata was restored using that worker's run config
and matching source/asset hashes. Actor/critic tensors were checked unchanged;
the original checkpoint remains untouched. No standing qualification was added.

The r3 chain resumes at **4,096 environments**, the count that completed the
previous sustained block. It uses **100-update blocks**, a **300 MiB reserve**
and a **16-hour ceiling**. The same stand/walk/run stages and independent
nominal/push/retention gates apply. Read `ACTIVE_RUN.json` and the indicated
live state for actual progress; this note is a dated restart record.

All files remain local. No Git commit/push or external experiment logger.

## Model and weights

The source is the independently reopened wrist-corrected v29 F3D. Its 23 body
axes and saved CAD frames are retained. Current hardware assumptions include
95% added-transmission efficiency, 7 N·m/45 RPM elbows, 120 RPM shoulder pitch,
and pose-dependent shared motor-space ankle/waist constraints. Fingers and
wrists are static. No stereo camera is simulated.

[Mass estimate](MASS_ESTIMATE.md) and [part basis CSV](MASS_BASIS.csv) record
**34.46 kg including the battery**, or **33.98 kg** using AmazingHand's
published 400 g complete-hand value. Training retains the conservative estimate.
Each leg is about 8.7 kg and each arm with a hand is 2.3–2.6 kg. These are
component estimates with provisional gearset, print, hardware and electronics
allowances, not weighed assemblies. Bounding-box part inertias approximate the
native shapes. The older 38 kg model and the 24 kg movement fixture are separate.

## Method, gates and evidence

Primary public Unitree RL Lab, Humanoid-Gym, AMP, Cyclotron/Asimov and
BeyondMimic implementations/papers were reviewed together with old journal
GIFs, source videos, rewards and checkpoint evaluations. Findings and source
hashes are in `training/RESEARCH.md` and `training/research/sources.json`.
Earlier locomotion achieved forward speed but had slipping/stiff-gait
limitations; recovery rewards repeatedly rose without a strict standing pass.
Old 22-axis policy weights are incompatible with current v29.

The new policy uses CAD-IK gait references with residual PPO, four-frame
proprioceptive actor history, a privileged critic and dynamics variation. It
is not AMP or a proven human-motion controller. Train stand, then
0.35/0.65/1.0 m/s walk, then 1.5/2.0/2.5 m/s run. Separate nominal and pushed
20-second evaluations cover all earlier commands. Failure continues training;
earlier-skill regression rolls back. Promotion uses raw physics gates for
survival, posture, tracking, slip, loaded feet, support, bilateral steps,
cadence, clearance and running flight. Resets never erase failed trials.

Four-second contact preflight passed at 337.45 N support versus 338.09 N
expected. Shared differential tests and actual PPO/checkpoint-load smoke tests
passed their execution checks. The smoke checkpoint did **not** pass learned
standing. Physics tests do not certify balance, gait or full casing contact.

Benchmarks at 4,096/6,144/8,192 environments passed. 8,192 achieved about
10,019 environment steps/s, with 1,368 MiB minimum sampled free VRAM. The
unattended chain preserves a **300 MiB reserve** and falls back to 6,144 then
4,096 on memory failure. Its ceiling is 18 hours; an unpassed stage stays
unpassed. Source snapshots, checkpoints, raw gate telemetry, stdout/stderr,
live state and GPU CSV are saved in the run.

The first attempt's benchmarks are retained. Its evaluation checkpoint save
failed because RSL-RL 5's logger writer was uninitialized; the fix was tested
before the replacement run. A `.pt` file alone is not completion evidence.

The sustained 8,192 block reached the 300 MiB guard at update 42, saved a
memory checkpoint and resumed from it at 6,144. Advancing resumed updates were
observed with over 2 GiB free. This verifies the fallback after the short
benchmarks. Fourteen CPU-only gate tests passed, including rejection of
fall/rise, sliding, one-leg, support, bad-torso and invalid-pose exploits.
The robot-training skill passed its quick validator under Isaac Python.

## Remaining qualification

The contact asset uses simplified envelopes, with self-collision enabled.
It underapproximates actual housings/casing seams. Real masses, loaded motor
curves, thermal duty, reflected gear inertia, controller current and battery
sag still need measurement. Natural gait needs later visual review. No get-up,
backflip, payload or hardware-readiness claim follows from this chain.

All changes and logs remain local. No Git commit, push or external logger.
