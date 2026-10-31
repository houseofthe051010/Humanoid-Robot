#pragma once
// Commissioning defaults deliberately do not claim a measured joint/motor mapping.
// Fill zero/sign/reduction and nonlinear differential adapters before enabling output.
#define ROBOT_CALIBRATED 0
static const float motor_zero[NM]={0};
static const float motor_turns_per_joint_rad[NM]={0};
static const float servo_zero[6]={2048,2048,2048,2048,2048,2048};
static const float servo_ticks_per_rad[6]={0};
// Wrist IDs 3..6 and hand IDs 1..16 are outside the locomotion network.
