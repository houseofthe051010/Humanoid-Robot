# Current actuator calculations — September 30, 2026

Current profile: `eff95_elbow7_20260930`. Values are user-selected planning assumptions for physical v29. Actual link mass/inertia, thermal duty and contact dynamics remain unqualified. Factory-geared motor outputs and servo outputs already include their internal reduction; they are not derated twice.

**Efficiency is 95% overall for each added transmission or rod linkage.** Knee 8×2 uses one overall 95% assumption, rather than 95% twice. Direct 7010/6010 and neck/elbow outputs retain their supplied output values. The shoulder-pitch speed target is 120 RPM, requiring 480 RPM at its geared motor output, below the adopted 500 RPM cap.

| Joint, same on both sides | Sustained/rated N·m | Peak/operating cap N·m | Speed ceiling RPM | Meaning |
|---|---:|---:|---:|---|
| ankle pitch | 59.37 | 148.42 | 229.9 | Neutral pure-axis; shared motor limits |
| ankle roll | 34.14 | 85.34 | 399.9 | Neutral pure-axis; shared motor limits |
| waist pitch | 53.14 | 106.27 | 214.5 | Neutral pure-axis; shared motor limits |
| waist roll | 35.83 | 71.67 | 318.1 | Neutral pure-axis; shared motor limits |
| waist yaw | 18.00 | 45.00 | 400.0 | User planning assumption |
| hip pitch | 114.00 | 256.50 | 221.8 | User planning assumption |
| hip roll | 114.00 | 256.50 | 221.8 | User planning assumption |
| hip yaw | 18.00 | 45.00 | 400.0 | User planning assumption |
| knee pitch | 121.60 | 273.60 | 207.9 | User planning assumption |
| shoulder pitch | 35.62 | 71.25 | 120.0 | Physical 4:1; capped input torque |
| shoulder roll | 15.00 | 30.00 | 400.0 | User planning assumption |
| head yaw | 0.98 | 2.94 | 45.0 | 12 V rated / stall / no-load |
| elbow pitch | 7.00 | 7.00 | 45.0 | User 7 N·m / 45 RPM operating box |
| head pitch | 0.98 | 2.94 | 45.0 | 12 V rated / stall / no-load |

## Transmission and torque caps

DJI 10018 77 KV uses 8 N·m sustained / 18 burst at the bare shaft. Both hip pitch and roll use 15:1: 8×15×0.95=114 sustained and 18×15×0.95=256.5 peak. Knee uses 8:1 planetary ×2:1 chain: 121.6 / 273.6 N·m. Nominal no-load estimates at 43.2 V are 221.76 RPM hips and 207.9 RPM knees; full-charge estimates are 258.72 / 242.55. These are speed ceilings, not claims that peak torque persists to no-load speed.

Shoulder pitch physically adds 4:1. Input caps remain 9.375 N·m sustained / 18.75 peak, equivalent to a 2.5 multiplier of the 6010 torque ratings before losses. Joint output is **35.625 / 71.25 N·m** after 95% efficiency. Its selected 120 RPM needs 480 motor-output RPM. The extra planetary is still planned hardware, not a newly modeled gearbox. Shoulder roll remains direct 15 / 30 N·m at 400 RPM.

## CAD-dependent ankle and waist differentials

`assets/differential_geometry.json` derives rod-eye centres, shaft axes and rod lengths from the saved native v29 joint frames. For q=[pitch,roll] and shaft angles θ, the solver computes J(q)=∂θ/∂q. Velocity mapping is θ̇=Jq̇; the selected torque model is **τ_joint=0.95 Jᵀ τ_motor**. Requested effort is transformed to both motor shafts, clipped there and transformed back. This scalar loss model is a planning approximation, not a measured bidirectional friction/regeneration model.

Near neutral, approximate peak envelopes are:

- Ankles: |τ_pitch|/148.42 + |τ_roll|/85.34 ≤1. Sustained denominators are 59.37 and 34.14 N·m.
- Waist: |τ_pitch|/106.27 + |τ_roll|/71.67 ≤1. Sustained denominators are 53.14 and 35.83 N·m.

