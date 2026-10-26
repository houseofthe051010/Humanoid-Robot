# Humanoid robot — current build report

**Physical CAD revision v26 · 2026-09-30 · documentation maintained locally.**

**Completed CAD pass:** Saved Fusion version 4 is complete, unmodified and open at the verified 23-axis rest pose. Native motion and saved-source checks pass. The full F3Z backup has verified file/dependency integrity; standalone package reimport was not performed. The upper-body F3D and individual concept-part exports have separate qualifications below.


This report is the current engineering reference for the physical robot. The old lower-leg grant and the simplified 1.524 m / 22-DOF Isaac training asset remain separate baselines. Earlier prices, simulated masses and torque demands do not automatically describe this CAD.

![Current physical CAD](../../evidence/v26/v26_whole_robot_final.png)

## Current layout and dimensions

The original side-facing waist motor arrangement and straight rearward oval metal spine are retained. Abandoned V-spine work is preserved. The torso skin attaches to a spine-mounted internal frame, with battery restraints and an electronics box above the battery. Actual supplier 6010 references occupy both shoulder axes. Supported upper-arm and forearm forks reach the wrists. Full-size AmazingHand references now attach through the wrist connectors. The stereo-camera head uses separate serial-servo yaw and pitch, and a removable rear shell.

| Dimension | Current nominal geometry |
|---|---|
| Sole-to-head standing height | **1590.2 mm**, approximately 1.59 m / 5 ft 2.6 in |
| Shoulder height above sole | 1340.2 mm |
| Shoulder-roll centre spacing | 394 mm |
| Upper-arm / forearm pivot length | 260 / 240 mm |
| Torso shell | Nominal 2.5 mm skin; maximum width about 302 mm, depth about 146 mm |
| Spine section | 18×10 mm oval; retained 0.55 mm wall is provisional |
| Battery pack envelope | 140×85×160 mm; 36-cell 12S3P plan |
| Electronics enclosure | 150×86×93 mm outside; 144×80×87 mm main cavity before bosses |
| Head change from v25 | Pitch servo/axis lowered 18 mm; head, camera and visor lowered 12 mm |
| Hands | Full scale; right 120.6×133.8×169.8 mm, left 118.8×134.1×169.8 mm in source pose |

World +Y is rearward, Z is up and X spans the sides. Floor datum is Z−14.83656864 mm; head top is Z1575.36343136 mm. Height is their difference. The current native audit measures standing height from the head shell to the lowest sole, with all body angles neutral except the ±6° shoulder rest abduction. Servo CAD retains its actual dimensions; no physical motor was shortened to obtain the lower head.

## Mechanisms and interfaces

### Legs, hips and waist

The retained legs use paired ankle drives and linked pitch/roll outputs, knee chain-layout references and estimated DJI10018 hip/knee packages. Planned reductions are knee 8:1 internal ×2:1 chain, hip roll 15:1 and hip pitch 17:1; these are user planning targets, not finished manufactured gearsets.

The physical hip chain is pelvis → tilted hip pitch → hip roll → hip yaw → thigh → knee → shin → ankle. Pitch retains the measured 25° shaft tilt on each side. Native hip frames derive from the actual bearing cylinder faces; each frame's primary axis supplies its revolute direction. The left roll/yaw axes point opposite the right because their bearing faces define the native frames; use the measured joint map for sign conventions. Fixed motor housings and moving outputs belong to their respective rigid links. Knee positive flexion is intended to move the lower leg backward (+Y) from a pelvis-anchored standing pose; direction is certified only by the recorded native movement check below.

Waist order is yaw → **lower pitch** → **upper roll**. The retained two 6010 outputs use 26 mm cranks and 60 mm rod-eye spacing. M6 rod ends remain; no extra swivels were added. A swivel would add a separate two-axis pivot between the link and mount to supply articulation beyond the rod end's tilt. Current geometry uses the user's **35° maximum rod-end tilt assumption**, which still requires verification with real washers, spacers and fasteners.

Historical v21 checks sampled pure pitch −30°/+20°, pure roll ±30° and combined ±10° corners. These establish only those discrete poses; they do not establish a full rectangular combined workspace. New native-joint limits and motion tests are distinct from mechanical travel qualification.

### Spine, torso, battery and electronics

The internal shoulder crossmember has two spaced oval-spine saddles and removable caps. It carries shoulder bearing backing rings and attaches the skin to the spine. The provisional pack is a solid envelope with a 134×77×22 mm BMS/wiring reservation and retained cradle/restraints. Actual cells, BMS, fuse, interconnects and pack thermal details are unselected.

The electronics enclosure above it reserves space for a host, converters and interfaces. Actual board mounts, connector ports, airflow and wiring remain to detail after selection. Neck servos require their specified regulated 12 V supply; hand and logic rails must match the selected hardware. Raw pack voltage is not a substitute for those regulated rails.

