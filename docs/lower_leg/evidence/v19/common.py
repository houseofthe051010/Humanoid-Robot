source=(ROOT/'v18/common.py').read_text().replace("OUT=ROOT/'v18'","OUT=ROOT/'v19'").replace("x.name=='Legs_hip_waist_v18'","x.name=='Legs_hip_waist_v19'")
exec(compile(source,'<v19 shared helpers>','exec'))
PX=26*math.cos(math.radians(25))+55*math.sin(math.radians(25));PZ=824.6;RX=120.;RZ=753.6
u=(math.cos(math.radians(25)),0,-math.sin(math.radians(25)))
w=(math.sin(math.radians(25)),0,math.cos(math.radians(25)))
_native_parts=parts
def parts(group):
    rows=_native_parts(group)
    if 'H01_Hip_roll_110OD_106ID_case' in rows:
        rows['H01_Hip_roll_117OD_106ID_case']=rows['H01_Hip_roll_110OD_106ID_case']
    return rows
def pp(t,a=0,b=0):return (PX+u[0]*t+w[0]*b,Y+a,PZ+u[2]*t+w[2]*b)
def pcyl(a,b,r):return cy(pp(a),pp(b),r)
def rcyl(a,b,r):return cy((RX,Y+a,RZ),(RX,Y+b,RZ),r)
def ring(a,b,ro,ri):return sub(cy(a,b,ro),cy(a,b,ri))
def world_replace(go,o,rows,desc,ap):
    inv=o.createForAssemblyContext(go).transform2.copy();inv.invert()
    return replace(o.component,[(n,transform(b,inv)) for n,b in rows],desc,ap)
def getpart(go,key):return next(o for o in go.component.occurrences if o.component.partNumber.startswith(key))
