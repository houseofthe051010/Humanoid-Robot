# Ankle pitch, ankle roll and knee shaft screen

September 20, 2026. Applies to the saved v11 leg's unchanged v9 ankle/knee geometry. No geometry was modified and no FEA was run. This calculation does not inspect subsequent unsaved user edits.

## Conclusion

All three smooth 8 mm shafts pass a simplified transverse bodyweight-only standing calculation with the assumed material. The ankle pitch and knee shafts fail the assumed ordinary-steel 3x and 5x one-leg load cases even with favorable load placement. The ankle roll shaft is shorter and stronger in bending, but its 5x result is sensitive to contact/load distribution and cannot be approved for running or jumps. Actuator reactions can make actual pivot loads substantially greater than bodyweight alone.

## Inputs and geometry evidence

Predicted total mass: 90 lb = 40.82 kg; weight 400.34 N. Diameter 8 mm, elastic modulus 200 GPa, illustrative yield stress 250 MPa. The purchased steel grade and heat treatment are unknown; 250 MPa is a screening assumption, not a certified minimum. A 5x case means total joint transverse force of 5 times bodyweight, not 5g net upward acceleration. It is a hypothetical load case, not a prediction of a specific jump.

Geometry comes from `E:\Aditya\robot_sim\outputs\shin_cad_20260912\v9\geometry_audit.json`; v11 `layout_validation.json` verifies the lower-leg components were retained. Outer race midplanes define supports, not the projecting collar tips. The roll block center differs from the support midpoint by 0.025 mm; that small asymmetry is neglected here.

| Shaft | Stock length | Bearing race center spacing L | Central load-block width b | Race center to block edge a |
|---|---:|---:|---:|---:|
| Ankle roll | 53 mm | 39.0 mm | 21 mm | 9.00 mm |
| Ankle pitch | 92 mm | 74.3 mm | 28 mm | 23.15 mm |
| Knee | 104 mm | 86.3 mm | 42 mm | 22.15 mm |

Roll race centers: Y=-7.85 and 31.15 mm. Pitch: X=±37.15 mm. Knee: X=±43.15 mm. The ankle load block is printed PA-CF; the knee block is four aluminum slices. Neither a perfect rigid bond nor composite shaft/block stiffness is established.

## Beam calculation

For total transverse load F, each support carries F/2. I=pi*d^4/64; section modulus Z=pi*d^3/32. Compare two idealized ways for the central block to load a simply supported smooth shaft:

1. Favorable edge transfer: half the load enters at each outer block face. Maximum moment M=F*(L-b)/4=F*a/2.
2. Uniform contact load across the block width: M=F*(2L-b)/8.

Bending stress is M/Z. These are sensitivity models, not rigorous lower/upper bounds for the real contact assembly. A concentrated center load gives still higher stress; collars, shaft fit and real block stiffness can alter the stress distribution. Beam theory reference: [MIT, Bending of Beams and Plates](https://web.mit.edu/course/3/3.11/www/modules/chap4.html).

| Total transverse load on one joint | Roll bending stress | Pitch bending stress | Knee bending stress |
|---|---:|---:|---:|
| Half bodyweight, 200 N | 18–28 MPa | 46–60 MPa | 44–65 MPa |
| One bodyweight, 400 N | 36–57 MPa | 92–120 MPa | 88–130 MPa |
| Three bodyweights, 1,201 N | 108–170 MPa | 277–360 MPa | 265–390 MPa |
| Five bodyweights, 2,002 N | 179–284 MPa | 461–600 MPa | 441–650 MPa |

Each range runs from edge transfer to uniform contact. Compare against the assumed 250 MPa yield stress. Yield/stress is not a fatigue safety factor. At one bodyweight the uniform-contact yield ratios are 4.41, 2.08 and 1.92 respectively. Peak transverse shear in the exposed shaft segments at 5x is about 26.5 MPa; bending dominates these cases. Shear and bending maxima occur at different section locations and were not artificially combined as coincident maxima.

Uniform-contact bare-shaft center deflection is F*(8L^3-4L*b^2+b^3)/(384EI). At one bodyweight this is 0.011 mm roll, 0.080 mm pitch and 0.119 mm knee. At 5x the elastic extrapolations are 0.054, 0.398 and 0.597 mm. Once yielding occurs, these do not predict actual deflection or permanent set. The ideal perfectly stiff central-block short-stub model gives smaller 5x deflections of 0.006, 0.103 and 0.090 mm; those are different support/compliance assumptions, not evidence of safety.

## Loads missing from bodyweight-only screening

The ankle links form another load path between shin and foot. Foot equilibrium requires the pivot reaction to balance both ground reaction and rod forces. The archived v8 neutral calculation at the assumed 40 Nm per motor produced roughly 1.74 kN in each near-vertical rod. Their combined force is approximately 3.48 kN; its vertical component can add to or oppose ground reaction. This means substituting robot weight for pivot force is insufficient. A physically consistent full case must also balance ankle moment, ground contact position, acceleration and motor direction. The archived 40 Nm is an assumption, not measured motor performance.

Opposite rod forces can create a roll moment and unequal bearing reactions even when their net force is small. Joint offsets, off-axis forces and posture also matter. The future knee chain produces additional radial load and potentially asymmetric reactions. Its chain tension and hub/bearing arrangement remain undecided. These shafts were treated as support pivots, not assumed to carry the entire geared motor output torque through shaft torsion.

The existing 6 mm heel linkage shaft is a separate part and remains unqualified under its previous motor-force screen.

## Collar, sleeve and bearing implications

A bearing's projecting inner ring/collar may stiffen the enclosed shaft locally but does not create an additional independently supported bearing. A loose central spacer does not automatically give composite bending stiffness. Credit for reinforcement requires its actual fit, preload/contact, length and load transfer to be modeled or tested. No reinforcement credit is included here.

Two 608 ratings cannot simply be added and compared with robot weight. The load must first be resolved into each bearing's radial/axial reactions; shock and unequal sharing must be checked. A higher dynamic rating describes rolling fatigue capacity and does not raise the permitted short-impact load. [SKF bearing selection guidance](https://www.skf.com/binaries/pub12/Images/0901d196807026e8-100-700_SKF_bearings_and_mounted_products_2018_tcm_12-314117.pdf) explicitly includes short heavy shocks in static safety checks. Purchased bearing/housing ratings remain unknown.

## Sizing implication

For 5x bodyweight alone, assumed 250 MPa yield and a nominal factor of 2 against first yield, the two contact models require:

| Joint | Calculated diameter, edge to uniform contact |
|---|---:|
| Roll | 9.0–10.5 mm |
| Pitch | 12.4–13.5 mm |
| Knee | 12.2–13.9 mm |

These numbers are preliminary sizing requirements for this isolated load case, not final purchase recommendations. Real actuator loads may govern. Stronger certified steel raises yield capacity but changes elastic bending stiffness little; increasing diameter or shortening the effective bending span addresses stiffness. Printed block strength, pinch bolts, creep, shaft notches, fatigue, bearings and housings still require separate checks.

Reproduce all values with [shaft_screen_8mm.py](evidence/shaft_screen_8mm.py); numerical output is [shaft_screen_8mm.json](evidence/shaft_screen_8mm.json). Next inputs: actual shaft material certificate, bearing/collar dimensions, complete actuator/ground-force equilibrium, chain geometry, reinforcement contact details and landing force/time history.
