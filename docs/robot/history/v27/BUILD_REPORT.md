# Humanoid robot — current build report

**Physical CAD revision v27 · 2026-09-30 · documentation maintained locally.**

**Completed cosmetic CAD pass:** `Humanoid_complete_v27`, saved Fusion version 3, is complete and unmodified. Forty-three separate cosmetic solids were added. All 1,785 original BRep signatures, eight hand meshes, 367 original placements, 333 joint configurations and 23 anatomical values are preserved. The full F3Z package has verified file/dependency integrity; native package reimport was not performed. Manufacturing and continuous-motion qualification remain separate.


This report is the current engineering reference for the physical robot. The old lower-leg grant and the simplified 1.524 m / 22-DOF Isaac training asset remain separate baselines. Earlier prices, simulated masses and torque demands do not automatically describe this CAD.

![Current physical CAD](evidence/v27/handoff_iso.png)

## Current layout and dimensions

The original side-facing waist motor arrangement and straight rearward oval metal spine are retained. Abandoned V-spine work is preserved. The preserved internal shoulder/spine frame, battery restraints and electronics box remain. A twelve-piece torso covering and separate limb/pelvis casings provide the new exterior; final cosmetic fasteners/retention are not yet detailed. Actual supplier 6010 references occupy both shoulder axes. Supported upper-arm and forearm forks reach the wrists. Full-size AmazingHand references now attach through the wrist connectors. The stereo-camera head uses separate serial-servo yaw and pitch, and a removable rear shell.

| Dimension | Current nominal geometry |
|---|---|
| Sole-to-head standing height | **1590.2 mm**, approximately 1.59 m / 5 ft 2.6 in |
| Shoulder height above sole | 1340.2 mm |
| Shoulder-roll centre spacing | 394 mm |
| Upper-arm / forearm pivot length | 260 / 240 mm |
| Torso covering | Twelve split panels; largest individual native width 150.75 mm and band height 193.5 mm; nominal 2.5 mm profile offset |
| Spine section | 18×10 mm oval; retained 0.55 mm wall is provisional |
| Battery pack envelope | 140×85×160 mm; 36-cell 12S3P plan |
| Electronics enclosure | 150×86×93 mm outside; 144×80×87 mm main cavity before bosses |
| Head change from v25 | Pitch servo/axis lowered 18 mm; head, camera and visor lowered 12 mm |
| Hands | Full scale; right 120.6×133.8×169.8 mm, left 118.8×134.1×169.8 mm in source pose |

World +Y is rearward, Z is up and X spans the sides. Floor datum is Z−14.83656864 mm; head top is Z1575.36343136 mm. Height is their difference. The current native audit measures standing height from the head shell to the lowest sole, with all body angles neutral except the ±6° shoulder rest abduction. Servo CAD retains its actual dimensions; no physical motor was shortened to obtain the lower head.

## New outer casings

The pale tapered limbs and torso use dark joint breaks, a tapered graphite pelvis and three blue/teal identifiers. The original skeleton, motor layout, spine, electronics, head and hands remain. Covers are separate components on their original rigid links; no body joint was added. The earlier T01 torso skin is hidden and preserved.

| Group | New solids |
|---|---:|
| Split torso bands | 12 |
| Upper-arm / forearm front and rear skins | 4 / 4 |
| Thigh front and rear skins | 4 |
| Split shin/calf skins | 8 |
| Hip-roll front caps / split pelvis | 2 / 2 |
| Knee and ankle front guards / blue marks | 4 / 3 |

[Casing design](CASING_DESIGN.md) records exact dimensions, palette, print splits and checks. [Casing inventory](CASING_INVENTORY.csv) contains each actual solid. The torso is split across both height and width; shin panels are also split into upper/lower pieces. These dimensions address bed size but do not certify a selected printer, orientation, supports, panel retention or minimum wall thickness.

## Mechanisms and interfaces

### Legs, hips and waist

The retained legs use paired ankle drives and linked pitch/roll outputs, knee chain-layout references and estimated DJI10018 hip/knee packages. Planned reductions are knee 8:1 internal ×2:1 chain, hip roll 15:1 and hip pitch 17:1; these are user planning targets, not finished manufactured gearsets.

