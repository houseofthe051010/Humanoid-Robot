#include <math.h>
#include <string.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_log.h"
#include "esp_timer.h"
#include "robot.h"
#include "calibration.h"
// Board transport + exact actor prototype. No automatic motor enable at boot.
// Replace these joint adapters with measured mappings, especially CAD differentials.
static bool joints(float q[NJ],float dq[NJ]){
 if(!ROBOT_CALIBRATED)return false;
 int64_t now=esp_timer_get_time();
 for(int i=0;i<NM;i++){
  feedback_t f;if(!can_feedback(i,&f)||!f.valid||now-f.stamp>100000||motor_turns_per_joint_rad[i]==0)return false;
  // Ankle and waist differential axes require a coupled nonlinear solve, not this direct formula.
  if(i==4||i==5||i==10||i==11||i==16||i==17)return false;
  int j=motors[i].joint;q[j]=(f.pos-motor_zero[i])/motor_turns_per_joint_rad[i];dq[j]=f.vel/motor_turns_per_joint_rad[i];
 }
 // Head feedback can be read from STS IDs 1/2. PWM elbows have no feedback in the schematic.
 // Never invent elbow angles or infer them from commanded PWM.
 return false;
}
static void targets(const float a[NJ]){
 // This function is gated by joints(); transport encoders are implemented separately.
 // Apply calibrated nonlinear differential mapping and native speed/torque limits here before use.
 for(int i=0;i<NM;i++){int j=motors[i].joint;
  extern const float stand[NJ];float q=stand[j]+.25f*fmaxf(-100.f,fminf(100.f,a[j]));
  can_position(i,motor_zero[i]+q*motor_turns_per_joint_rad[i]);}
}
void app_main(void){
 ESP_LOGI("robot","Exact final actor self-test: %s",policy_selftest()?"PASS":"FAIL");
 bool model_ok=policy_selftest();
 ESP_ERROR_CHECK(can_start());servos_start();imu_start();camera_start();
 float obs[400]={0},previous[NJ]={0},q[NJ]={0},dq[NJ]={0},action[NJ];
 TickType_t tick=xTaskGetTickCount();int64_t start=esp_timer_get_time();unsigned step=0;
 for(;;){
  can_poll();servos_poll();imu_t imu;bool ready=model_ok&&imu_snapshot(&imu)&&joints(q,dq);
  if(ready&&policy_observe(&imu,q,dq,0.f,(esp_timer_get_time()-start)*1e-6f,previous,obs)){
   policy_forward(obs,action);for(int i=0;i<NJ;i++)if(!isfinite(action[i]))ready=false;
   if(ready){memcpy(previous,action,sizeof(action));targets(action);}
  }
  if(!ready){memset(obs,0,sizeof(obs));memset(previous,0,sizeof(previous));}
  if(step++%50==0)ESP_LOGI("robot","policy_ready=%d camera_frames=%u; motor output unarmed",ready,camera_frames());
  vTaskDelayUntil(&tick,pdMS_TO_TICKS(20));
 }
}
