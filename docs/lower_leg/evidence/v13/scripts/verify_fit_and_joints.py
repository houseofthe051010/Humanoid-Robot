exec(compile((ROOT/'v13/check_fit.py').read_text(),'<fit>','exec'))
report=json.loads((OUT/'fit_validation.json').read_text())
report['retained_vendor_reference_overlaps']=[];report['new_interface_interferences']=[]
for row in report['interface_interferences']:
 if row['one']=='N02_Knee_shaft_8mm' and row['two'].startswith('N04') and ('Inner & Outer Ring' in row['body2'] or 'Set Screw' in row['body2']):report['retained_vendor_reference_overlaps'].append(row)
 else:report['new_interface_interferences'].append(row)
(OUT/'fit_validation.json').write_text(json.dumps(report,indent=2))
assert not report['chain_interferences'] and not report['new_interface_interferences'] and not report['errors'] and not report['solids'],report
exec(compile((OUT/'build_joints_source.py').read_text(),'<joints>','exec'))
