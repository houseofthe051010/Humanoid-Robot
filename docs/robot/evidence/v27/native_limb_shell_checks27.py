"""Staged read-only native casing checks; definitions only, never auto-dispatched.

One explicit call checks ONE panel and at most twelve original body proxies.
Importing this module makes zero Fusion calls. Root owns all native dispatch.
"""
import ctypes
import hashlib
import json
import math
import threading
import time
from pathlib import Path


def _bounds27(body):
    box = body.preciseBoundingBox
    return [[float(v)*10 for v in point.asArray()] for point in (box.minPoint, box.maxPoint)]


def _finite27(value):
    return isinstance(value,(int,float)) and not isinstance(value,bool) and math.isfinite(value)


def _valid_bounds27(box):
    return (isinstance(box, list) and len(box) == 2 and all(isinstance(row, list) and len(row) == 3 for row in box)
            and all(_finite27(v) for row in box for v in row) and all(a <= b for a,b in zip(*box)))


def _overlap27(a, b, padding=0):
    return all(a[0][i]-padding <= b[1][i] and b[0][i]-padding <= a[1][i] for i in range(3))


def _same_bounds27(a, b, tolerance=.002):
    return _valid_bounds27(a) and _valid_bounds27(b) and all(abs(x-y) <= tolerance for ar,br in zip(a,b) for x,y in zip(ar,br))


def _private27():
    class Memory(ctypes.Structure):
        _fields_ = [("cb",ctypes.c_ulong),("PageFaultCount",ctypes.c_ulong)] + [
            (name,ctypes.c_size_t) for name in ("PeakWorkingSetSize","WorkingSetSize","QuotaPeakPagedPoolUsage",
            "QuotaPagedPoolUsage","QuotaPeakNonPagedPoolUsage","QuotaNonPagedPoolUsage","PagefileUsage",
            "PeakPagefileUsage","PrivateUsage")]
    stats = Memory(); stats.cb = ctypes.sizeof(stats)
    handle = ctypes.windll.kernel32.GetCurrentProcess; handle.restype = ctypes.c_void_p
    get = ctypes.windll.psapi.GetProcessMemoryInfo
    get.argtypes = [ctypes.c_void_p, ctypes.POINTER(Memory), ctypes.c_ulong]; get.restype = ctypes.c_int
    if not get(handle(),ctypes.byref(stats),stats.cb):
        raise RuntimeError("Native memory guard unavailable")
    return int(stats.PrivateUsage)


def _context27(application, folder):
    import adsk.fusion
    before_path = folder / "casing_before.json"
    before = json.loads(before_path.read_text(encoding="utf-8-sig"))
    if (before.get("capture_schema") != "casing_preservation_v1" or before.get("capture_complete") is not True
            or before.get("capture_errors") or before.get("has_pending_snapshot") is not False
            or len(before.get("actual_angles_rad",{})) != 23):
        raise RuntimeError("Complete, fresh, neutral before capture required")
    if time.time()-float(before.get("generated_epoch",0)) > 6*3600:
        raise RuntimeError("Before capture is stale")
    document = application.activeDocument
    if not document or document.name != "Humanoid_complete_v27":
        raise RuntimeError("Only exact Humanoid_complete_v27 is allowed")
    design = adsk.fusion.Design.cast(document.products.itemByProductType("DesignProductType"))
    if not design or design.snapshots.hasPendingSnapshot:
        raise RuntimeError("No native design or pending snapshot")
    root = design.rootComponent
    occurrences = {"<root>/"+o.fullPathName.replace("+","/"): o for o in root.allOccurrences}
    return design, root, before, before_path, occurrences


def _angles27(root, occurrences, before):
    targets = before["actual_angles_rad"]; actual = {}
    for row in before["joints"]:
        if row["name"] not in targets:
            continue
        owner = root if row["component_path"] == "<root>" else occurrences[row["component_path"]].component
        joint = owner.asBuiltJoints.itemByName(row["name"])
        if not joint or not joint.isValid or joint.isSuppressed:
            raise RuntimeError("Missing/invalid anatomical joint: "+row["name"])
        actual[row["name"]] = float(joint.jointMotion.rotationValue)
    if set(actual) != set(targets) or any(not math.isfinite(actual[n]) or
            abs(math.atan2(math.sin(actual[n]-targets[n]),math.cos(actual[n]-targets[n]))) > 1e-6 for n in targets):
        raise RuntimeError("All 23 anatomical angles must match the before capture")
    return actual


