import adsk.core, adsk.fusion, json, time
from pathlib import Path
OUT=Path(__file__).parent
doc=app.activeDocument
assert doc.name=='Humanoid_complete_v31',doc.name
d=adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'))
root=d.rootComponent
source=dict(name=doc.name,modified=doc.isModified,id=doc.dataFile.id,version=doc.dataFile.versionNumber,
            pending_snapshot=d.snapshots.hasPendingSnapshot)
archive=OUT/'Input_live_v31_user_edits_preserved.f3d'
assert not archive.exists(),'Preserved archive already exists; do not overwrite'
assert d.exportManager.execute(d.exportManager.createFusionArchiveExportOptions(str(archive),root))
assert archive.exists() and archive.stat().st_size>1000000
assert doc.saveAs('Humanoid_complete_v32',doc.dataFile.parentFolder,
    'V32: shallow perforated shin plates and closely fitted thigh covers around existing oval rails. Mechanism and enlarged v31 waist preserved.','')
app.userInterface.palettes.itemById('TextCommands').isVisible=False
result=dict(source=source,document=doc.name,archive=str(archive),bytes=archive.stat().st_size,epoch=time.time())
(OUT/'input_checkpoint.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
