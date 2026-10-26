# Updated assumption: solid-filled waist interior

The user subsequently specified that the hollow interior should be filled with PA12-CF, retaining motor pockets and functional openings. The hollow-shell results below are historical and are not the prediction for this solid-filled concept. This means adding material to the CAD cavity, not merely selecting 100% slicer infill for the existing walls.

**Quick prediction:** a substantially solid PA12-CF waist is likely adequate for the expected static weight of this robot. With 10–20 kg above yaw, the completed lower-body budget puts the robot roughly in the 29–40 kg range after the extra waist material. The remaining concerns shift toward motor attachment, positive retention, seam connections and motor bearings. This is a concept prediction, not an impact qualification.

For a numerical sensitivity, assume the fill provides an equivalent **10 mm effective backing section** at both motor supports, continuously joined to the surrounding material. This is an analytical assumption, not a measured minimum thickness of a revised CAD model. Retaining the same intentionally conservative annular-strip model and stress criterion:

- Hip vertical-reaction screen: 232 × (10/3)^2 = approximately **2,576 N per hip**.
- Central yaw-seat screen: 340 × (10/5)^2 = approximately **1,360 N**.
- With an illustrative 15 kg upper body, approximately 2.5 kg solid waist including motor, and an 8.2 kg hanging leg, one-foot static hip reaction is approximately **252 N**; a 3× illustrative load is **756 N**. Yaw demand at 3× is approximately **451 N**. These load components are below the assumed 10 mm-backed-section screen.

This supports the favorable prediction for a filled waist, but the factors above do not include combined actuator torque, seam failure, creep or local load introduction. Do not interpret 2,576 N as a tested hip or robot load rating. Filling cannot increase the space between two motor pockets; any narrow remaining ligament still needs to exist in the final geometry. The split casing still requires structural fasteners.

A quick integration of the coded outer loft, minus approximate motor envelopes, suggests approximately **1.8–2.6 kg of plastic** for the filled casing; its central 7010 adds approximately 0.33 kg. This is an envelope estimate, not an exact Boolean volume. Relative to the original 0.685 kg plastic shell, add approximately **1.1–1.9 kg**. The completed lower-body central estimate becomes about **19 kg**; the earlier broad planning uncertainty remains. No Fusion inspection or CAD change was performed for this update.

Preferred material and orientation remain Fiberon PA12-CF10 and each half's mating face down. Print the load-bearing fill densely with continuous connections to the motor seats; isolated sparse infill would not meet this assumption.

---

# V15 waist: quick PA12-CF mass and strength prediction

2026-09-22. Geometry unchanged. This is a short-term analytical screen, not FEA, a measured failure load, or an approved operating rating.

## Prediction

The broad shell is substantial; the local motor seats and unfinished attachments govern. With an assumed 15 kg above the waist yaw, two-foot standing looks plausible. One-foot standing is borderline in the more conservative hip-seat model. Impacts are not supported by this calculation. Improving the 3 mm hip rear seats is more useful than thickening the whole casing.

## Mass budget

| Assembly | Estimated mass |
|---|---:|
| Each leg, existing geometry plus motor allocations | 7.33 kg |
| Waist plastic, both halves | 0.685 kg |
| Waist plastic plus central 7010 | 1.02 kg |
| Both legs and waist, modeled budget | 15.68 kg |
| Missing lower-body mechanisms/electronics/hardware allowance | 1.80 kg |
| Working completed lower-body budget | **17.48 kg**, planning range **14.48–21.10 kg** |

This excludes the torso and battery. The upper-body mass cannot be deduced from leg mass. Hip pitch and roll are unselected: 1.0 and 0.75 kg per leg are explicit allocations, with ranges 0.7–1.3 and 0.5–1.0 kg. Each 7010 uses a provisional 0.334 kg allowance (manufacturer mass not independently confirmed); electronics are allocated rather than treated as solid blocks. Steel, aluminum, PA12-CF and TPU use 7.85, 2.70, 1.06 and 1.20 g/cm³. Mixed bearing/shaft components are separated by body. Complete motor masses replace motor geometry; their duplicated output geometry is not counted twice.

