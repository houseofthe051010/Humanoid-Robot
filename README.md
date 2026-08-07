# Humanoid Robot

This is my project to build a human-sized bipedal robot. In this repo I have all my current designs for my robot's shin and lower leg, and the iterations of gearboxes I have made for my actuators.

Right now, I am using pre-made actuators and am waiting on a grant to further complete my robot.

## Electronics

Each ankle motor is controlled by a single-axis ODrive 3.6 clone. Both ODrives connect to an STM32F103 over CAN. The STM32 handles the live PID control and communicates with a host computer over SPI (likely a raspberry pi later on) for high level controls.

This is a wiring diagram of how i'll utilize CAN buses for each motor [`Schematics/`](Schematics/).

![Electronics architecture](Schematics/schematic.png)

## Design

At first, I was thinking of a 2-DOF ankle design but now I am thinking of 1-DOF as its much cheaper and is really what I need. This came from a lot of thinking, as I am utilizing a lot of plastic for this build (though I will utilize aluminum in places where necessary). A lot of my body will be plastic and needs to be designed appropriately to support a bipedal's weight that is 5 foot tall. Currently I have a 1-dof ankle structure with a linkage system for only ankle pitch motion.

A bipedal can easily walk on level ground with ankle pitch. I have also attached a 50mm bearing hole for attaching the knee.



## Bill of materials

| Category | Item | Quantity | Unit price (USD) | Line total (USD) | Product link |
| --- | --- | ---: | ---: | ---: | --- |
| Actuation | SteadyWin GIM6010-48 48:1 planetary geared ankle motor, without driver | 2 | $156.00 | $312.00 | [Buy](https://rcdrone.top/products/steadywin-gim6010-48-planetary-reducer-servo-motor) |
| Structure | 6061-T6 aluminum square tubing, 1 in x 1 in x 0.125 in wall x 24 in | 2 | $14.89 | $29.78 | [Buy](https://www.onlinemetals.com/en/buy/aluminum/1-x-0-125-aluminum-square-tube-6061-t6-extruded/pid/18014) |
| Fabrication | SUNLU PA6-CF black filament, 1.75 mm, 1 kg, 80% PA / 20% carbon fiber | 1 | $44.99 | $44.99 | [Buy](https://store.sunlu.com/products/nylon6-carbon-fiber-pa6-cf-3d-printer-filament-1kg) |
| Mechanical | KP08 pillow block bearing, 8 mm bore | 10 | $2.95 | $29.50 | [Buy](https://www.crcibernetica.com/8-mm-pillow-block-mounted-ball-bearing-kp08/) |
| Motor control | ODrive S V3.6 FOC single-axis BLDC motor controller, 60 A, CAN/PWM | 2 | $31.61 | $63.22 | [Buy](https://www.banggood.com/ODrive-S-V3_6-FOC-BLDC-Motor-Controller-60A-Support-CAN-PWM-Pulse-Encoder-TLE5012B-AS5047-AMT10X-MT6816-ARM-Cortex-M4-p-2043307.html) |
| Embedded control | STM32F103C8T6 Blue Pill development board, pre-soldered | 1 | $8.99 | $8.99 | [Buy](https://shillehtek.com/products/shillehtek-pre-soldered-authentic-stm32f103c8t6-arm-stm32) |
| Host computing | Raspberry Pi 5 Desktop Kit, 8 GB (host computer, storage, power, cooling, and accessories) | 1 | $235.00 | $235.00 | [Buy](https://www.canakit.com/official-raspberry-pi-5-desktop-kit.html) |
| **Total** |  |  |  | **$723.48** |  |

## Notes

This is a long project, and I don't think macondo runs long enough for me to complete it, which is why i'm completing the lower leg first, and then will add on in different hack club events.
