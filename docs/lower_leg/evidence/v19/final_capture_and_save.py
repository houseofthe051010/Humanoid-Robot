exec(compile((ROOT/'v19/common.py').read_text(),'<common>','exec'))
exec(compile((ROOT/'v19/final_audit.py').read_text(),'<final geometry audit>','exec'))
for go in (right,left):
 o=parts(go)['H01_Hip_roll_117OD_106ID_case'];o.component.partNumber='H01_Hip_roll_110OD_106ID_case'
for o in wg.component.occurrences:
 n=o.component.partNumber.split('_')[0]
 if n in ('W19','W20'):
  o.component.partNumber=n+'_GIM6010_8_waist_motor';o.component.name=n+'_GIM6010_8_waist_motor'
exec(compile((ROOT/'v19/capture_preview.py').read_text(),'<final previews>','exec'))
view((220,-380,1100),(0,Y,983),29,'v19_waist_drive')
view((480,-880,1180),(0,Y,900),62,'v19_complete_revision')
exec(compile((ROOT/'v19/save_release.py').read_text(),'<native archive>','exec'))
