# Current evidence — v30

| Record | Result and limits |
|---|---|
| [Input CRC](evidence/v30/input_archive_crc.json) | Live user edits preserved in full native checkpoint |
| [Interfaces](evidence/v30/hip_interfaces30.json) | Independently measured axes, broader carriers and retained interfaces |
| [Clearance](evidence/v30/clearance_checks30.json) | 122 samples, no overlaps above 0.05 mm³; not continuous/global collision certification |
| [Tooth math](evidence/v30/sprocket_math_check.json) / [native sprockets](evidence/v30/chain_sprockets30.json) | Closed/tangent arc profiles, pitch spacing and retained 8T/16T placement |
| [Organization](evidence/v30/casing_organization30.json) | 65 moved components, 18 rigid physical owners, original 47 joints and rough prototypes preserved |
| [Native motion](evidence/v30/native_cover_motion30.json) | 23 body axes on reopened disposable copy; covers track owners, source pose unchanged |
| [Native integrity](evidence/v30/native_archive_integrity30.json) | Zstandard-aware ZIP payload CRC and hash pass |
| [Native reopen](evidence/v30/native_reopen30.json) | 1566 visible shapes, 65 constraints, all grounds/ranges/frames match |
| [Capacity handoff](evidence/v30/training_capacity_handoff30.json) | Actual 4096→6144 decision after 232.05 qualifying seconds; live PPO snapshot, not walking qualification |

Tooth construction sources: [Martin sprocket engineering](https://www.martinsprocket.com/docs/catalogs/engineering/engineering%20catalog/sprocket-engineering-data.pdf) and [TNB tooth generator](https://tnbpositioners.com/tools/sprocket/). Dimensional profile qualification is separate from material, chain engagement and strength.

Training evidence lives under the run selected by `E:/Aditya/robot_sim/physical_v29/training/ACTIVE_RUN.json`. Read live state, GPU CSV and latest independent gate. [Capacity monitoring](TRAINING_AUTOMATIC_VRAM_20261001.md) and [reward repair](TRAINING_REWARD_REPAIR_20261001.md) state what their tests prove. Earlier movement/collision records stay in [v29 history](history/v29/EVIDENCE.md).
