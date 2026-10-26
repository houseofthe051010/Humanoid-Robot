exec(compile((ROOT/'v21/common.py').read_text(),'<common>','exec'))
cfg=json.loads((OUT/'upper_layout.json').read_text());g=cfg['ground_z_mm'];yr=Y+25
for old in list(wg.component.occurrences):
 if old.component.partNumber.startswith('U06_'):wg.component.features.removeFeatures.add(old)
guide=newpart(wg.component,'U06_Upper_body_PLACEMENT_SKETCHES','Editable placement sketches only: shoulders, arms, neck and head. Heights measured from the neutral lowest sole.','layout only, no mass')
c=guide.component
def sketch(name,plane,offset):
 pi=c.constructionPlanes.createInput();pi.setByOffset(plane,adsk.core.ValueInput.createByReal(-offset/10/plane.geometry.normal.y));pl=c.constructionPlanes.add(pi);pl.isLightBulbOn=False
 sk=c.sketches.add(pl);sk.name=name;sk.isLightBulbOn=True;sk.isComputeDeferred=True;return sk
def line(sk,a,b,construction=False):
 e=sk.sketchCurves.sketchLines.addByTwoPoints(sk.modelToSketchSpace(pt(a)),sk.modelToSketchSpace(pt(b)));e.isConstruction=construction;e.isFixed=True;return e
def circle(sk,p,r):
 e=sk.sketchCurves.sketchCircles.addByCenterRadius(sk.modelToSketchSpace(pt(p)),r/10);e.isFixed=True;return e
def poly(sk,points,closed=False):
 for a,b in zip(points,points[1:]+([points[0]] if closed else [])):line(sk,a,b)
def label(sk,text,x,z,width=230,height=30,size=10):
 a=sk.modelToSketchSpace(pt((x,-120,z)));b=sk.modelToSketchSpace(pt((x+width,-120,z-height)))
 a.z=0;b.z=0
 inp=sk.sketchTexts.createInput2(text,size/10)
 inp.setAsMultiLine(a,b,adsk.core.HorizontalAlignments.LeftHorizontalAlignment,adsk.core.VerticalAlignments.TopVerticalAlignment,0)
 return sk.sketchTexts.add(inp)
front=sketch('U20_FRONT_upper_body_joint_placements',c.xZConstructionPlane,120)
fy=-120
def f(x,h):return (x,fy,g+h)
line(front,f(0,960),f(0,1600.2),True)
line(front,f(-180,1340.2),f(180,1340.2),True)
for s in (-1,1):
 for h,r in ((1340.2,32),(1080.2,25),(840.2,19)):circle(front,f(s*180,h),r)
 line(front,f(s*180,1340.2),f(s*180,1080.2),True)
 line(front,f(s*180,1080.2),f(s*180,840.2),True)
 # Limb outlines remain sketches, not fabricated solids.
 for side in (-1,1):
  line(front,f(s*180+side*28,1308.2),f(s*180+side*22,1105.2))
  line(front,f(s*180+side*22,1055.2),f(s*180+side*17,859.2))
 poly(front,[f(s*180-30,821.2),f(s*180-35,730.2),f(s*180-23,690.2),f(s*180+23,690.2),f(s*180+35,730.2),f(s*180+30,821.2)],True)
 poly(front,[f(s*145,1335.2),f(s*115,1220.2),f(s*90,1090),f(s*65,1050)])
 poly(front,[f(s*145,1360.2),f(s*45,1400.2),f(s*24,1420.2)])
circle(front,f(0,1400.2),18)
head=front.sketchCurves.sketchEllipses.add(front.modelToSketchSpace(pt(f(0,1510.2))),front.modelToSketchSpace(pt(f(0,1600.2))),front.modelToSketchSpace(pt(f(75,1510.2))));head.isFixed=True
line(front,f(-35,1535.2),f(35,1535.2))
front.isComputeDeferred=False
ann=sketch('U21_FRONT_height_and_segment_annotations_mm',c.xZConstructionPlane,120)
for x,h,w,text in [(100,1600.2,290,'HEAD TOP 1600.2 mm / 5 ft 3 in'),(225,1340.2,240,'SHOULDERS 1340.2 mm'),(225,1080.2,240,'ELBOWS 1080.2 mm'),(225,840.2,240,'WRISTS 840.2 mm'),(60,1420.2,260,'NECK BASE 1400.2 mm'),(-470,1240.2,260,'UPPER ARM 260 mm'),(-470,990.2,260,'FOREARM 240 mm'),(-470,740.2,260,'HAND ENVELOPE 150 mm')]:
 label(ann,text,x,g+h,w)
for h in (1340.2,1080.2,840.2):line(ann,f(210,h),f(225,h))
line(ann,f(-180,1378),f(180,1378));line(ann,f(-180,1371),f(-180,1385));line(ann,f(180,1371),f(180,1385));label(ann,'360 mm shoulder centers',-95,g+1396,220,20,8)
line(ann,f(-525,0),f(-525,1600.2));line(ann,f(-535,0),f(-515,0));line(ann,f(-535,1600.2),f(-515,1600.2));label(ann,'1600.2 mm',-675,g+825,140)
line(ann,f(-545,0),f(275,0));label(ann,'GROUND / neutral sole datum',-150,g-8,330)
label(ann,'PLACEMENT STUDY - arms, shoulders and neck not engineered',-460,g+1660.2,960,30,11)
ann.isComputeDeferred=False
# Cell-grid and BMS-zone sketch is retained inside the solid battery envelope;
# user can hide U01 to inspect. It is not a cell or wiring assembly.
pack=sketch('U22_Battery_36_cell_grid_and_BMS_reservation',c.xZConstructionPlane,-(yr-99))
for ix in range(6):
 for iz in range(6):circle(pack,(-56.25+ix*22.5,yr-99,1059+10.775+iz*22.5),10.775)
poly(pack,[(-67,yr-99,1193),(67,yr-99,1193),(67,yr-99,1215),(-67,yr-99,1215)],True)
pack.isComputeDeferred=False;pack.isLightBulbOn=False
rigid(wg.component,getpart(wg,'W08_'),guide,'U_joint_upper_body_placement_sketches')
cfg['native_sketches']=[s.name for s in c.sketches];cfg['elbow_height_mm']=1080.2;cfg['wrist_height_mm']=840.2;cfg['hand_tip_height_mm']=690.2
(OUT/'upper_layout.json').write_text(json.dumps(cfg,indent=2));result={'sketches':cfg['native_sketches'],'height_mm':cfg['height_mm']}
