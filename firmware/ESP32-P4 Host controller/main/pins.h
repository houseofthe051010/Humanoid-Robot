#pragma once
// Waveshare ESP32-P4-Module-DEV-KIT P6 header; GPIO numbers, not header positions.
#define CAN_A_TX 1  // P6.21
#define CAN_A_RX 2  // P6.20
#define CAN_B_TX 3  // P6.18
#define CAN_B_RX 4  // P6.17
#define CAN_C_TX 5  // P6.15
#define CAN_C_RX 6  // P6.14
#define STS_PIN 20  // P6.12, UART1 single wire
#define HAND_PIN 21 // P6.10, UART2 single wire
#define ELBOW_L_PIN 22 // P6.11
#define ELBOW_R_PIN 23 // P6.6
#define IMU_SDA 7   // P6.2, shared onboard I2C
#define IMU_SCL 8   // P6.4
#define IMU_INT 26  // P6.30
#define IMU_RST 36  // P6.23
// USB0 uses dedicated DP/DM pads and the carrier's USB host socket/jumper.