### Shoulders, elbows, forearms and hands

Shoulder pitch uses an external **6810, 50×65×7 mm bearing**. Its driven output carries the perpendicular 80 mm OD roll housing. Roll has a driven front flange and fixed rear 25 mm journal with a **6005, 25×47×12 mm bearing**, supporting the upper-arm fork from both sides. These bearings carry external loads; gearbox torque capacity and bearing seat/load design remain separate requirements.

The supplier 6010 geometry has **eight M2.5 fixed mounting holes on a 40.5 mm pitch circle** and **six M3 output holes on a 25 mm pitch circle**. Fixed housings attach to the frame/carrier; exposed output partitions follow the appropriate native joints. Upper arms have nominal 34×10 mm cheeks, two braces and a 260 mm pivot length. Elbows use two 6005 bearings around a generic 25 mm dual-sided output shaft; the front has six mounting holes and the rear four. The 52 mm OD×20 mm actuator reservation is provisional because the elbow actuator is unselected.

Forearms have two 28×8 mm rails, braces and a 240 mm pivot length. Their final material remains unresolved: the current native tag is `Concept metal` and the appearance is aluminum gray, while earlier scripts inherited plastic appearance. The wrist adapter connects their four-M3 **24×18 mm** mounting pattern to the AmazingHand's three-M2.5 / 42 mm pitch circle and retains an 18 mm cable bore. Top-down M3 screws have radius 3.2 mm, 3 mm-deep forearm head counterbores and nominal OD4.6×4 mm adapter insert pockets. Hands use each side's official full-size eight-microservo source assembly, without Fusion finger articulation. [Hand rationale, source attribution and MG90 evaluation](../../HAND_OPTIONS.md) explains what is selected and what still needs a prototype.

The 6° shoulder-abducted rest pose gives hand-envelope X separation from the neutral hips of **18.89 mm right / 19.08 mm left**. This is a conservative envelope result at neutral hips; it does not qualify every hip/arm pose. Unabducted construction zero is not assumed collision-free.

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

The older 8 mm knee/ankle shaft analysis remains in [shaft strength screening](../../../lower_leg/SHAFT_STRENGTH_8MM.md). Favorable static screens do not qualify jumps, cyclic loading or motor-link reactions. The retained thin spine, clamp preload, printed forks, hip transmissions, bearing fits and fastener engagement still need engineering detailing.

## Validation and saved artifacts

| Check | Current evidence status |
|---|---|
| Lowered/split head geometry | Native geometry complete; sampled interference/fits below; printed fit trial separate |
| Hip chain reconstruction | Six physical bearing-derived hip frames recorded; direction test below |
| Hand import and wrist connectors | Two official source hands and 18 mm wrist adapters recorded; fingers rigid |
| Native body-joint directions, fixed/moving parts and reset | PASS; 23 recorded body-axis tests |
| Intact ankle/waist differential checks | PASS; 5 recorded paired-output tests |
| Current native rest angles and standing-height measurement | PASS; 23 body-angle targets recorded |
| Sampled head yaw/pitch clearance | PASS; nine discrete yaw/pitch poses, not a continuous swept-range guarantee |
| Head/neck active solids and selected fits | PASS for 42 inspected solids and selected fits |
| Material colors and structure audit | 49 completed batches; 236 appearance overrides and 17 metadata updates recorded; four printed bearing reducers corrected to polymer |
| Native timeline feature-health inspection | 0 feature issues recorded |
| Reopened saved Fusion source | PASS; version 4; 1785 BRep bodies, 8 meshes, 333 native joints, 367 occurrences compared |
| Full F3Z package integrity and reference graph | PASS; native standalone reimport not performed |
| Final native handoff | PASS; saved version 4, unmodified, no pending snapshot; 23 axes / 367 occurrence placements retained |
| Individual concept-part STEP/STL file review | PASS; 10 pairs; watertight STL topology and millimetre scale/STEP structure; fit/material/strength remain unqualified |
| Independently reopened compact v26 archives | PASS — one upper-body module; waist/spine and both leg modules were not exported in this pass |

[Inspection records and source provenance](../../EVIDENCE.md) contain the individual JSON files, including rejected construction attempts and final check results.

Fresh post-recovery native checks use the actual current joint frames and occurrence poses for each bounded measurement. Other body angles are recorded before and after each test rather than assumed neutral. The 5 explicit paired-fixture records state their temporary fixed-ancestor and companion-output arrangements and verify measured output angles with the motor/rod loops retained. Original constraints are restored after testing. The final saved rest pose and standing height are verified separately.

The independently verified v25 compact upper archive is preserved as the previous checkpoint. A successful motion test establishes only the measured hierarchy and direction; sampled interference checks do not prove continuous swept clearance, cable travel, strength, thermal ratings or payload. Large arm/leg travel and hand/hip proximity require explicit limits and later full collision review.

