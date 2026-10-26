# Current physical robot BOM — v29

[Build report](BUILD_REPORT.md) · [CSV](BOM.csv) · [CAD inventory](CAD_PARTS.csv) · [Actuator calculations](ACTUATOR_CALCULATIONS.md).

Quantities describe current CAD or explicitly planned hardware. Component references must not be counted twice. Prices remain blank except the dated September 29 camera quote. This is not a current purchasing quotation.

September 30 motor assumptions are configured in the isolated physical simulation. Gearset designs, thermal ratings, exact motor variants and measured elbow continuous duty remain to qualify. The additional shoulder-pitch 4:1 stage is planned hardware, not new CAD. The active casing set has 51 cosmetic pieces and two structural waist halves; old generic elbow bearings and guards are excluded.

## Mass planning

[Mass estimate](MASS_ESTIMATE.md) / [part basis CSV](MASS_BASIS.csv): conservative total 34.46 kg with battery; 33.98 kg using the official 400 g complete-hand value. Motor variants, printed fill, bearings and unmodeled gearset/electronics allowances are explicit estimates. The complete hand mass includes its servos; do not add the separately listed servo masses again. This mass report does not change BOM quantities or qualify a purchase.

## Actuation

| ID | Item | Quantity | Status |
|---|---|---:|---|
| ACT-01 | GWK7010 motor reference | 7 | Modeled; exact purchase variant to confirm |
| ACT-02 | Casing-free GWK6010-8 motor | 6 | Actual supplier CAD; planned variant |
| ACT-03 | DJI10018 77 KV motor | 6 | Estimated geometry; user-selected motor type |
| ACT-04 | Feetech STS3215 12 V / 30 kg.cm dual-shaft serial servo | 2 | User-imported CAD; verify 12 V variant before ordering |
| ACT-05 | ANNIMOS/DSSERVO RDS51160 double-shaft 24 V elbow servo | 2 | User selected; RDS51150 CAD dimension proxy |
| ACT-06 | AmazingHand mechanisms (servos listed separately) | 2 | Official source design selected for CAD integration; hardware not purchased |
| ACT-07 | Feetech SCS0009 microservo (original hand design) | 16 | Reference choice; MG90 replacement not validated |

## Bearings

| ID | Item | Quantity | Status |
|---|---|---:|---|
| BRG-01 | 6810 / 61810 bearing, 50 x 65 x 7 mm | 2 | Nominal envelope modeled |
| BRG-02 | 6005 bearing, 25 x 47 x 12 mm | 3 | Nominal envelope modeled |
| BRG-03 | 6007 bearing, 35 x 62 x 14 mm | 2 | Retained nominal envelope |
| BRG-04 | 61810 / 6810 bearing, 50 x 65 x 7 mm | 4 | Retained nominal envelopes |
| BRG-05 | Hip-pitch bearing envelope, 40 x 52 x 7 mm | 4 | Retained dimension reference; model TBD |
| BRG-06 | 8 mm ankle/knee/heel bearing positions | 16 | Legacy reference; final stock blocks vs bare bearings TBD |

## Cosmetic casings

| ID | Item | Quantity | Status |
|---|---|---:|---|
| CAS-01 | Split torso band skins, including four revised lower motion hems | 12 | Active v29 concept; print/retention pending |
| CAS-02 | Upper-arm skins | 4 | Active v29 concept; print/retention pending |
| CAS-03 | Forearm skins | 4 | Active v29 concept; print/retention pending |
| CAS-04 | Thigh skins | 4 | Active v29 concept; print/retention pending |
| CAS-05 | Split shin/calf skins | 8 | Active v29 concept; print/retention pending |
| CAS-08 | Torso identifier and two calf marks | 3 | Active v29 concept; print/retention pending |
| CAS-09 | Hip roll-case front caps | 2 | Active v29 concept; print/retention pending |
| CAS-10 | Split tapered pelvis front fairing | 0 | Superseded; hidden source geometry preserved |
| CAS-11 | Two knee and two ankle front guards | 0 | Superseded; hidden source geometry preserved |
| CAS-12 | Rounded open-back knee shrouds | 2 | Active v29 concept; print/retention pending |
| CAS-13 | Rounded ankle cowls | 2 | Active v29 concept; print/retention pending |
| CAS-14 | Hip-yaw motor collars | 1 | Active v29 concept; print/retention pending |
| CAS-15 | Inboard-open shoulder cuffs | 2 | Active v29 concept; print/retention pending |
| CAS-16 | Wrist transition guards | 2 | Active v29 concept; print/retention pending |
| CAS-17 | Elbow inner and outer side guards | 0 | Removed for servo elbows |
| CAS-18 | Rounded rectangular neck yaw collar | 1 | Active v29 concept; print/retention pending |
| CAS-19 | Shoe uppers and raised sole rims | 4 | Active v29 concept; print/retention pending |

## Electronics

| ID | Item | Quantity | Status |
|---|---|---:|---|
| ELE-01 | Host computer | 1 | Unselected for whole robot |
| ELE-02 | Regulated 12 V neck-servo supply | 1 | Unselected |
| ELE-03 | Host / logic / camera regulators | 1 | Unselected |
| ELE-04 | BLDC FOC control channels | 19 | Architecture/reference; actual controllers not selected |
| ELE-05 | Motor encoders, magnets, cables and serial/CAN interfaces | TBD | Not finalized |
| ELE-06 | Electronics enclosure and lid | 1 | Concept CAD |
| ELE-07 | Wi-Fi/network interface and auxiliary sensors | TBD | Host-dependent selection |
| ELE-08 | Regulated 24 V supply for both elbow servos | 1 | Unselected |
| ELE-09 | Elbow PWM command interface / custom servo control | 2 | Custom current-sense/encoder control planned |

