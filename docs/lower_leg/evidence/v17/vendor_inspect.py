from pathlib import Path
import json
from OCP.STEPControl import STEPControl_Reader
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_SOLID, TopAbs_FACE
from OCP.TopoDS import TopoDS
from OCP.Bnd import Bnd_Box
from OCP.BRepBndLib import BRepBndLib
from OCP.BRepAdaptor import BRepAdaptor_Surface
from OCP.GeomAbs import GeomAbs_Plane, GeomAbs_Cylinder
from OCP.GProp import GProp_GProps
from OCP.BRepGProp import BRepGProp

out=Path(__file__).parent
def items(shape,typ):
    ex=TopExp_Explorer(shape,typ)
    while ex.More():
        yield ex.Current();ex.Next()
def xyz(p):return [round(p.X(),5),round(p.Y(),5),round(p.Z(),5)]
def bounds(shape):
    b=Bnd_Box();BRepBndLib.Add_s(shape,b);return xyz(b.CornerMin())+xyz(b.CornerMax())
files={
 'GWK7010':Path(r'C:\Users\rshan\Downloads\GWK7010-8_3D_model.stp'),
 'GIM6010':Path(r'C:\Users\rshan\Downloads\Planetary-Reduction-Motor\Planetary Reduction Motor\GIM6010-8\GIM6010-8\GIM6010-8  3D Model-Standard Version.stp'),
}
data={}
for name,path in files.items():
    reader=STEPControl_Reader();assert reader.ReadFile(str(path))==1;reader.TransferRoots()
    solids=[]
    for i,s in enumerate(items(reader.OneShape(),TopAbs_SOLID)):
        prop=GProp_GProps();BRepGProp.VolumeProperties_s(s,prop)
        row={'index':i,'bounds':bounds(s),'volume':prop.Mass(),'planes':[],'cylinders':[]}
        for fi,f in enumerate(items(s,TopAbs_FACE)):
            sf=BRepAdaptor_Surface(TopoDS.Face(f));typ=sf.GetType()
            if typ==GeomAbs_Plane:
                p=sf.Plane();pr=GProp_GProps();BRepGProp.SurfaceProperties_s(f,pr)
                if pr.Mass()>5:row['planes'].append({'index':fi,'origin':xyz(p.Location()),'axis':xyz(p.Axis().Direction()),'area':pr.Mass()})
            elif typ==GeomAbs_Cylinder:
                c=sf.Cylinder();row['cylinders'].append({'index':fi,'origin':xyz(c.Location()),'axis':xyz(c.Axis().Direction()),'r':c.Radius()})
        solids.append(row)
    data[name]=solids
    print(name,[{'index':s['index'],'bounds':s['bounds'],'volume':s['volume'],'cylinders':len(s['cylinders'])} for s in solids])
(out/'vendor_inventory.json').write_text(json.dumps(data,indent=2))
