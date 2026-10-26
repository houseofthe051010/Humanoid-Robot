"""File-only source-vertex bound screen; no native calls or CAD changes."""
import hashlib
import itertools
import json
import struct
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent

def run(folder=BASE):
    after_path = folder / 'casing_after_final.json'
    after = json.loads(after_path.read_text(encoding='utf-8'))
    parts = json.loads((folder/'casing_inventory_staged.json').read_text())['inventory']
    matrices = {r['path']:r['transform_cm'] for r in after['occurrences']}
    dtype = np.dtype([('normal','<f4',(3,)),('vertices','<f4',(3,3)),('attribute','<u2')])
    rows = []
    all_disjoint = True
    for side in ('R','L'):
        name = 'AmazingHand_'+side+'_Printed_shells'
        mesh = next(r for r in after['meshes'] if r['name']==name)
        source = folder.parent/'v26'/'references'/(name+'.stl')
        data = source.read_bytes()
        count = struct.unpack_from('<I',data,80)[0]
        assert len(data)==84+count*50
        vertices = np.frombuffer(data,dtype=dtype,offset=84,count=count)['vertices'].astype(np.float64)
        triangles = vertices
        vertices = vertices.reshape(-1,3)
        native_bounds = np.stack((vertices.min(axis=0),vertices.max(axis=0)))
        native_error = float(np.max(np.abs(native_bounds-np.array(mesh['bounds_mm']))))
        assert native_error < .00002
        matrix = np.array(matrices[mesh['component_path']]).reshape(4,4)
        world_vertices = vertices@matrix[:3,:3].T+matrix[:3,3]*10
        world_bounds = np.stack((world_vertices.min(axis=0),world_vertices.max(axis=0)))
        tests = []
        for cover in parts:
            if cover['group']=='thigh' and cover['side']==('Right' if side=='R' else 'Left'):
                box = cover['world_bounds_mm']
                gaps = [max(box[0][i]-world_bounds[1,i],world_bounds[0,i]-box[1][i]) for i in range(3)]
                disjoint = max(gaps)>0
                all_disjoint &= disjoint
                tests.append({'cover':cover['component'],'world_bounds_mm':box,
                              'axis_separation_mm':[float(v) for v in gaps],'disjoint':bool(disjoint)})
        zero = int((np.linalg.norm(np.cross(triangles[:,1]-triangles[:,0],triangles[:,2]-triangles[:,0]),axis=1)==0).sum())
        rows.append({'mesh_name':name,'component_path':mesh['component_path'],
            'source_stl':str(source),'source_stl_sha256':hashlib.sha256(data).hexdigest(),
            'triangle_count':count,'capture_triangle_count':mesh['triangle_count'],
            'zero_area_triangle_count':zero,'source_native_bounds_mm':native_bounds.tolist(),
            'native_bounds_match_max_mm':native_error,
            'root_transform_applied_once_cm':matrices[mesh['component_path']],
            'world_vertex_bounds_mm':world_bounds.tolist(),'same_side_thigh_tests':tests})
    output={'file_only':True,'native_calls':0,'cad_mutations':0,'source_geometry_bound_separation_pass':bool(all_disjoint),
        'source_after_sha256':hashlib.sha256(after_path.read_bytes()).hexdigest(),'rows':rows,
        'qualification':'Preserved import-source STL vertices transformed once by current root-context occurrence matrices. Source bounds match current native mesh bounds within 0.00002 mm; source/native triangle counts differ slightly, so this is source-geometry separation, not native vertex equality. Gross transformed-box overlaps are conservative, not collision evidence. Static rest only; no swept range qualification.'}
    (folder/'hand_source_vertex_separation27.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    return output

if __name__=='__main__':
    result=run()
    print(json.dumps({'source_geometry_bound_separation_pass':result['source_geometry_bound_separation_pass'],
        'gaps_X_mm':{r['mesh_name']:r['same_side_thigh_tests'][0]['axis_separation_mm'][0] for r in result['rows']}},indent=2))