def print_split_plan27(bounds_mm, usable_height_mm=180, seam_gap_mm=.4):
    """Pure file-only plan: horizontal splits in assembled Z, no CAD modification.

    Assumes upright prints; the printer/bed is unselected. A 316 mm shin yields
    two ~158 mm segments. Final retention/lips and actual oriented bed fit remain.
    """
    if not _valid_bounds27(bounds_mm) or not math.isfinite(usable_height_mm) or usable_height_mm <= 0:
        raise ValueError("Valid bounds and positive usable print height required")
    z0,z1 = bounds_mm[0][2],bounds_mm[1][2]
    count = max(1,math.ceil((z1-z0)/usable_height_mm))
    cuts = [z0+(z1-z0)*index/count for index in range(1,count)]
    return {"planning_only": True, "printer_size_is_assumed": True, "usable_height_mm": usable_height_mm,
            "piece_count": count, "cut_planes_world_z_mm": cuts, "suggested_split_gap_mm": seam_gap_mm,
            "segment_height_before_gap_mm": (z1-z0)/count,
            "full_bounds_mm": bounds_mm, "footprint_mm": [bounds_mm[1][i]-bounds_mm[0][i] for i in (0,1)],
            "scope": "Separate upper/lower PRINTED skin parts only; do not cut, drill or lengthen any original frame/rail. Front and rear calf panels each require this split.",
            "remaining": "Add removable cosmetic joining lips/retention, check actual oriented bed dimensions and seam hardware clearance before claiming print-ready."}


ALLOWED_REPLACED_COSMETIC_IDS27 = frozenset({
    "<root>/Upper_body_v26:1/T01_Torso_shell_2p5mm_concept:1/T01_torso_shell_with_neck_retainer_clearance",
})


def check_limb_panel27(application, region, side, panel, batch_start=0, batch_size=8, folder=None, attempt="static"):
    """Backward-compatible exact limb naming wrapper; no auto-dispatch."""
    if region not in ("shin","thigh") or side not in ("Left","Right") or panel not in ("front","rear"):
        raise ValueError("Exact shin/thigh, Left/Right, front/rear required")
    return check_casing_panel27(application,"C27_"+side+"_"+region+"_"+panel,
                               batch_start,batch_size,folder,attempt)


