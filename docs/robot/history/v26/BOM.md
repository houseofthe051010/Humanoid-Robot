# Whole-robot planning BOM

Revision v26 · September 30, 2026. [Build report](../../BUILD_REPORT.md) · [CSV](../../BOM.csv) · [Hand design](../../HAND_OPTIONS.md).

This list describes the current design and unresolved selections. It is not a list of parts confirmed purchased. Blank prices mean unknown, not free. There is no supported whole-robot cost total. A motor split into stator/output CAD parts still counts as one purchased motor; each reference bearing and camera also counts once.

| Item | Quantity | Selection status |
|---|---:|---|
| GWK7010 references | 7 | Four ankle, two hip yaw, one waist yaw; verify actual purchased variant |
| Casing-free GWK6010-8 | 6 | Two waist and four shoulder motors; supplier geometry |
| DJI10018 77 KV references | 6 | Two knee, two hip pitch, two hip roll; custom reductions unfinished |
| Feetech STS3215 12 V / 30 kg·cm | 2 | Neck yaw/pitch; verify 12 V variant |
| Elbow actuators | 2 | Unselected; supported shaft/cavity reserved |
| AmazingHand mechanisms | 2 | Full-scale source design; three fingers plus thumb per hand |
| Hand SCS0009 microservos | 16 | Original source design; MG90 substitution requires mechanical/control validation |
| 6810/61810 50×65×7 bearings | 6 | Two shoulder pitch and four hip-roll references |
| 6005 25×47×12 bearings | 7 | One neck yaw, two shoulder rear supports and four elbow supports |
| Yahboom AI VIEW camera | 1 | Official CAD; $199 before shipping/tax, checked September 29 |
| 21700 cells / 12S BMS | 36 / 1 | Models unselected; pack/BMS envelope reserved |
| BLDC FOC channels | 19 | Motor count; controller selection incomplete; elbows may add channels |
| Host, regulators, encoders and wiring | See CSV | Architecture and actual parts remain incomplete |

The CSV also covers transmissions, structure, wrist adapters and the hand's small purchased hardware. Hand hardware quantities come from the original assembly guide. Threaded-rod nominal cut lengths differ between preparation and assembly pages; use the supplied length tool and one prototype finger before batch cutting. A sub-$100 hand using MG90 conversions remains a cost target, not a verified BOM total.

The root [bom.csv](../../../../bom.csv) and [earlier lower-leg grant record](../../../archive/LOWER_LEG_GRANT.md) preserve the previous $761.45 prototype scope. Those prices were not revalidated and must not be added to this planning BOM without reconciling duplicate or superseded parts.
