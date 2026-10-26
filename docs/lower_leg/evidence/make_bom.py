"""Generate a price-free, per-leg engineering BOM; stock ownership is deliberately separate."""
import csv,json
from pathlib import Path
BASE=Path(__file__).resolve().parents[3];OUT=BASE/'docs/lower_leg';OUT.mkdir(exist_ok=True)
rows=[]
def add(group,item,qty,spec,source,status='CAD nominal; verify actual parts',material=''):
 rows.append(dict(id=f'LL-{len(rows)+1:03}',assembly=group,item=item,quantity_per_leg=qty,unit='each',specification=spec,material=material,cad_source=source,status=status,ownership='Not audited'))
add('Foot','Aluminum foot plate',1,'100 x122 x4 mm; eight current 5.4 mm through holes','F01',material='Aluminum; alloy TBD')
add('Foot','Printed sole',1,'Preserved outline;10 mm thick with flat underside and bottom nut access','F02',material='Printed plastic; final formulation TBD')
add('Ankle and knee','8 mm bore pillow block assembly',8,'2 roll +2 pitch +2 heel +2 knee; includes bearing/collar and supplier set screws','F03,F04,S02,S03,F06L/R,N04L/R','Purchased style represented; actual bearing and housing ratings require confirmation')
add('Ankle','Smooth roll shaft',1,'Diameter8 x53 mm','A01/Roll_shaft_8mm',material='Steel; grade unknown')
add('Ankle','Smooth pitch shaft',1,'Diameter8 x92 mm','A01/Pitch_shaft_8mm',material='Steel; grade unknown')
add('Heel','Smooth cross-shaft with end threads',1,'Diameter6 x97 mm; M6x1 end retention modeled','F08','Saved CAD is97 mm; user-owned96 mm shaft needs retention fit review', 'Steel; grade unknown')
add('Knee','Smooth knee shaft',1,'Diameter8 x104 mm after narrowing','N02','Geometry only; fails assumed mild-steel5x landing screen', 'Steel; grade unknown')
add('Ankle','Printed cross-axis block',1,'Two perpendicular8 mm bores and M3 pinch clamps','A01/Upper_clamp_split',material='PA-CF; exact grade/print orientation TBD')
add('Shin','Ankle-to-shin adapter',1,'Rail centres X +/-10 mm,Y6 mm; unchanged bearing interface','S01',material='PA-CF')
add('Shin','Continuous oval steel rail',2,'18 x10 stadium; assumed0.55 wall;354.6 mm long','S05L/R',material='Salvaged steel; measure section')
add('Shin','Dual motor carrier',1,'Narrowed rail sockets; separate removable motor covers','S06',material='PA-CF')
for side in ['A','B']:add('Shin','Motor cover '+side,1,'5 mm thick; original vendor motor profile','S10_'+side,material='PA-CF')
add('Shin','Crush sleeve',12,'5 OD x3.4 ID x10 mm','H01',material='Steel')
add('Ankle drive','GWK7010-8 motor assembly',2,'Supplied vendor STEP; housing and output CAD bodies constitute one motor','M01A/B + M02 vendor output','Motor torque40 Nm is a screening assumption, not a validated continuous rating')
add('Ankle drive','Aluminum output crank',2,'6 mm thick;23 mm crank radius; six M3 mounting positions','M02A/B/Body1',material='6061-T6 nominal')
add('Ankle drive','Female rod-end bearing',4,'M6x1 right hand female thread;6 mm spherical bore;9 mm inner-ring width','L01 housings + M02/F08 inner rings','Wixroyd65720.W0006 surrogate CAD; confirm purchased SI6 dimensions')
for side,L in [('A',285.1265),('B',202.8568)]:
 add('Ankle drive','M6 threaded link '+side,1,f'M6x1 RH; CAD stock length{L:.4f} mm;12 mm nominal engagement each end','L01_'+side,material='Steel; grade unknown')
