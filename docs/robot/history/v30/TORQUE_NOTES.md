# Torque evidence and remaining qualification

## Current user configuration — September 30, 2026

[Current actuator calculations](ACTUATOR_CALCULATIONS.md) supersede the earlier selection assumptions below: 7010 18/45 N·m, 6010 15/30, both 400 RPM at factory output; DJI 8/18 shaft N·m with 15:1 hips and 16:1 knees; additional 4:1 shoulder pitch with a 2.5-equivalent torque cap; CAD-dependent coupled ankle/waist mapping. Current 95% profile,7 N·m/45 RPM elbow and 120 RPM shoulder pitch supersede the earlier assumptions below; real loaded/thermal duty remains pending. Historical evidence below is retained.


Retained planning and older Isaac torque evidence. V29 has a new 1.6002 m joint-motion test, but its proxy mass/drives do not measure physical torque demand. The native casing material is still a Steel placeholder, so native mass/inertia is not an appropriate printed-robot mass model. [Current report](BUILD_REPORT.md).


The earlier Isaac screenshot gives **joint-output** demands. The larger left/right RMS and peak values are preserved here; this is not a new simulation of the physical arms/head or imported hands.

| Joint | Earlier RMS / peak N·m | Hardware or planning assumption |
|---|---|---|
| Hip yaw | 18.2 / 49.6 | 7010 reference; user assumes 45 N·m burst |
| Hip roll | 61.0 / 132.3 | DJI10018 with 15:1 planned |
| Hip pitch | 122.4 / 205.8 | DJI10018 with 17:1 planned |
| Knee | 63.6 / 243.0 | DJI10018 with 8:1×2:1 planned |
| Ankle pitch / roll | 52.8 / 115; 20.1 / 65 | Two 7010 references; configuration-dependent linkage |
| Waist yaw / pitch | 18.5 / 35.3; 16.4 / 60 | 7010 yaw and two 6010 drives; old simulation omitted waist roll |
| Shoulder pitch / roll | 13.0 / 32; 17.2 / 30 | 6010 assumed 30 N·m burst; sustained curve unconfirmed |
| Elbow | 3.8 / 9.4 | RDS51160 selected; 24 V / 170 kg·cm stall is approximately 16.67 N·m from user screenshot, not continuous torque |
| Head yaw / pitch | 5.5 / 7; 2.6 / 7 | 2.94 N·m stall serial servos; revised head needs new dynamics |

The user's 17 N·m DJI shaft assumption gives ideal output products of 272 N·m knee, 255 N·m hip roll and 289 N·m hip pitch. Losses, speed, current convention and heating reduce usable torque. These are planning arithmetic, not measured ratings. The old shoulder peak of 32 N·m exceeds the assumed 30 N·m burst slightly, and the old head demands exceed servo stall. New masses and required motions must be evaluated before declaring sufficient torque. Do not multiply an already-geared output rating by its internal reduction again.

The older 8 mm knee/ankle shaft analysis remains in [shaft strength screening](../lower_leg/SHAFT_STRENGTH_8MM.md). Favorable static screens do not qualify jumps, cyclic loading or motor-link reactions. The retained thin spine, clamp preload, printed forks, hip transmissions, bearing fits and fastener engagement still need engineering detailing.

The 150 kg CAD proxy establishes packaging only; its electrical/torque ratings are not those of the selected 24 V 160 kg servo. Actual continuous torque, speed, current, supply and payload tests remain pending. The original axis fixture used test drives. The September 30 custom actuator now uses user-supplied limits; physical qualification remains pending.
