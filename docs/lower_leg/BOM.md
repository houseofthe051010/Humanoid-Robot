# Lower-leg engineering BOM — v9 baseline with v11 thigh updates

Price-free BOM for **one modeled leg and its knee/thigh interfaces**, not a whole robot inventory. Quantities describe the design; purchases/ownership have not been audited. A second mirrored leg usually doubles quantities, but electronics and body-wide items must be planned separately.

Source: live v8 checked against the saved v8 geometry, followed by the v9 revision scripts. Supplier motor bodies, bearing balls/races and rod-end inner rings are bundled into purchased assemblies so they are not double-counted. Hidden earlier layouts are recorded separately.

**Do not order unresolved hardware by guessing a length.** The final rows identify required screws that were missing or incomplete in the inherited model. The8 mm knee shaft is geometry only and is not approved for the assumed jump load. See [knee calculation](KNEE_STRENGTH_V9.md).

[Download/edit BOM.csv](BOM.csv)

| ID | Assembly | Item | Qty/leg | Specification | Status |
|---|---|---|---:|---|---|
| LL-001 | Foot | Aluminum foot plate | 1 | 100 x122 x4 mm; eight current 5.4 mm through holes | CAD nominal; verify actual parts |
| LL-002 | Foot | Printed sole | 1 | Preserved outline;10 mm thick with flat underside and bottom nut access | CAD nominal; verify actual parts |
| LL-003 | Ankle and knee | 8 mm bore pillow block assembly | 8 | 2 roll +2 pitch +2 heel +2 knee; includes bearing/collar and supplier set screws | Purchased style represented; actual bearing and housing ratings require confirmation |
| LL-004 | Ankle | Smooth roll shaft | 1 | Diameter8 x53 mm | CAD nominal; verify actual parts |
| LL-005 | Ankle | Smooth pitch shaft | 1 | Diameter8 x92 mm | CAD nominal; verify actual parts |
| LL-006 | Heel | Smooth cross-shaft with end threads | 1 | Diameter6 x97 mm; M6x1 end retention modeled | Saved CAD is97 mm; user-owned96 mm shaft needs retention fit review |
| LL-007 | Knee | Smooth knee shaft | 1 | Diameter8 x104 mm after narrowing | Geometry only; fails assumed mild-steel5x landing screen |
| LL-008 | Ankle | Printed cross-axis block | 1 | Two perpendicular8 mm bores and M3 pinch clamps | CAD nominal; verify actual parts |
| LL-009 | Shin | Ankle-to-shin adapter | 1 | Rail centres X +/-10 mm,Y6 mm; unchanged bearing interface | CAD nominal; verify actual parts |
| LL-010 | Shin | Continuous oval steel rail | 2 | 18 x10 stadium; assumed0.55 wall;354.6 mm long | CAD nominal; verify actual parts |
| LL-011 | Shin | Dual motor carrier | 1 | Narrowed rail sockets; separate removable motor covers | CAD nominal; verify actual parts |
| LL-012 | Shin | Motor cover A | 1 | 5 mm thick; original vendor motor profile | CAD nominal; verify actual parts |
| LL-013 | Shin | Motor cover B | 1 | 5 mm thick; original vendor motor profile | CAD nominal; verify actual parts |
| LL-014 | Shin | Crush sleeve | 12 | 5 OD x3.4 ID x10 mm | CAD nominal; verify actual parts |
| LL-015 | Ankle drive | GWK7010-8 motor assembly | 2 | Supplied vendor STEP; housing and output CAD bodies constitute one motor | Motor torque40 Nm is a screening assumption, not a validated continuous rating |
| LL-016 | Ankle drive | Aluminum output crank | 2 | 6 mm thick;23 mm crank radius; six M3 mounting positions | CAD nominal; verify actual parts |
| LL-017 | Ankle drive | Female rod-end bearing | 4 | M6x1 right hand female thread;6 mm spherical bore;9 mm inner-ring width | Wixroyd65720.W0006 surrogate CAD; confirm purchased SI6 dimensions |
| LL-018 | Ankle drive | M6 threaded link A | 1 | M6x1 RH; CAD stock length285.1265 mm;12 mm nominal engagement each end | CAD nominal; verify actual parts |
| LL-019 | Ankle drive | M6 threaded link B | 1 | M6x1 RH; CAD stock length202.8568 mm;12 mm nominal engagement each end | CAD nominal; verify actual parts |
| LL-020 | Ankle drive | Oval reinforcement A | 1 | 18 x10 x assumed0.55 wall;230 mm long | CAD nominal; verify actual parts |
| LL-021 | Ankle drive | Oval reinforcement B | 1 | 18 x10 x assumed0.55 wall;140 mm long | CAD nominal; verify actual parts |
| LL-022 | Ankle drive | Threaded rod-to-oval end adapter | 4 | 20 mm insert plus1.5 mm flange; modeled M6 female thread | CAD nominal; verify actual parts |
| LL-023 | Ankle drive | Central rod guide A | 1 | Length follows link;6.4 mm running bore | CAD nominal; verify actual parts |
| LL-024 | Ankle drive | Central rod guide B | 1 | Length follows link;6.4 mm running bore | CAD nominal; verify actual parts |
| LL-025 | Heel | 8-to-6 mm bearing reducer | 2 | 8 OD x6 ID x12 mm | Carries radial load; no strength qualification |
| LL-026 | Heel | Outer axial spacer | 2 | 8.5 OD x6.2 ID x4.95 mm | Axial spacing only; no shaft bending credit |
| LL-027 | Heel | Central axial spacer | 1 | 8.5 OD x6.2 ID x37 mm | Steel replacement discussed but not implemented |
| LL-028 | Ankle drive | Upper rod-end pin | 2 | M6 nominal; CAD envelope; length and retention TBD | Needs hardware selection; do not infer finished fastener from envelope |
| LL-029 | Ankle drive | Upper inner-ring spacer | 2 | 4.5 mm long;7 mm OD nominal envelope | Through-bore/actual pin fit requires final hardware detailing |
| LL-030 | Electronics | ODrive controller board assembly | 1 | 15 source bodies; connector bodies removed for direct wiring | Exact controller variant and electrical connections require confirmation |
| LL-031 | Electronics | Upper rail clip | 1 | Sockets at20 mm centre spacing; PCB position retained | CAD nominal; verify actual parts |
| LL-032 | Electronics | PCB spacer | 2 | 2 mm thick; M3 bore | CAD nominal; verify actual parts |
| LL-033 | Knee | Machined knee slice 1 | 1 | 11 mm X thickness; four slices42 mm total; centre piece removed | CAD nominal; verify actual parts |
| LL-034 | Knee | Machined knee slice 2 | 1 | 10 mm X thickness; four slices42 mm total; centre piece removed | CAD nominal; verify actual parts |
| LL-035 | Knee | Machined knee slice 4 | 1 | 10 mm X thickness; four slices42 mm total; centre piece removed | CAD nominal; verify actual parts |
| LL-036 | Knee | Machined knee slice 5 | 1 | 11 mm X thickness; four slices42 mm total; centre piece removed | CAD nominal; verify actual parts |
| LL-037 | Knee | Sprocket interface blank | 1 | 70 mm OD x6 mm; six registration/tie positions; no teeth | Layout only; transmission may change for QDD |
| LL-038 | Thigh interface | Oval clamp L base | 1 | Shifted4 mm inward with knee bearings | CAD nominal; verify actual parts |
| LL-039 | Thigh interface | Oval clamp L cap | 1 | Shifted4 mm inward with knee bearings | CAD nominal; verify actual parts |
| LL-040 | Thigh interface | Oval clamp R base | 1 | Shifted4 mm inward with knee bearings | CAD nominal; verify actual parts |
| LL-041 | Thigh interface | Oval clamp R cap | 1 | Shifted4 mm inward with knee bearings | CAD nominal; verify actual parts |
| LL-042 | Thigh interface | Continuous oval thigh rail | 2 | 18 x10 x assumed0.55 wall;233.8 mm long v11 layout | Provisional cut length; also UL-001, do not double count |
| LL-043 | Knee drive | DJI10018 77KV motor | 1 | 105 mm OD,30 mm body,6 mm rear projection,24 mm prop posts estimated | V10 thigh-mounted reference; also UL-002, do not double count; actual dimensions and performance unverified |
| LL-044 | Foot | M5 socket screw | 8 | M5x20 | CAD nominal; verify actual parts |
| LL-045 | Foot | M5 washer | 16 | 10 OD x5.3 ID x1 mm | CAD nominal; verify actual parts |
| LL-046 | Foot | M5 hex nut | 8 | M5;8 AF;4 mm thick | CAD nominal; verify actual parts |
| LL-047 | Heel | M6 thin retaining nut | 2 | M6x1;10 AF; verify3.85 mm available engagement | CAD nominal; verify actual parts |
| LL-048 | Motor covers | M3 socket screw | 12 | M3x12 | CAD nominal; verify actual parts |
| LL-049 | Motor covers | M3 countersunk screw | 16 | M3x12 | CAD nominal; verify actual parts |
| LL-050 | Motor covers | M3 heat-set insert | 12 | 4.6 OD x5 mm envelope;4.3 mm pilot needs calibration | CAD nominal; verify actual parts |
| LL-051 | Cranks | M3 washer | 12 | 1 mm thick | CAD nominal; verify actual parts |
| LL-052 | Electronics | M3 socket screw | 2 | M3x10 | CAD nominal; verify actual parts |
| LL-053 | Electronics | M3 washer | 2 | 1 mm thick | CAD nominal; verify actual parts |
| LL-054 | Electronics | M3 nut | 2 | M3 standard | CAD nominal; verify actual parts |
| LL-055 | Knee stack | M3 socket screw | 4 | M3x55; verify availability/cutdown from longer stock | CAD nominal; verify actual parts |
| LL-056 | Knee stack | M3 nut | 6 | 4 tie nuts +2 rail nuts | CAD nominal; verify actual parts |
| LL-057 | Knee stack | Registration dowel | 2 | Diameter6 x48 mm | CAD nominal; verify actual parts |
| LL-058 | Knee stack | M3 rail crossbolt | 2 | M3x50 | CAD nominal; verify actual parts |
| LL-059 | Knee stack | M3 shaft set screw | 2 | M3x10 | CAD nominal; verify actual parts |
| LL-060 | Thigh clamps | M3 socket screw | 8 | M3x35 | CAD nominal; verify actual parts |
| LL-061 | Thigh clamps | M3 nut | 8 | M3 standard | CAD nominal; verify actual parts |
| LL-062 | Thigh clamps | M5 socket screw | 4 | M5x16 | CAD nominal; verify actual parts |
| LL-063 | Thigh clamps | M5 washer | 4 | 1 mm thick | CAD nominal; verify actual parts |
| LL-064 | Thigh clamps | M5 nut | 4 | M5 standard | CAD nominal; verify actual parts |
| LL-065 | Ankle cross block | M3 pinch screw | 2 | Nominal under-head lengths31 and27 mm in envelope; choose stock lengths after fit check | CAD nominal; verify actual parts |
| LL-066 | Ankle cross block | M3 nut | 2 | M3 standard | CAD nominal; verify actual parts |
| LL-067 | Shin | Rail crossbolts and nuts | 10 | M3;4 adapter +6 carrier; lengths TBD from final seats | Required assembly hardware; not fully represented in CAD; finalize before ordering |
| LL-068 | Ankle adapter | Pitch pillow mounting screws and nuts | 4 | M5; final length TBD | Required assembly hardware; not fully represented in CAD; finalize before ordering |
| LL-069 | Cranks | Motor-output screws | 12 | M3;6 mm crank +1 mm washer +up to5 mm engagement; candidateM3x12 | Required assembly hardware; not fully represented in CAD; finalize before ordering |
| LL-070 | Links | M6 jam nuts | 4 | M6x1 RH; final adjustment/engagement budget must include nut thickness | Required assembly hardware; not fully represented in CAD; finalize before ordering |
| LL-071 | Preserved references | Earlier GIM10015 layout motor | 1 | Retained hidden; exclude from build quantity totals | Reference only; not an additional installed part |
| LL-072 | Preserved references | Earlier GWK7010 layout copy | 1 | Retained hidden; exclude from build quantity totals | Reference only; not an additional installed part |
| LL-073 | Preserved references | User-added root layout body | 1 | Retained hidden; exclude from build quantity totals | Reference only; not an additional installed part |

## Not yet designed or counted

V10 adds a provisional knee motor shell and caps, mounting fastener envelopes, a yaw motor reference and hip/pelvis envelopes; see [upper-leg BOM](UPPER_LEG_BOM.csv). UL-001 and UL-002 repeat LL-042 and LL-043 for context and must not be added twice. QDD planetary, final chain/sprocket transmission, encoders, encoder mounts, completed hip/waist/torso, battery, wiring/connectors, heatsinks and full-body fasteners remain unresolved. The DJI prop posts remain uncut reference features. Removing a motor feature requires inspection of the actual motor.

The old8 mm knee centre piece is removed. The empty N00 component is a joint datum and has zero physical quantity. A proposed steel centre spacer on the heel shaft is not silently substituted for the current printed spacer.