def check_casing_panel27(application, component_name, batch_start=0, batch_size=8, folder=None,
                         attempt="static", replaced_cosmetic_body_ids=None, minimum_clearance_mm=0):
    """Read-only exact neutral overlap test of one new panel, one small batch.

    Complete only after every candidate batch passes. Broad-phase rejection uses
    fresh before-capture world bounds; narrow phase uses current placed body
    proxies and copied temporary BRep intersections. No original is modified.
    """
    import adsk.core
    import adsk.fusion
    if threading.current_thread() is not threading.main_thread():
        raise RuntimeError("Root must dispatch on Fusion main thread")
    if (not isinstance(component_name,str) or not component_name.startswith("C27_")
            or any(not (c.isalnum() or c in "_-") for c in component_name)):
        raise ValueError("Use one exact safe C27 component name, no pattern or prefix matching")
    if not isinstance(batch_start,int) or batch_start < 0 or not isinstance(batch_size,int) or not 1 <= batch_size <= 12:
        raise ValueError("Use a nonnegative start and batch size 1..12")
    if not isinstance(attempt,str) or not attempt or any(not (c.isalnum() or c in "_-") for c in attempt):
        raise ValueError("Use a safe nonempty attempt label")
    if not _finite27(minimum_clearance_mm) or not 0 <= minimum_clearance_mm <= 10:
        raise ValueError("Optional static distance target must be a finite 0..10 mm")
    folder = Path(folder or r"E:\Aditya\robot_sim\outputs\shin_cad_20260912\v27")
    design,root,before,before_path,occurrences = _context27(application,folder)
    angles_before = _angles27(root,occurrences,before)
    name = component_name
    matching = [o for o in occurrences.values() if o.component.name == name]
    if len(matching) != 1:
        raise RuntimeError("Exact new panel missing/ambiguous: "+name)
    occurrence = matching[0]
    bodies = list(occurrence.bRepBodies)
    if len(bodies) != 1:
        raise RuntimeError("Panel must contain exactly one body")
    skin = bodies[0]
    volume = float(skin.volume)*1000
    if not skin.isSolid or skin.lumps.count != 1 or not math.isfinite(volume) or volume <= 0:
        raise RuntimeError("Panel must be a positive single connected solid (one BRep lump)")
    skin_bounds = _bounds27(skin)
    planning = before.get("planning",{}).get("visible_physical_breps")
    if not isinstance(planning,list):
        raise RuntimeError("Before capture lacks fresh visible root-context geometry bounds")
    exclusions = set(replaced_cosmetic_body_ids or [])
    if not exclusions <= ALLOWED_REPLACED_COSMETIC_IDS27:
        raise ValueError("Only the explicitly replaced original cosmetic T01 torso skin may be excluded; no structural exclusions")
    before_ids = {row["component_path"]+"/"+row["name"] for row in before["bodies"]}
    if not exclusions <= before_ids:
        raise ValueError("Excluded cosmetic torso ID is absent from the fresh before capture")
    candidates = []
    for row in planning:
        if row["component_path"]+"/"+row["name"] in exclusions:
            continue
        box = row.get("bounds_world_mm")
        if not _valid_bounds27(box):
            raise RuntimeError("Invalid before geometry bounds")
        if _overlap27(skin_bounds,box,minimum_clearance_mm+.002):
            candidates.append(row)
    candidates.sort(key=lambda r:r["component_path"]+"/"+r["name"])
    selected = candidates[batch_start:batch_start+batch_size]
    ids = [r["component_path"]+"/"+r["name"] for r in candidates]
    report = {"schema":1,"read_only":True,"native_mutations":0,"pass":False,"panel":name,
              "before_sha256":hashlib.sha256(before_path.read_bytes()).hexdigest(),"skin_bounds_mm":skin_bounds,
              "skin_volume_mm3":volume,"skin_lumps":skin.lumps.count,"candidate_count":len(candidates),
              "skin_face_count":skin.faces.count,"skin_edge_count":skin.edges.count,
              "candidate_ids":ids,"batch_start":batch_start,"batch_size":batch_size,"checks":[],
              "excluded_original_cosmetic_ids":sorted(exclusions),"minimum_clearance_target_mm":minimum_clearance_mm,
              "angles_before_rad":angles_before,"print_split":print_split_plan27(skin_bounds),
              "scope":"Actual static pose only; optional native minimum distance is explicitly recorded. Not swept clearance, minimum 2.5 mm wall, fit/strength/thermal or manufacturing qualification."}
    out = folder / (name+"_clearance_"+attempt+"_"+str(batch_start).zfill(3)+".json")
    if out.exists():
        raise RuntimeError("Evidence exists; preserve it and choose a new attempt label")
    begin = time.time(); memory = _private27()
    report.update(started_epoch=begin,memory_before_bytes=memory)
    def persist():
        out.write_text(json.dumps(report,indent=2),encoding="utf-8")
    def guard():
        current = _private27()
        if current > 24*1024**3 or current-memory > 512*1024**2 or time.time()-begin > 60:
            raise RuntimeError("Read-only clearance batch exceeded memory/time budget")
        return current
    persist()
    manager = adsk.fusion.TemporaryBRepManager.get()
    try:
        for row in selected:
            guard()
            owner = root if row["component_path"] == "<root>" else occurrences[row["component_path"]]
            matches = [body for body in owner.bRepBodies if body.name == row["name"]]
            if len(matches) != 1:
                raise RuntimeError("Original placed body missing/ambiguous")
            original = matches[0]; actual_bounds = _bounds27(original)
            if not _same_bounds27(actual_bounds,row["bounds_world_mm"]):
                raise RuntimeError("Original current precise bounds changed since before capture")
            check = {"original":row["component_path"]+"/"+row["name"],"actual_bounds_world_mm":actual_bounds}
            if not _overlap27(skin_bounds,actual_bounds):
                check.update(intersection_mm3=0.0,method="Actual precise bounds disjoint")
            else:
                intersection = manager.copy(skin)
                if not manager.booleanOperation(intersection,manager.copy(original),adsk.fusion.BooleanTypes.IntersectionBooleanType):
                    raise RuntimeError("Native intersection Boolean failed; cannot classify as clear")
                overlap = float(intersection.volume)*1000
                if not math.isfinite(overlap) or overlap < -1e-8:
                    raise RuntimeError("Invalid native intersection volume")
                check.update(intersection_mm3=max(0.0,overlap),method="TemporaryBRep intersection of actual root-context proxies")
            check["pass"] = check["intersection_mm3"] <= .01
            if minimum_clearance_mm > 0:
                if check["intersection_mm3"] > .01:
                    check["minimum_distance_mm"] = 0.0
                else:
                    # Installed core.py explicitly supports persistent BRepBody
                    # inputs and centimetre-valued results. Do not assume a
                    # TemporaryBRep offset/inflation API exists.
                    measurement = application.measureManager.measureMinimumDistance(skin,original)
                    distance = float(measurement.value)*10 if measurement else None
                    if not _finite27(distance) or distance < 0:
                        raise RuntimeError("Native minimum-distance measurement failed")
                    check["minimum_distance_mm"] = distance
                check["minimum_clearance_pass"] = check["minimum_distance_mm"] >= minimum_clearance_mm-.002
                check["pass"] = check["pass"] and check["minimum_clearance_pass"]
            report["checks"].append(check); persist(); guard()
        report["angles_after_rad"] = _angles27(root,occurrences,before)
        report["has_pending_snapshot_after"] = design.snapshots.hasPendingSnapshot
        if report["has_pending_snapshot_after"]:
            raise RuntimeError("Read-only check must not leave a pending position snapshot")
        report["batch_complete"] = len(report["checks"]) == len(selected)
        report["all_candidates_covered_by_this_job"] = batch_start == 0 and len(selected) == len(candidates)
        report["pass"] = report["batch_complete"] and all(r["pass"] for r in report["checks"])
        report["memory_after_bytes"] = guard(); report["elapsed_seconds"] = time.time()-begin
        persist(); return report
    except Exception as error:
        report["error"] = repr(error); report["elapsed_seconds"] = time.time()-begin; persist(); raise


