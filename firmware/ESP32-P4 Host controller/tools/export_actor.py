"""Export the supplied actor without changing its weights; run in the training Python environment."""
from pathlib import Path
import hashlib,json
import numpy as np
import torch
R=Path(__file__).resolve().parents[1]
training=R.parent/'ISAAC Lab training'
p=training/'checkpoints/final_1226.pt'
saved=torch.load(p,map_location='cpu',weights_only=False)
s=saved['actor_state_dict']
arrays=[]
for layer in [0,2,4,6]:
    arrays.extend([s[f'mlp.{layer}.weight'].numpy().astype('<f4').ravel(),s[f'mlp.{layer}.bias'].numpy().astype('<f4')])
(R/'main/actor.bin').write_bytes(np.concatenate(arrays).tobytes())
obs=np.random.default_rng(71).uniform(-.5,.5,400).astype('float32')
x=torch.from_numpy(obs)
for i in [0,2,4,6]:
    x=torch.nn.functional.linear(x,s[f'mlp.{i}.weight'],s[f'mlp.{i}.bias'])
    if i!=6:x=torch.nn.functional.elu(x)
names=json.loads((training/'config/run_config.json').read_text())['joints']
motion=np.load(training/'source/physical_v29/training/assets/motion_reference.npz')
stand=[float(motion['stand'][motion['names'].tolist().index(n)]) for n in names]
def c_array(name,values,static=True):
    return ('static ' if static else '')+'const float '+name+f'[{len(values)}]={{'+','.join(f'{float(v):.9e}f' for v in values)+'};\n'
(R/'main/policy_meta.h').write_text('#pragma once\n'+c_array('stand',stand,False)+c_array('golden_obs',obs)+c_array('golden_action',x.detach().numpy()))
(R/'policy_export.json').write_text(json.dumps(dict(checkpoint_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),actor_sha256=hashlib.sha256((R/'main/actor.bin').read_bytes()).hexdigest(),joint_order=names,dimensions=[400,512,256,128,23],activation='ELU',observation_normalization=False,action_scale=.25,period_s=.02),indent=2))
print('Actor exported:',(R/'main/actor.bin').stat().st_size,'bytes')
