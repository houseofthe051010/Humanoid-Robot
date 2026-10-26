exec(compile((ROOT/'v15/common.py').read_text(),'<common>','exec'))
dest=OUT/'deliverables';path=dest/'Legs_and_waist_v15.f3d'
assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(path)))
result={'native':str(path)}
