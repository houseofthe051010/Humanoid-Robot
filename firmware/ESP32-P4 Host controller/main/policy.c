#include <math.h>
#include <string.h>
#include "robot.h"
#include "policy_meta.h"
extern const float weights[] asm("_binary_actor_bin_start");
void policy_forward(const float obs[400],float action[NJ]){
 float a[512],b[512];const float *in=obs,*p=weights;
 const int widths[]={400,512,256,128,23};
 for(int layer=0;layer<4;layer++){
  int ni=widths[layer],no=widths[layer+1];float *out=layer==3?action:(layer%2?a:b);
  const float *bias=p+ni*no;
  for(int j=0;j<no;j++){float sum=bias[j];for(int k=0;k<ni;k++)sum+=in[k]*p[j*ni+k];out[j]=(layer<3&&sum<0)?expm1f(sum):sum;}
  p=bias+no;in=out;
 }
}
bool policy_selftest(void){float out[NJ];policy_forward(golden_obs,out);
 for(int i=0;i<NJ;i++){if(!isfinite(out[i])||fabsf(out[i]-golden_action[i])>0.0002f)return false;}
 return true;}
bool policy_observe(const imu_t *imu,const float q[NJ],const float dq[NJ],float speed,float elapsed,const float prev[NJ],float obs[400]){
 // IMU quaternion is x,y,z,w. Assumes calibrated sensor-to-torso mounting.
 float x=imu->quat[0],y=imu->quat[1],z=imu->quat[2],w=imu->quat[3];
 float norm=sqrtf(x*x+y*y+z*z+w*w);if(!isfinite(norm)||norm<.5f||norm>1.5f)return false;
 x/=norm;y/=norm;z/=norm;w/=norm;
 float f[80]={0};for(int i=0;i<3;i++)f[i]=imu->gyro[i]*.2f;
 f[3]=2*(w*y-x*z);f[4]=-2*(y*z+w*x);f[5]=2*(x*x+y*y)-1;
 f[6]=speed; // lateral and yaw-rate commands default to zero; no camera input in this policy.
 for(int i=0;i<NJ;i++){if(!isfinite(q[i])||!isfinite(dq[i]))return false;f[9+i]=q[i]-stand[i];f[32+i]=dq[i]*.05f;f[55+i]=prev[i];}
 float period=speed>=1.5f?1.f/(.9f+.5f*fabsf(speed)):.8f;
 if(speed>.1f){f[78]=sinf(6.28318530718f*elapsed/period);f[79]=cosf(6.28318530718f*elapsed/period);}
 memmove(obs,obs+80,320*sizeof(float));memcpy(obs+320,f,sizeof(f));return true;
}
