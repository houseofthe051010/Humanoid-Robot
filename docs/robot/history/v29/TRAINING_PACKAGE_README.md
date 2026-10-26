# Physical v29 locomotion training

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
Details/evidence: [reward repair](REWARD_REPAIR_20261001.md).

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

The October 1 chain is training the current **23-axis, 1.6002 m robot** in Isaac
Lab. It uses a free base, gravity, floor contact, self-collision and the saved
CAD joint frames. Fingers and wrists are rigid; no cameras are instantiated.
The older 22-axis policies and the fixed-base movement fixture are separate.

Read [ACTIVE_RUN.json](ACTIVE_RUN.json) for the current run directory, then its
live `state.json`. The first sustained standing block was observed advancing
through PPO iterations at **8,192 environments**. This is execution evidence,
not a passed standing policy. The supervisor continues after this chat ends.

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

## Training and promotion

The chain trains stand, walking at 0.35/0.65/1.0 m/s, then running at
1.5/2.0/2.5 m/s. The active r4 run uses 25 PPO updates per block. Separate nominal and pushed
20-second rollouts cover every earlier command before promotion. Failed new
commands continue training; loss of an earlier command rolls back to the last
passing checkpoint. Reward averages cannot promote a policy.

Gates check survival, actual pelvis and torso posture, height, speed, lateral
drift, foot slip, loaded stance, COM support, bilateral completed steps,
cadence, clearance and running flight. Invalid differential poses, non-foot
contact and crossing prevent a pass. A reset never erases a fallen trial.
Numerical gates still require subsequent visual review for natural movement.

The policy is reference-guided residual PPO: four frames of proprioceptive
actor observations, an asymmetric privileged critic, and CAD-specific IK gait
priors. It is not AMP or a pretrained commercial Unitree policy. See
[research and previous-policy review](RESEARCH.md) for primary sources and the
limitations of the earlier locomotion and recovery experiments.

## GPU and unattended operation

Measured PPO benchmarks:

| Environments | Environment steps/s | Minimum sampled free VRAM |
|---|---:|---:|
| 4,096 | 7,156 | 3,248 MiB |
| 6,144 | 9,017 | 2,286 MiB |
| 8,192 | 10,019 | 1,368 MiB |

The selected count is 8,192. The reserve is **300 MiB**, checked each PPO
update, with additional GPU samples every three seconds. A memory failure
preserves a checkpoint where possible and retries at 6,144, then 4,096.
Fallback does not relax torque limits or behavioral gates. Non-memory errors
produce a failed state and retain diagnostics. The original r2 chain had an 18-hour ceiling; the active r3 restart has a
16-hour ceiling; an unpassed stage remains unpassed when that budget ends. Keep the
computer awake and avoid opening another GPU-heavy application during training.

During the first sustained block, free VRAM reached 275 MiB at update 42. The
guard saved `memory_recovery.pt` and the supervisor resumed from that checkpoint
at **6,144 environments**. Advancing PPO updates at 6,144 were observed with
over 2 GiB free. This verifies fallback beyond the short benchmarks. Inspect
live state for later changes. `total_training_iterations` counts completed
blocks; partial updates retained in a memory checkpoint are recorded in that
worker's `progress.jsonl` instead.

Use PowerShell to inspect current progress:

```powershell
$robotRun = Get-Content -Raw 'E:\Aditya\robot_sim\physical_v29\training\ACTIVE_RUN.json' | ConvertFrom-Json
$robotState = Get-Content -Raw $robotRun.state_file | ConvertFrom-Json
$robotState | Select-Object status, stage, operation, environment_count, progress, memory_fallback, promotions
Get-Content -LiteralPath (Join-Path $robotState.operation_path 'stdout.log') -Tail 30
nvidia-smi
```

The supervisor PID in state and its process command line identify the owned
run. A Windows venv launcher PID may differ from the actual Python PID. Do not
stop all Python processes. `result.json` confirms worker completion even if
Kit cleanup hangs; a checkpoint file alone does not. The supervisor handles
cleanup of its own child tree after saving evidence.

## Files and evidence

| File | Purpose |
|---|---|
| [Mass estimate](MASS_ESTIMATE.md) | Total/limb mass and explicit uncertainty |
| `mass_estimate.json`, `mass_by_link.csv` | Every part's basis, link COM and approximate inertia |
| [Research](RESEARCH.md), `research/sources.json` | Primary code/papers, source hashes and old-policy review |
| `assets/robot_training.urdf` | Separate lightweight contact/mass asset |
| `assets/motion_reference.npz`, `motion_validation.json` | CAD IK references and feasibility checks |
| `checks/preflight_07` | Four-second gravity/contact/transmission check: 337.45 N support versus 338.09 N expected |
| `checks/ppo_smoke_01`, `checks/reload_01` | Four real PPO updates and a checkpoint-load execution test; standing gate failed |
| `checks/initial_save_01` | Fixed RSL-RL 5 evaluation logger/save test; unqualified initial policy |
| `test_gates.py` | 14 CPU-only tests reject fall/rise, slipping, one-leg, posture, invalid-pose and support exploits |
| Run `source/physical_v29` | Frozen worker, environment, evaluation, hardware and assets |
| Run `chain_config.json`, `state.json`, `gpu.csv` | Provenance, live state and GPU monitoring |
| Each worker directory | stdout/stderr, config, progress, checkpoints and result/failure JSON |
| Each gate directory | Raw telemetry plus named pass/fail checks |

The first run's successful benchmarks are reused only after checking identical
dynamics, mass and reference files. Its later logger failure is preserved. The
replacement run uses the verified save fix and starts with an **unqualified**
standing prior; it must learn and pass the full standing gate.

Workers read their frozen source tree. Later workspace changes do not update
running Python code. Any playback or checkpoint evaluation must use the
matching source and asset. Do not resume older 22-axis checkpoints. To start a
new chain, run `supervisor.py --help`, choose a new output directory, and
preserve the previous one; directories are never overwritten for a fresh run.

## Physical limitations

The training mass is **34.46 kg** including the battery. Using AmazingHand's
published 400 g complete-hand mass instead of the conservative 640 g allowance
gives **33.98 kg**. Neither total is weighed. Printed structures, purchased
gearsets and bearing references still need slicer/catalog/weighing evidence.

Contact boxes simplify and underapproximate real housings and casing seams.
Armature/gains are planning choices. Loaded motor curves, thermal duty,
battery sag and controller current limits remain unqualified. All current
user torque/speed assumptions, 95% added-transmission efficiency and shared
pose-dependent ankle/waist constraints are applied. Locomotion training does
not certify recovery, backflips, payload or physical safety.

All files, logs and documentation remain local. No Git commit/push or external
experiment service is used.