for side,L in [('A',230),('B',140)]:add('Ankle drive','Oval reinforcement '+side,1,f'18 x10 x assumed0.55 wall;{L} mm long','L02_'+side,material='Salvaged steel')
add('Ankle drive','Threaded rod-to-oval end adapter',4,'20 mm insert plus1.5 mm flange; modeled M6 female thread','L03A/B upper/lower',material='PA-CF')
for side in ['A','B']:add('Ankle drive','Central rod guide '+side,1,'Length follows link;6.4 mm running bore','L04_'+side,material='PA-CF')
add('Heel','8-to-6 mm bearing reducer',2,'8 OD x6 ID x12 mm','F07L/R','Carries radial load; no strength qualification', 'PA-CF')
add('Heel','Outer axial spacer',2,'8.5 OD x6.2 ID x4.95 mm','F10','Axial spacing only; no shaft bending credit', 'PA-CF')
add('Heel','Central axial spacer',1,'8.5 OD x6.2 ID x37 mm','F10','Steel replacement discussed but not implemented', 'PA-CF')
add('Ankle drive','Upper rod-end pin',2,'M6 nominal; CAD envelope; length and retention TBD','M02A/B/M6_upper_rod_end_pin','Needs hardware selection; do not infer finished fastener from envelope','Steel')
add('Ankle drive','Upper inner-ring spacer',2,'4.5 mm long;7 mm OD nominal envelope','M02A/B','Through-bore/actual pin fit requires final hardware detailing','Steel nominal')
add('Electronics','ODrive controller board assembly',1,'15 source bodies; connector bodies removed for direct wiring','E03','Exact controller variant and electrical connections require confirmation')
add('Electronics','Upper rail clip',1,'Sockets at20 mm centre spacing; PCB position retained','E04',material='TPU')
add('Electronics','PCB spacer',2,'2 mm thick; M3 bore','E05_1/2',material='TPU')
for i,t in [(1,11),(2,10),(4,10),(5,11)]:add('Knee','Machined knee slice '+str(i),1,f'{t} mm X thickness; four slices42 mm total; centre piece removed','N01_'+str(i),material='6061-T6 nominal')
add('Knee','Sprocket interface blank',1,'70 mm OD x6 mm; six registration/tie positions; no teeth','N03','Layout only; transmission may change for QDD','Material TBD')
for side in ['L','R']:
 for piece in ['base','cap']:add('Thigh interface','Oval clamp '+side+' '+piece,1,'Shifted4 mm inward with knee bearings','N05_'+side+'_'+piece,material='6061-T6 nominal')
add('Thigh interface','Oval upper-leg stub',2,'18 x10 x assumed0.55 wall;90 mm long reference','N06L/R','Layout stubs; not final thigh cut lengths','Steel')
add('Knee drive','DJI10018 77KV motor',1,'105 mm OD,30 mm body,6 mm rear projection,24 mm prop posts estimated','R01','Planned purchase; parked photo-derived reference; not measured or mounted')
hardware=[
 ('Foot','M5 socket screw',8,'M5x20','F09,F11'),('Foot','M5 washer',16,'10 OD x5.3 ID x1 mm','F09,F11'),('Foot','M5 hex nut',8,'M5;8 AF;4 mm thick','F09,F11'),
 ('Heel','M6 thin retaining nut',2,'M6x1;10 AF; verify3.85 mm available engagement','F11'),
 ('Motor covers','M3 socket screw',12,'M3x12','H02'),('Motor covers','M3 countersunk screw',16,'M3x12','H02'),('Motor covers','M3 heat-set insert',12,'4.6 OD x5 mm envelope;4.3 mm pilot needs calibration','H02'),
 ('Cranks','M3 washer',12,'1 mm thick','M02A/B'),
 ('Electronics','M3 socket screw',2,'M3x10','E06'),('Electronics','M3 washer',2,'1 mm thick','E06'),('Electronics','M3 nut',2,'M3 standard','E06'),
 ('Knee stack','M3 socket screw',4,'M3x55; verify availability/cutdown from longer stock','N07'),('Knee stack','M3 nut',6,'4 tie nuts +2 rail nuts','N07'),('Knee stack','Registration dowel',2,'Diameter6 x48 mm','N07'),('Knee stack','M3 rail crossbolt',2,'M3x50','N07'),('Knee stack','M3 shaft set screw',2,'M3x10','N07'),
 ('Thigh clamps','M3 socket screw',8,'M3x35','N08'),('Thigh clamps','M3 nut',8,'M3 standard','N08'),('Thigh clamps','M5 socket screw',4,'M5x16','N08'),('Thigh clamps','M5 washer',4,'1 mm thick','N08'),('Thigh clamps','M5 nut',4,'M5 standard','N08'),
 ('Ankle cross block','M3 pinch screw',2,'Nominal under-head lengths31 and27 mm in envelope; choose stock lengths after fit check','A01'),('Ankle cross block','M3 nut',2,'M3 standard','A01')]
