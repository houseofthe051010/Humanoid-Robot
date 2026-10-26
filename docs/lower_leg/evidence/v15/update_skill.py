from pathlib import Path
p=Path(r'C:\Users\rshan\.codex\skills\humanoid-robot-training\SKILL.md')
s=p.read_text(encoding='utf-8').replace("September 2026 v14 enclosed-adapter correction based on the user's live v13", "September 2026 v15 slide-on motor mounts and waist layout based on the user's live v14")
p.write_text(s,encoding='utf-8')
p=p.parent/'references/fusion-lower-leg-workflow.md';s=p.read_text(encoding='utf-8')
head='## Current v15 slide-on mounts and waist yaw'
if head not in s:
 s=s.replace('## Current v14 enclosed oval adapter','## Historical v14 enclosed oval adapter')
 i=s.index('## Historical v14')
 s=s[:i]+'''## Current v15 slide-on mounts and waist yaw

Native: `E:\\Aditya\\robot_sim\\outputs\\shin_cad_20260912\\v15\\deliverables\\Legs_and_waist_v15.f3d`. Repo record/BOM: `docs/lower_leg/UPPER_LEG_V15.md` and `BOM_V15.csv`; geometry, motion and archive checks in `docs/lower_leg/evidence/v15`. It imports the full preserved live v14 archive and retains 101 native joints per leg. Native lower-leg positions and the previous5mm lowering are unchanged.

User preferences: knee motor mounts should be continuous slide-on oval sleeves, not split clamps. P15 is a125mm rear sleeve with broad curved load spread; P05 is a78mm sleeve with upper180-degree curved shell joining the top and both sides, lower half open. Their bores are10.2×18.2mm for the existing10X×18Y tubes. Old P04 caps/P10/P11 are hidden, clamp M4 hardware removed; fourM3 axial case ties retained. New plastic is not structurally qualified. The thicker rear mount occupies the old5mm encoder reservation: do not continue claiming that encoder fits. Three phase-wire passages were restored.

Hip pitch now has110mm OD×50mm depth at25degrees: front mounting faces fixed,10mm extra only behind. The user clarified the new central7010 motor is **waist yaw, vertical shaft**, not waist roll. W01 duplicates existing vendor geometry atX0/Y23.343134, bottomZ876/output top aboutZ904. W02/W03 are curved printed waist halves, nominal5mm section offsets and6mm pitch barrels; exact envelope cuts,0.4mm seam and M4 seam provisions. Waist is an independent standing-pose reference, not an articulated pelvis. Motors, support bearings, print fits, axial sleeve retention and fasteners remain provisional. User has deferred further chain calculations; preserve sprocket/bracket geometry unless explicitly requested.

API lessons: Native BaseFeature replacement can preserve the component identity and existing joints: remove the old body with a RemoveFeature, add temporary BRep in a new edited BaseFeature and finishEdit. Keep construction lofts hidden in a named non-part component, excluded from exports/BOM. Ellipse major radius must be the larger radius; transform model coordinates with modelToSketchSpace and account for construction-plane normal when offsetting. Successful Boolean unions may leave detached solid shells or sealed old holes. Inspect `body.shells` and `shell.isVoid`: remove entire detached shells by `TemporaryBRepManager.deleteFaces`, retaining all faces of the intended main shell; remove an entire obsolete void shell to fill it. Never delete arbitrary surface subsets without checking closure. Validate positive volume, a single non-void shell, enclosure sections and neighboring-body intersections afterward. Do not treat shell count alone as connected-solid count when internal voids exist. Capture after the mutation job finishes; reopen the archive and verify native joints before claiming delivery.

''' +s[i:]
 p.write_text(s,encoding='utf-8')
print('Updated CAD skill routing and v15 interaction lessons.')
