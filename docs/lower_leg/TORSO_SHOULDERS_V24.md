# V24 upper-body packaging and supported shoulder forks

Working Fusion document: `Humanoid_shoulders_electronics_v24` (new cloud copy of the user's straight-spine v23 design).

## Saved files

The full robot is saved in Fusion as `Humanoid_shoulders_electronics_v24`, cloud version 4. Original v23 source remains preserved. Use `deliverables/Torso_shoulders_electronics_v24.f3d` for the independently reopened upper-body assembly (100 solid bodies, 31 valid joints including five revolute joints). `deliverables/Torso_shoulders_electronics_v24.step` is the neutral STEP assembly; individual concept-part STEP files and preview PNGs are also included.

The full robot's local F3D export retains inherited external-reference metadata and Fusion rejects opening it as a new local design. That export is retained under `diagnostic_archives`, not presented as a portable assembly. The full cloud document and verified upper-body archive are the usable native deliverables.

## Geometry

- The torso shell connects to an internal shoulder crossmember and lower mounting rail. Two removable rear clamp caps capture the existing 18 × 10 mm oval spine. Their mating faces include a 0.6 mm closing gap; nominal spine socket is 18.3 × 10.3 mm.
- The reinforced shoulder openings hold simplified 6810 bearing envelopes, 50 mm ID × 65 mm OD × 7 mm wide, with separate outer retainers and generic pitch output hubs.
- Each pitch output carries an 80 mm OD × 50 mm long hollow roll-actuator housing. Pitch and roll axes intersect; roll axes are 394 mm apart. Housings reserve geometry for a future motor/gearbox rather than representing a selected actuator.
- Each roll joint has a front driven flange (60 mm OD, six M4 clearance holes on 48 mm PCD) and a fixed rear 25 mm journal. A 6005 bearing envelope (25 × 47 × 12 mm) supports the opposite fork arm. Both sides of the fork rotate together; the rear journal stays with the actuator housing.
- Shoulder-to-elbow distance is 260 mm. Fork rails are nominally 34 mm wide × 10 mm thick, with transverse braces, ending in an elbow housing reference of 60 mm OD and 25 mm through-bore. The elbow drive is not designed.
- Existing neck 6005 bearing and servo placeholder are retained. The generic yaw output uses a 25 mm journal, 40 mm flange, four M3 clearance holes on 32 mm PCD and a 10 mm axial passage. The head has a matching flange socket. The actual servo spline/coupler and collar fastening remain to design.
- The electronics enclosure sits above the battery. Overall size including lid is 150 W × 86 D × 93 H mm. Main internal cavity is 144 × 80 × 87 mm before corner bosses. The body/lid have ventilation, two rear cable openings, and removable mounting/screw references. Board-specific standoffs and ports await the host computer and electronics selection.
- The old waist motor layout, rearward straight spine and battery placement are retained. Nominal robot height remains 1600.2 mm above the inherited foot-floor datum. Shoulder axis height is 1340.2 mm above that datum.

## Design status

This is editable packaging and mechanism concept CAD. Nominal bearing fits are not manufacturing tolerances. Thin spine wall, printed members, bearing loads, fasteners, fatigue and impacts have not been structurally qualified. The simplified one-piece bearing rings stand for complete bearings and do not model internal rolling contacts. Screw/nut references are simplified; final lengths, inserts/captures and thread engagement require detailing. The shell remains the existing continuous envelope; access panels and print splits remain future work.

Shoulder actuator internals, torque/speed/thermal limits, elbow actuator, neck coupling, cable routing, electronics board fits, final bearing retention and printable assembly details are open. Do not treat this revision as a manufacturing-ready or simulation-ready robot.

For fabrication, split the generic pitch hub's inboard retaining collar into a removable part or substitute the selected actuator's actual output interface so the bearing can be installed. Neck outer-race retention, servo spline coupling and the shell's service/print splits also need detailing.

## Verification files

Use `validation.json`, `motion_report.json`, `archive_reopen.json` and `saved_release.json` for measured results. Native motion checks and sampled intersections are distinct from a continuous swept-volume check. Source and abandoned V-spine revisions are preserved.

Measured in the final working model: 100 positive-volume, single-lump solid bodies; no reported feature health issues in the new components; zero intersections among the selected non-fastener structural/interface bodies and retained spine/battery at neutral. Simplified hardware/thread engagement is excluded from that clearance assertion. Spine, battery and both waist crank/output bounding boxes match the pre-joint baseline.

All five native motion tests pass, with zero error at the recorded 0.000001 mm precision for precise bounds and at most 5.7e-14 native-matrix coefficient error. Each returns to neutral with zero recorded error. Tested commands: left/right pitch +15 degrees, left roll +15 degrees, right roll -15 degrees, neck yaw +30 degrees. All 30 separate temporary-body collision samples pass (each arm, pitch -90/-45/0/45/90 degrees combined with outward roll 0/45/90 degrees). These samples are not a certified continuous workspace, and do not validate inward roll, cables, actuator internals or all existing leg geometry.

The earlier coarse `boundingBox` rotation comparison was rejected because cached conservative bounds differ between native and temporary bodies. `motion_aabb_diagnostic.json` preserves that diagnostic; `motion_report.json` uses `preciseBoundingBox` plus independently calculated occurrence transforms.
