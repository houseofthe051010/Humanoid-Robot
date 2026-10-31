# ESP32-P4 host controller

ESP-IDF prototype for the Waveshare ESP32-P4-Module-DEV-KIT. Includes the final trained actor, three CAN interfaces, two servo UART buses, elbow PWM, BNO085 readings and USB camera frame counting.

## Pins

GPIO numbers below match the labels in the [schematic](../../Schematics/Humanoid_Electronics.pdf).

| Function | GPIO | P6 header pin |
|---|---|---|
| CAN A TX / RX | 1 / 2 | 21 / 20 |
| CAN B TX / RX | 3 / 4 | 18 / 17 |
| CAN C TX / RX | 5 / 6 | 15 / 14 |
| UART1 head / wrists, single wire | 20 | 12 |
| UART2 hands, single wire | 21 | 10 |
| Left / right elbow PWM | 22 / 23 | 11 / 6 |
| BNO085 SDA / SCL | 7 / 8 | 2 / 4 |
| BNO085 INT / RST | 26 / 36 | 30 / 23 |
| Camera | Dedicated USB0 D+ / D− and VBUS | Carrier USB host socket |

Power BNO085 VIN at 3.3 V, share GND and leave P0/P1 low for I2C address 0x4A. GPIO7/8 share the carrier's I2C peripherals. Select the carrier's USB HOST jumper setting. Single-wire servo outputs are open drain and require suitable pull-ups/logic levels; schematic pull-up values remain TBD.

## Build

Toolchain: ESP-IDF 6.0.1, target `esp32p4`. The component manager downloads `espressif/usb_host_uvc` 2.6.0.

The verified default build targets chip revision 3.1+. For an older P4 module, select the matching silicon revision in `idf.py menuconfig` before rebuilding; pre-3.0 and 3.x binaries are not interchangeable.

```sh
idf.py set-target esp32p4
idf.py build
idf.py -p PORT flash monitor
```

`main/actor.bin` contains the unmodified 400 → 512 → 256 → 128 → 23 ELU actor. `tools/export_actor.py` regenerates it from the adjacent training package using PyTorch. A fixed numerical self-test runs at boot; observations use five 80-value frames at a nominal 50 Hz.

## Prototype status

- CAN: three 500 kbit/s buses, receive queues, encoder/heartbeat decoding, CAN Simple position/state messages and persistent transmit buffers. Proposed node IDs and motor routing are in `can_motors.c`; commission the controllers to match. Driver firmware versions, periodic feedback and control mode need hardware checks.
- Servos: STS/SCS packet checksums and position writes, STS position/speed polling, and two 50 Hz PWM outputs. IDs 1/2 are head servos; 3–6 are wrists. Hand IDs 1–16 are separate. Verify register tables, baud rates and position conventions.
- IMU: minimal BNO085 SHTP/I2C rotation-vector and calibrated-gyro reception with timestamps. Sensor mounting rotation and hardware packet captures need validation.
- Camera: opens a 320×240 MJPEG UVC stream at 15 fps and counts completed nonempty frames. No image/depth processing. AI VIEW's documented Orbbec SDK path is not ported; actual USB descriptors/formats must match before this UVC path can receive frames.
- Policy: exact weights and observation assembly are present. Automatic motor enable is absent. `calibration.h` remains uncommissioned; differential kinematics, measured offsets/ratios/signs, native limit projection, head conversion and elbow feedback are unfinished. `joints()` therefore returns false and the loop stays unarmed. The PWM elbows expose no position feedback in the current schematic. Camera data is not a policy input.

This is a transport/inference starting point, not working walking firmware. No board has been flashed or hardware-tested.

## References

- [Waveshare board schematic](https://files.waveshare.com/wiki/ESP32-P4-Module-DEV-KIT/ESP32-P4-Module-DEV-KIT.pdf)
- [ESP-IDF TWAI](https://docs.espressif.com/projects/esp-idf/en/latest/esp32p4/api-reference/peripherals/twai.html)
- [SteadyWin GDS68 downloads](https://steadywin.cn/en/col.jsp?id=124)
- [Adafruit BNO085 pinouts](https://learn.adafruit.com/adafruit-9-dof-orientation-imu-fusion-breakout-bno085/pinouts)
- [Espressif UVC driver](https://github.com/espressif/esp-usb/tree/master/host/class/uvc/usb_host_uvc)
- [Yahboom AI VIEW camera instructions](https://www.yahboom.net/study/AIVIEW_Camera/11563/)
