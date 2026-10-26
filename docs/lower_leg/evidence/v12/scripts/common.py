import adsk.core,adsk.fusion,math,json,time
from pathlib import Path
BASE=Path(r'E:\Aditya\robot_sim\outputs\shin_cad_20260912');OUT=BASE/'v12'
doc=next(x for x in app.documents if x.name=='Legs_gearbox_hip_v12');doc.activate()
d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'));d.activateRootComponent();root=d.rootComponent
parts={o.component.name:o for o in root.occurrences};ocs=parts;records=[];joint_records=[]
P3=adsk.core.Point3D;V3=adsk.core.Vector3D;V=adsk.core.ValueInput;OP=adsk.fusion.FeatureOperations;TM=adsk.fusion.TemporaryBRepManager.get();tm=TM
src=(BASE/'v7'/'build_shin.py').read_text()
exec(compile(src[src.index('def pt('):src.index('for n,v,unit,desc')],'<native_helpers>','exec'))
def move_bodies(c,delta,name,selected=None):
 bs=list(c.bRepBodies) if selected is None else selected
 if not bs:return
 mi=c.features.moveFeatures.createInput2(obj(bs));mi.defineAsFreeMove(mat(*delta));f=c.features.moveFeatures.add(mi);f.name=name
 return f
def rebuild(name):
 c=parts[name].component
 for f in reversed(list(c.features)):f.deleteMe()
 assert c.bRepBodies.count==0,(name,c.bRepBodies.count)
 return c
def color(c,source='S01_Ankle_to_oval_rail_adapter_finish'):
 ap=d.appearances.itemByName(source)
 if ap:
  for b in c.bRepBodies:b.appearance=ap
def save_checkpoint(name):
 assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(OUT/(name+'.f3d'))))
def progress(stage):
 (OUT/'progress.json').write_text(json.dumps({'stage':stage,'time':time.time()}))
