import adsk.core,adsk.fusion,json,math
OUT=ROOT/'v14';doc=next(x for x in app.documents if x.name=='Bilateral_legs_v14');doc.activate();d=adsk.fusion.Design.cast(app.activeProduct);root=d.rootComponent
TM=adsk.fusion.TemporaryBRepManager.get();BT=adsk.fusion.BooleanTypes;OP=adsk.fusion.FeatureOperations;P3=adsk.core.Point3D;V3=adsk.core.Vector3D
Y=23.343134;K=435.6
def pt(a):return P3.create(*(v/10 for v in a))
def obj(items):
 o=adsk.core.ObjectCollection.create()
 for x in items:o.add(x)
 return o
def cy(p,q,r):return TM.createCylinderOrCone(pt(p),r/10,pt(q),r/10)
def bx(lo,hi):return TM.createBox(adsk.core.OrientedBoundingBox3D.create(pt([(a+b)/2 for a,b in zip(lo,hi)]),V3.create(1,0,0),V3.create(0,1,0),*((b-a)/10 for a,b in zip(lo,hi))))
def boolean(a,b,op):assert TM.booleanOperation(a,b,op);return a
def un(a,b):return boolean(a,b,BT.UnionBooleanType)
def sub(a,b):return boolean(a,b,BT.DifferenceBooleanType)
def ix(a,b):return boolean(a,b,BT.IntersectionBooleanType)
def oval(x,z0,z1,r):return un(un(bx((x-4,6-r,z0),(x+4,6+r,z1)),cy((x-4,6,z0),(x-4,6,z1),r)),cy((x+4,6,z0),(x+4,6,z1),r))
def tool(c,b,name):
 bf=c.features.baseFeatures.add();bf.name=name;bf.startEdit();c.bRepBodies.add(b,bf);bf.finishEdit();return bf.bodies.item(0)
def combine(c,b,op,name):
 target=c.bRepBodies.item(0);ap=target.appearance;t=tool(c,b,name+'_tool');ci=c.features.combineFeatures.createInput(target,obj([t]));ci.operation=op;f=c.features.combineFeatures.add(ci);f.name=name
 for b in f.bodies:b.appearance=ap
 return f
report=[]
for go in root.occurrences:
 side=go.component.name.removesuffix('_leg');sgn=1 if side=='Right'else -1;g=go.component;parts={o.component.partNumber:o for o in g.occurrences}
 tr=adsk.core.Matrix3D.create();tr.setCell(0,0,sgn);tr.translation=V3.create(sgn*13,0,0)
 def placed(b):assert TM.transform(b,tr);return b
 # Restore the removed outside wall around the drive-side shin oval. The
 # original tube sockets and existing fastening passages stay open.
 a=bx((-21,-1,393.6),(-10,44,K+.05))
 for x in [-10,10]:sub(a,oval(x,392,K+.05,5.1))
 sub(a,cy((-22,Y,K),(-9,Y,K),4.05))
 for yy in [18.5,36]:
  for zz in [K-15,K+15]:sub(a,cy((-22,yy,zz),(-9,yy,zz),1.65))
 for zz in [K-8,K+8]:sub(a,cy((-22,36,zz),(-9,36,zz),3.05))
 sub(a,cy((-10,-2,418),(-10,50,418),1.65))
 c=parts['N01_Aluminum_knee_stack_1'].component
 combine(c,placed(a),OP.JoinFeatureOperation,'V14_restore_full_oval_enclosure')
 c.description='V14 outer wall restored to fully surround shin oval; 0.1mm nominal socket clearance,1.9mm minimum nominal outer wall. Existing fastener passages retained. Knee lowered5mm.'
 # Shorten only the top of each continuous shin tube and move its cross hole.
 for label,x in [('L',-10),('R',10)]:
  c=parts['S05_Continuous_oval_steel_rail_'+label].component
  wall=sub(oval(x,410,425,5),oval(x,409,426,4.45))
  fill=ix(cy((x,-2,418),(x,14,418),1.75),wall)
  combine(c,placed(fill),OP.JoinFeatureOperation,'V14_close_previous_crossbolt_hole')
  combine(c,placed(cy((x,-2,413),(x,14,413),1.65)),OP.CutFeatureOperation,'V14_lower_crossbolt_hole_5mm')
  combine(c,placed(bx((x-11,-2,430.6),(x+11,15,437))),OP.CutFeatureOperation,'V14_shorten_shin_5mm')
  c.description='Continuous18x10 stadium steel tube,0.55mm assumed wall,361.6mm long,Z69..430.6. V14 top shortened5mm; crossbolt atZ413.'
 moved=[]
 for n,o in parts.items():
  if not n.startswith(('N','P','Q','R01','T','V13')) or not o.component.bRepBodies.count:continue
  c=o.component;m=adsk.core.Matrix3D.create();m.translation=V3.create(0,0,-.5)
  mi=c.features.moveFeatures.createInput2(obj(list(c.bRepBodies)));mi.defineAsFreeMove(m);c.features.moveFeatures.add(mi).name='V14_lower_knee_and_upper_assembly_5mm';moved.append(n)
 # Shift the actual native knee axis datum, preserving all existing joints.
 sk=g.sketches.itemByName(side+'_Knee_pitch_axis');assert sk,side
 p=sk.modelToSketchSpace(P3.create(0,0,0));q=sk.modelToSketchSpace(P3.create(0,0,-.5));m=adsk.core.Matrix3D.create();m.translation=p.vectorTo(q)
 assert sk.move(obj(list(sk.sketchCurves)),m)
 adsk.doEvents()
 report.append({'side':side,'moved_components':moved,'knee_z_mm':430.6,'shin_length_mm':361.6,'adapter_outer_x_canonical_mm':-21,'chain_work':'none; existing geometry retained'})
(OUT/'edit_result.json').write_text(json.dumps(report,indent=2));result=report
