# Decisions remaining after v29

The geometry changes and requested 23-joint movement tests are complete. September 30 motor torque/RPM assumptions are now configured. Physical thermal, electrical and load qualification remains open.

1. Qualify the configured user assumptions against exact hardware variants, loaded torque-speed curves and thermal duty. Current values are `physical_v29/assets/actuator_limits.json`; the former null file is historical. Elbow7 N·m sustained at 45 RPM is a user assumption; qualify it on the actual actuator. Current shoulder pitch uses 35.625 /71.25 N·m at 95% and 120 RPM; verify the physical4:1 stage and motor speed margin.
2. Confirm exact RDS51160 dimensions, two output splines/horns, bearing/support behavior, case mounting and allowable electrical rail. The 65×30×48 mm 150 kg CAD reference is an authorized dimensional proxy. Final horns/fasteners must match actual hardware.
3. Recheck the knee chain center distance, chain length/tensioning and guards after the 30 mm thigh extension. Existing visual sprockets/reduction targets remain; no actual chain was selected.
4. Review minimum remaining sections/load paths and reinforcement of the relieved structural waist holders. Clearance removal is substantial; thicker nominal skins/ribs and single-solid topology do not qualify printed load capacity.
5. Decide whether to restore a left hip-yaw collar. One right collar was active in source/release; procurement inventory records actual visible geometry rather than assuming symmetry.
6. Choose physical mass/material/density/infill and model useful collision shapes before gravity, contact, standing, payload or locomotion tests. Older training policies and torque demands do not qualify the resized robot.
7. Complete transmission designs, motor torque-speed/thermal data, shaft/bearing fits, thin-spine strength, new elbow/forearm material and fastener/tool access.
8. Select host, exact JP50/P60C or alternative cells, BMS, converters, control interfaces and cooling/wiring. Confirm 50.4 V full-charge compatibility and pulse repetition; cell current arithmetic does not qualify the pack. Add a regulated elbow servo rail; do not connect selected 24 V servos to raw 12S.
9. Detail removable cosmetic retention/print splits and test combined body/cable travel with the revised proportions. V28 pose samples remain historical. Shoe attachment/sole compression tolerance still needs a prototype.
10. Choose original SCS0009 hand actuators versus a measured MG90 redesign/current-sense serial board. Equivalent force capability, mechanical fit and sub-$100 total are not established. Hands and wrists remain static in this pass.
11. Confirm desired palm orientation and any future powered wrist; retain current rigid connectors until specified. The resized arms require a fresh combined hand/hip-clearance review.
