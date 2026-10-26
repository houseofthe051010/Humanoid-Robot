"""File-only before/after audit for cosmetic casings; never calls Fusion.

Run with fresh native capture JSON files. Historical v26 release rows alone lack
centroid/precise-bound identity evidence and cannot produce a qualified pass.
"""
import argparse
import fnmatch
import hashlib
import json
import math
from pathlib import Path


DEFAULT_TOLERANCES = {
    "distance_mm": 0.002,
    "volume_absolute_mm3": 0.01,
    "volume_relative": 1e-7,
    "area_absolute_mm2": 0.01,
    "area_relative": 1e-7,
    "matrix_entry": 1e-7,
    "angle_rad": 1e-6,
}


def signature(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def identity(row, kind):
    """Canonical component/occurrence paths are independent of document names."""
    if row.get("stable_id"):
        return str(row["stable_id"])
    if kind == "occurrences":
        return str(row.get("path") or row.get("occurrence_path") or "")
    owner = row.get("component_path") or row.get("owner_path")
    if not owner or not row.get("name"):
        return ""
    return str(owner).rstrip("/") + "/" + str(row["name"])


def finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def numeric_sequence(value, count):
    return isinstance(value, list) and len(value) == count and all(finite(v) for v in value)


def vector_match(a, b, tolerance, count=3):
    return numeric_sequence(a, count) and numeric_sequence(b, count) and all(abs(x-y) <= tolerance for x, y in zip(a, b))


def bounds_match(a, b, tolerance):
    return (isinstance(a, list) and isinstance(b, list) and len(a) == len(b) == 2
            and all(vector_match(x, y, tolerance) for x, y in zip(a, b))
            and all(lo <= hi for lo, hi in zip(a[0], a[1]))
            and all(lo <= hi for lo, hi in zip(b[0], b[1])))


def matrix_match(a, b, tolerances):
    if a is None or b is None:
        return a is None and b is None
    return numeric_sequence(a, 16) and numeric_sequence(b, 16) and all(
        abs(x-y) <= (tolerances["distance_mm"]/10 if i in (3, 7, 11) else tolerances["matrix_entry"])
        for i, (x, y) in enumerate(zip(a, b)))


def scalar_match(a, b, absolute, relative=0):
    return finite(a) and finite(b) and abs(a-b) <= max(absolute, abs(b)*relative)


def motion_match(a, b, tolerances):
    if not isinstance(a, dict) or not isinstance(b, dict) or set(a) != set(b):
        return False
    for name, old in b.items():
        new = a[name]
        if not isinstance(old, dict) or not isinstance(new, dict):
            return False
        if new.get("unit") != old.get("unit") or not finite(new.get("value")) or not finite(old.get("value")):
            return False
        tol = tolerances["angle_rad"] if old["unit"] == "rad" else tolerances["distance_mm"]/10
        delta = new["value"] - old["value"]
        if old["unit"] == "rad":
            delta = math.atan2(math.sin(delta), math.cos(delta))
        if abs(delta) > tol:
            return False
        la, lb = new.get("limits", {}), old.get("limits", {})
        if not isinstance(la, dict) or not isinstance(lb, dict):
            return False
        if set(la) != set(lb):
            return False
        for field, value in lb.items():
            if field.endswith("_enabled"):
                if la[field] != value:
                    return False
            elif not scalar_match(la[field], value, tol):
                return False
    return True


def matches_policy(row, key, patterns):
    values = (key, row.get("component", ""), row.get("component_path", ""), row.get("name", ""))
    return any(fnmatch.fnmatchcase(str(value), pattern) for pattern in patterns for value in values)


def compare(before, after, policy=None):
    policy = policy or {}
    tolerances = dict(DEFAULT_TOLERANCES)
    tolerances.update(policy.get("tolerances", {}))
    report = {
        "schema": 1, "file_only": True, "native_calls": 0, "cad_mutations": 0,
        "pass": False, "errors": [], "token_drift": [], "authorized_cosmetic_changes": [],
        "added": {}, "original_counts": {}, "tolerances": tolerances,
        "scope": "Original identity/path, physical signatures, placed/local occurrence poses and grounds, all original joint states/configuration, 23 anatomical values and existing meshes. Added declared skins and rigid cover attachments are separate.",
        "limitations": "Matching volume/centroid/bounds/area/topology is a signature audit, not exact BRep identity or a full swept collision/strength/thermal qualification. Raw Fusion entity-token text is not a persistent geometry identifier; token drift alone is diagnostic, while canonical paths/stable IDs must still match.",
    }
    errors = report["errors"]
    for name, value in tolerances.items():
        if name not in DEFAULT_TOLERANCES or not finite(value) or value < 0:
            errors.append({"category": "policy", "key": name, "reason": "Tolerance must be a known, finite, non-negative number"})
    if errors:
        return report
    if before.get("capture_schema") != "casing_preservation_v1" or after.get("capture_schema") != "casing_preservation_v1":
        errors.append({"category": "capture_schema", "reason": "Need fresh casing_preservation_v1 captures, not legacy volume-only export rows"})
    if before.get("capture_complete") is not True or after.get("capture_complete") is not True:
        errors.append({"category": "capture_schema", "reason": "Both native captures must explicitly be complete"})
    if before.get("coordinate_domains") != after.get("coordinate_domains") or not before.get("coordinate_domains"):
        errors.append({"category": "coordinate_domains", "reason": "Native local and assembly/root-context domains must be recorded identically"})
    for phase, capture in (("before", before), ("after", after)):
        if capture.get("has_pending_snapshot") is not False:
            errors.append({"category": "snapshot", "phase": phase, "reason": "Capture must explicitly have no pending position snapshot"})

    for kind in ("bodies", "meshes", "occurrences", "joints"):
        indexed = []
        for phase, capture in (("before", before), ("after", after)):
            rows = capture.get(kind)
            if not isinstance(rows, list):
                errors.append({"category": "capture_schema", "phase": phase, "kind": kind, "reason": "Missing list"})
                rows = []
            entries = {}
            for row in rows:
                if not isinstance(row, dict):
                    errors.append({"category": "capture_schema", "phase": phase, "kind": kind, "reason": "Row must be an object"})
                    continue
                key = identity(row, kind)
                if not key or key in entries:
                    errors.append({"category": "identity", "phase": phase, "kind": kind, "key": key, "reason": "Missing or duplicate canonical identity"})
                else:
                    entries[key] = row
                if not isinstance(row.get("entity_token"), str) or not row["entity_token"]:
                    errors.append({"category": "identity", "phase": phase, "kind": kind, "key": key, "reason": "Fresh native entity token is required for resolution evidence"})
                if not isinstance(row.get("resolved_identity"), str) or not row["resolved_identity"]:
                    errors.append({"category": "identity", "phase": phase, "kind": kind, "key": key, "reason": "Native resolved identity must be recorded"})
            indexed.append(entries)
        old, new = indexed
        if kind == "bodies":
            for key in policy.get("authorized_original_cosmetic_body_ids", []):
                if key not in old:
                    errors.append({"category": "policy", "key": key, "reason": "Authorized cosmetic body is absent from the before capture"})
        report["original_counts"][kind] = len(old)
        report["added"][kind] = []
        for key, row in old.items():
            is_cosmetic = kind == "bodies" and key in policy.get("authorized_original_cosmetic_body_ids", [])
            if key not in new:
                if is_cosmetic and policy.get("allow_cosmetic_body_removal") is True:
                    report["authorized_cosmetic_changes"].append({"key": key, "change": "Removed authorized original cosmetic body"})
                else:
                    errors.append({"category": "missing_original", "kind": kind, "key": key})
                continue
            current = new[key]
            if row.get("entity_token") and current.get("entity_token") and row["entity_token"] != current["entity_token"]:
                report["token_drift"].append({"kind": kind, "key": key})
            if row.get("resolved_identity") is not None and current.get("resolved_identity") != row["resolved_identity"]:
                errors.append({"category": "resolved_identity", "kind": kind, "key": key})
            failed = []
            if kind == "bodies":
                required = ("volume_mm3", "centroid_mm", "bounds_mm", "solid")
                if any(field not in row or field not in current for field in required):
                    failed.append("missing_physical_signature")
                else:
                    if not scalar_match(current["volume_mm3"], row["volume_mm3"], tolerances["volume_absolute_mm3"], tolerances["volume_relative"]): failed.append("volume_mm3")
                    if not vector_match(current["centroid_mm"], row["centroid_mm"], tolerances["distance_mm"]): failed.append("centroid_mm")
                    if not bounds_match(current["bounds_mm"], row["bounds_mm"], tolerances["distance_mm"]): failed.append("bounds_mm")
                    if current["solid"] != row["solid"]: failed.append("solid")
                for field in ("area_mm2", "face_count", "edge_count", "vertex_count", "geometry_sha256"):
                    if field in row:
                        equal = scalar_match(current.get(field), row[field], tolerances["area_absolute_mm2"], tolerances["area_relative"]) if field == "area_mm2" else current.get(field) == row[field]
                        if not equal: failed.append(field)
                if failed and is_cosmetic and "missing_physical_signature" not in failed:
                    if (current.get('solid') is not True or not finite(current.get('volume_mm3')) or current['volume_mm3'] <= 0
                            or not numeric_sequence(current.get('centroid_mm'), 3)
                            or not bounds_match(current.get('bounds_mm'), current.get('bounds_mm'), 0)):
                        errors.append({"category":"cosmetic_body", "key":key, "reason":"Modified cosmetic cover must remain a positive-volume solid with valid centroid/bounds"})
                    report["authorized_cosmetic_changes"].append({"key": key, "fields": failed})
                    failed = []
            elif kind == "meshes":
                for field in ("node_count", "triangle_count"):
                    if field not in row or current.get(field) != row[field]: failed.append(field)
                if not bounds_match(current.get("bounds_mm"), row.get("bounds_mm"), tolerances["distance_mm"]): failed.append("bounds_mm")
                for field in ("vertex_sha256", "triangle_sha256"):
                    if field in row and current.get(field) != row[field]: failed.append(field)
            elif kind == "occurrences":
                for field in ("component", "ground_to_parent"):
                    if field not in row or current.get(field) != row[field]: failed.append(field)
                for field in ("transform_cm", "owner_local_transform_cm"):
                    if not numeric_sequence(current.get(field), 16) or not numeric_sequence(row.get(field), 16) or not matrix_match(current.get(field), row.get(field), tolerances): failed.append(field)
            elif kind == "joints":
                for field in ("type", "valid", "suppressed"):
                    if field not in row or current.get(field) != row[field]: failed.append(field)
                if not current.get("valid"): failed.append("invalid_joint")
                if not motion_match(current.get("motion_state"), row.get("motion_state"), tolerances): failed.append("motion_state")
                if "frame_cm" not in row or not matrix_match(current.get("frame_cm"), row.get("frame_cm"), tolerances): failed.append("frame_cm")
                if row.get("type") != 0 and (not numeric_sequence(row.get("frame_cm"), 16) or not numeric_sequence(current.get("frame_cm"), 16)):
                    failed.append("missing_nonrigid_frame")
            if failed:
                errors.append({"category": "changed_original", "kind": kind, "key": key, "fields": failed})
        for key in sorted(set(new) - set(old)):
            row = new[key]
            report["added"][kind].append(key)
            patterns = policy.get("allowed_new_joint_patterns", []) if kind == "joints" else policy.get("allowed_added_patterns", [])
            if not matches_policy(row, key, patterns):
                errors.append({"category": "undeclared_addition", "kind": kind, "key": key})
            if kind == "joints" and (row.get("type") != 0 or row.get("valid") is not True or row.get("suppressed") is not False):
                errors.append({"category": "new_joint", "key": key, "reason": "Only declared valid unsuppressed rigid cover attachments may be added"})
            if kind == "bodies" and (row.get("solid") is not True or not finite(row.get("volume_mm3")) or row["volume_mm3"] <= 0
                                      or not numeric_sequence(row.get("centroid_mm"), 3)
                                      or not bounds_match(row.get("bounds_mm"), row.get("bounds_mm"), 0)):
                errors.append({"category": "new_body", "key": key, "reason": "Added cover must be a positive-volume solid with valid centroid/bounds"})

    old_angles, new_angles = before.get("actual_angles_rad", {}), after.get("actual_angles_rad", {})
    if not isinstance(old_angles, dict) or not isinstance(new_angles, dict):
        errors.append({"category": "body_axes", "reason": "Anatomical values must be objects keyed by joint name"})
        old_angles = old_angles if isinstance(old_angles, dict) else {}
        new_angles = new_angles if isinstance(new_angles, dict) else {}
    if len(old_angles) != 23 or set(old_angles) != set(new_angles):
        errors.append({"category": "body_axes", "reason": "The original 23 anatomical axis names must be retained exactly"})
    for key in old_angles:
        if not scalar_match(new_angles.get(key), old_angles[key], tolerances["angle_rad"]):
            errors.append({"category": "body_axis_angle", "key": key})
    for phase, capture, angles in (("before", before, old_angles), ("after", after, new_angles)):
        joint_rows = capture.get("joints", [])
        if not isinstance(joint_rows, list):
            joint_rows = []
        for name, angle in angles.items():
            rows = [row for row in joint_rows if isinstance(row, dict) and row.get("name") == name]
            if len(rows) != 1 or rows[0].get("type") != 1:
                errors.append({"category": "body_axis_joint", "phase": phase, "key": name, "reason": "Each anatomical value must correspond to exactly one revolute joint"})
                continue
            state = rows[0].get("motion_state", {})
            rotation = state.get("rotationValue", {}) if isinstance(state, dict) else {}
            if not isinstance(rotation, dict) or rotation.get("unit") != "rad" or not scalar_match(rotation.get("value"), angle, tolerances["angle_rad"]):
                errors.append({"category": "body_axis_joint", "phase": phase, "key": name, "reason": "Captured anatomical angle disagrees with the native joint state"})
    report["body_axis_count"] = len(old_angles)
    report["pass"] = not errors
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--before", type=Path, required=True)
    parser.add_argument("--after", type=Path, required=True)
    parser.add_argument("--policy", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    before = json.loads(args.before.read_text(encoding="utf-8-sig"))
    after = json.loads(args.after.read_text(encoding="utf-8-sig"))
    policy = json.loads(args.policy.read_text(encoding="utf-8-sig"))
    report = compare(before, after, policy)
    report["inputs"] = {label: {"path": str(path), "sha256": signature(path)} for label, path in (("before", args.before), ("after", args.after), ("policy", args.policy))}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("pass", "original_counts", "body_axis_count")}, indent=2))
    print("errors:", len(report["errors"]), "token drift diagnostics:", len(report["token_drift"]))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
