from pathlib import Path
import json,time
OUT=Path(ROOT)/'v32'
for script in ('06_native_motion.py','07_save_export.py','08_reopen_verify.py'):
 (OUT/'release_progress32.json').write_text(json.dumps(dict(script=script,state='running',epoch=time.time()),indent=2))
 scope=dict(app=app,adsk=adsk,ROOT=ROOT,__file__=str(OUT/script),result=None)
 exec(compile((OUT/script).read_text(),str(OUT/script),'exec'),scope)
 (OUT/'release_progress32.json').write_text(json.dumps(dict(script=script,state='complete',result=scope.get('result'),epoch=time.time()),indent=2))
result=dict(state='complete',release=str(OUT/'saved_release32.json'),reopen=str(OUT/'native_reopen32.json'))