The physical hip chain is pelvis → tilted hip pitch → hip roll → hip yaw → thigh → knee → shin → ankle. Pitch retains the measured 25° shaft tilt on each side. Native hip frames derive from the actual bearing cylinder faces; each frame's primary axis supplies its revolute direction. The left roll/yaw axes point opposite the right because their bearing faces define the native frames; use the measured joint map for sign conventions. Fixed motor housings and moving outputs belong to their respective rigid links. Knee positive flexion is intended to move the lower leg backward (+Y) from a pelvis-anchored standing pose; direction is certified only by the recorded native movement check below.

Waist order is yaw → **lower pitch** → **upper roll**. The retained two 6010 outputs use 26 mm cranks and 60 mm rod-eye spacing. M6 rod ends remain; no extra swivels were added. A swivel would add a separate two-axis pivot between the link and mount to supply articulation beyond the rod end's tilt. Current geometry uses the user's **35° maximum rod-end tilt assumption**, which still requires verification with real washers, spacers and fasteners.

Historical v21 checks sampled pure pitch −30°/+20°, pure roll ±30° and combined ±10° corners. These establish only those discrete poses; they do not establish a full rectangular combined workspace. New native-joint limits and motion tests are distinct from mechanical travel qualification.

### Spine, torso, battery and electronics

The internal shoulder crossmember has two spaced oval-spine saddles and removable caps. It carries shoulder bearing backing rings and the original skin attachment; the new cosmetic panels still need their final removable retention detailed. The provisional pack is a solid envelope with a 134×77×22 mm BMS/wiring reservation and retained cradle/restraints. Actual cells, BMS, fuse, interconnects and pack thermal details are unselected.

The electronics enclosure above it reserves space for a host, converters and interfaces. Actual board mounts, connector ports, airflow and wiring remain to detail after selection. Neck servos require their specified regulated 12 V supply; hand and logic rails must match the selected hardware. Raw pack voltage is not a substitute for those regulated rails.

### Shoulders, elbows, forearms and hands

Shoulder pitch uses an external **6810, 50×65×7 mm bearing**. Its driven output carries the perpendicular 80 mm OD roll housing. Roll has a driven front flange and fixed rear 25 mm journal with a **6005, 25×47×12 mm bearing**, supporting the upper-arm fork from both sides. These bearings carry external loads; gearbox torque capacity and bearing seat/load design remain separate requirements.

The supplier 6010 geometry has **eight M2.5 fixed mounting holes on a 40.5 mm pitch circle** and **six M3 output holes on a 25 mm pitch circle**. Fixed housings attach to the frame/carrier; exposed output partitions follow the appropriate native joints. Upper arms have nominal 34×10 mm cheeks, two braces and a 260 mm pivot length. Elbows use two 6005 bearings around a generic 25 mm dual-sided output shaft; the front has six mounting holes and the rear four. The 52 mm OD×20 mm actuator reservation is provisional because the elbow actuator is unselected.

Forearms have two 28×8 mm rails, braces and a 240 mm pivot length. Their final material remains unresolved: the current native tag is `Concept metal` and the appearance is aluminum gray, while earlier scripts inherited plastic appearance. The wrist adapter connects their four-M3 **24×18 mm** mounting pattern to the AmazingHand's three-M2.5 / 42 mm pitch circle and retains an 18 mm cable bore. Top-down M3 screws have radius 3.2 mm, 3 mm-deep forearm head counterbores and nominal OD4.6×4 mm adapter insert pockets. Hands use each side's official full-size eight-microservo source assembly, without Fusion finger articulation. [Hand rationale, source attribution and MG90 evaluation](HAND_OPTIONS.md) explains what is selected and what still needs a prototype.

The retained 6° shoulder-abducted rest pose gave hand-envelope X separation from the original neutral hips of **18.89 mm right / 19.08 mm left** in v26. Current source-STL vertex bounds also clear the new thigh skins by **13.30 mm right / 13.50 mm left along X**; current native mesh bounds and placements match the retained references, but slight source/native triangle-count differences prevent a vertex-by-vertex native equality claim. This is a conservative envelope result at neutral hips; it does not qualify every hip/arm pose. Unabducted construction zero is not assumed collision-free.

### Neck, printable head and vision

The old MG996/DS3230 surrogate is hidden and preserved. Two imported Feetech STS3215 references provide yaw and pitch. The oval-spine adapter supports the yaw output with a 6005 bearing, servo retaining clamp and outer-race cap. The pitch yoke uses the driven horn on one side and passive horn on the other. The pitch motor is lower, inside the head's lower volume.

