exec(compile((ROOT/'v21/common.py').read_text(),'<common>','exec'))
wc=wg.component
def pref(k):return getpart(wg,k+'_')
rep={'parts':[],'hits':[],'axes':[]}
for o in wc.occurrences:
 for b in o.createForAssemblyContext(wg).bRepBodies:
  rep['parts'].append({'part':o.component.partNumber,'body':b.name,'bounds':bounds(b),'solid':b.isSolid,'outer_shells':sum(not s.isVoid for s in b.shells)})
for n,want in (('WJ01_lower_waist_pitch',[1,0,0]),('WJ02_upper_waist_roll',[0,1,0])):
 j=wc.asBuiltJoints.itemByName(n);v=j.createForAssemblyContext(wg).jointMotion.rotationAxisVector.asArray();assert max(abs(abs(a)-b) for a,b in zip(v,want))<1e-6
 rep['axes'].append({'name':n,'axis':v,'origin':list(j.transform.translation.asArray())})
def inter(a,b):
 if not a.boundingBox.intersects(b.boundingBox):return 0
 t=TM.copy(a);assert TM.booleanOperation(t,TM.copy(b),BT.IntersectionBooleanType)
 return t.volume*1000
pairs=[('W07','W08'),('W05','W06'),('W05','W07'),('W06','W07'),('W19','W20'),('W19','W05'),('W20','W05'),('W19','W06'),('W20','W06'),('W19','W07'),('W20','W07'),('W23','W07'),('W24','W07'),('W23','W19'),('W24','W20'),('W25','W05'),('W26','W05'),('W25','W06'),('W26','W06'),('W25','W07'),('W26','W07'),('W21','W06'),('W21','W07'),('W07','W16'),('W07','W11'),('W11','W12'),('W06','W09'),('W09','W10'),('W05','W21')]
for a,b in pairs:
 for aa in pref(a).createForAssemblyContext(wg).bRepBodies:
  for bb in pref(b).createForAssemblyContext(wg).bRepBodies:
   if any(t in aa.name or t in bb.name for t in ('Output_M3_reference','M6_crank_pin_reference')):continue
   v=inter(aa,bb)
   if v>.05:rep['hits'].append({'parts':a+'/'+b,'a':aa.name,'b':bb.name,'mm3':v})
(OUT/'waist_neutral_check.json').write_text(json.dumps(rep,indent=2))
for c in [root]+list(d.allComponents):
 for coll in (c.sketches,c.constructionAxes,c.constructionPlanes,c.constructionPoints,c.asBuiltJoints):
  for x in coll:x.isLightBulbOn=False
for o in root.occurrences:
 if o.component.name.startswith('ZZ_') or 'GWK6010-8 3D Model' in o.component.name:o.isLightBulbOn=False
d.activateRootComponent();app.userInterface.activeSelections.clear();vp=app.activeViewport;cam=vp.camera;cam.isSmoothTransition=False;cam.cameraType=adsk.core.CameraTypes.OrthographicCameraType;cam.eye=pt((400,-600,1240));cam.target=pt((0,Y+20,978));cam.upVector=V3.create(0,0,1);cam.isFitView=False;cam.setExtents(29,29);vp.camera=cam;adsk.doEvents();vp.refresh();vp.saveAsImageFile(str(OUT/'waist_working.png'),1500,1500)
result={'axes':rep['axes'],'hits':rep['hits'],'nonsolids':[p for p in rep['parts'] if not p['solid']],'disconnected':[p for p in rep['parts'] if p['outer_shells']!=1]}