| Purpose | Location |
|---|---|
| **Full assembly F3Z backup** | [Humanoid_complete_v26_full_20260930.f3z](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/Humanoid_complete_v26_full_20260930.f3z); 212,423,529 bytes; source v4 plus historical GWK dependency; file/dependency integrity PASS, native package reimport unperformed |
| Working full Fusion document | `Humanoid_complete_v26`; inspect the live document before further editing |
| Saved cloud revision | `Humanoid_complete_v26`, version 4; lineage `urn:adsk.wipprod:dm.lineage:mYos55HxTZOEOQZzqMfz1Q` |
| F3D artifact — independently reopened | [Upper_body_hands_head_v26.f3d](E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26/deliverables/Upper_body_hands_head_v26.f3d) |
| Individual concept-part STEP/STL exports | 20 files with [direct links and fit-trial scope](../../EXPORTS.md); forearm material unselected |
| Prior completed cloud save | Version 3 completed before hidden STS reference localization; preserved save record in the evidence index |
| Saved-source opening after restart | Version 4 opened by exact lineage; completion True; unmodified True; saved-source comparison PASS |
| Current design / procurement status | [BOM](../../BOM.md), [CSV](../../BOM.csv), [Native occurrence inventory](../../CAD_PARTS.csv) / [joint inventory](../../JOINTS.csv) |
| Local source construction/checks | `E:/Aditya/robot_sim/outputs/shin_cad_20260912/v26` |
| Original hand source and attribution | [Hand record](../../HAND_OPTIONS.md); `v26/references/AmazingHand` in output directory |



The native inventories include preserved source/legacy occurrences and passive/rigid constraints. They are separate from the procurement BOM: 333 native joints are not 333 controlled robot axes, and an occurrence is not necessarily an additional purchased part.

Successful native F3D exports retain the assembled hand reference meshes. The upper-body **STEP format is BRep-only and excludes those hand meshes**; original printable hand STEP/STL parts remain available in the source directory. New custom head/wrist/forearm geometry requires a fit trial. Manufacturing and module files are listed above only after an export is recorded; a file being written does not establish that Fusion can reopen it.

The primary full-assembly backup is the native **F3Z package**, which includes saved source version 4 and the historical GWK6010 model dependency. Independent checks verify its outer and nested ZIP CRCs, expected size/hash, declared root and every dependency member/ID. This is package-integrity evidence, not native standalone reimport or geometry/pose qualification of the imported package. The successful saved-source v4 comparison is separate. The failed standalone full F3D remains diagnostic history in the evidence index; its failed import does not establish whether meshes are present. Reopen comparisons include BRep volume/solid state, original hand-mesh names/node and triangle counts/bounds, native occurrence poses and ground states, and joint configuration/motion values. They do not hash every mesh vertex or establish dynamics. The previous compact v25 archives remain editable backups.

The qualified upper-body F3D uses the current source **assembly-context placements** as its baseline. A fresh read-only source capture corrected the earlier raw-component context mismatch; the existing native-imported archive then passed the original strict tolerances. The raw mismatch and its diagnosis remain in the evidence history. No CAD repair or new native import was claimed by that comparison.

## Documentation map and history

[BOM](../../BOM.md) is the buying/status view; the CAD inventory is the native component view. [Physical revision index](../../../lower_leg/README.md) links retained dated records. [Historical grant](../../../archive/LOWER_LEG_GRANT.md) preserves the earlier lower-leg project and prices. [Training file locations](../../../../Learning/HumanoidTraining/FILE_LOCATIONS.md) retain the separate Isaac pipeline and checkpoints.

These documentation edits are **local only**. No Git commit, GitHub push or online publication is part of this task. CAD revisions may be saved in the user's existing Fusion project as checkpoints; that is separate from publishing the repository.

## Decisions to confirm after review

1. Which exact microservo will the physical hand use: original SCS0009 or a measured MG90/SG90 redesign? The current hand CAD retains the original SCS0009 geometry. The sub-$100 target needs a priced prototype BOM.
2. Which elbow motor/reduction fits the supported generic output and 52×20 mm reservation? A wrist actuator is not included in this pass.
3. Which host, cells, BMS, converters and controllers will occupy the reserved electronics/pack spaces? Actual board dimensions determine ports, cooling and mounts.
4. Do purchased motor variants and transmissions match the planning torque/ratio assumptions? Measure final bearing seats, shaft fits, clamp sections and servo-horn interfaces before fabrication.
5. Which physical motion/payload tests should drive the new dynamics model? Older Isaac policies and torque tables are separate evidence and do not qualify this CAD.
6. Should the resting palms face inward toward the thighs or keep the imported fore/aft orientation? Wrist rotation and a powered wrist are not included in the current rigid connector.
7. Should the forearm forks use aluminum rails or printed PA12-CF? Their current `Concept metal` tag and aluminum-gray color conflict with an earlier plastic appearance; neither manufacturing choice is strength-qualified.
