# ESP32-P4 host controller

Implementation has not started. The previous Raspberry Pi/STM32 code is preserved in the local archive.

Planned interfaces: three CAN buses for 15 SteadyWin drivers and two dual ODrives; separate single-wire UART buses for head/wrist and hand servos; PWM for the two elbow servos; BNO085 IMU; USB host for the AI VIEW camera.

## Driver research — October 31, 2026

[SteadyWin's official downloads](https://steadywin.cn/en/col.jsp?id=124) publish a GDS68 motor manual and MotorWizard software. The downloaded rev2.2 manual documents CAN SIMPLE, CANopen, MIT control and host examples. Public driver firmware source has not been verified. Host control uses the installed driver firmware; rewriting the FOC firmware is not required.

Confirm the purchased board and firmware version before choosing a protocol. USB commands and CAN MIT commands use different shaft conventions in this manual; reductions and units must be mapped explicitly.

The [ESP-IDF TWAI driver](https://docs.espressif.com/projects/esp-idf/en/latest/esp32p4/api-reference/peripherals/twai.html) supports three P4 controllers. Each bus requires an external transceiver. Pin allocation, bus timing, UART turnaround, sensor integration and camera USB protocol remain to be implemented and tested.
