exec(compile((ROOT/'v19/edge_rounds.py').read_text(),'<edge rounds>','exec'))
exec(compile((ROOT/'v19/validate_new_drive.py').read_text(),'<waist motion>','exec'))
motion_result=result
exec(compile((ROOT/'v19/capture_preview.py').read_text(),'<previews>','exec'))
shots.append(view((220,-380,1100),(0,Y,983),29,'v19_waist_drive'))
view((480,-880,1180),(0,Y,900),62,'v19_complete_revision')
result=motion_result