## Hand electronics

| ID | Item | Quantity | Status |
|---|---|---:|---|
| HND-13 | Optional MG90 replacement current-sense serial boards | 16 | User proposal; not designed or qualified |

## Hand hardware

| ID | Item | Quantity | Status |
|---|---|---:|---|
| HND-03 | M2 ball joints with included screws and nuts | 32 | Original assembly-guide quantity |
| HND-04 | 6 mm ID bushings | 16 | Original assembly-guide quantity |
| HND-05 | 2×10 mm parallel pins | 16 | Original assembly-guide quantity |
| HND-06 | 2×16 mm parallel pins | 16 | Original assembly-guide quantity |
| HND-07 | M2.5 large washers | 8 | Original assembly-guide quantity |
| HND-08 | Thermoplastic 2.5×6 mm screws | 32 | Original assembly-guide quantity |
| HND-09 | Thermoplastic 2.5×8 mm screws | 8 | Original assembly-guide quantity |
| HND-10 | M2 threaded rod cut pieces, nominal 18 mm | 16 | Original assembly drawing nominal length |
| HND-11 | M2 threaded rod cut pieces, nominal 25 mm | 8 | Original assembly drawing nominal length |
| HND-12 | Modified servo cross horns and packaged screws | 16 | Original servo package; reworked horns |

## Hand structure

| ID | Item | Quantity | Status |
|---|---|---:|---|
| HND-01 | AmazingHand printed digit parts | 80 | Official full-size geometry |
| HND-02 | AmazingHand palm, top shell, hand plate and wrist interface | 8 | Official full-size geometry |

## Hardware

| ID | Item | Quantity | Status |
|---|---|---:|---|
| HW-01 | M2.5/M3/M4/M5/M6 screws, inserts, nuts, washers and spacers | TBD | Visual references; final purchase quantities unresolved |
| HW-02 | Wrist, head seam and pitch clamp fasteners | TBD | Native concepts; procurement lengths to detail |

## Linkages

| ID | Item | Quantity | Status |
|---|---|---:|---|
| LNK-01 | Waist M6 spherical rod ends | 4 | Existing hardware type; tilt assumption user-reported |
| LNK-02 | Waist M6 tie rods | 2 | Modeled nominal geometry |
| LNK-03 | Waist double-supported 6 mm cross-pin | 1 | Modeled |
| LNK-04 | Ankle link rods and rod ends | 4 | Retained source geometry |

## Power

| ID | Item | Quantity | Status |
|---|---|---:|---|
| PWR-01 | 21700 lithium-ion cells | 36 | 12S3P plan; JP50/P60C candidates, not selected |
| PWR-02 | 12S BMS | 1 | Unselected; bay reserved |
| PWR-03 | Battery interconnects, insulation, fuse and wiring | 1 | Undetailed |
| PWR-04 | Battery enclosure/cradle/restraints | 1 | Provisional CAD |

## Structure

| ID | Item | Quantity | Status |
|---|---|---:|---|
| STR-01 | Oval metal spine, 18 x 10 mm envelope | 1 | Modeled; section strength unresolved |
| STR-02 | Shin/thigh rails and leg adapters | 1 | v29 revised thigh rails; lower-leg mechanism retained |
| STR-03 | Hip motor sleeves, 110 OD / 106 ID | 4 | Modeled nominal aluminum tube |
| STR-04 | Torso cosmetic covering assembly | 1 | v27 split geometry; retention/physical print fit pending |
| STR-05 | Internal shoulder/spine frame | 1 | Concept CAD |
| STR-06 | Removable spine clamp caps | 2 | Concept CAD |
| STR-07 | Shoulder pitch motor face plates | 2 | Prototype metal geometry |
| STR-08 | Shoulder pitch carrier / roll housing | 2 | Concept CAD |
| STR-09 | Shoulder output hubs, collars and retainers | 2 | Concept CAD |
| STR-10 | 275 mm upper-arm forks and elbow case cradles | 2 | v29 concept CAD |
| STR-11 | Dual-sided servo elbow horns and output connector provisions | 2 | v29 packaging CAD; spline/horn fit pending |
| STR-12 | 250 mm dual-sided forearm forks | 2 | v29 concept CAD; final material unresolved |
| STR-13 | Oval-spine/neck-bearing adapter | 1 | Concept CAD |
| STR-14 | Neck yaw clamp, collar, cap and cradle | 1 | Concept CAD |
| STR-15 | Two-sided head-pitch yoke | 1 | Concept CAD |
| STR-16 | Head front shell, removable rear shell and open visor | 1 | Concept CAD |
| STR-17 | Forearm-to-AmazingHand wrist adapter | 2 | V26 concept; final native evidence below |
| STR-18 | Reinforced front and rear waist structural holders | 2 | v29 relieved structural holders; strength pending |

## Transmissions

| ID | Item | Quantity | Status |
|---|---|---:|---|
| TRN-01 | Knee internal reduction | 2 | Undesigned; 8:1 planning target |
| TRN-02 | Knee chain reduction stage | 2 | Retained visual sprockets; 2:1 planning target |
| TRN-03 | Hip-roll reduction | 2 | Undesigned; 15:1 user target |
| TRN-04 | Hip-pitch reduction | 2 | Undesigned; 15:1 user target |
| TRN-05 | Additional shoulder-pitch planetary | 2 | 4:1 user plan; not modeled or designed |

## Vision

| ID | Item | Quantity | Status |
|---|---|---:|---|
| VIS-01 | Yahboom AI VIEW depth camera / Astra SV1301S U3 | 1 | Recommended; official STEP modeled |

Exact interfaces, sources and qualifications are in the CSV. Actual masses, fastener quantities, printed load capacity and assembled battery limits remain open. Documentation stays local; no commit or push.
