# Humanoid Robot

This is my project to build a human-sized bipedal robot. In this repo I have all my current designs for my robot's shin and lower leg, and the iterations of gearboxes I have made for my actuators.

Right now, I am using pre-made actuators and am waiting on a grant to further complete my robot.

This grant is for building and testing the robot's two lower-leg and ankle assemblies. It is the first stage of the humanoid and is not funding the complete robot.

This is the current prototype, showing both lower-leg assemblies side by side.

![Two lower-leg prototype assemblies](Assets/2x%20Lower%20Leg%20Assembly.png)

## Electronics

Each ankle motor is controlled by a single-axis ODrive 3.6 clone. Both ODrives connect to an STM32F103 over CAN. The STM32 handles the live PID control and communicates with a host computer over SPI (likely a raspberry pi later on) for high level controls.

This is a wiring diagram of how i'll utilize CAN buses for each motor [`Schematics/`](Schematics/).

![Electronics architecture](Schematics/schematic.png)

## Design

At first, I was thinking of a 2-DOF ankle design but now I am thinking of 1-DOF as its much cheaper and is really what I need. This came from a lot of thinking, as I am utilizing a lot of plastic for this build (though I will utilize aluminum in places where necessary). A lot of my body will be plastic and needs to be designed appropriately to support a bipedal's weight that is 5 foot tall. Currently I have a 1-dof ankle structure with a linkage system for only ankle pitch motion.

A bipedal can easily walk on level ground with ankle pitch. I have also attached a 50mm bearing hole for attaching the knee.

I also kept my earlier 2-DOF single-leg assembly as a backup in case I return to a 2-DOF ankle in the future.

![Backup 2-DOF lower-leg assembly](Assets/1x%20Prototype%202-DOF%20Lower%20Leg%20Assembly.png)

## Bill of materials

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

1. I haven't assembled it myself yet as I am waiting on the grant to do so, but here is how I have planned it out

### Assembly the foot base

1. Get all the pillow bearing blocks (either printed as a prototype or steel consumer pillow blocks)
2. Assembly them in a way to allow a pitch axis of the motor to spin.
3. On the pitch axis, attach the foot structural support piece.

### Assemble Shin/Motor

1. Cut the aluminum tubing to 200MM length
2. Plug it in the foot structural support piece
3. Screw it tight with m3 screws
4. Assemble motor by inserting the motor inside the motor structural supports; secure with m3 screws 
5. Now attach the entire assembly with the metal tubing, secure using m3 screws

### Get working model

6. Mount the odrive using the odrive mount/casing. 
7. Connect to bench power supply and test.


## Notes

This is a long project, and I don't think macondo runs long enough for me to complete it, which is why i'm completing the lower leg first, and then will add on in different hack club events.