Actual saved linkage asymmetry and posture dependence are included in the runtime matrix. Pitch and roll can act simultaneously, but cannot both reach their separate pure-axis maxima simultaneously. Motor-output speed caps remain 400 RPM; efficiency does not change geometric speed reduction. Ankle neutral pitch/roll ratios are about 1.736 / 1.000 and waist 1.864 / 1.257. The older fixed 1.15 ankle factor is unused.

Some corners of the anatomical waist limit rectangle have no feasible rod closure or allowed crank travel. Invalid poses are flagged; these tests use valid pure-axis samples. Passive rod/crank visuals are attached packaging meshes, not an animated passive PhysX closed loop. Rod-end tilt/contact, compliance and whole-workspace strength remain unqualified.

## Supplier torque/current and speed/voltage constants


The attached Excel tables were read without substituting their rated/maximum torque or speed rows for the user's assumptions. The **2026 exoskeleton Sheet1** has WGG7010-8 F14=0.65 N·m/A and F13=9.25 output RPM/V; WGG6010-8 C14=0.39 and C13=21.6667. The other table's first sheet has different GIM6010-8 constants M16=0.47 for 24 V and N16=0.65 for 48 V. These variants must not be treated as identical purchased hardware. Full cells and SHA256 source hashes are in `assets/motor_constants_20260930.json`.

| Reference | Approx. current for sustained assumption | Approx. current for peak assumption |
|---|---:|---:|
| WGG7010-8, 0.65 N·m/A | 27.7 A at 18 N·m | 69.2 A at 45; 76.9 A at 50 |
| WGG6010-8, 0.39 N·m/A | 38.5 A at 15 N·m | 76.9 A at 30 |
| GIM6010-8 24 V,0.47 | 31.9 A at 15 | 63.8 A at 30 |
| GIM6010-8 48 V,0.65 | 23.1 A at 15 | 46.2 A at 30 |
| DJI 77 KV, ideal Kt=9.5493/77≈0.1240 | 64.5 A at 8 shaft N·m | 145.1 A at 18 shaft N·m |

These are **T/Kt using each source's current convention**. Sheets do not identify phase RMS/peak, Iq or bus current, and the supplier's constants and operating data are not perfectly self-consistent. They cannot be summed to obtain battery current or used uncalibrated as controller phase limits. DJI conversion is an ideal SI estimate; actual winding/controller convention is unresolved.

WGG7010 speed from Kv is **399.6 RPM nominal /466.2 full**; it does not establish >500 RPM for this 8:1 variant. WGG6010 gives936 /1092 before the user's 400 ceiling. GIM6010-8 instead gives498.6 /581.7. A 50 N·m 7010 boost costs approximately 23.5% more I²R heat than 45 N·m at the same resistance, but does not establish a continuous 50 rating.

## Servo sources and custom control

