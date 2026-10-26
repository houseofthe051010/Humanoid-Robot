exec(compile((ROOT/'v15/common.py').read_text(),'<common>','exec'))
out=[]
for go,sg in groups():
 c=next(o.component for o in go.component.occurrences if o.component.partNumber=='P05_Gearbox_front_cover')
 b=TM.copy(c.bRepBodies.item(0));sub(b,place(bx((-12,-100,619),(-7,140,639)),sg))
 assert b.isSolid and b.shells.count==1
 replace(c,b,'V15_curved_upper_shell_finished')
 out.append({'side':go.component.name,'solid':b.isSolid,'shells':b.shells.count})
result=out
