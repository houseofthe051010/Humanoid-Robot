from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from OCP.STEPControl import STEPControl_Reader
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_FACE,TopAbs_EDGE
from OCP.TopoDS import TopoDS
from OCP.BRepAdaptor import BRepAdaptor_Curve
from OCP.gp import gp_Pnt

reader=STEPControl_Reader();reader.ReadFile(r'C:\Users\rshan\Downloads\GWK7010-8_3D_model.stp');reader.TransferRoots()
faces=[];ex=TopExp_Explorer(reader.OneShape(),TopAbs_FACE)
while ex.More():faces.append(TopoDS.Face(ex.Current()));ex.Next()
fig,axs=plt.subplots(1,3,figsize=(13,4.5))
for ax,fi in zip(axs,[1212,1240,1135]):
    ex=TopExp_Explorer(faces[fi],TopAbs_EDGE)
    while ex.More():
        c=BRepAdaptor_Curve(TopoDS.Edge(ex.Current()));u0,u1=c.FirstParameter(),c.LastParameter();points=[]
        for k in range(65):
            p=gp_Pnt();c.D0(u0+(u1-u0)*k/64,p);points.append((p.Y(),p.Z()))
        ax.plot([p[0] for p in points],[p[1] for p in points],color='#167393',lw=1)
        ex.Next()
    ax.set_title('Vendor face '+str(fi));ax.set_aspect('equal');ax.grid(alpha=.2)
fig.tight_layout();fig.savefig(Path(__file__).parent/'drawings'/'GWK7010_interface_faces.png',dpi=150)
