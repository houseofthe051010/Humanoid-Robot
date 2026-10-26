exec(compile((ROOT/'v11/common.py').read_text(),'<common>','exec'))
exec(compile((OUT/'capture_layout.py').read_text(),'capture_reviewed','exec'))
native=OUT/'deliverables/Leg_compact_shelled_v11.f3d'
assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(native)))
result={'native':str(native),'camera_and_visibility_saved':True}
