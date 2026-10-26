import adsk.core,adsk.fusion,json
base=ROOT/'v11';path=base/'deliverables/Leg_compact_shelled_v11.f3d'
source=next(d for d in app.documents if d.name=='Leg_compact_shelled_v11')
check=app.importManager.importToNewDocument(app.importManager.createFusionArchiveImportOptions(str(path)))
check.name='VERIFY_v11_archive'
d=adsk.fusion.Design.cast(check.products.itemByProductType('DesignProductType'));root=d.rootComponent
ocs={o.component.name:o for o in root.occurrences}
bad=[{'component':c.name,'feature':f.name,'message':f.errorOrWarningMessage}for c in [root]+[o.component for o in root.occurrences]for f in c.features if f.healthState!=adsk.fusion.FeatureHealthStates.HealthyFeatureHealthState]
new={n:c.component.bRepBodies.count for n,c in ocs.items() if n.startswith(('T0','T1'))}
j=root.asBuiltJoints.itemByName('Knee_pitch')
try:
 j.jointMotion.rotationValue=.35;adsk.doEvents()
 m=ocs['N04_Knee_pillow_block_L'].transform2.asArray()
 follow={n:max(abs(a-b)for a,b in zip(m,ocs[n].transform2.asArray())) for n in list(new)+['R01_DJI_10018_77KV_ESTIMATED_REFERENCE'] if not n.startswith('T08')}
finally:j.jointMotion.rotationValue=0;adsk.doEvents()
rail=ocs['N06_Upper_leg_oval_stub_R'].bRepBodies.item(0)
hub=next(b for b in ocs['R01_DJI_10018_77KV_ESTIMATED_REFERENCE'].bRepBodies if b.name=='Rear_bearing_hub_EST')
result={'archive':str(path),'components':root.occurrences.count,'native_joints':root.asBuiltJoints.count,'timeline_features':d.timeline.count,'invalid_joints':[j.name for j in root.asBuiltJoints if not j.isValid],'feature_warnings':bad,'new_component_body_counts':new,'thigh_rail_length_mm':(rail.boundingBox.maxPoint.z-rail.boundingBox.minPoint.z)*10,'encoder_gap_mm':(rail.boundingBox.minPoint.x-hub.boundingBox.maxPoint.x)*10,'pitch_tilt_deg':d.userParameters.itemByName('layout_hip_pitch_tilt').value*180/3.141592653589793,'max_new_part_follow_matrix_error':max(follow.values()),'native_new_part_follow_errors':follow}
(base/'archive_reopen_verification.json').write_text(json.dumps(result,indent=2))
check.close(False);source.activate()
