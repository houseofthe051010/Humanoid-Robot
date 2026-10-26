# Robot BOM — v31

Prototype quantities and references; manufacturing/load qualification remains open. [CSV](BOM.csv).

| ID | Item | Quantity | Status |
|---|---|---:|---|
| ACT-01 | GWK7010 motor reference | 7 motor | Modeled; exact purchase variant to confirm |
| ACT-02 | Casing-free GWK6010-8 motor | 6 motor | Actual supplier CAD; planned variant |
| ACT-03 | DJI10018 77 KV motor | 6 motor | Estimated geometry; user-selected motor type |
| ACT-04 | Feetech STS3215 12 V / 30 kg.cm dual-shaft serial servo | 2 servo | User-imported CAD; verify 12 V variant before ordering |
| ACT-05 | ANNIMOS/DSSERVO RDS51160 double-shaft 24 V elbow servo | 2 servo | User selected; RDS51150 CAD dimension proxy |
| ACT-06 | AmazingHand mechanisms (servos listed separately) | 2 hand | Official source design selected for CAD integration; hardware not purchased |
| ACT-07 | Feetech SCS0009 microservo (original hand design) | 16 servo | Reference choice; MG90 replacement not validated |
| BRG-01 | 6810 / 61810 bearing, 50 x 65 x 7 mm | 2 bearing | Nominal envelope modeled |
| BRG-02 | 6005 bearing, 25 x 47 x 12 mm | 3 bearing | Nominal envelope modeled |
| BRG-03 | 6007 bearing, 35 x 62 x 14 mm | 2 bearing | Retained nominal envelope |
| BRG-04 | 61810 / 6810 bearing, 50 x 65 x 7 mm | 4 bearing | Retained nominal envelopes |
| BRG-05 | Hip-pitch bearing envelope, 40 x 52 x 7 mm | 4 bearing | Retained dimension reference; model TBD |
| BRG-06 | 8 mm ankle/knee/heel bearing positions | 16 position | Legacy reference; final stock blocks vs bare bearings TBD |
| CAS-01 | Split torso bands with shoulder flare/collars | 12 panel | V30 native geometry; print retention pending |
| CAS-02 | Upper-arm skins | 4 panel | Active v29 concept; print/retention pending |
| CAS-03 | Forearm skins | 4 panel | Active v29 concept; print/retention pending |
| CAS-04 | Thigh skins | 4 panel | Active v29 concept; print/retention pending |
| CAS-05 | Split shin/calf skins | 8 panel | Active v29 concept; print/retention pending |
| CAS-08 | Torso identifier and two calf marks | 3 accent | Active v29 concept; print/retention pending |
| CAS-09 | Hip roll-case front caps | 0 cap | Removed from active display; hidden native history preserved |
| CAS-10 | Split tapered pelvis front fairing | 0 panel | Superseded; hidden source geometry preserved |
| CAS-11 | Two knee and two ankle front guards | 0 guard | Superseded; hidden source geometry preserved |
| CAS-12 | Rounded open-back knee shrouds | 2 shroud | Active v29 concept; print/retention pending |
| CAS-13 | Rounded ankle cowls | 2 cowl | Active v29 concept; print/retention pending |
| CAS-14 | Hip-yaw motor collars | 1 collar | Active v29 concept; print/retention pending |
| CAS-15 | Inboard-open shoulder cuffs | 2 cuff | V30 radial motion relief |
| CAS-16 | Wrist transition guards | 2 guard | Active v29 concept; print/retention pending |
| CAS-17 | Elbow inner and outer side guards | 0 cheek | Removed for servo elbows |
| CAS-18 | Rounded rectangular neck yaw collar | 1 collar | Active v29 concept; print/retention pending |
| CAS-19 | Shoe uppers and raised sole rims | 4 piece | Active v29 concept; print/retention pending |
| ELE-01 | Host computer | 1 computer | Unselected for whole robot |
| ELE-02 | Regulated 12 V neck-servo supply | 1 converter | Unselected |
| ELE-03 | Host / logic / camera regulators | 1 set | Unselected |
| ELE-04 | BLDC FOC control channels | 19 channel | Architecture/reference; actual controllers not selected |
| ELE-05 | Motor encoders, magnets, cables and serial/CAN interfaces | TBD set | Not finalized |
| ELE-06 | Electronics enclosure and lid | 1 set | Concept CAD |
| ELE-07 | Wi-Fi/network interface and auxiliary sensors | TBD set | Host-dependent selection |
| HND-13 | Optional MG90 replacement current-sense serial boards | 16 channel | User proposal; not designed or qualified |
| HND-03 | M2 ball joints with included screws and nuts | 32 ball joint | Original assembly-guide quantity |
| HND-04 | 6 mm ID bushings | 16 bushing | Original assembly-guide quantity |
| HND-05 | 2×10 mm parallel pins | 16 pin | Original assembly-guide quantity |
| HND-06 | 2×16 mm parallel pins | 16 pin | Original assembly-guide quantity |
| HND-07 | M2.5 large washers | 8 washer | Original assembly-guide quantity |
| HND-08 | Thermoplastic 2.5×6 mm screws | 32 screw | Original assembly-guide quantity |
| HND-09 | Thermoplastic 2.5×8 mm screws | 8 screw | Original assembly-guide quantity |
| HND-10 | M2 threaded rod cut pieces, nominal 18 mm | 16 piece | Original assembly drawing nominal length |
| HND-11 | M2 threaded rod cut pieces, nominal 25 mm | 8 piece | Original assembly drawing nominal length |
| HND-12 | Modified servo cross horns and packaged screws | 16 servo set | Original servo package; reworked horns |
| HND-01 | AmazingHand printed digit parts | 80 printed instance | Official full-size geometry |
| HND-02 | AmazingHand palm, top shell, hand plate and wrist interface | 8 printed part | Official full-size geometry |
| HW-01 | M2.5/M3/M4/M5/M6 screws, inserts, nuts, washers and spacers | TBD set | Visual references; final purchase quantities unresolved |
| HW-02 | Wrist, head seam and pitch clamp fasteners | TBD set | Native concepts; procurement lengths to detail |
| LNK-01 | Waist M6 spherical rod ends | 4 rod end | Existing hardware type; tilt assumption user-reported |
| LNK-02 | Waist M6 tie rods | 2 rod | Modeled nominal geometry |
| LNK-03 | Waist double-supported 6 mm cross-pin | 1 pin | Modeled |
| LNK-04 | Ankle link rods and rod ends | 4 link assembly | Retained source geometry |
| PWR-01 | 21700 lithium-ion cells | 36 cell | 12S3P plan; JP50/P60C candidates, not selected |
| PWR-02 | 12S BMS | 1 board | Unselected; bay reserved |
| PWR-03 | Battery interconnects, insulation, fuse and wiring | 1 pack set | Undetailed |
| PWR-04 | Battery enclosure/cradle/restraints | 1 set | Provisional CAD |
| STR-01 | Oval metal spine, 18 x 10 mm envelope | 1 tube | Modeled; section strength unresolved |
| STR-02 | Shin/thigh rails and leg adapters | 1 robot set | v29 revised thigh rails; lower-leg mechanism retained |
| STR-03 | Hip motor sleeves, 110 OD / 106 ID | 4 sleeve | Modeled nominal aluminum tube |
| STR-04 | Torso cosmetic covering assembly | 1 assembly | v27 split geometry; retention/physical print fit pending |
| STR-05 | Internal shoulder/spine frame | 1 frame | Concept CAD |
| STR-06 | Removable spine clamp caps | 2 cap | Concept CAD |
| STR-07 | Shoulder pitch motor face plates | 2 plate | Prototype metal geometry |
| STR-08 | Shoulder pitch carrier / roll housing | 2 carrier | Concept CAD |
| STR-09 | Shoulder output hubs, collars and retainers | 2 side set | Concept CAD |
| STR-10 | 275 mm upper-arm forks and elbow case cradles | 2 fork | v29 concept CAD |
| STR-11 | Dual-sided servo elbow horns and output connector provisions | 2 side set | v29 packaging CAD; spline/horn fit pending |
| STR-12 | 250 mm dual-sided forearm forks | 2 fork | v29 concept CAD; final material unresolved |
| STR-13 | Oval-spine/neck-bearing adapter | 1 adapter | Concept CAD |
| STR-14 | Neck yaw clamp, collar, cap and cradle | 1 set | Concept CAD |
| STR-15 | Two-sided head-pitch yoke | 1 yoke | Concept CAD |
| STR-16 | Head front shell, removable rear shell and open visor | 1 set | Concept CAD |
| STR-17 | Forearm-to-AmazingHand wrist adapter | 2 adapter | V26 concept; final native evidence below |
| STR-18 | Enlarged continuous waist shell halves | 2 half | V31 native prototype; manufacturing and strength unqualified |
| TRN-01 | Knee internal reduction | 2 gearbox | Undesigned; 8:1 planning target |
| TRN-02 | Knee chain reduction stage | 2 stage | V30 native ANSI #40 roller tooth profiles; chain selection pending |
| TRN-03 | Hip-roll reduction | 2 gearbox | Undesigned; 15:1 user target |
| TRN-04 | Hip-pitch reduction | 2 gearbox | Undesigned; 15:1 user target |
| VIS-01 | Yahboom AI VIEW depth camera / Astra SV1301S U3 | 1 camera | Recommended; official STEP modeled |
| ELE-08 | Regulated 24 V supply for both elbow servos | 1 supply | Unselected |
| ELE-09 | Elbow PWM command interface / custom servo control | 2 channel | Custom current-sense/encoder control planned |
| TRN-05 | Additional shoulder-pitch planetary | 2 gearbox | 4:1 user plan; not modeled or designed |
| CAS-20 | Shoulder roll-case pod halves | 4 half | V30 native prototype |
| CAS-21 | Shoulder rear teal inserts | 2 ring | V30 native prototype |
| STR-19 | Planar rounded hip pitch-to-roll hoods | 2 carrier | V31 native prototype; manufacturing and strength unqualified |
| STR-20 | Roll-to-yaw U cradles with solid outer caps | 2 cradle | V31 native prototype; manufacturing and strength unqualified |
| STR-21 | Reinforced fixed hip-roll endcaps | 4 endcap | V30 geometry; hardware and strength pending |
| HW-03 | Waist seam M4 x 25 screw references | 4 screw | Native reference; procurement details pending |
| HW-04 | Hip carrier M4 x 18 screw references | 16 screw | Native reference; procurement details pending |
| HW-05 | M4 nut envelopes for new waist/hip bolts | 20 nut | Native reference; procurement details pending |
| HW-06 | Original vertical waist-yaw mounting positions | 4 position | Native reference; procurement details pending |
| HW-07 | Shoulder pod M3 seam mounting positions | 8 position | Native reference; procurement details pending |
| STR-22 | Dual 7010 ankle motor holders with integral side walls | 2 holder | V31 native prototype; manufacturing and strength unqualified |
