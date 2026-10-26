"""First-pass beam/annular-strip screening, not FEA or a load rating."""
import json,math,csv
from pathlib import Path
P=Path(__file__).resolve().parent
ss=json.loads((P/'sections_verified.json').read_text())['sections']
m=json.loads((P/'mass_summary.json').read_text())
g=9.81;strength=42.1;sf=3.;local_factor=2.;screen=strength/sf/local_factor
secs=[]
for x in [0,15,30,45,52,60,75]:
    rs=[s for s in ss if s['kind']=='global'and s['axis']=='x'and s['position_mm']==x]
    aa=[s['volume_mm3']/s['thickness_mm']for s in rs]
    zc=sum(a*s['com_mm'][2]for a,s in zip(aa,rs))/sum(aa)
    iy=0
    for a,s in zip(aa,rs):
        cx,cy,cz=s['com_mm'];mass=s['mass']
        # Fusion world-origin kg cm2 -> centroid geometric section mm4.
        ic=(s['inertia_kgcm2'][2]*100/mass-cx*cx-cz*cz)*a
        ic-=a*s['thickness_mm']**2/12
        assert ic>0
        iy+=ic+a*(cz-zc)**2
    zlo=min(s['min_mm'][2]for s in rs);zhi=max(s['max_mm'][2]for s in rs)
    Z=iy/max(zhi-zc,zc-zlo)
    secs.append(dict(x_mm=x,area_mm2=sum(aa),Iyy_mm4=iy,Z_mm3=Z,screen_moment_Nm=screen*Z/1000))
def ring(a,b,t,area):
    fraction=area/(math.pi*(b*b-a*a))
    meanr=2/3*(b**3-a**3)/(b*b-a*a)
    def f(lever):return screen*(2*math.pi*b*fraction)*t*t/(6*lever)
    return dict(a_mm=a,b_mm=b,t_mm=t,measured_area_mm2=area,circumference_fraction=fraction,inner_edge_load_limit_N=f(b-a),distributed_load_limit_N=f(b-meanr),distributed_lever_mm=b-meanr)
yawarea=sum(s['volume_mm3']/.2 for s in ss if s['kind']=='yaw_seat')
hiparea=sum(s['volume_mm3']/.2 for s in ss if s['kind']=='hip_seat')
yaw=ring(18,39,5,yawarea);hip=ring(18,55,3,hiparea)
hip['vertical_inner_edge_limit_N']=hip['inner_edge_load_limit_N']/math.sin(math.radians(25))
hip['vertical_distributed_limit_N']=hip['distributed_load_limit_N']/math.sin(math.radians(25))
waist=m['Waist_layout_v15']['mass_kg']
swing=(m['Left_leg']['mass_kg']+m['Right_leg']['mass_kg'])/2+.9
scenarios=[]
for U in [10,15,20]:
 for D in [1,2,3]:
    Rtwo=D*g*(U+waist)/2
    Rone=D*g*(U+waist+swing)
    fyaw=D*g*(U+.334)
    moment=D*g*((U+waist)*.075+swing*.150)
    scenarios.append(dict(upper_mass_kg=U,load_factor=D,yaw_load_N=fyaw,two_leg_reaction_each_N=Rtwo,one_leg_stance_reaction_N=Rone,swing_hip_downforce_N=D*g*swing,global_screen_moment_Nm=moment,yaw_screen_utilization=fyaw/yaw['inner_edge_load_limit_N'],hip_two_screen_utilization=Rtwo/hip['vertical_inner_edge_limit_N'],hip_one_screen_utilization=Rone/hip['vertical_inner_edge_limit_N']))
caps=[]
for D in [1,2,3]:
    ymax=yaw['inner_edge_load_limit_N']/(D*g)-.334
    hip2=2*hip['vertical_inner_edge_limit_N']/(D*g)-waist
    hip1=hip['vertical_inner_edge_limit_N']/(D*g)-waist-swing
    caps.append(dict(load_factor=D,yaw_upper_kg=ymax,two_leg_upper_kg=min(ymax,hip2),one_leg_upper_kg=min(ymax,hip1)))
out=dict(method='conditional short-term screening only',criterion_MPa=screen,factor_of_safety=sf,local_factor=local_factor,waist_kg=waist,swing_leg_kg=swing,sections=secs,yaw_seat=yaw,hip_seat=hip,scenarios=scenarios,conditional_upper_mass_thresholds=caps)
(P/'calculation_results.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
