# Humanoid Robot

This is my ongoing project to build a human-sized humanoid robot. This repository is where I keep the mechanical designs, electronics schematics, and bill of materials as I work through the design.

Right now, most of the work is focused on the lower legs. The repository includes my shin, ankle, and foot assembly along with cyclodial and planetary gearbox designs for C6374 motors.

## Electronics

Each ankle motor is controlled by a single-axis ODrive 3.6 clone. Both ODrives connect to an STM32F103 over CAN. The STM32 handles the real-time control and communicates with a Raspberry Pi or another host computer over SPI.

The current electronics architecture and wiring diagram can be found in [`Schematics/`](Schematics/).

![Electronics architecture](Schematics/schematic.png)

## Repository contents

- [`CAD/`](CAD/) contains the source CAD, STEP exports, actuator designs, and leg assembly.
- [`Schematics/`](Schematics/) contains the KiCad schematic and a rendered image.
- [`BOM.csv`](BOM.csv) contains the current parts list, quantities, prices, and product links.

## Bill of materials

The BOM is still growing as the design develops. The prices from my original screenshots are kept in the CSV, while the STM32 and host-computer allowance are included so the total better represents what it would cost someone else to reproduce the project.

Current estimated total: **$644.38 USD**

## Notes

This project is still in development, so the CAD, wiring, and component choices may change. The schematic is an architecture and wiring reference, not a custom motor-controller PCB. Check the actual pinout and ratings of every board before connecting power.
