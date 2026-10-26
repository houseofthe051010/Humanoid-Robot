# Current mechanical architecture — v29

[Build report](BUILD_REPORT.md) · [BOM](BOM.md) · [Joint map](JOINTS.csv).

## Legs, hips and structural waist

The serial anatomical chain remains pelvis → tilted hip pitch → hip roll → hip yaw → thigh → knee → shin → ankle pitch/roll → foot. Hip pitch follows the actual 25° tilted shafts. Measured native axes are retained, including mirrored signs; use JOINTS.csv and export metadata rather than the older simplified Isaac model's convention.

Four thigh oval rails are nominally 264.8 mm long, with 30 mm added below the knee motor region. Their lower endpoints and the knee output stay unchanged; the motor, thigh upper attachments, hips and pelvis move up 30 mm. The existing chain layout therefore needs a new center-distance/chain-length check. Planned reductions remain knee 8:1 internal ×2:1 chain, hip roll 15:1 and hip pitch 17:1; manufactured gearsets remain undesigned.

Both structural waist holders have clearance cuts covering conservative full-turn envelopes around the actual hip output forks and output-flange regions, with 3 mm added radial/axial room. Each holder remains one connected solid. The thicker structural envelope/ribs remain elsewhere, but removal of substantial material requires a fresh minimum-section and load review before printing. No printed strength is established by a clearance pass.

Waist articulation remains yaw → lower pitch → upper roll, driven by two 6010 motors through 26 mm cranks and M6 rods. The 35° rod-end tilt is the user's hardware assumption. Native motor/rod revolutes and ball closures remain separate from the three anatomical waist axes. Previous workspace samples belong to earlier revisions; changed packaging needs its own full combined-travel/cable checks.

## Torso, spine and electronics

The straight rearward 18×10 mm oval spine and original shoulder crossmember/clamps remain. Torso height decreases 20 mm relative to the raised pelvis, so shoulders/head move up only 10 mm. The retained spine wall is provisional and not strength-qualified. Battery remains 140×85×160 mm. The existing 150×86×93 mm enclosure above it reserves host, converters and interface space; board mounts, ports, cooling and cables await component selection.

Use regulated voltage rails matching actual servos/host/camera. The selected elbow servos require a 24 V rail; raw 12S exceeds their stated voltage range. The neck servo variant requires its own specified rail. Converter/regeneration design and current capability remain unselected.

## Shoulders and new servo elbows

Shoulder pitch retains external 6810 (50×65×7 mm) load-support bearings and actual supplier 6010 geometry. Pitch output carries an 80 mm OD perpendicular roll housing, with driven front flange and a fixed rear 25 mm journal/6005 (25×47×12 mm) support. External bearings carry arm loads; motor/gear torque capacity remains a separate requirement. Supplier mounting is eight M2.5 holes on 40.5 mm PCD; output is six M3 on 25 mm PCD.

Upper arms now span 275 mm from shoulder roll to elbow. Each elbow uses a double-shaft servo as the joint: case fixed in upper-arm cradle, both outputs rotating the 250 mm forearm fork. The servo's long case dimension points toward the upper arm, with its shaft transverse to the arm's bending plane. No separate generic elbow motor cavity, 25 mm output shaft, elbow 6005 pair or floating cosmetic cheek remains.

The user selected RDS51160 24 V / 160 kg·cm class hardware. Geometry is the authorized RDS51150 proxy from Downloads: 65×30×48 mm case, 65×62×30 mm complete reference envelope including outputs. The 150 kg and 160 kg units must not be assumed electrically identical. Modeled 36 mm horn PCD and 4.1/3.1 mm bores are packaging provisions; measure actual splines, horns, fasteners and case before manufacture. Continuous torque/current/thermal ratings and limits are pending.

Forearm forks retain the distal four-M3 24×18 mm interface. Wrist adapters retain the hand's three-M2.5 42 mm PCD and 18 mm cable bore. Hands are full-scale AmazingHand references with eight SCS0009 servos per hand; hands/wrists stay rigid in this simulation pass. Source/license and MG90 substitution limits are in [Hand options](HAND_OPTIONS.md). The old 6° shoulder-abducted rest is baked into revised geometry; exported q=0 is this pose. Old neutral hand-clearance numbers do not qualify the resized arms.

## Neck, head and camera

Two actual-size Feetech STS3215 references provide yaw/pitch. The 6005-supported yaw output carries the lower pitch cradle and external split case clamp; driven/passive pitch horns support the printed head from both sides. Split head shell, open camera visor and Yahboom AI VIEW/Astra SV1301S U3 official camera geometry are retained. See v26 history for original clamp/head construction details; exact variant, print fit, cable travel and neck dynamics remain pending.

## Organization and export

Forty-two top-level rigid-link/mechanism groups contain 372 occurrences. Source part names survive under their physical owner; fasteners and covers are grounded to that parent. Forty-seven native constraints retain 23 anatomical revolutes plus passive/drive revolutes and six ball closures. Hidden joint datum bodies are construction geometry and excluded from BOM/mesh export. Legacy prototypes and source history remain in the preserved input/v28, rather than cluttering the current fabrication assembly.

URDF represents 24 rigid links and 23 anatomical outputs. Native differential closure rods and drive axes remain in F3D; URDF carries their packaging geometry on mounting links and does not infer a constant transmission mapping. CAD front −Y maps to Isaac +X through a proper rotation. Source left/right names are retained. Appearance colors describe intended roles; inherited physical-material/density values are not a measured mass model.