[Feetech STS3215-C018](https://www.feetechrc.com/525603.html) specifies 10 kg·cm rated / 30 kg·cm stall and 0.222 s/60° no-load at 12 V: 0.981 / 2.942 N·m and 45.05 RPM. The user elbow screenshot gives 170 kg·cm stall and 0.21 s/60° at 24 V: 16.67 N·m and 47.62 RPM no-load.

The user now selects **7 N·m sustained at 45 RPM** for the elbow. Both sustained torque and the operating command cap are 7 N·m; the advertised stall/no-load values remain metadata. This is an assumed operating box, not a measured loaded curve. It supersedes the earlier linear elbow approximation. The neck retains its documented linear stall-to-no-load planning curve. Custom driver/encoder feedback remains planned hardware; mechanical and thermal qualification is pending.

## 12S3P battery comparison

36 cells; nominal 43.2 V and full 50.4 V. Series count raises voltage, three parallel raises current/capacity.

- **Ampace JP50:** strong choice for explicitly specified short bursts. [Manufacturer product page](https://en.ampace.com/products/power-tools-product-matrix/jp/69) lists 5 Ah, 50 A high-power continuous and 180 A for 5 s; the detailed parameter table additionally distinguishes 60 A maximum continuous from 40 A full-discharge continuous. These are different duty qualifications. 12S3P is 15 Ah, about644–648 Wh, approximately2.59 kg bare cells. Full-discharge cell arithmetic is 120 A; headline 50 A gives 150 A; 180 A / 5 s gives 540 A for 5 s at cell level, not an assembled-pack guarantee.
- **Molicel P60C:** [manufacturer page](https://www.molicel.com/product/inr-21700-p60c/) lists 6 Ah and 100 A discharge. 12S3P gives 18 Ah  / 777.6 Wh  / 2.70 kg bare cells, with 300 A listed-current arithmetic. The public page does not establish unrestricted continuous duty or a 120 A pulse duration; get the application datasheet before selecting a thermal budget. This is the highest listed discharge current among these reviewed manufacturer references, not a proof of the best robot pack.

No reviewed reference establishes the user's 75 A continuous plus>120 A burst as an unrestricted general 21700 rating. A practical first full-discharge budget for the JP50 example is **120 A pack**, about 5.18 kW nominal before sag; 150 A is 6.48 kW under its separate higher-current duty. Actual pack limits are the minimum of cells, temperature, BMS, interconnects, wiring, connectors and fuse. Pulse duration and repetition matter. 12S voltage does not add torque beyond the driver current cap. 24 V elbows and 12 V neck require appropriate regulated rails. Exoskeleton sheet voltage range stops at 48 V, so exact electronics must be verified for 50.4 V full12S.

Battery sufficiency cannot be proved from the sum of phase-current estimates. A gait power trace needs simultaneous shaft speed/torque, calibrated copper losses and converter efficiency. No verified battery-current/thermal/regeneration model has been added to Isaac.

## Isaac checks and GUI preview

Use `hardware_actuators.make_actuators()` with `assets/actuator_limits.json`. URDF differential limits are bounding boxes; the custom actuator supplies actual shared constraints. Continuous torque is recorded but no time/thermal model is enforced. The optional 50 N·m waist-yaw boost stays off.

`validation/eff95_elbow7_20260930` contains passing finite-difference/closure/95%-power/shared-limit tests and all **23** strict Isaac movement/FK/reset checks. `validation/eff95_elbow7_20260930_visual` records the larger, smooth fast preview. Both use fixed base, disabled gravity/contacts, proxy masses/inertia and test-only 0.05 kg·m² armature. Strict gains are 120/15 for waist/hip/knee and 35/4 otherwise; fast preview uses 120/8 on heavy joints at 10 ms steps. Neither fixture qualifies locomotion or real load capability.

```powershell
& 'E:\Aditya\robot_sim\env_isaaclab\Scripts\python.exe' -X utf8 `
  'E:\Aditya\robot_sim\physical_v29\test_joints.py' `
  --device cpu --hardware_actuators --visual_fast --seconds_per_joint 2.5 --repeat
```

The GUI labels each joint, shows target/measured angles, and provides front/side/three-quarter views, pause, repeat and stop. Each axis takes about 2.5 simulated seconds plus a brief reset; wall time depends on rendering. Wrists and fingers stay static. Close the window to end the test. `--exit_after_cycle` closes after one pass.

## Wrist correction

The v29 hand mesh copy omitted the 6° resting shoulder rotation that the forearms and adapters already carried. Native mesh coordinates were assumed to be root-context coordinates. All eight complete hand category meshes are now rotated into the adapter frames, preserving original meshes hidden. Six M2.5 axes are coaxial with the adapters within 0.003 mm. All 1537 BReps and 47 joints are unchanged. The corrected full native archive independently reopens; affected simulation visuals are synchronized. Evidence: `outputs/shin_cad_20260912/v29/wrist_review_20260930`.

All documentation remains local. No Git commit, push or publication was performed.
