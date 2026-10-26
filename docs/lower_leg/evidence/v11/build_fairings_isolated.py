import adsk.core,adsk.fusion
doc=next(x for x in app.documents if x.name=='Leg_compact_shelled_v11');doc.activate()
design=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'))
assembly=design.rootComponent
visibility={o.component.name:o.isLightBulbOn for o in assembly.occurrences}
for o in assembly.occurrences:o.isLightBulbOn=False
try:
 scope={'ROOT':ROOT,'app':app,'adsk':adsk,'result':None}
 exec(compile((ROOT/'v11/build_fairings.py').read_text(),'build_fairings_isolated','exec'),scope)
 result=scope['result']
finally:
 for o in assembly.occurrences:o.isLightBulbOn=visibility.get(o.component.name,True)
