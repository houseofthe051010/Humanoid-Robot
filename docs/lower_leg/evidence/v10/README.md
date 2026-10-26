# V10 evidence

Geometry JSON is in millimetres unless named otherwise. The live inventory is the preserved input before edits. Fusion scripts require the in-process ShinWorkbench bridge and local work directory; do not run them with ordinary Python. Reproduction sequence: back up/import live v9 with open_revision.py; build_upper_leg.py; finish_mount_access.py; validate_layout.py; validate_knee.py; export_revision.py; reopen_verify.py. Inspect the exact current source and document before replaying any mutation. The final corrected builder has the proper M02_Aluminum_crank_A name; the original live run resumed after correcting that lookup.

The original live input archive and full outputs remain under E:\Aditya\robot_sim\outputs\shin_cad_20260912\v10. This evidence folder deliberately does not duplicate the large native/STEP files.
