# V13 chain packaging and knee revision

September 21, 2026. Target robot height remains 1600.2 mm. This revision changes packaging, not the robot's load rating. See [validation evidence](evidence/v13/fit_validation.json), [active BOM](BOM_V13.csv) and [future work](FUTURE_WORK.md).

## Source and scope

The live `Bilateral_legs_v12` contained user edits that differed between legs: the right motor was already 30 mm below the released v12 position and its sprocket had moved inward. The untouched document was archived as `v13/Input_live_v12_20260921_preserved.f3d`. V13 copies the live right-leg solids into a canonical source, applies this revision, and reflects that source to rebuild the other leg. Original user documents remain untouched.

The source and paired v13 files have reconstructed native lower-leg joints. They do not recover the original part feature history from the copied solids. The preserved input retains the original history. All artifacts are under `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v13`; deliverables are in its `deliverables` folder.

## Implemented dimensions

Coordinates below are the canonical single leg in millimetres; the paired assembly adds ±130 mm lateral placement/reflection.

| Item | V13 geometry |
|---|---|
| Knee motor body reference | Estimated DJI 10018, 105 mm OD; unchanged motor details |
| Aluminum motor tube | 106 mm ID, 110 mm OD, 2 mm wall; 45 mm axial length, X −8 to 37 |
| Rear mounting plate | Separate 8 mm plate, X37–45, with right-rail saddles |
| Front cover | Separate 3 mm plate, X−11 to −8; bridge and clamp to opposite rail |
| Motor centre | Z565, 25 mm below released v12 Z590; live right leg moved up 5 mm from its surviving Z560 edit |
| Gearbox reservation | Nominal 13 mm from tube front to estimated motor front; final gearbox depth deferred by user |
| Knee pivot | Z435.6, raised 12 mm relative to the old shin block, rather than translating the entire leg |
| Shin oval tubes | Two per leg, 18×10 mm stadium, assumed 0.55 mm wall, length366.6; Z69–435.6 |
| Thigh oval tubes | Two per leg, 10 mm across X ×18 across Y, assumed 0.55 mm wall, length234.8; Z450.2–685 |
| Hip references | Retained positions; yaw vertical, separate roll, pitch25° |
| Leg centre spacing | Retained provisional260 mm; not a gait optimization |

The four aluminum knee slices gain a rounded crown, relocated shaft passage and tie/dowel pattern. The shin tubes extend12 mm upward, while the thigh tubes start12 mm higher to keep the hips fixed. The drive-side saddle and bearing pedestal are narrowed for the chain and sprocket. The opposite side keeps the previous bearing casting.

## Sprockets and support

| Parameter | Motor driver | Knee driven |
|---|---:|---:|
| Teeth | 8 | 16 |
| Pitch |12.70 mm|12.70 mm|
| Pitch diameter |33.19 mm|65.10 mm|
| Outside diameter |38.28 mm|71.37 mm|
| Tooth face width |7.21 mm|7.21 mm|

These values come from the user's attached dimension table. Teeth use approximate roller-pocket cuts, not a validated manufacturing profile. No actual chain links or internal planetary gears are modeled. The ratio is2:1.

Both sprockets are centred on X−31. This is10 mm inward from the released v12 motor blank centreX−41. Their centre distance is129.4 mm. A hidden `V13_Chain_clearance_ENVELOPE` reserves22 mm overall width and12.2 mm radial plate height around the pitch path. This includes a provisional pin/connector allowance; select the actual chain before freezing clearances. The envelope does not represent slack, articulation detail, chain tension adjustment or dynamic deflection.

The output uses a16 mm shaft/32 mm flange reference with a19 mm compact driver hub. The retained6 mm opposite-rail support pin is39 mm long. A6.395 mm knee sprocket standoff carries four recessed M3 ties and two6 mm dowels. Coupling, output bearings, torque transfer and retention remain unfinished.

**Drive-side bearing change:** the shelf pillow-block outer casting conflicts with the chain. V13 replaces that casting with a custom CNC aluminum pedestal while retaining its bearing/cartridge solids and bearing centre. The provisional25.8 mm through-seat follows the donor cartridge envelope; it is not a specified fit for a bare608 bearing. Axial shoulders, retention and strength need review. The new drive-side saddle uses twoM4x20 side screws and two top-entering M4x45 pedestal screws. Its inner face leaves1.395 mm nominal axial clearance to the16T sprocket.

## Assembly notes

The tube and separate plates replace the old monolithic thick plastic case. Four external M3x60 tie-bolt envelopes clamp the plates around the2 mm wall tube; there are no modeled threads in that thin wall. The front cover provides clearance for the motor's estimated uncut prop posts. Motor mounting dimensions remain photo estimates until the actual motor is measured. Printed bridges/caps and final bearing supports are not load-qualified.

Replaced hardware groups remain identified in the BOM. The former four-bolt large motor sprocket interface is hidden and excluded because it does not fit the8T root diameter. Rejected cosmetic fairings remain hidden. No unrelated ankle geometry was intentionally redesigned.

## Verification and limits

Machine-readable results are stored in `evidence/v13`: neutral chain and interface intersections, sampled native knee movement, paired assembly checks and archive reopen checks. Refer to their actual results; geometry checks do not constitute an FEA or impact test. The neutral audit separately reports inherited shaft-to-donor-bearing overlaps instead of silently treating them as fitted bearing interfaces. These include simplified set-screw contacts and approximately0.1 mm donor bore alignment discrepancies.

The stock8 mm knee/ankle shaft strength concerns remain open. This revision does not implement or validate a9 mm support-overhang redesign. There is no demonstrated allowable jumping load, fatigue life, chain rating, gearbox strength or motor thermal rating. Full hip articulation is still not modeled.

An8T driver has less than four teeth engaged in this open-chain layout. [Renold's sprocket guidance](https://www.renold.com/products/sprockets-and-accessories/sprockets/) recommends greater engagement for ordinary service; the requested8T geometry needs a supplier/load review before use. Exact40H chain dimensions vary by product; see the [PEER catalog](https://www.peerchain.com/wp-content/uploads/2022/08/PEERCHAIN-DIGITAL-CATALOG-4-19-22-1.pdf) and select the actual chain/connecting link before manufacture.

## Saved release checks

- Neutral audit: 51,829 body-pair checks; 0 new interface intersections and 0 chain-envelope intersections. 6 inherited donor bearing/set-screw overlaps are separately recorded.
- Source knee: 4 sampled poses at0°,45°,90°,120°; 0 collision poses and 0 Boolean-error poses. This is sampled clearance, not a continuous sweep or load simulation.
- Paired assembly: 104 components and 101 native joints per leg; no invalid joints or empty visible solids. Reflected body bounds matched. Neutral separation between the two leg assemblies is25.486 mm; full hip motion remains unchecked.
- Both native archives were reopened and their joint/body checks repeated. Paired knee attachment following was checked again after import. STEP exports contain visible geometry only.
