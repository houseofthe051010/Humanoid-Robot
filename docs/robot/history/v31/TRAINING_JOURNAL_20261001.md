# October 1 physical-v29 training handoff

Reviewed older humanoid journals, source walking/running videos and dashboard
GIFs, guarded locomotion/recovery code and failure reports. The old 22-axis
model is preserved. Primary policy research and exact sources are indexed in
the new training package.

Built a separate component-mass/light-contact asset, CAD IK gait references,
history/asymmetric-critic residual PPO and independent stand/walk/run gates.
Fixed fictitious overlapping hip-marker collisions while keeping self-collision
enabled. Physics/contact/shared-transmission checks passed; PPO and checkpoint
reload executed. Their short rollout was not a learned standing pass.

All three environment-count benchmarks passed. The first attempt then failed
an RSL-RL evaluation logger/save call. Fixed that call, retested saving, kept
the failure evidence, and launched the replacement sustained stand block at
8,192 environments. Iterations were observed advancing with more than 300 MiB
free VRAM. Exact live progress and promotions belong in the run's state/gate
files, not this dated note. No stage is certified by this entry.

Mass estimate is 34.46 kg conservative or 33.98 kg with the published hand
mass; it is not weighed. Local build report, BOM mass basis, simulation
handoff, source index and robot-training skill were updated. No Git commit or
push and no external experiment service.


## Stationary walking reward repair

R4 passed standing but not walking. Saved joint/contact telemetry showed
stationary leg oscillation. User requested a fix. The ordered-step and
signed-progress reward repair passed 23 targeted CPU tests; the recorded
planted-foot rollout lost 96.43% of its positive motion credit. Existing
behavioral thresholds remain. A fresh r5 chain starts from the trusted stand
actor, resetting critic/optimizer estimates when the reward changes. The new
chain performs fresh Isaac checks and capacity benchmarks, revalidates stand,
then adds an easier 0.15 m/s walking stage. No walking success is claimed by
this entry. Full details: TRAINING_REWARD_REPAIR_20261001.md. Local only.

## CAD v30 and automatic capacity continuation

Native v30 was saved/exported and independently reopened with 1,566 visible
shapes and all 65 constraints/ranges/grounds matched. All 23 body axes preserved
cover ownership during disposable-copy motion tests, with zero live pose change.
The 122 sampled hip/waist/shoulder interface checks passed. Broader measured hip
carriers, closed fitted waist cups, articulated shoulder covers and actual ANSI
#40 sprocket arcs are delivered. Print/CNC strength and v30 dynamics remain open.

R10 resumed frozen-v29 PPO at 4,096 environments with preserved checkpoints and
corrected measured-step rewards. Live updates and the 180-second capacity
qualification were observed. The ramp applies one tier at a saved boundary,
preserving a 300 MiB reserve and independent stage/retention gates. Fast blocks
now use measured timing to leave enough observation time. These are execution/
capacity checks; walking had zero completed steps at this dated audit and had
not passed. Read ACTIVE_RUN.json for subsequent progress.

Report, BOM, current file index and skill references were organized locally.
Old releases/runs and user concepts are preserved. No Git commit/push.
