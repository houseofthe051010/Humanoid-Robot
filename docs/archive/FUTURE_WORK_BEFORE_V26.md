# Earlier open design questions

Historical text preserved on 2026-09-30. [Current whole-robot report](../robot/BUILD_REPORT.md) supersedes its current-state statements.

# Future work and questions to investigate

## September 29 — v24 upper-body follow-up

The electronics bay is now modeled and spine-mounted in [v24](../lower_leg/TORSO_SHOULDERS_V24.md), along with shell attachments, shoulder/neck bearing envelopes, roll placeholders and forks to the elbows. Full working Fusion document: `Humanoid_shoulders_electronics_v24`.

- Select the actual computer, power converter and control electronics; adapt the 144×80×87 mm main cavity with standoffs, ports, cooling and wiring.
- Select shoulder motors/transmissions, then finalize the 80×50 mm roll housings, pitch coupling, removable inboard bearing collar, tolerances and bearing retention. Complete the neck servo coupling and outer-race retention.
- Detail shell print/service splits and fasteners; design elbows/forearms and route cables. Qualify spine, frame, forks and bearings for actual loads. Current checks establish sampled geometry and native joint motion only.

## September 21 — v15 priorities

- Resolve encoder placement: the new rear slide sleeve occupies the old5mm reservation.
- Select print material/orientation, slide fit, axial retention and actual assembly sequence. Check plastic creep, motor heat, sleeve stress and the curved connections under gearbox reactions.
- Finalize waist yaw support bearings, bolt interfaces and motor/driver cooling. Add proper pelvis/hip joints and validate sweeps before treating the waist as articulated.
- Choose actual110×50 hip-pitch motors and recheck the pockets, wiring, attachment access and tolerances. The current motors are envelopes.
- Detail the waist seam fasteners and fastening bosses, service access and printed tolerances.
- Earlier chain questions remain deferred; the user's current scope explicitly excludes further chain calculations or neighboring bracket redesign.


## September 21 — v13 priorities

[V13](../lower_leg/UPPER_LEG_V13.md) supersedes the v12 case and chain packaging below. It uses a106ID/110OD aluminum tube, a nominal13 mm gearbox reservation, and approximate8T/16T sprockets at129.4 mm centre distance. The33 mm reservation and unspecified chain circles below are historical.

- Select an actual40H chain and connecting link; measure total pin width and plate height against the provisional22×12.2 mm envelope. Resolve discrete link count and tension adjustment: the present centre distance is a layout value, not a cut-chain specification.
- Review8T engagement, polygonal speed variation, tooth/root strength, wear and shock load with the chain supplier. At this geometry the small sprocket wraps about166° (approximately3.7 teeth). The requested tooth form is an approximate CAD visualization only. Consider a larger driver if the load review requires it.
- Detail the custom drive-side aluminum bearing pedestal: cartridge identification, seat tolerance, axial shoulders/retention, M4 engagement, machined wall thickness and load path. It replaces one stock outer casting per leg; retaining its bearing centre does not establish pedestal strength.
- Finalize the output carrier/bearings, compact8T hub torque transfer,6 mm support pin,6.395 mm knee standoff and fourM3 ties/two6 mm dowels. Calculate torque and chain loads before approving these interfaces.
- Confirm that the motor's photo-estimated dimensions fit the106 mm tube bore. Design final gearbox depth after physical inspection; the current13 mm nominal reservation is not an assertion that the desired planetary will fit.
- Resolve inherited approximate shaft-to-bearing geometry and perform toleranced assembly checks. Neutral chain clearance and sampled CAD motion are not impact, fatigue or FEA validation.
- Motor lowering adds space near yaw, but driver PCBs, heatsinks, connectors and wiring still need measured envelopes.

