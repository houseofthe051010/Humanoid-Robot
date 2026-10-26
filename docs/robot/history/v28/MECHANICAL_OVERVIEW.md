# Preserved mechanical architecture

This is the detailed physical v26/v27 mechanism reference retained in v28. The new casing geometry and its measured clearance belong in [Casing design](CASING_DESIGN.md). References to provisional cover retention remain applicable. See [Current build report](BUILD_REPORT.md) for the saved revision.


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
