exec(compile((ROOT/'v19/build_waist.py').read_text(),'<build waist>','exec'))
exec(compile((ROOT/'v19/validate_fit.py').read_text(),'<fit>','exec'))
saved_result=result
exec(compile((ROOT/'v19/capture_preview.py').read_text(),'<capture>','exec'))
result=saved_result
