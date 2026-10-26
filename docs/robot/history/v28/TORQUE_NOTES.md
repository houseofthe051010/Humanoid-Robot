# Torque evidence and remaining qualification

Retained planning and older Isaac evidence; this is not a new simulation of the 1.59 m casing-loaded robot. The native casing material is still a Steel placeholder, so native mass/inertia is not an appropriate printed-robot mass model. [Current report](BUILD_REPORT.md).


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
| Elbow | 3.8 / 9.4 | Actuator unselected |
| Head yaw / pitch | 5.5 / 7; 2.6 / 7 | 2.94 N·m stall serial servos; revised head needs new dynamics |

The user's 17 N·m DJI shaft assumption gives ideal output products of 272 N·m knee, 255 N·m hip roll and 289 N·m hip pitch. Losses, speed, current convention and heating reduce usable torque. These are planning arithmetic, not measured ratings. The old shoulder peak of 32 N·m exceeds the assumed 30 N·m burst slightly, and the old head demands exceed servo stall. New masses and required motions must be evaluated before declaring sufficient torque. Do not multiply an already-geared output rating by its internal reduction again.

The older 8 mm knee/ankle shaft analysis remains in [shaft strength screening](../lower_leg/SHAFT_STRENGTH_8MM.md). Favorable static screens do not qualify jumps, cyclic loading or motor-link reactions. The retained thin spine, clamp preload, printed forks, hip transmissions, bearing fits and fastener engagement still need engineering detailing.
