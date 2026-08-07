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

The [`CAD/Actuators/`](CAD/Actuators/) folder contains my planetary and cycloidal C6374 gearbox designs.

<!-- Add a description of the gearbox designs and their reduction ratios here. -->

## Bill of materials

This table shows the full replication cost. My current Macondo grant request is only $360 for the parts I still need; the rest are already owned or outside this grant request.

| Category | Item | Quantity | Unit price (USD) | Line total (USD) | Product link |
| --- | --- | ---: | ---: | ---: | --- |
| Actuation | SteadyWin GIM6010-48 48:1 planetary geared ankle motor, without driver | 2 | $156.00 | $312.00 | [Buy](https://rcdrone.top/products/steadywin-gim6010-48-planetary-reducer-servo-motor) |
| Structure | 6061-T6 aluminum square tubing, 1 in x 1 in x 0.125 in wall x 24 in | 2 | $14.89 | $29.78 | [Buy](https://www.onlinemetals.com/en/buy/aluminum/1-x-0-125-aluminum-square-tube-6061-t6-extruded/pid/18014) |
| Fabrication | SUNLU PA6-CF black filament, 1.75 mm, 1 kg, 80% PA / 20% carbon fiber | 1 | $44.99 | $44.99 | [Buy](https://store.sunlu.com/products/nylon6-carbon-fiber-pa6-cf-3d-printer-filament-1kg) |
| Mechanical | KP08 pillow block bearing, 8 mm bore | 10 | $2.95 | $29.50 | [Buy](https://www.crcibernetica.com/8-mm-pillow-block-mounted-ball-bearing-kp08/) |
| Mechanical | M3 stainless-steel bolt, nut, flat-washer and spring-washer assortment, 720 pieces | 1 | $9.99 | $9.99 | [Buy](https://www.amazon.com/dp/B0FG2BRXL3) |
| Motor control | ODrive S V3.6 FOC single-axis BLDC motor controller, 60 A, CAN/PWM | 2 | $31.61 | $63.22 | [Buy](https://www.banggood.com/ODrive-S-V3_6-FOC-BLDC-Motor-Controller-60A-Support-CAN-PWM-Pulse-Encoder-TLE5012B-AS5047-AMT10X-MT6816-ARM-Cortex-M4-p-2043307.html) |
| CAN bus | SN65HVD230 3.3 V CAN bus transceiver module | 1 | $0.94 | $0.94 | [Buy](https://www.aliexpress.com/item/1005008512626947.html) |
| CAN bus | 120 ohm 1/4 W 1% metal-film termination resistors, 100-pack | 1 | $0.94 | $0.94 | [Buy](https://www.aliexpress.com/item/32526023399.html) |
| Electronics | 10 kOhm 1/4 W metal-film resistors, 100-pack | 1 | $0.50 | $0.50 | [Buy](https://www.aliexpress.com/item/1005006006915852.html) |
| Power | XT60 male and female connector set, 5 pairs | 1 | $5.60 | $5.60 | [Buy](https://www.aliexpress.com/item/1005009991978695.html) |
| Wiring | Variable-AWG wire allowance | 1 | $20.00 | $20.00 | [Reference](https://www.aliexpress.com/item/4001131337448.html) |
| Embedded control | STM32F103C8T6 Blue Pill development board, pre-soldered | 1 | $8.99 | $8.99 | [Buy](https://shillehtek.com/products/shillehtek-pre-soldered-authentic-stm32f103c8t6-arm-stm32) |
| Host computing | Raspberry Pi 5 Desktop Kit, 8 GB (host computer, storage, power, cooling, and accessories) | 1 | $235.00 | $235.00 | [Buy](https://www.canakit.com/official-raspberry-pi-5-desktop-kit.html) |
| **Total** |  |  |  | **$761.45** |  |

## Assembly instructions

The complete assembly is still a prototype, so check fit and alignment before tightening everything.

1. Print the parts in [`CAD/Assembly/Individual STLs/`](CAD/Assembly/Individual%20STLs/) using PA6-CF. The STL names match their source STEP names.
2. Fit the two `Foot Mounting Plate` parts and `Rounded Bearing Support` to the `Foot Base`, then install the purchased pillow-block bearings on the pitch axis.
3. Attach the `Shin Support Attachment` and cut the aluminum shin tube to 200 mm. Drill the tube from the CAD hole locations, then fasten it with M3 hardware.
4. Use the `Electronics Mounting Tray` and `Encoder Holder` parts for the controller and encoder mounting points. The `Lower Leg Support Assembly` STEP files are reference assemblies, not single printable bodies.
5. Mount one GIM6010 motor and one ODrive to each lower leg. Confirm that both ankles move freely by hand before applying power.
6. Wire and test one motor at a time with the ankle unloaded. Only enable both axes after motor direction, encoder direction, current limits, and travel limits have been checked.

### Power and signal wiring

- Use a current-limited 50 V bench supply rated for at least 10 A per motor, or 20 A when both motors may run together. Add a fuse and emergency disconnect appropriate for the wiring and expected current.
- The 50 V rail connects only to the ODrive power inputs. Power the STM32, CAN transceiver, and Raspberry Pi from their correct low-voltage supplies and join their signal grounds.
- Connect STM32 `PA12` to the SN65HVD230 `D/TX` input and `PA11` to `R/RX`. Daisy-chain `CANH`, `CANL`, and ground to both ODrives with a twisted pair. Put one 120 ohm resistor at each physical end of the bus.
- Connect Raspberry Pi SPI0 `CE0`, `SCLK`, `MISO`, and `MOSI` to STM32 `PA4`, `PA5`, `PA6`, and `PA7`. Both sides use 3.3 V logic and must share ground.
- STM32 UART debug uses `PA9` TX and `PA10` RX at 115200 baud.

## STM32 controller firmware

The prototype PlatformIO project is in [`Code/stm32_controller/`](Code/stm32_controller/). It targets a Blue Pill STM32F103C8, talks to ODrive nodes 0 and 1 at 500 kbit/s using the legacy ODrive v3.x CANSimple packet format, and acts as an SPI slave to the Raspberry Pi. It supports enable, idle, clear-errors, emergency-stop, and position commands with velocity and torque feed-forward. Motors stay idle after boot until the host explicitly enables them. The packet IDs and payloads follow the [official ODrive v3.x CANSimple source](https://github.com/odriverobotics/ODrive/tree/master/Firmware/communication/can).

Before using the controller, configure and calibrate each ODrive over USB. Give the first board CAN node ID `0`, the second node ID `1`, and set both to `500000` baud. Save the configuration, reboot, and confirm each motor works safely on USB before connecting the shared CAN bus. Clone firmware may expose slightly different configuration property names.

```python
odrv0.config.enable_can_a = True
odrv0.can.config.baud_rate = 500000
odrv0.axis0.config.can.node_id = 0  # use 1 on the second ODrive
odrv0.axis0.config.can.heartbeat_rate_ms = 100
odrv0.axis0.config.can.encoder_rate_ms = 20
odrv0.save_configuration()
```

The 24-byte SPI request begins with `0xA5`, followed by command, motor (`0` or `1`), sequence, position in turns, velocity feed-forward in turns/s, and torque feed-forward in Nm. Command values are `1` move, `2` enable, `3` idle, `4` emergency stop, and `5` clear errors. The reply begins with `0x5A` and returns the status, sequence, both encoder estimates, and combined axis errors. [`Code/rpi_host/ankle_controller.py`](Code/rpi_host/ankle_controller.py) provides calls such as `enable(0)` and `move_position(0, 1.5)`. UART accepts `p <motor> <turns>`, `enable <motor>`, `idle <motor>`, `clear <motor>`, and `estop`.

This firmware is a starting point for the prototype and has not yet been hardware-tested. Current limits, encoder setup, travel limits, control gains, emergency-stop behavior, and host-side timeout handling must be verified with the real parts before the robot carries weight.

### Build and flash with ST-Link

Connect the ST-Link `SWDIO`, `SWCLK`, `GND`, and 3.3 V reference to Blue Pill `PA13`, `PA14`, `GND`, and `3V3`. Keep the 50 V motor supply disconnected for the first flash.

```text
cd Code/stm32_controller
pio run
pio run -t upload
pio device monitor -b 115200
```


## Notes

This is a long project, and I don't think macondo runs long enough for me to complete it, which is why i'm completing the lower leg first, and then will add on in different hack club events.
