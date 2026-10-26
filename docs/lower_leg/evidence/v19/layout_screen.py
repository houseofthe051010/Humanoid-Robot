import math,json
from OCP.BRepPrimAPI import BRepPrimAPI_MakeCylinder
from OCP.BRepAlgoAPI import BRepAlgoAPI_Common
from OCP.BRepExtrema import BRepExtrema_DistShapeShape
from OCP.gp import gp_Pnt,gp_Dir,gp_Ax2
from OCP.GProp import GProp_GProps
from OCP.BRepGProp import BRepGProp
def cy(c,u,a,b,r):
    return BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(*[c[i]+a*u[i] for i in range(3)]),gp_Dir(*u)),r,b-a).Shape()
def gap(a,b):
    dd=BRepExtrema_DistShapeShape(a,b);dd.Perform();return round(dd.Value(),2)
u=(math.cos(math.radians(25)),0,-math.sin(math.radians(25)))
yaw=cy((0,0,876),(0,0,1),0,28,40)
rows=[]
for px in (53,56,59):
    for pz in (798.6,810.6,822.6,834.6):
        p=cy((px,0,pz),u,-28,28,55)
        lp=cy((-px,0,pz),(-u[0],0,u[2]),-28,28,55)
        pg=gap(p,lp);yg=gap(p,yaw)
        if pg<2 or yg<2:continue
        for rx in (110,120,130):
            for rz in (747.6,759.6):
                r=cy((rx,0,rz),(0,1,0),-34,28,55)
                g=gap(p,r)
                if g>1:
                    rows.append({'px':px,'pz':pz,'rx':rx,'rz':rz,'pitch_roll_gap':g,'pitch_pair_gap':pg,'yaw_gap':yg})
print(json.dumps(rows,indent=2))
