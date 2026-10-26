exec(compile((ROOT/'v13/common.py').read_text(),'<common>','exec'))
exec(compile((OUT/'native_joints.py').read_text(),'<joints>','exec'))
rows=json.loads((OUT/'source_joint_inventory.json').read_text());add_joints(d,root,parts,rows)
parts['S01_Ankle_to_oval_rail_adapter'].isGrounded=True
(OUT/'native_source_joints.json').write_text(json.dumps({'joints':root.asBuiltJoints.count,'invalid':[j.name for j in root.asBuiltJoints if not j.isValid]},indent=2))
result={'joints':root.asBuiltJoints.count}
