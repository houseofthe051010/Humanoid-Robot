exec(compile((ROOT/'v19/common.py').read_text(),'<common>','exec'))
wc=wg.component
def pref(k):return next(o for o in wc.occurrences if o.component.partNumber.startswith(k+'_'))
report=[]
for mkey,ckey,s in (('W19','W23',-1),('W20','W24',1)):
 motor=pref(mkey);crank=pref(ckey);mp=motor.createForAssemblyContext(wg);cp=crank.createForAssemblyContext(wg)
 body=next(b for b in mp.bRepBodies if b.name=='GIM6010_vendor_solid_0')
 xa,xb=sorted((s*38,s*50.1));tool=cy((xa,Y,995),(xb,Y,995),17)
 moving=ix(TM.copy(body),tool);stationary=sub(TM.copy(body),TM.copy(moving));assert moving.volume>0 and stationary.volume>0
 rows=[(b.name,stationary if b.name=='GIM6010_vendor_solid_0' else TM.copy(b)) for b in mp.bRepBodies]
 world_replace(wg,motor,rows,motor.component.description+' Central output partition follows its crank; internal gearbox construction is not inferred.',black)
 inv=cp.transform2.copy();inv.invert();add(crank.component,transform(moving,inv),'GIM6010_vendor_rotating_output_partition',black)
 report.append({'motor':mkey,'crank':ckey,'partition_radius_mm':17,'moving_volume_mm3':moving.volume*1000})
(OUT/'6010_output_partition.json').write_text(json.dumps(report,indent=2));result=report
exec(compile((OUT/'validate_new_drive.py').read_text(),'<recheck moving outputs>','exec'))
saved=result
exec(compile((OUT/'validate_fit.py').read_text(),'<final hip fit after fillets>','exec'))
result={'waist':saved,'hips':result}