def merge_panel_checks27(reports):
    """Pure offline coverage check; cannot turn a partial batch into full PASS."""
    if not reports:
        raise ValueError("Need reports")
    first = reports[0]; expected = first["candidate_ids"]; seen = {}
    for report in reports:
        if any(report.get(k) != first.get(k) for k in ("panel","before_sha256","skin_bounds_mm","candidate_ids",
                                                       "skin_lumps","skin_face_count","skin_edge_count",
                                                       "excluded_original_cosmetic_ids","minimum_clearance_target_mm")):
            raise ValueError("Mixed source, panel geometry or candidate lists")
        if first.get("skin_volume_mm3") is not None:
            a,b = report.get("skin_volume_mm3"),first["skin_volume_mm3"]
            if not _finite27(a) or not _finite27(b) or abs(a-b) > max(.01,abs(b)*1e-7):
                raise ValueError("Panel volume changed between batches")
        if not report.get("pass") or not report.get("batch_complete") or report.get("error"):
            raise ValueError("Failed/incomplete batch")
        for check in report["checks"]:
            if check["original"] in seen:
                raise ValueError("Duplicate body check")
            if check["original"] not in expected or check.get("pass") is not True or not _finite27(check.get("intersection_mm3")) or not 0 <= check["intersection_mm3"] <= .01:
                raise ValueError("Unexpected body or nonclear intersection")
            target = first.get("minimum_clearance_target_mm",0)
            if target > 0 and (check.get("minimum_clearance_pass") is not True or
                    not _finite27(check.get("minimum_distance_mm")) or check["minimum_distance_mm"] < target-.002):
                raise ValueError("Minimum-distance target not satisfied")
            seen[check["original"]] = check
    complete = set(seen) == set(expected)
    return {"read_only":True,"panel":first["panel"],"pass":complete,
            "coverage_complete":complete,"candidate_count":len(expected),"checked_count":len(seen),
            "excluded_original_cosmetic_ids":first.get("excluded_original_cosmetic_ids",[]),
            "minimum_clearance_target_mm":first.get("minimum_clearance_target_mm",0),
            "missing":sorted(set(expected)-set(seen)),"scope":first["scope"]}
