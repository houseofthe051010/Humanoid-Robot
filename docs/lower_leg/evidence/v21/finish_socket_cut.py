exec(compile((ROOT/'v21/common.py').read_text(),'<common>','exec'))
o=getpart(wg,'W07_');shape=TM.copy(o.createForAssemblyContext(wg).bRepBodies.item(0));before=shape.volume*1000;yr=Y+25
# Cut the capsule as separate primitives to avoid a Boolean seam between the
# arch roots and the union-built capsule cutter.
for cutter in (bx((-4,yr-5.15,980.8),(4,yr+5.15,1041)),cy((-4,yr,980.8),(-4,yr,1041),5.15),cy((4,yr,980.8),(4,yr,1041),5.15)):
 sub(shape,cutter)
for z in (993,1004):sub(shape,cy((0,yr-18,z),(0,yr+18,z),2.15))
test=TM.copy(shape);spine=getpart(wg,'W08_').createForAssemblyContext(wg).bRepBodies.item(0);TM.booleanOperation(test,TM.copy(spine),BT.IntersectionBooleanType)
assert test.volume*1000<.001,test.volume*1000
world_replace(wg,o,[('W07_final_continuous_spine_bore',shape)],o.component.description,plastic)
result={'before_mm3':before,'after_mm3':shape.volume*1000,'spine_intersection_mm3':test.volume*1000}
