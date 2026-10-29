# Humanoid Robot

This is my project to build a human-sized bipedal robot. In this repo I have all my current designs for my robot's shin and lower leg, and the iterations of gearboxes I have made for my actuators.

Right now, I am using pre-made actuators and am waiting on a grant to further complete my robot.

This grant is for building and testing the robot's two lower-leg and ankle assemblies. It is the first stage of the humanoid and is not funding the complete robot.

This is the current prototype, showing both lower-leg assemblies side by side.

![Two lower-leg prototype assemblies](Assets/2x%20Lower%20Leg%20Assembly.png)

## Electronics

Each ankle motor is controlled by a single-axis ODrive 3.6 clone. Both ODrives share one CAN bus with an STM32F103. The ODrives run the motor-control loops; the STM32 relays position commands from a Raspberry Pi 5 over SPI. UART is available for setup and debugging.

This is a wiring diagram of how i'll utilize CAN buses for each motor [`Schematics/`](Schematics/).

![Electronics architecture](Schematics/schematic.png)

## Design

At first, I was thinking of a 2-DOF ankle design but now I am thinking of 1-DOF as its much cheaper and is really what I need. This came from a lot of thinking, as I am utilizing a lot of plastic for this build (though I will utilize aluminum in places where necessary). A lot of my body will be plastic and needs to be designed appropriately to support a bipedal's weight that is 5 foot tall. Currently I have a 1-dof ankle structure with a linkage system for only ankle pitch motion.

A bipedal can easily walk on level ground with ankle pitch. I have also attached a 50mm bearing hole for attaching the knee.

I also kept my earlier 2-DOF single-leg assembly as a backup in case I return to a 2-DOF ankle in the future.

![Backup 2-DOF lower-leg assembly](Assets/1x%20Prototype%202-DOF%20Lower%20Leg%20Assembly.png)

## Gearbox designs

The [`CAD/Actuators/`](CAD/Actuators/) folder has my custom planetary and cycloidal C6374 designs.

These gearboxes were built by me as a part of prototyping and learning on how to make my robot. They are there as they helped me decide how to make my robot and what actuators to use. I chose the cyclodial gearbox over the plantery in my design as it was easier to print with lower backlash, had high reductions, and was stronger, giving me 50+nm torque around 100mm size. Though, I chose to use a pre-built one as it was much less complex. 

## Bill of materials

[Download BOM CSV](bom.csv)

