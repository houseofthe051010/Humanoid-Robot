exec(compile((ROOT/'v15/common.py').read_text(),'<common>','exec'))
r=[]
for c in d.allComponents:
 if not c.partNumber.startswith(('P15','W02','W03','P05')):continue
 for b in c.bRepBodies:
  ss=[]
  for s in b.shells:
   boxes=[f.boundingBox for f in s.faces]
   ss.append({'faces':s.faces.count,'isVoid':getattr(s,'isVoid',None),'min':[min(bb.minPoint.asArray()[i] for bb in boxes)*10 for i in range(3)],'max':[max(bb.maxPoint.asArray()[i]for bb in boxes)*10 for i in range(3)]})
  r.append({'component':c.name,'body':b.name,'shells':ss})
(OUT/'shell_inspection.json').write_text(json.dumps(r,indent=2));result=r
