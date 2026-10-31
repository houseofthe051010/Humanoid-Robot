#pragma once
#include <stdbool.h>
#include <stdint.h>
#include "esp_err.h"
#define NJ 23
#define NM 19
typedef struct {float pos,vel; int64_t stamp; bool valid;} feedback_t;
typedef struct {float quat[4],gyro[3]; int64_t quat_time,gyro_time;} imu_t;
typedef struct {uint8_t bus,node; int8_t joint; bool odrive;} motor_t;
extern const motor_t motors[NM];
esp_err_t can_start(void);
void can_poll(void);
bool can_feedback(unsigned i,feedback_t *f);
esp_err_t can_position(unsigned i,float turns);
esp_err_t can_idle_all(void);
esp_err_t can_enable_all(void);
void servos_start(void);
void servos_poll(void);
bool servo_feedback(unsigned id,feedback_t *f);
esp_err_t servo_goal(bool hands,unsigned id,unsigned ticks);
void elbow_goal(unsigned side,unsigned pulse_us);
void imu_start(void);
bool imu_snapshot(imu_t *out);
void camera_start(void);
unsigned camera_frames(void);
void policy_forward(const float obs[400],float action[NJ]);
bool policy_selftest(void);
bool policy_observe(const imu_t *imu,const float q[NJ],const float dq[NJ],
                    float speed,float elapsed,const float prev[NJ],float obs[400]);