Pitch case retention uses a **split 7 mm-high external collar and floor**, with a removable front cap and **two M3 screws outside the actual case**. Nominal case clearance is 0.2 mm and the split gap 0.3 mm. The modeled screw shanks have zero case intersections. Supplier-ear through bolts were rejected after the actual CAD mount-region probe; the design does not claim four ear bolts. Physical case fit, compression and torque retention still require a prototype, and an alternate ear mount needs a manufacturer drawing.

A defined hollow front shell and removable rear shell replace the earlier egg-shaped reference; nominal wall is 2.5 mm, with four M3 seam positions and an open camera visor. The rear lower lip is relieved by 8 mm for downward-pitch torso clearance while retaining the lower servo and head height. Actual print tolerances, insert fit, cable clearance and fastener access still need a printed trial.

The recommended **Yahboom AI VIEW / Astra SV1301S U3** was listed at **$199 before tax/shipping** when researched September 29. Its MX6000 engine provides processed depth over USB3; published active binocular/structured-light specifications include a 40 mm baseline and indoor 0.25–2.5 m range. USB3 depth modes include 1280×800 at 30 fps and 640×400 at 60 fps. Official STEP geometry is installed in the head; published mass is 45.7 g. The open visor leaves the optics uncovered. Object recognition and robot perception remain host software, not assumed onboard inference. [Manufacturer](https://category.yahboom.net/products/aiview-depth-camera), [official specification image](https://cdn.shopify.com/s/files/1/0066/9686/1780/files/AI_VIEW_depth_camera_specifications_and_size.jpg?v=1779420877), [CAD/tutorial](https://www.yahboom.net/study/AIVIEW_Camera).

The 12 V / 30 kg·cm STS3215 rating is about **2.94 N·m stall**, not continuous torque. Confirm the actual variant; the older 7.4 V model has different ratings. [Feetech variants](https://www.feetechrc.com/products.html?keyword=STS3215).

## Articulation, colors and assembly organization

The intended whole-robot hierarchy contains **23 revolute body joints**: six per leg, three waist, three per arm and two neck. Hands and wrists are rigid packaging references in this pass, as requested. Passive linkage joints can make Fusion's total joint count larger than 23; they are not extra controlled body axes.

Material colors identify intended part roles: blue printed structure, pale printed cosmetic shells, silver/gray metal shafts and frame parts, dark motor housings and soft pads, green boards and copper electrical metal where identifiable. They are visual labels, not assignments of density, strength or manufacturing approval. Current material/organization evidence is recorded below. Reusable source components and hidden legacy references remain preserved; hardware ownership should follow the rigid link it fastens to, with left/right names retained for audit.

## Torque evidence and unresolved qualification

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

## Validation and saved artifacts

| Check | Current evidence and scope |
|---|---|
| Original skeleton preservation | PASS: 1,785 BRep signatures, 8 meshes, 367 original placements, 333 joints and 23 anatomical values unchanged; 43 bodies/occurrences added, no joints added |
| Final casing static fit | PASS: all 43 skins/guards/marks, 109 selected native batches and 934 original-BRep candidates; final repaired geometry matched to the final after capture |
| Hip-pitch cap clearance | PASS: ten calibrated samples, −45/−30/0/+30/+45° per side, versus both new fixed pelvis panels and original W02/W03/W04; no whole-body or continuous sweep claim |
| Hand/thigh at recorded rest | Retained source vertices give positive X gaps 13.30/13.50 mm; conservative transformed full-mesh box overlaps were inconclusive, not collisions |
| Final native source handoff | PASS: complete/unmodified version 3, 410 occurrences and 23 axes; no pending snapshot; TextCommands hidden and Fusion left open |
| Saved v27 native source | Complete and unmodified version 3, `cNq9ppTGSpuNdIKGufBJ0w` |
| Full v27 F3Z reference package | File/dependency integrity PASS; 219,727,989 bytes; saved source v3 plus GWK motor dependency v1; native standalone package reimport unperformed |
| Inherited v26 articulation | 23 body-axis direction/reset tests and 5 paired differential fixtures PASS; v27 preserves their joints and rest settings; new covers do not inherit full swept clearance |
| Inherited head/material checks | v26 nine head-pose samples, selected 42-solid head fits, material-role audit and zero feature issues remain preserved baseline evidence |
| Compact casing-only F3D | PASS: independent native reopen, all 43 connected solids, identity placements, precise bounds/volumes, palette and physical-material placeholders retained; source unchanged |
| Manufacturing | Cosmetic attachments, material grade, printer/orientation fit, minimum wall, strength and new mass/dynamics remain provisional |

[Evidence index](EVIDENCE.md) separates final static checks, preservation, sampled hip motion, source save and export qualification. The geometry-signature audit uses volume/area/centroid at Fusion's default LowCalculationAccuracy, plus precise bounds and native identities/placements; it is not an exact BRep hash or validated mass/inertia measurement. Static zero-volume intersection checks use a 0.01 mm³ tolerance and do not guarantee minimum clearance, new-to-new panel separation, cable travel or continuous motion.

| Purpose | Location |
|---|---|
| **Current full assembly package** | [Humanoid_complete_v27_full_20260930.f3z](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v27/deliverables/Humanoid_complete_v27_full_20260930.f3z); verified file/dependency integrity, native package reimport unperformed |
| Saved Fusion source | `Humanoid_complete_v27`, version 3; `urn:adsk.wipprod:dm.lineage:cNq9ppTGSpuNdIKGufBJ0w` |
| New casing exports | [Export index](EXPORTS.md); qualification is recorded only when actual completed export/file/reopen evidence exists |
| Detailed exterior design | [Casing design](CASING_DESIGN.md) / [43-part inventory](CASING_INVENTORY.csv) |
| Procurement and native inventory | [BOM](BOM.md) / [CSV](BOM.csv); [410 occurrences](CAD_PARTS.csv) / [333 native constraints](JOINTS.csv) |
| Preserved v26 mechanical checkpoint | [v26 report](history/v26/BUILD_REPORT.md), [v26 exports](history/v26/EXPORTS.md) and retained original source/archive |
| Local construction and checks | `E:/Aditya/robot_sim/outputs/shin_cad_20260912/v27` |

Native occurrence counts include source/legacy objects; they are not procurement quantities. The 333 native constraints include passive/rigid relationships, while there remain 23 controlled body axes. The full F3Z includes external source dependencies; a valid ZIP/reference graph is distinct from a native archive reimport. Original hand source attribution and fit-trial head/wrist/forearm exports are retained in the v26 records.

## Documentation map and history

[BOM](BOM.md) is the buying/status view; the CAD inventory is the native component view. [Physical revision index](../lower_leg/README.md) links retained dated records. [Historical grant](../archive/LOWER_LEG_GRANT.md) preserves the earlier lower-leg project and prices. [Training file locations](../../Learning/HumanoidTraining/FILE_LOCATIONS.md) retain the separate Isaac pipeline and checkpoints.

These documentation edits are **local only**. No Git commit, GitHub push or online publication is part of this task. CAD revisions may be saved in the user's existing Fusion project as checkpoints; that is separate from publishing the repository.

## Decisions to confirm after review

1. Which exact microservo will the physical hand use: original SCS0009 or a measured MG90/SG90 redesign? The current hand CAD retains the original SCS0009 geometry. The sub-$100 target needs a priced prototype BOM.
2. Which elbow motor/reduction fits the supported generic output and 52×20 mm reservation? A wrist actuator is not included in this pass.
3. Which host, cells, BMS, converters and controllers will occupy the reserved electronics/pack spaces? Actual board dimensions determine ports, cooling and mounts.
4. Do purchased motor variants and transmissions match the planning torque/ratio assumptions? Measure final bearing seats, shaft fits, clamp sections and servo-horn interfaces before fabrication.
5. Which physical motion/payload tests should drive the new dynamics model? Older Isaac policies and torque tables are separate evidence and do not qualify this CAD.
6. Should the resting palms face inward toward the thighs or keep the imported fore/aft orientation? Wrist rotation and a powered wrist are not included in the current rigid connector.
7. Should the forearm forks use aluminum rails or printed PA12-CF? Their current `Concept metal` tag and aluminum-gray color conflict with an earlier plastic appearance; neither manufacturing choice is strength-qualified.
8. Which printer, polymer and removable panel retention should be used for the new casings? Current splits and geometric fit do not certify bed orientation, minimum walls, insert/fastener fit or print strength.
