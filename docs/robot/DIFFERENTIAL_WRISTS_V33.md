# Differential wrists v33 — October 23, 2026

Both wrists now use two head-type Feetech STS3215 servo references, staggered **48 mm along the forearm**. Spur idlers connect the offset motors to a compact bevel differential. Existing hands remain full size with their mirrored three-M2.5 / 42 mm PCD interfaces. The original forearm skin envelope is retained with small round nut-access ports; its internal corners and one cradle connector were relieved to fit the drive.

The fixed cassette is 63 mm wide and 46 mm deep before local skin relief, with a 145 mm axial envelope. Retained original forearm rails lie outside it; the new wrist output is placed within the original hand mounting span. Four STS3215 servo references are added, for six including the two head servos. Exact purchase variant and horn drill fit still need hardware confirmation.

## Saved work

- Native Fusion document: **Humanoid_differential_wrists_v33**, saved cloud version 3; `urn:adsk.wipprod:dm.lineage:TN2NRtV1SyiCdTDNvtloOQ`.
- [Full native F3D](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist33/deliverables/Humanoid_differential_wrists_v33.f3d), 294,525,001 bytes.
- SHA-256: `cf5748627bc2cd0a25889c2285a6cd00b0ef7349d01aeef0e8b994660b7d2b23`.
- Twenty-two [STEP subassemblies](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist33/deliverables) accompany the complete native model. STEP does not retain the native motion joints.
- [Input v32 cloud version 4 preserved](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist33/Input_latest_v32_version4_preserved.f3d), plus [source hash](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist33/input_sha256.json). This is newer than the old version-2 report.
- [Drive layout, fixed cassette hidden for clarity](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist33/wrist33_drive_layout.png), [cassette and hand](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist33/wrist33_isolated_assembly.png), [combined 20-degree pitch / 30-degree roll](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist33/wrist33_pitch20_roll30.png), [complete robot](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist33/robot_with_differential_wrists.png).

## Verified

| Check | Result and scope |
|---|---|
| Connected active solids | 88 active inspected solids; no disconnected lumps |
| Neutral interference | No detected inter-group solid intersections above 0.02 mm³; both forearm skins visible |
| Selected moving clearances | 18 solid-geometry poses, including +/-35° pitch and +/-60° roll combinations; no detected clashes |
| Native motion | 12 driven poses; servo cases and other robot roots remain fixed during these tests |
| Physical frames | Independent combined-pose matrix reconstruction agrees within 1e-5; see native_frame_check.json |
| Tooth geometry | 13 samples across a full tooth period have zero solid overlap for the prototype bevel pair |
| Native export | Archive CRC passes; independent Fusion reopen checks 117 new components and 87 joints without discrepancies |

The 65 original joint definitions remain, with 22 added wrist constraints (20 revolutes and two rigid frame attachments). Initial v32 cached placements normalized to the authored neutral assembly during Fusion recomputation; the exact pre-edit input is preserved separately. The motion tests compare against the resulting neutral assembly, not a false claim of bitwise preservation of every initial cached placement.

## Mechanical details and limits

Each input uses 24-tooth module-1 spurs. One motor uses one idler and the other three, giving two and four meshes respectively, both 1:1. The main cross-axis has a centrally supported 6 mm steel sleeve surrounding an M3 clamping bolt. Idlers use two-sided M3 supports with separate running sleeves and retaining nuts. Two spaced 608 bearings support the rolling output; MR128 references support the carrier. Retainers and service access are modelled.

In outward input-axis coordinates, `pitch=(A-B)/2`, `roll=-(A+B)/2`. Native revolutes are coordinated by [pose.py](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist33/pose.py); [Wrist33Pose.py](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist33/Wrist33Pose.py) is a Fusion CAD-only input dialog. Gear contact is **not** solved automatically by Fusion. No physical servo command is sent by these scripts.

The new tooth form is a faceted virtual-back-cone prototype, not a certified production bevel set. Selected clearances do not prove continuous whole-body clearance; mesh-hand collision is not part of the solid Boolean sweep. Hardware fit, tooth wear/backlash, shaft bending, fastener preload, cable service loops, material/print process and payload remain to test. A side cable exit is provided instead of claiming the old unobstructed 18 mm central passage survives through the rolling shaft. Stall torque is not a continuous wrist capacity.

No training asset, policy, native motor cap or unrelated FOC controller source was changed. No Git commit or push was made.

## Research references

- [Source Robotics differential wrist](https://github.com/Source-Robotics/Differential-robot-wrist): topology and packaging reference; their BLDC fixture was not copied as a finished design.
- [Feetech C018 listing](https://www.feetechrc.com/products.html?keyword=STS3215): head-type 12 V / 30 kg·cm nominal stall variant.
- [KHK gear dimensions](https://khkgears.net/gear-knowledge/gear-technical-reference/calculation-gear-dimensions/): pitch-cone conventions.

[Work log and repaired attempts](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist33/CHANGELOG.md) · [Native reopen](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist33/native_reopen.json) · [Clearance repairs](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist33/clearance_repairs.json) · [Sweep](E:/Aditya/robot_sim/outputs/shin_cad_20260912/wrist33/wrist_sweep.json).