September 20 v12 update: [paired-leg revision](../lower_leg/UPPER_LEG_V12.md) supersedes the old fairing concept. The circular case now bridges both rails, reserves33mm for the gearbox and carries an opposite6mm support-pin reference. Q01–Q03 replace the rough hip blocks as CNC concepts. Next, verify ring-gear reaction/retention, output coupling and bearings, the compact opposite support section, clamp preload/crush sleeves, actual motor hole/thread data and CNC access/split strategy. Confirm the assumed33mm cavity after measuring the motor and removable prop features. The260mm leg spacing has a neutral packaging basis; full hip sweeps, pelvic structure and gait may revise it. Neither the6mm support pin nor the existing8mm joint shafts have been qualified by these CAD changes. The historical questions below remain open unless explicitly superseded.

September 20 update: [8 mm ankle and knee shaft screen](../lower_leg/SHAFT_STRENGTH_8MM.md) compares actual bearing spans and edge/uniform block loading. Resolve full ground/actuator reactions and reinforcement contact before selecting final shaft diameters; geometry-only checks do not qualify the current shafts for impacts.

Updated 2026-09-19 for the v11 compact upper-leg layout. These are open questions, not verified capabilities or purchased-part specifications. See [current upper-leg layout](../lower_leg/UPPER_LEG_V11.md), [historical v10](../lower_leg/UPPER_LEG_V10.md), and [existing knee shaft screening](../lower_leg/KNEE_STRENGTH_V9.md).

V11 shortens the thigh reference to 320 mm, lowers the motor 85 mm, sets the requested pitch tilt to 25°, adds a distinct roll envelope and introduces curved protective fairings. The fairings need print-fit, attachment, ventilation and wall-thickness review. They provide no new strength qualification. The shorter thigh and Z500 mm intermediate-shaft reference further constrain transmission packaging.

## DJI10018 motor and internal planetary

