# Knee shaft strength screening — v9

**Result: the current8 mm shaft cannot be signed off for jumps/impacts.** For the user's90 lb body and5x bodyweight landing on one leg, even the favourable short-stub model predicts about **441 MPa bending stress**. Steel grade and actual impact history are unknown.

## Geometry and load path

After moving each side inward4 mm, the bearing outer-race midplanes are X=-43.150 and43.150 mm. Their spacing is86.300 mm. The four-piece block is42 mm wide, ending at X=±21 mm; its central8 mm slice is gone. The smooth shaft is8 x104 mm. Source race extents are recorded in `outputs/shin_cad_20260912/v9/input_geometry.json` and the body translations in `revise_rails.py`.

Each support force must cross roughly **22.15 mm** from bearing race centre to block edge. The collar projects toward the block, but it is not another ground-supported bearing. The extra collar material may stiffen part of the span; it does not remove the bending moment at the block edge. The left sprocket is not credited as a shaft-reinforcing sleeve.

This is deliberately a favourable force-transfer case: half the transverse load enters at each outer block face, avoiding a fictitious single load at the shaft centre. Assume the central aluminum block is perfectly stiff. With total load F, each reaction R=F/2, moment M=R a, bending stress σ=32M/(πd³). The short-stub estimate is δ=Ra³/(3EI), with I=πd⁴/64. Actual block/shaft contact and compliance require contact FEA.

90 lb =40.82 kg =400.3 N weight. “5x” means total ground force of5 times weight, not5g net upward acceleration (which would require6 times weight). One-leg landing is used. Joint forces from knee torque, posture and drivetrain reactions can add to this load; ground force alone is not the full knee joint load.

## Results

| Case | Total force N | Each bearing N | Shaft bending MPa | Assumed yield / stress | Stiff-block stub deflection mm |
|---|---:|---:|---:|---:|---:|
| Standing evenly on two legs | 200 | 100 | 44 | 5.67 | 0.009 |
| One-leg static support | 400 | 200 | 88 | 2.83 | 0.018 |
| 3x bodyweight on one leg | 1201 | 601 | 265 | 0.94 | 0.054 |
| 5x bodyweight on one leg | 2002 | 1001 | 441 | 0.57 | 0.090 |

**Material assumption:** E=200 GPa, yield=250 MPa as an illustrative ordinary-steel screen. This is not a claim that an unspecified AliExpress shaft is this grade. A certified stronger shaft may resist higher stress, but fatigue, notches, fretting, bearing alignment and block/fastener loads still need verification. Elastic deflections above yield are extrapolations and do not predict permanent deformation.

At5x, a bare-shaft two-edge-load model gives about0.468 mm centre deflection; a uniform distribution over the42 mm block gives about650 MPa. These are sensitivity models, not rigorous bounds on a nonlinear contact assembly. The favourable stiff-block case already exceeds assumed yield.

## Bearings are a separate check

The equal-share peak is1001 N per bearing. An SKF608 reference lists C0=1.37 kN and C=3.45 kN. This gives only about1.37 static rating/load ratio before side loads, unequal sharing and impact margin. That datasheet does not certify the purchased unbranded bearing, housing or mounting screws. The higher dynamic rating describes fatigue life under defined rotating loads; it is not permission to exceed a static-impact limit. Sources: [SKF608 datasheet](https://docs.rs-online.com/9931/A700000008717780.pdf), [SKF bearing selection and static load guidance](https://cdn.skfmediahub.skf.com/api/public/0901d196802809de/pdf_preview_medium/0901d196802809de_pdf_preview_medium.pdf).

## Practical design options

For this same favourable5x load case and assumed250 MPa steel, the ideal smooth diameter is9.7 mm just to reach yield, or12.2 mm for a nominal factor2. A12 mm shaft is a sensible next size to evaluate, but it requires matching bearings and interfaces and is not itself a complete approval. Moving the metal support faces closer to the bearings is another option. With8 mm and a factor2 against250 MPa, the allowable moment arm here would be only6.28 mm, versus22.15 mm now.

No shaft diameter or bearing change has been imposed on the CAD in this revision. The requested8 mm geometry remains, marked unqualified for impacts.

The knee motor and QDD ratio are not finalized. If40 Nm were transmitted entirely through an8 mm shaft, torsional shear alone would be approximately398 MPa; that is an illustrative alternative load path, not an asserted knee demand. A proper flanged output can bypass shaft torque while still leaving radial shaft bending to check.

Next analysis needs: certified shaft material/heat treatment, exact bearing/housing, QDD output torque and radial forces, landing posture and force/time history, aluminum block contact/clamping, and all fastener preloads. A printed spacer or loose steel spacer cannot be assigned composite bending stiffness without demonstrating load transfer.

Beam theory reference: [MIT—Bending of Beams and Plates](https://web.mit.edu/course/3/3.11/www/modules/chap4.html). Reproduce with `outputs/shin_cad_20260912/v9/knee_strength.py`. No FEA or instrumented impact test was run.
