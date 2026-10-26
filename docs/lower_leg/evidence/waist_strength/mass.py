"""V15 mass budget; modeled volume is not a motor's material volume."""
from pathlib import Path
import json,csv,collections
ROOT=Path(__file__).resolve().parent
inv=json.loads((ROOT.parent/'v15/inventory.json').read_text())
rows=[]
for c in inv:
    n=c['name'];mat=c['material'].lower();note='CAD volume x assumed density; nominal solid printed walls'
    v=sum(b['volume_mm3']for b in c['bodies'])/1000
    cat='structure'
    if 'GWK7010' in n:
        m=.334;lo=.30;hi=.40;cat='7010 motors';note='334 g provisional catalog mass, not independently manufacturer-confirmed; range is planning sensitivity'
    elif n.startswith('R01'):
        m=lo=hi=.756;cat='DJI motors';note='DJI T30 official 100x18/77KV motor 756 g; actual purchased variant unverified; no cut-post credit'
    elif n.startswith(('T07','T09')):
        m,lo,hi=(1.,.7,1.3)if n.startswith('T07')else(.75,.5,1.0)
        cat='unselected hip motors';note='Engineering allocation only, not vendor specification; includes future actuator reduction in this envelope'
    elif n.startswith('E03'):
        m=.06;lo=.04;hi=.08;cat='electronics';note='Board mass allocation; not density of solid electronics envelope'
    else:
        m=0
        for b in c['bodies']:
            bn=b['name'];rho=None
            if n.startswith('M02'):
                if 'vendor_visible_rotating_output' in bn:rho=0;note='Motor output already included in complete 7010 mass; custom crank Al, pins/rings/washers steel'
                elif bn=='Body1':rho=2.70
                else:rho=7.85
            elif n.startswith('A01'):rho=1.06 if bn=='Upper_clamp_split'else 7.85
            elif 'bearing assembly' in mat or '608 bearing' in mat:
                rho=2.70 if ('Standing bearing' in bn or 'CUSTOM_CNC' in bn)else 1.2 if 'Seal' in bn else 7.85
                note='Mixed bearing: housing aluminum, rings/balls/collar steel, seals elastomer; vendor housing alloy unverified'
            elif 'insert_installed' in bn:rho=8.5
            elif 'steel' in mat or n.startswith('F09'):rho=7.85
            elif 'aluminum' in mat or '6061' in mat or 'sprocket' in mat:rho=2.70
            elif 'tpu' in mat:rho=1.2
            elif 'pa' in mat or 'plastic' in mat:rho=1.06
            assert rho is not None,(n,bn,mat)
            m+=b['volume_mm3']/1000*rho/1000
        lo=m*.9;hi=m*1.1
    rows.append(dict(side=c['side'],component=n,volume_cm3=v,category=cat,mass_kg=m,low_kg=lo,high_kg=hi,basis=note))
with (ROOT/'mass_components.csv').open('w',newline='')as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
totals={}
for s in sorted(set(r['side']for r in rows)):
    rs=[r for r in rows if r['side']==s]
    totals[s]={k:sum(r[k]for r in rs)for k in ['mass_kg','low_kg','high_kg']}
    totals[s]['categories']={k:sum(r['mass_kg']for r in rs if r['category']==k)for k in sorted(set(r['category']for r in rs))}
totals['modeled_budget']={k:sum(r[k]for r in rows)for k in ['mass_kg','low_kg','high_kg']}
totals['unmodeled_lower_assembly_allocation']={'mass_kg':1.8,'low_kg':1.0,'high_kg':3.0,'basis':'Two knee gearsets 0.6 kg; chains 0.4; missing drivers/encoders/wiring 0.5; bearings/seam/retention hardware 0.3. Planning allocations, no chain dimensions calculated. Excludes torso and battery.'}
totals['completed_lower_assembly_budget']={k:totals['modeled_budget'][k]+totals['unmodeled_lower_assembly_allocation'][k]for k in ['mass_kg','low_kg','high_kg']}
(ROOT/'mass_summary.json').write_text(json.dumps(totals,indent=2))
print(json.dumps(totals,indent=2))
