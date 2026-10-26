"""Root-dispatchable, bounded, read-only Fusion capture for v27.

This file is only authored/syntax-checked by the documentation agent. Root must
dispatch it on Fusion's main thread. No legacy top-level jobs are executed.
"""
import ctypes
import json
import math
import threading
import time
from pathlib import Path


def capture27_private_bytes():
    class Counters(ctypes.Structure):
        _fields_ = [("cb", ctypes.c_ulong), ("PageFaultCount", ctypes.c_ulong),
                    ("PeakWorkingSetSize", ctypes.c_size_t), ("WorkingSetSize", ctypes.c_size_t),
                    ("QuotaPeakPagedPoolUsage", ctypes.c_size_t), ("QuotaPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t), ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
                    ("PagefileUsage", ctypes.c_size_t), ("PeakPagefileUsage", ctypes.c_size_t),
                    ("PrivateUsage", ctypes.c_size_t)]
    counters = Counters(); counters.cb = ctypes.sizeof(counters)
    get_process = ctypes.windll.kernel32.GetCurrentProcess
    get_process.restype = ctypes.c_void_p
    get_memory = ctypes.windll.psapi.GetProcessMemoryInfo
    get_memory.argtypes = [ctypes.c_void_p, ctypes.POINTER(Counters), ctypes.c_ulong]
    get_memory.restype = ctypes.c_int
    handle = get_process()
    if not get_memory(handle, ctypes.byref(counters), counters.cb):
        raise RuntimeError("Unable to read native process memory guard")
    return int(counters.PrivateUsage)


def capture27_path(occurrence):
    return "<root>/" + occurrence.fullPathName.replace("+", "/")


def capture27_native(entity):
    # Do not use wrapper truthiness or assume one nativeObject hop removes all
    # nested context. Geometry signatures remain in the actual native component.
    current = entity
    for _ in range(16):
        native = current.nativeObject
        if native is None:
            return current
        if native == current:
            # This SDK can return a fresh Python wrapper of the SAME native
            # entity forever. Native equality ends that chain only after the
            # assembly context has disappeared; do not equate hierarchy proxies.
            if native.assemblyContext is not None:
                raise RuntimeError("nativeObject equality retained assembly context")
            return native
        current = native
    raise RuntimeError("Unable to normalize nativeObject after 16 hops")


def capture27_token(entity, root_context_entity=None):
    native = capture27_native(entity)
    try:
        value = native.entityToken
        domain = "fully-unwrapped native object"
    except RuntimeError:
        # Only caller-provided root-context proxies are eligible. Fusion can
        # reject tokens from nested native occurrence wrappers; no identity is
        # invented or reduced to a component/name token in that situation.
        if root_context_entity is None or root_context_entity is native:
            raise
        value = root_context_entity.entityToken
        domain = "explicit root assembly-context proxy"
    if not value:
        raise RuntimeError("Native/root-context entity token unavailable")
    return value, domain


def capture27_bounds(box):
    return [[float(v)*10 for v in point.asArray()] for point in (box.minPoint, box.maxPoint)]


def capture27_union(left, right):
    if left is None:
        return [list(right[0]), list(right[1])]
    return [[min(a, b) for a, b in zip(left[0], right[0])],
            [max(a, b) for a, b in zip(left[1], right[1])]]


def capture27_joint_motion(motion):
    states = {}
    for value_name, limit_name, unit in (
        ("rotationValue", "rotationLimits", "rad"), ("pitchValue", "pitchLimits", "rad"),
        ("yawValue", "yawLimits", "rad"), ("rollValue", "rollLimits", "rad"),
        ("slideValue", "slideLimits", "cm"), ("primarySlideValue", "primarySlideLimits", "cm"),
        ("secondarySlideValue", "secondarySlideLimits", "cm")):
        if not hasattr(motion, value_name):
            continue
        state = {"value": float(getattr(motion, value_name)), "unit": unit}
        if hasattr(motion, limit_name):
            limits = getattr(motion, limit_name)
            state["limits"] = {
                "minimum": limits.minimumValue, "maximum": limits.maximumValue, "rest": limits.restValue,
                "minimum_enabled": limits.isMinimumValueEnabled, "maximum_enabled": limits.isMaximumValueEnabled,
                "rest_enabled": limits.isRestValueEnabled,
            }
        states[value_name] = state
    return states


def run_native_capture27():
    import adsk.core
    import adsk.fusion
    if threading.current_thread() is not threading.main_thread():
        raise RuntimeError("Capture must be dispatched on Fusion's main thread")
    root_dir = Path(globals().get("ROOT", r"E:\Aditya\robot_sim\outputs\shin_cad_20260912"))
    out_dir = root_dir / "v27"; out_dir.mkdir(parents=True, exist_ok=True)
    filename = str(globals().get("PARAM_CAPTURE_FILENAME", "casing_before.json"))
    if Path(filename).name != filename or not filename.endswith(".json") or "/" in filename or "\\" in filename:
        raise RuntimeError("Capture filename must be a simple JSON basename")
    destination = out_dir / filename
    if destination.exists() and not globals().get("PARAM_OVERWRITE", False):
        raise RuntimeError("Capture already exists; root must explicitly authorize overwriting this evidence")
    application = adsk.core.Application.get()
    document = application.activeDocument
    design = adsk.fusion.Design.cast(document.products.itemByProductType("DesignProductType"))
    if not design:
        raise RuntimeError("Active document does not contain a native Fusion Design")
    allowed_names = globals().get("PARAM_ALLOWED_DOCUMENT_NAMES", ("Humanoid_complete_v26", "Humanoid_complete_v27"))
    if document.name not in allowed_names:
        raise RuntimeError("Unexpected active source document: " + document.name)
    target_record = json.loads((root_dir / "v26/final_native_handoff26.json").read_text())
    target_names = set(target_record["body_angles_rad"])
    if len(target_names) != 23:
        raise RuntimeError("v26 target evidence does not contain exactly 23 anatomical axes")
    reference_name = globals().get("PARAM_REFERENCE_FILENAME")
    if reference_name is None and filename != "casing_before.json":
        reference_name = "casing_before.json"
    references = {}
    if reference_name:
        reference_path = out_dir / str(reference_name)
        reference = json.loads(reference_path.read_text())
        if reference.get("capture_complete") is not True:
            raise RuntimeError("Reference before capture is incomplete")
        for kind in ("bodies", "meshes", "occurrences", "joints"):
            for row in reference[kind]:
                key = row.get("stable_id") or row.get("path") or row["component_path"].rstrip("/") + "/" + row["name"]
                references[(kind, key)] = row
    begin = time.time(); memory_before = capture27_private_bytes()
    max_seconds = float(globals().get("PARAM_CAPTURE_MAX_SECONDS", 90))
    max_growth = int(globals().get("PARAM_CAPTURE_MAX_GROWTH_MB", 1024))*1024*1024
    max_private = int(globals().get("PARAM_CAPTURE_MAX_PRIVATE_MB", 24576))*1024*1024
    report = {
        "capture_schema": "casing_preservation_v1", "capture_complete": False,
        "document": document.name, "generated_epoch": begin, "native_calls": "read-only",
        "cad_mutations": 0, "coordinate_domains": {
            "body_signatures": "native-component millimetres",
            "occurrence_transform": "root assembly context; centimetre translation",
            "owner_local_transform": "native owner local; centimetre translation",
            "joint_frame": "native owner-local current AsBuiltJoint.transform; centimetre translation",
        }, "bodies": [], "meshes": [], "occurrences": [], "joints": [],
        "actual_angles_rad": {}, "capture_errors": [], "planning": {
            "visible_physical_breps": [], "visible_component_world_unions": {},
            "native_part_unions": {}, "named_body_world_unions": {},
            "qualification": "Precise bounding-envelope planning data, not collision clearance or swept workspace.",
        }, "memory_before": memory_before, "reference_filename": reference_name,
        "identity_resolution_scope": "Prior token is resolved natively and resulting objects are compared; raw token text is not used as an equality test.",
    }

    def guard():
        current = capture27_private_bytes()
        if current > max_private or current-memory_before > max_growth:
            raise RuntimeError("Read-only capture exceeded private-memory budget")
        if time.time()-begin > max_seconds:
            raise RuntimeError("Read-only capture exceeded time budget")
        return current

    def identify(row, entity, kind, key, root_context_entity=None):
        native = capture27_native(entity)
        token, domain = capture27_token(entity, root_context_entity)
        row.update(entity_token=token, entity_token_domain=domain, resolved_identity=key)
        previous = references.get((kind, key))
        if previous:
            resolved = design.findEntityByToken(previous["entity_token"])
            equal = any(capture27_native(candidate) == native for candidate in resolved)
            row["prior_token_resolution_match"] = equal
            if not equal:
                row["resolved_identity"] = "UNRESOLVED_OR_DIFFERENT:" + key

    def persist():
        temporary = destination.with_name(destination.name + ".tmp")
        temporary.write_text(json.dumps(report, indent=2), encoding="utf-8")
        temporary.replace(destination)

    try:
        original_document = document.name
        original_modified = document.isModified
        component = design.rootComponent
        occurrences = list(component.allOccurrences)
        report["source_modified_before"] = original_modified
        report["has_pending_snapshot_before"] = design.snapshots.hasPendingSnapshot
        components = [("<root>", component)]
        for occurrence in occurrences:
            guard()
            path = capture27_path(occurrence)
            native_occurrence = capture27_native(occurrence)
            row = {
                "path": path, "name": occurrence.name, "component": occurrence.component.name,
                "transform_cm": list(occurrence.transform2.asArray()),
                "owner_local_transform_cm": list(native_occurrence.transform2.asArray()),
                "ground_to_parent": native_occurrence.isGroundToParent, "visible": occurrence.isVisible,
            }
            identify(row, occurrence, "occurrences", path, occurrence)
            report["occurrences"].append(row)
            if not any(existing == occurrence.component for _, existing in components):
                components.append((path, occurrence.component))
        physical_cache = []
        for path, owner in [("<root>", component)] + [(capture27_path(o), o) for o in occurrences]:
            guard()
            for body in owner.bRepBodies:
                guard()
                native = capture27_native(body)
                cached = next((data for prior, data in physical_cache if prior == native), None)
                if cached is None:
                    properties = native.physicalProperties
                    cached = {
                        "volume_mm3": float(properties.volume)*1000,
                        "centroid_mm": [float(v)*10 for v in properties.centerOfMass.asArray()],
                        "bounds_mm": capture27_bounds(native.preciseBoundingBox), "solid": native.isSolid,
                        "area_mm2": float(properties.area)*100, "face_count": native.faces.count,
                        "edge_count": native.edges.count, "vertex_count": native.vertices.count,
                    }
                    physical_cache.append((native, cached))
                row = {"component_path": path, "name": native.name, "component": native.parentComponent.name, **cached}
                key = path + "/" + native.name
                identify(row, body, "bodies", key, body)
                report["bodies"].append(row)
                if body.isVisible and (path == "<root>" or owner.isVisible):
                    bounds = capture27_bounds(body.preciseBoundingBox)
                    planning = report["planning"]
                    planning["visible_physical_breps"].append({"component_path": path, "name": native.name, "bounds_world_mm": bounds, "volume_mm3": cached["volume_mm3"]})
                    planning["visible_component_world_unions"][path] = capture27_union(planning["visible_component_world_unions"].get(path), bounds)
                    planning["native_part_unions"][path] = capture27_union(planning["native_part_unions"].get(path), cached["bounds_mm"])
                    planning["named_body_world_unions"][native.name] = capture27_union(planning["named_body_world_unions"].get(native.name), bounds)
            for mesh_body in owner.meshBodies:
                guard()
                native = capture27_native(mesh_body); mesh = native.mesh
                if not mesh:
                    raise RuntimeError("Mesh data unavailable: " + path + "/" + native.name)
                row = {"component_path": path, "name": native.name, "node_count": mesh.nodeCount,
                       "triangle_count": mesh.triangleCount, "bounds_mm": capture27_bounds(native.boundingBox)}
                identify(row, mesh_body, "meshes", path + "/" + native.name, mesh_body)
                report["meshes"].append(row)
        for path, owner in components:
            guard()
            for joint in owner.asBuiltJoints:
                guard(); motion = joint.jointMotion
                frame = joint.transform if int(motion.jointType) != 0 else None
                row = {"component_path": path, "name": joint.name, "type": int(motion.jointType),
                       "valid": joint.isValid, "suppressed": joint.isSuppressed,
                       "motion_state": capture27_joint_motion(motion),
                       "frame_cm": list(frame.asArray()) if frame else None}
                identify(row, joint, "joints", path + "/" + joint.name)
                report["joints"].append(row)
                if joint.name in target_names:
                    if joint.name in report["actual_angles_rad"] or row["type"] != 1:
                        raise RuntimeError("Ambiguous/non-revolute anatomical joint: " + joint.name)
                    report["actual_angles_rad"][joint.name] = float(motion.rotationValue)
        if set(report["actual_angles_rad"]) != target_names:
            raise RuntimeError("Native source does not expose all 23 v26 anatomical joints")
        report["has_pending_snapshot"] = design.snapshots.hasPendingSnapshot
        report["source_modified_after"] = document.isModified
        if document.name != original_document or document.isModified != original_modified:
            raise RuntimeError("Read-only capture changed the source document/modified state")
        report["capture_complete"] = True
    except Exception as error:
        report["capture_errors"].append(str(error))
    finally:
        report["finished_epoch"] = time.time()
        report["memory_after"] = capture27_private_bytes()
        report["row_counts"] = {kind: len(report[kind]) for kind in ("bodies", "meshes", "occurrences", "joints")}
        persist()
    return {"pass": report["capture_complete"], "path": str(destination), "rows": report["row_counts"],
            "body_axis_count": len(report["actual_angles_rad"]), "errors": report["capture_errors"],
            "private_growth_bytes": report["memory_after"]-memory_before, "cad_mutations": 0}


if not globals().get("CAPTURE_DEFINITIONS_ONLY", False):
    cancel_marker = Path(globals().get("ROOT", r"E:\Aditya\robot_sim\outputs\shin_cad_20260912")) / "v27" / "cancel_capture.flag"
    if cancel_marker.exists():
        result = {"pass": False, "canceled": True, "cad_mutations": 0,
                  "reason": "Root canceled the unconsumed request while native/UI access was unavailable."}
    else:
        result = run_native_capture27()
