import math
from OCP.BRepPrimAPI import BRepPrimAPI_MakeCylinder
from OCP.BRepAlgoAPI import BRepAlgoAPI_Common
from OCP.gp import gp_Pnt,gp_Dir,gp_Ax2
from OCP.GProp import GProp_GProps
from OCP.BRepGProp import BRepGProp
def cylinder(c,u,a,b,r):
    p=[c[i]+a*u[i] for i in range(3)]
    return BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(*p),gp_Dir(*u)),r,b-a).Shape()
def overlap(a,b):
    s=BRepAlgoAPI_Common(a,b).Shape();p=GProp_GProps();BRepGProp.VolumeProperties_s(s,p);return round(p.Mass(),1)
u=(math.cos(math.radians(25)),0,-math.sin(math.radians(25)))
w=cylinder((0,0,876),(0,0,1),0,28,39)
for px in (59,62,65):
    for pz in (798.6,804.6,810.6,816.6):
        p=cylinder((px,0,pz),u,-34,28,58.5)
        for rx in (130,140,150):
            r=cylinder((rx,0,759.6),(0,1,0),-34,28,58.5)
            vol=overlap(p,r);v2=overlap(p,w)
            if vol<200 and v2<200:print(px,pz,rx,'pitch_roll',vol,'pitch_waist',v2)
