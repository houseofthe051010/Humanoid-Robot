exec(compile((ROOT/'v17/common.py').read_text(),'<v17 common>','exec'))
for o in wg.component.occurrences:
    o.isLightBulbOn=True;o.createForAssemblyContext(wg).isLightBulbOn=True
    if o.component.partNumber.startswith(('W05_','W06_','W07_','W10_','W12_')):
        for b in o.component.bRepBodies:
            if 'vendor' in b.name:continue
            b.appearance=plastic
            for f in b.faces:f.appearance=plastic
right.isLightBulbOn=True;left.isLightBulbOn=True;wg.isLightBulbOn=True
for o in root.occurrences:
    if o.component.name.startswith('ZZ_'):o.isLightBulbOn=False
for b in root.bRepBodies:
    if b.name.startswith('ZZ_User_rough'):b.isLightBulbOn=False
app.userInterface.activeSelections.clear();adsk.doEvents();app.activeViewport.refresh()
result={'display':'nylon waist parts colored blue; final assembly visible; replaced rough guide hidden'}