| Type | Buy / Fabricate | Item | Quantity | Unit price (USD) | Final price (USD) | Product link | Notes |
|---|---|---|---:|---:|---:|---|---|
| Electrical | Buy | SteadyWin GWK7010-8 motor | 7 | $81.61 | $571.27 | [Product](https://www.aliexpress.com/item/3256803276650569.html) |  |
| Electrical | Buy | SteadyWin GWK6010-8 motor | 6 | $72.58167 | $435.49 | [Product](https://www.aliexpress.com/item/3256806290989080.html) |  |
| Electrical | Buy | DJI 10018 77 KV motor | 6 | $64.68375 | $388.10 | [Product](https://www.aliexpress.com/item/3256811842519170.html) |  |
| Electrical | Buy | Feetech STS3215-C018 12 V servo | 6 | $37.39 | $224.34 | [Product](https://www.aliexpress.us/item/3256811423365280.html) |  |
| Electrical | Buy | RDS51160 24 V elbow servo | 2 | $39.99 | $79.98 | [Product](https://www.ebay.com/itm/186554276132) |  |
| Electrical | Buy | Feetech SCS0009 hand servo | 16 | $8.00 | $128.00 | [Product](https://www.seeedstudio.com/Feetech-SCS0009-Servo-p-6535.html) |  |
| Mechanical | Buy | 6810 / 61810 bearing, 50 x 65 x 7 mm | 2 |  |  |  |  |
| Mechanical | Buy | 6005 bearing, 25 x 47 x 12 mm | 3 |  |  |  |  |
| Mechanical | Buy | 6007 bearing, 35 x 62 x 14 mm | 2 |  |  |  |  |
| Mechanical | Buy | 61810 / 6810 bearing, 50 x 65 x 7 mm | 4 |  |  |  |  |
| Mechanical | Buy | 40 x52 x7mm hip-pitch bearing | 4 | $19.99 | $79.96 | [Product](https://vxb.com/products/6808rs-ball-bearing-40x52x7-sealed) |  |
| Mechanical | Buy | M2 ball joints with supplied hardware | 32 |  |  |  |  |
| Mechanical | Buy | 6 mm ID bushings | 16 |  |  |  |  |
| Mechanical | Buy | 2×10 mm parallel pins | 16 |  |  |  |  |
| Mechanical | Buy | 2×16 mm parallel pins | 16 |  |  |  |  |
| Mechanical | Buy | M 2.5 large washers | 8 |  |  |  |  |
| Mechanical | Fabricate - Cut | M 2 threaded rod cut pieces, nominal 18 mm | 16 |  |  |  |  |
| Mechanical | Fabricate - Cut | M 2 threaded rod cut pieces, nominal 25 mm | 8 |  |  |  |  |
| Mechanical | Buy | Waist M 6 spherical rod ends | 4 |  |  |  |  |
| Electrical | Buy | Ampace JP40 21700 4000mAh cell | 36 | $5.99 | $215.64 | [Product](https://21700supply.com/products/ampace-jp40-battery) |  |
| Electrical | Buy | Yahboom AI VIEW depth camera | 1 | $199.00 | $199.00 | [Product](https://www.yahboom.store/products/aiview-depth-camera) |  |
| Mechanical | Buy | 688 roll output bearing 8 x 16 x 5 mm | 4 |  |  |  |  |
| Mechanical | Buy | MR 128 carrier bearing 8 x 12 x 3.5 mm | 4 |  |  |  |  |
| Electrical | Buy | Arbite JCS 00040002010002 AS 5047 P differential-SPI encoder board | 4 |  |  | [Product](https://jcsdoc.arbite.io/devices/JCS0004_dev_encoder_absolute/on_axis_differential_spi/JCS00040002010002/hw_reference/oa_ae_diff_hw_installation/) |  |
| Electrical | Buy | GDZ468H motor driver | 15 | $85.00 | $1,275.00 | [Product](https://steadywin-motor.com/products/steadywin-driver-board) |  |
| Electrical | Buy | ODrive motor controller | 2 |  |  |  |  |
| Electrical | Buy | Waveshare ESP32-P4-Module-DEV-KIT with ESP32-C6 | 1 | $19.99 | $19.99 | [Product](https://www.waveshare.com/product/mcu-tools/development-boards/esp32-p4-module-dev-kit.htm) |  |
| Electrical | Buy | Adafruit 4754 BNO085 IMU | 1 | $29.50 | $29.50 | [Product](https://www.adafruit.com/product/4754) |  |
| Mechanical | Buy | 6808/61808-2RS bearing,40 x52 x7mm | 1 | $19.99 | $19.99 | [Product](https://vxb.com/products/6808rs-ball-bearing-40x52x7-sealed) |  |
| Mechanical | Buy | M2.5 female-female10mm standoff | 4 |  |  |  |  |
| Mechanical | Buy | M2 female-female10mm standoff | 4 |  |  |  |  |
| Mechanical | Buy | ANSI40 roller chain,36pitches per loop | 2 | $6.015 | $12.03 | [Product](https://www.ebay.com/itm/145702524459) |  |
| Electrical | Buy | 12S battery management system | 1 |  |  |  |  |
| Electrical | Buy | 5V logic/hand-servo DC/DC converter | 1 |  |  |  |  |
| Electrical | Buy | 12V neck/wrist DC/DC converter | 1 |  |  |  |  |
| Electrical | Buy | 24V elbow DC/DC converter | 1 |  |  |  |  |
| Electrical | Buy | CAN transceiver module | 3 |  |  |  |  |
| Electrical | Buy | Encoder magnet for10018 motor | 6 |  |  |  |  |
| Mechanical | Buy | Oval steel tubing | TBD length |  |  |  |  |
| Mechanical | Buy | EONO3D PETG filament, 1.75 mm, 1 kg spool | TBD | $10.00 |  | [Product](https://www.amazon.com/dp/B0G2BQQ5RT) |  |

## Assembly instructions


1. Print the parts in [`CAD/Assembly/Individual STLs/`](CAD/Assembly/Individual%20STLs/) using PA6-CF. The STL names match their source STEP names.
2. Fit the two `Foot Mounting Plate` parts and `Rounded Bearing Support` to the `Foot Base`, then install the purchased pillow-block bearings on the pitch axis.
3. Attach the `Shin Support Attachment` and cut the aluminum shin tube to 200 mm. Drill the tube from the CAD hole locations, then fasten it with M3 hardware.
4. Use the `Electronics Mounting Tray` and `Encoder Holder` parts for the controller and encoder mounting points. The `Lower Leg Support Assembly` STEP files can be used as reference assemblies.
5. Mount one motor and one ODrive to each lower leg. Confirm that both ankles move freely by hand before applying power.
6. Wire and test one motor at a time with the ankle unloaded. 

### Power and signal wiring

- Use a current-limited 50 V bench supply rated for at least 10 A per motor, or 20 A when both motors  run together.
- The 50 V rail connects only to the ODrive power inputs. Power the STM32, CAN transceiver, and Raspberry Pi from their voltage regulations with GND connections.
- Connect STM32 CAN to Odrive CAN, merging them as you connect them, and UART to host computer.

## STM32 controller firmware

This protocol is used for Odrive comms: [ODrive v3.x CANSimple protocol](https://github.com/odriverobotics/ODrive/tree/master/Firmware/communication/can). UART can also be used for testing.

The first ODrive uses CAN ID `0` and the second ID `1` at 500 kbit/s. The Raspberry Pi helper in controls them as the host [`firmware/rpi_host/ankle_controller.py`](firmware/rpi_host/ankle_controller.py) has position, enable, idle, and stop commands. This was used to test my custom gearboxes.

### Build and flash with ST-Link

Connect the ST-LINK to the STM32. 

```text
cd firmware/stm32_controller
pio run
pio run -t upload
pio device monitor -b 115200
```

## Notes

This is a long project, and I don't think macondo runs long enough for me to complete it, which is why i'm completing the lower leg first, and then will add on in different hack club events.