- Measure the actual 77 KV motor: usable internal diameter/depth, rotor/stator interfaces, shaft/bearing geometry, rear projection, four mounting holes and allowable thread engagement. The present 105 mm OD, 30 mm body and 40 × 66 mm hole pattern remain estimates. Verify which prop features can be removed without damaging rotor retention or balance.
- Can a 6:1 or preferred 8:1 planetary fit inside the available cavity? For a simple fixed-ring, sun-input, carrier-output set, reduction is `1 + Nr/Ns`. An 8:1 set requires `Nr = 7 Ns`, and its planet tooth count is `(Nr - Ns)/2`. Check assembly phasing, planet-to-planet clearance, contact ratio, undercut/profile shift and tool access before choosing teeth/module. [KHK planetary examples](https://khkgears.net/pdf/2025/internal-gears.pdf).
- **Can CNC-machined 7075 aluminum survive the small sun gear required by the 8:1 arrangement?** Calculate tooth-root bending, contact stress, fatigue, wear, face width, planet load sharing and shock overload. Also check ring retention, planet pins/bearings, carrier stiffness, lubrication and heat. Compare 6:1 against 8:1; aluminum availability does not establish strength. Do not substitute a tensile-strength check for gear tooth/contact calculations.
- Establish a continuous and transient torque-speed envelope for the actual motor/controller/gearbox. The user's reported 100 A for 180 seconds has not been independently verified. It does **not** establish a permissible 140 A burst for less than one second. Identify whether each current value is DC-bus, phase RMS, phase peak or controller q-axis current; determine winding resistance, cooling conditions, saturation and controller limits. Current conventions affect the torque constant. [Maxon current definitions](https://support.maxongroup.com/hc/en-us/articles/360006288554-Strength-of-BLDC-EC-motor-with-sinusoidal-commutation).
- Evaluate 12S versus 13S only with actual cell chemistry, full-charge voltage, sag, controller voltage margin and regenerative braking. More voltage primarily changes available speed/headroom; it does not independently validate torque at a chosen current.

## Recorded torque assumptions

The planning assumption is **15 N·m at the motor shaft**, not a tested result. Multiplication below is ideal and excludes all losses:

| Internal reduction | Chain reduction | Combined reduction | Ideal knee torque at assumed 15 N·m |
|---|---|---|---|
| 6:1 | 2:1 | 12:1 | 180 N·m |
| 6:1 | 2.5:1 | 15:1 | 225 N·m |
| 8:1 | 2:1 | 16:1 | 240 N·m |
| 8:1 | 2.5:1 | 20:1 | 300 N·m |

The optional final 1:1 chain adds no ideal torque multiplication. With two chain stages, delivered torque is `Tmotor × planetary ratio × primary ratio × ηplanetary × ηchain1 × ηchain2`. Speed falls by the combined reduction; motor inertia reflected to the knee scales approximately with its square. Higher reduction is therefore not an unconditional improvement for a backdrivable leg.

Under compatible ideal SI conventions, `Kt = 60/(2π × 77) ≈ 0.124 N·m/A`; 140 A would correspond to approximately 17.4 N·m before losses/saturation. This arithmetic is not a measured motor constant or a current authorization, and must not mix battery current with torque-producing phase current. At unchanged winding resistance, 140 A gives 1.96 times the copper heating of 100 A; burst acceptability still requires the actual initial temperature and thermal/transient limits. [Maxon motor heating](https://support.maxongroup.com/hc/en-us/articles/360004427413-On-the-heating-of-motors-in-hand-held-tools).

## Chain, intermediate shaft and encoder

- Compare direct 2:1 or 2.5:1 to the preferred packaging option: **2.5:1 to an intermediate shaft, then 1:1 to the knee**. The reference circles are not sprocket outside diameters or selected tooth counts. Choose chain pitch, integer tooth counts, minimum driver teeth, wrap, chain length, adjustment/tensioning, guards and lubrication together.
- Check 7075 versus 6061 sprocket bending, fatigue and wear. Compare the cost of commercial sprockets with a separately drilled mounting pattern or bolt-on hub, rather than requiring custom sprockets. No supplier or price has been selected.
- Resolve axial spacing between the two chain planes, sprocket hubs and bearing supports. The intermediate shaft needs support for chain force and overhung moments, preferably on both sides. The current circles do not prove that a complete chain assembly fits. Provide removable access and enough room for both tension adjustment and assembly tools.
- The proposed intermediate-shaft encoder can simplify packaging, but does not directly measure knee backlash, chain stretch or compliance downstream of it. Decide whether final knee-side sensing is still needed for control and calibration.
- Confirm the internal planetary output interface and which motor face provides the final output. The v10 layout assumes the drive faces left and the stationary four-hole face faces the right rail. Rotor prop posts are retained only as uncut reference geometry.
- Confirm that a real encoder fits in the provisional 5 mm axial space behind the rear hub, with magnet spacing, PCB/connector and cable bend clearance. The CAD reserves only a 28 mm diameter envelope there.

## Printed motor shell and thigh rails

- Check the four actual mounting threads and engagement before using the provisional M4 hardware. Determine whether the motor bosses are threaded or through holes.
- Validate the 8 mm printed mounting web, its stress concentrations and the split clamp's slip resistance, rail crushing, fastener preload, printed-material creep and moisture/temperature sensitivity. Two clamps on one thin-walled rail do not establish adequate torque capacity. Consider a bridge to the other rail or metal reinforcement if the load path requires it.
- The fixed planetary ring and motor housing can transmit substantial gearbox reaction into the shell. Do not size this structure using only 15 N·m raw motor torque if it also supports the gearbox reaction. Include chain loads, motor mass, landing acceleration and off-axis moments.
- Specify filament grade, print orientation, perimeters, conditioning and insert/nut design. 100% infill does not remove directional strength or creep. Use representative coupons and load tests alongside FEA.

## Hip and overall robot

- **Can the GWK7010's own bearings support the leg, or is an independent structural bearing pair needed?** Obtain radial/axial/moment ratings and stiffness, then include foot contact forces, leg inertia, hip offsets and impacts. Its predicted 40–50 N·m peak remains untested.
- Determine hip pitch motor model, required reduction and direction of tilt. V11 uses the user's requested 25° magnitude. A separate Ø90 × 36 mm roll envelope is present, but its motor and the serial order/spacing of all three hip axes remain undecided.
- Reconcile the provisional 320 mm thigh and 757.6 mm standing hip height with a 1600.2 mm full robot. Finish pelvis, torso, neck and head dimensions; check left/right-leg clearance and full hip motion before fixing the proportions.
- Replace reference crosshead/pelvis blocks with a real load path. They currently have no verified bearing seats or attachment hardware and cannot be treated as manufactured structure.
- Continue knee shaft redesign: the existing 8 mm shaft was **not** validated for jumping. The earlier favourable ordinary-steel 5× single-leg landing screen predicted about 441 MPa bending stress versus an assumed 250 MPa yield. New chain forces and torque transfer need a revised joint free-body diagram. See [v9 knee calculation](../lower_leg/KNEE_STRENGTH_V9.md).
- After interfaces stabilize, split lower leg, upper leg, leg pair, pelvis and upper body into linked Fusion subassemblies with explicit interface datums and revision ownership. This layout does not yet restructure the whole robot or export a new Isaac articulation.

## V15 waist structural follow-up

See [PA12-CF waist prediction](../lower_leg/WAIST_PA12CF_STRENGTH_V15.md). Investigate thicker hip rear seats (3 to approximately 6 mm), blended roots, positive motor torque/pull-out retention, seam bolts and yaw-bearing load capacity. Confirm selected motors, completed mass, conditioned print properties and creep/fatigue before assigning an operating load. No geometry changed in this assessment.

## V16 articulated waist follow-up

The [V16 yaw/pitch/roll prototype](../lower_leg/WAIST_GIMBAL_V16.md) connects the fixed 7010 mounting annulus to the casing and the moving output to a CNC orthogonal pitch/roll gimbal. Verify whether the 7010 output bearings can carry torso axial, radial and overturning loads; if not, design an independent yaw bearing path. Check the exact fixed and rotating motor-hole threads, fastener engagement and output torque transfer. Select pitch/roll pin steel and bushing material, fit, wear life, retention, lubrication, and load rating from a free-body diagram including impact and differential actuator reactions. Measure the spine oval wall and detail transverse fasteners with crush protection. Add differential drive tabs, stops, wiring and motor-driver packaging, then run full-range collision and structural checks. The current 10 mm pitch and 8 mm roll pin sizes are geometry references, not qualified shaft diameters.

## V18 current hip and waist follow-up

[V18](../lower_leg/HIP_WAIST_V18.md) supersedes the v16 interface assumptions and axis order. Both hip pitch and roll use the estimated 105 mm DJI10018 reference inside an estimated housing; no GIM10015 is selected. Design the planetary and actual output before freezing the current housing envelope or the provisional 50 mm flat roll openings. The narrow roll journals and 40x52 bearing references were removed: select new bearings, retaining geometry and output coupling to suit that interface. The larger opening itself is not a torque rating. Verify the estimated 40x66 motor rear pattern and removable prop features on the real motor.

The 7010 mount uses eight small holes on 48 mm PCD; the 40.5 mm PCD screws hold the gearbox together. Its output uses six small holes on 25 mm PCD, not the three larger locating features. Verify actual thread engagement before manufacture. Hip yaw now has a separate 6007 envelope above each lowered motor; bearing fit, retention, torque transfer and structural rating remain unqualified.

The nylon waist has lower roll and upper pitch, nominal 10/8 mm pins with M3 reinforcement references, two M6 rod ears, and two inward-facing GIM6010 placement references. Determine differential crank radius, anchor geometry, rod-end angular limits, full travel, motor mounting and driver/cable routing. Check conditioned PA12-CF properties, pin/bushing wear and the proposed 20 N·m rod-load path before deciding whether the base or other interfaces require metal. The previous v15 mass/strength estimate does not qualify the changed v18 geometry.
