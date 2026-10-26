import ast,json,time
from pathlib import Path
out=Path(__file__).parent;helper=out.parent/'v26/audit_full_archive_references.py'
tree=ast.parse(helper.read_text());nodes=[]
for n in tree.body:
 if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='paths' for t in n.targets):break
 nodes.append(n)
scope={'__file__':str(helper)};exec(compile(ast.Module(body=nodes,type_ignores=[]),str(helper),'exec'),scope)
record=scope['audit'](out/'deliverables/Humanoid_complete_v32.f3d')
(out/'native_archive_integrity32.json').write_text(json.dumps(dict(epoch=time.time(),archive=record),indent=2))
assert record['zip_payload_crc_pass'],record['zip_crc_errors']
print(json.dumps({k:record[k] for k in ('path','bytes','sha256','entry_count','zip_payload_crc_pass')},indent=2))
