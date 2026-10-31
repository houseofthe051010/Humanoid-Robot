# Isaac Lab training

Training remains stopped. Networks have not been copied into this folder.

Local evidence and checkpoints: `E:/Aditya/robot_sim/physical_v29/training/`.
Final review: `diagnostics/final_check_20261010_0905/REPORT.md`.
Saved checkpoint recorded by ACTIVE_RUN.json: `runs/locomotion_20261007_r40_goal_budget_full_state/1226_run_350_train_406/candidate.pt`.

Deployment needs the actor weights, observation order and normalization, action scaling, joint/motor mapping, differential kinematics and control period. A checkpoint alone is insufficient. The current CAD and hardware must be reconciled with the frozen training model.

A feed-forward actor can be exported as C/C++ weights and inference code. Verify desktop numerical equivalence and then measure P4 latency and memory before combining inference with motor and sensor tasks. No hardware deployment or qualified locomotion is claimed here.
