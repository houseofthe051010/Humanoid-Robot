def polygon_plate(points,y0,depth,name,radius=3):
 pi=cc.constructionPlanes.createInput();pi.setByOffset(cc.xZConstructionPlane,adsk.core.ValueInput.createByReal(-y0/10))
 plane=cc.constructionPlanes.add(pi);plane.isLightBulbOn=False
 sk=cc.sketches.add(plane);sk.name=name;sk.isComputeDeferred=True
 rounded=[]
 for i,p in enumerate(points):
  prev=points[i-1];nxt=points[(i+1)%len(points)]
  u=[prev[k]-p[k] for k in (0,1)];v=[nxt[k]-p[k] for k in (0,1)]
  lu=math.hypot(*u);lv=math.hypot(*v);u=[x/lu for x in u];v=[x/lv for x in v]
  theta=math.acos(max(-1,min(1,sum(u[k]*v[k] for k in (0,1)))))
  dist=min(radius/math.tan(theta/2),lu*.3,lv*.3);rr=dist*math.tan(theta/2)
  bis=[u[k]+v[k] for k in (0,1)];bl=math.hypot(*bis)
  center=[p[k]+bis[k]/bl*rr/math.sin(theta/2) for k in (0,1)]
  mid=[center[k]+(p[k]-center[k])*math.sin(theta/2) for k in (0,1)]
  rounded.append(([p[k]+u[k]*dist for k in (0,1)],mid,[p[k]+v[k]*dist for k in (0,1)]))
 def sp(p):return sk.modelToSketchSpace(pt((p[0],y0,p[1])))
 for i,(a,m,b) in enumerate(rounded):
  sk.sketchCurves.sketchArcs.addByThreePoints(sp(a),sp(m),sp(b))
  sk.sketchCurves.sketchLines.addByTwoPoints(sp(b),sp(rounded[(i+1)%len(rounded)][0]))
 sk.isComputeDeferred=False;sk.isLightBulbOn=False;assert sk.profiles.count==1
 f=cc.features.extrudeFeatures.addSimple(sk.profiles.item(0),adsk.core.ValueInput.createByReal(depth/10),adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
 shape=TM.copy(f.bodies.item(0));bb=bounds(shape)
 assert abs(bb[0][1]-y0)<.001 and abs(bb[1][1]-y0-depth)<.001,(name,bb)
 return shape

def soften_side_edges(body,ys,name,radius=1.5):
 nb=add(cc,TM.copy(body),name+'_edge_rounding_source')
 source_name=nb.name
 edges=adsk.core.ObjectCollection.create()
 for e in nb.edges:
  bb=e.boundingBox
  if not any(abs(bb.minPoint.y*10-y)<.001 and abs(bb.maxPoint.y*10-y)<.001 for y in ys):continue
  edges.add(e)
 assert edges.count>0,name
 inp=cc.features.filletFeatures.createInput()
 inp.edgeSetInputs.addConstantRadiusEdgeSet(edges,adsk.core.ValueInput.createByReal(radius/10),False)
 fillet=cc.features.filletFeatures.add(inp);fillet.name=name+'_R'+str(radius)+'_edge_rounds'
 assert fillet and fillet.healthState==0,(name,fillet.errorOrWarningMessage)
 matches=[b for b in fillet.bodies if b.name==source_name]
 assert len(matches)==1,(name,[b.name for b in fillet.bodies])
 return TM.copy(matches[0])