for group,item,qty,spec,src in hardware:add(group,item,qty,spec,src,material='Metal; grade/finish to select')
for group,item,qty,spec,src in [
 ('Shin','Rail crossbolts and nuts',10,'M3;4 adapter +6 carrier; lengths TBD from final seats','S01,S06,H01'),
 ('Ankle adapter','Pitch pillow mounting screws and nuts',4,'M5; final length TBD','S01,S02,S03'),
 ('Cranks','Motor-output screws',12,'M3;6 mm crank +1 mm washer +up to5 mm engagement; candidateM3x12','M02A/B'),
 ('Links','M6 jam nuts',4,'M6x1 RH; final adjustment/engagement budget must include nut thickness','L01A/B')]:
 add(group,item,qty,spec,src,'Required assembly hardware; not fully represented in CAD; finalize before ordering')
for item,src in [('Earlier GIM10015 layout motor','U01 and GIM10015-9-3D-Model'),('Earlier GWK7010 layout copy','U02'),('User-added root layout body','U03')]:
 add('Preserved references',item,1,'Retained hidden; exclude from build quantity totals',src,'Reference only; not an additional installed part')
with (OUT/'BOM.csv').open('w',newline='',encoding='utf-8-sig')as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
text=['# Lower-leg engineering BOM — v9','', 'Price-free BOM for **one modeled leg and its knee/thigh interfaces**, not a whole robot inventory. Quantities describe the design; purchases/ownership have not been audited. A second mirrored leg usually doubles quantities, but electronics and body-wide items must be planned separately.','', 'Source: live v8 checked against the saved v8 geometry, followed by the v9 revision scripts. Supplier motor bodies, bearing balls/races and rod-end inner rings are bundled into purchased assemblies so they are not double-counted. Hidden earlier layouts are recorded separately.','', '**Do not order unresolved hardware by guessing a length.** The final rows identify required screws that were missing or incomplete in the inherited model. The8 mm knee shaft is geometry only and is not approved for the assumed jump load. See [knee calculation](KNEE_STRENGTH_V9.md).','', '[Download/edit BOM.csv](BOM.csv)','', '| ID | Assembly | Item | Qty/leg | Specification | Status |','|---|---|---|---:|---|---|']
for r in rows:text.append('| '+' | '.join(str(r[k]).replace('|','/')for k in ['id','assembly','item','quantity_per_leg','specification','status'])+' |')
text+=['','## Not yet designed or counted','', 'QDD planetary, knee motor bracket, final chain/sprocket transmission, encoders, encoder mounts, complete upper legs, hip/waist/torso, battery, wiring/connectors, heatsinks and full-body fasteners. The DJI prop posts remain shown as uncut reference features. Removing a motor feature requires inspection of the actual motor.','', 'The old8 mm knee centre piece is removed. The empty N00 component is a joint datum and has zero physical quantity. A proposed steel centre spacer on the heel shaft is not silently substituted for the current printed spacer.']
(OUT/'BOM.md').write_text('\n'.join(text)+'\n',encoding='utf-8')
print(json.dumps({'rows':len(rows),'csv':str(OUT/'BOM.csv'),'markdown':str(OUT/'BOM.md')},indent=2))