The [official DJI T30 specification](https://www.dji.com/t30/specs) gives 756 g for its 100×18 mm, 77 KV motor. This is the reference for each DJI motor; the purchased variant and any material removed still need confirmation.

The 1.8 kg allowance comprises two knee gearsets 0.6 kg, chains 0.4 kg, missing drivers/encoders/wiring 0.5 kg, and bearings/retention/seam hardware 0.3 kg. These are planning allocations, not a chain-size calculation. Ranges are sensitivities, not statistical confidence bounds.

## Material and printing choice

**Choose Polymaker Fiberon PA12-CF10 as the calculation/reference filament.** It has a strong, explicitly documented printed layer-direction result. This is not a claim that it beats every PA12-CF product in every loading direction.

| Candidate | Published tensile data | Interpretation |
|---|---|---|
| Fiberon PA12-CF10 | Dry XY/Z 77.4/52.2 MPa; wet XY/Z 71.7/42.1 MPa | Selected for documented directional and conditioned data |
| Raise3D Industrial PA12 CF | Dry XY/Z 72/43 MPa; conditioned XY/Z 73/42 MPa | Similar conditioned layer strength; conditioning differs |
| Fiberlogy PA12+CF15 | 120 MPa, orientation unspecified on product page | Cannot treat this as printed layer-bond strength |

Sources: [Fiberon TDS V1.1](https://fiberon.polymaker.com/wp-content/uploads/TDS_FIBERON-PA12-CF10_V1.1_EN.pdf), [Raise3D TDS V2](https://s1.raise3d.com/2022/02/Raise3D-Industrial-PA12-CF_TDS-V2.0.pdf), [Fiberlogy product specifications](https://fiberlogy.com/en/filaments/nylon-en/nylon-pa12cf-en/). Different test conditions prevent a definitive universal strength ranking.

Print each front/rear half **flat mating/seam face down**, with the cavity facing upward: printer build direction is robot fore/aft (±Y), and robot width X and height Z lie in the layers. This is the preferred orientation for the dominant vertical and cross-waist loads, not a proven optimum for every torque. Use dense walls/seats (100% local infill), ample continuous perimeters, a wear-resistant nozzle and dry filament. The selected datasheet's coupons used 300°C nozzle, 50°C bed and 100°C/16 h annealing. Its product page lists a different annealing duration; the calculation references the TDS condition. Check fits after annealing. Fore/aft loads, seam opening and some motor-seat bending still load layer bonds.

## Geometry and equations

V15 has nominal 5 mm shell section offsets, 6 mm radial pitch barrels, **3 mm pitch rear annular seats**, and a **5 mm yaw bottom annular seat**. Pitch motor OD is 110 mm and axis tilt 25°. Pitch centers are X±52 mm; leg centers ±130 mm are not the same datum. Nominal offsets are not a minimum-wall certification.

A nominal screening stress of **42.1 / (3 × 2) = 7.02 MPa** is used: wet layer-direction typical tensile strength, factor 3, and additional local factor 2. These are chosen screening factors, not manufacturer allowables or a creep/fatigue model.

For a radial cantilever-strip approximation of an annular seat:

`stress = 6 F L / (2π b f t²)`

Here b is outer support radius, t thickness, f the small area correction for the seam, and L the load lever arm. One case puts circumferentially distributed load at the inner rim (long lever); another distributes pressure over the annulus (shorter lever). Neither represents concentrated bolt loading, and the first is conservative only within this idealized support model.

| Seat | Radii / thickness | Inner-rim screen | Distributed-pressure screen |
|---|---|---:|---:|
| Central yaw | 18–39 mm / 5 mm | 340 N downward | 774 N downward |
| Each hip rear seat | 18–55 mm / 3 mm | 98 N axial | 236 N axial |
| Hip equivalent vertical reaction, axial part = R sin25° | same | **232 N per hip** | **558 N per hip** |

The hip numbers check the axial rear-seat bending component only. Radial contact, motor reaction torque, retention and combined stresses still require completed interfaces. The large difference between the two pressure assumptions is why these are not actual failure-load predictions.

Measured broad-shell section moduli over the sampled hip region are approximately 35,300–129,000 mm³. A gross beam screen gives 248 N·m at the smallest sampled value versus roughly 24 N·m in the 15 kg upper-body static example. This supports the judgment that local seats deserve attention first; it does not prove all intervening necks, seam attachments or buckling modes pass.

## Loads, including the hanging leg

Let U be mass above yaw, W = 1.02 kg waist, S = 8.23 kg completed swing-leg allocation, and D an illustrative effective vertical load multiplier (1 = static; 3 = three times the static force, not a specified jump height).

- Two-foot stance, each hip: `R = D g (U + W)/2`.
- One-foot stance, supporting hip: `R = D g (U + W + S)`; the opposite hip carries the hanging leg downward.
- Yaw bottom seat: approximately `F = D g (U + 0.334)` including the motor allowance.

The supporting leg's own weight is not added again at its hip: it is below that interface. An accelerating/swinging leg requires its own actual acceleration and inertia, not necessarily the same D.

| Upper body U | Static yaw-seat load | Static hip, two-foot (each) | Static supporting hip, one-foot |
|---|---:|---:|---:|
| 10 kg | 101 N | 54 N | 189 N |
| 15 kg | 150 N | 79 N | 238 N |
| 20 kg | 199 N | 103 N | 287 N |

At U = 15 kg, the conservative inner-rim hip screen is 232 N versus 238 N demanded in single support. At D = 3, the one-foot hip demand rises to 714 N and yaw demand to 451 N. The current local-seat model does not pass those cases. Under the alternative distributed-pressure assumption, static performance is better, but that contact condition is not established.

Do not interpret the ratios as a certified payload rating. The four M4 seam provisions have no selected fastening arrangement; motor-shaped pockets do not establish torque transfer or positive pull-out retention. In particular, the hanging-leg load reverses the hip load direction. The yaw motor's own bearing capacity is separate from the plastic seat. Creep, heat, repeated loads, impact waveform and motor torque are unqualified.

## Most effective next change

Increase the hip rear-seat thickness from 3 to about 6 mm and blend it into the barrel with generous fillets, then detail positive motor retention and seam hardware. In this simple bending model, doubling thickness gives four times the seat capacity; that is a scaling prediction, not validation of a revised casing. No CAD changes were made.

## Reproduce

[evidence/waist_strength/mass_components.csv](evidence/waist_strength/mass_components.csv) lists every mass entry. Run `python evidence/waist_strength/mass.py` and then `python evidence/waist_strength/calculate.py`. Geometry inputs and calculation outputs are alongside them. The initial temporary-body physical-property API returned zero mass, so only the subsequent verified section measurements are used. The source robot geometry was not edited.
