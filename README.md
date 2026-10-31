# Humanoid Robot

A human-sized humanoid robot built with oval steel tubes, printed PETG parts, aluminum parts and electric actuators. Designed in Fusion 360.

[CAD](CAD/) · [Build journal](JOURNAL.md)

## Electronics

An ESP32-P4/C6 connects the motors, servos, IMU and depth camera. Three CAN buses connect the motor controllers.

![Electronics schematic](Schematics/schematic.png)

[Schematic PDF](Schematics/Humanoid_Electronics.pdf) · [KiCad project](Schematics/Humanoid_Electronics.kicad_pro)

## Bill of materials

[Download CSV](bom.csv)

| Type | Item | Quantity | Unit price (USD) | Final price (USD) | Product | Notes |
|---|---|---:|---:|---:|---|---|
| Electrical | SteadyWin GWK7010-8 motor | 7 | $81.61 | $571.27 | [Product](https://www.aliexpress.com/item/3256803276650569.html) |  |
| Electrical | SteadyWin GWK6010-8 motor | 6 | $72.58 | $435.49 | [Product](https://www.aliexpress.com/item/3256806290989080.html) |  |
| Electrical | DJI 10018 77 KV motor | 6 | $64.68 | $388.10 | [Product](https://www.aliexpress.com/item/3256811842519170.html) |  |
| Electrical | Feetech STS3215-C018 12 V servo | 6 | $37.39 | $224.34 | [Product](https://www.aliexpress.us/item/3256811423365280.html) |  |
| Electrical | RDS51160 24 V elbow servo | 2 | $39.99 | $79.98 | [Product](https://www.ebay.com/itm/186554276132) |  |
| Electrical | Feetech SCS0009 hand servo | 16 | $8.00 | $128.00 | [Product](https://www.seeedstudio.com/Feetech-SCS0009-Servo-p-6535.html) |  |
| Mechanical | 6810 / 61810-2RS bearing, 50 x 65 x 7 mm | 2 | $3.34 | $6.68 | [Product](https://www.aliexpress.us/item/3256801627485902.html) |  |
| Mechanical | 6005-2RS bearing, 25 x 47 x 12 mm | 3 | $4.27 | $12.81 | [Product](https://www.aliexpress.us/item/3256811637396893.html) |  |
| Mechanical | 6007-2RS bearing, 35 x 62 x 14 mm | 2 | $7.15 | $14.30 | [Product](https://www.aliexpress.us/item/3256811637396893.html) |  |
| Mechanical | 61810 / 6810-2RS bearing, 50 x 65 x 7 mm | 4 | $3.34 | $13.36 | [Product](https://www.aliexpress.us/item/3256801627485902.html) |  |
| Mechanical | 6808-2RS hip-pitch bearing, 40 x 52 x 7 mm | 4 | $2.96 | $11.84 | [Product](https://www.aliexpress.us/item/3256801627485902.html) |  |
| Mechanical | M2 ball joints with supplied hardware | 32 | $0.47 | $14.90 | [Product](https://www.aliexpress.us/item/3256804294185019.html) |  |
| Mechanical | SF-1 bushing, 6 x 8 x 4 mm | 16 | $1.08 | $17.20 | [Product](https://www.aliexpress.us/item/3256808597367437.html) |  |
| Mechanical | 2×10 mm parallel pins | 16 | $0.10 | $1.52 | [Product](https://www.aliexpress.us/item/3256809715362151.html) |  |
| Mechanical | 2×16 mm parallel pins | 16 | $0.10 | $1.63 | [Product](https://www.aliexpress.us/item/3256809715362151.html) |  |
| Mechanical | M 2 threaded rod cut pieces, nominal 18 mm | 16 | $0.26 | $4.20 | [Product](https://www.aliexpress.us/item/3256809843990889.html) |  |
| Mechanical | M 2 threaded rod cut pieces, nominal 25 mm | 8 | $0.36 | $2.92 | [Product](https://www.aliexpress.us/item/3256809843990889.html) |  |
| Mechanical | SI6 M6 right-hand female rod ends, waist | 4 | $1.59 | $6.36 | [Product](https://www.aliexpress.us/item/3256805716018286.html) |  |
| Electrical | Ampace JP40 21700 4000mAh cell | 36 | $5.99 | $215.64 | [Product](https://21700supply.com/products/ampace-jp40-battery) |  |
| Electrical | Yahboom AI VIEW depth camera | 1 | $199.00 | $199.00 | [Product](https://www.yahboom.store/products/aiview-depth-camera) |  |
| Mechanical | 688RS wrist bearing, 8 x 16 x 5 mm | 4 | $1.76 | $7.03 | [Product](https://www.aliexpress.us/item/3256806175977496.html) |  |
| Mechanical | MR128RS bearing, 8 x 12 x 3.5 mm | 4 | $1.61 | $6.44 | [Product](https://www.aliexpress.us/item/3256806175977496.html) |  |
| Electrical | AS5047P SPI/ABI encoder board, 26 x 22 mm | 4 | $8.15 | $32.60 | [Product](https://www.aliexpress.us/item/3256812971045214.html) |  |
| Electrical | SteadyWin GDS68 motor driver | 15 | $48.99 | $734.85 | [Product](https://a.aliexpress.com/_mMuNSO7) |  |
| Electrical | ODrive V3.6-compatible dual motor controller, 56V | 2 | $45.89 | $91.78 | [Product](https://usa.banggood.com/ODrive-V3_6-FOC-BLDC-Motor-Controller-Dual-Motor-56V-60A-High-Performance-ARM-Cortex-M4-Encoder-CAN-PWM-Compatible-p-2043305.html) |  |
| Electrical | Waveshare ESP32-P4-Module-DEV-KIT with ESP32-C6 | 1 | $19.99 | $19.99 | [Product](https://www.waveshare.com/product/mcu-tools/development-boards/esp32-p4-module-dev-kit.htm) |  |
| Electrical | Adafruit 4754 BNO085 IMU | 1 | $29.50 | $29.50 | [Product](https://www.adafruit.com/product/4754) |  |
| Mechanical | 6808/61808-2RS waist bearing, 40 x 52 x 7 mm | 1 | $2.96 | $2.96 | [Product](https://www.aliexpress.us/item/3256801627485902.html) |  |
| Mechanical | M2.5 female-female 10 mm brass standoff | 4 | $0.15 | $0.59 | [Product](https://www.aliexpress.us/item/3256807944006881.html) |  |
| Mechanical | M2 female-female 10 mm brass standoff | 4 | $0.10 | $0.41 | [Product](https://www.aliexpress.us/item/3256807944006881.html) |  |
| Mechanical | ANSI40 roller chain,36pitches per loop | 2 | $6.02 | $12.03 | [Product](https://www.ebay.com/itm/145702524459) |  |
| Electrical | JBD 8-20S 60A Bluetooth BMS, configured for 12S | 1 | $32.39 | $32.39 | [Product](https://a.aliexpress.com/_mrJHXH5) |  |
| Electrical | GYVRM JDL480525 5V 25A DC/DC converter | 1 | $36.39 | $36.39 | [Product](https://www.aliexpress.us/item/3256806039634617.html) |  |
| Electrical | 12V 20A neck/wrist DC/DC converter | 1 | $29.69 | $29.69 | [Product](https://www.aliexpress.us/item/3256807940510408.html) |  |
| Electrical | 24V 10A elbow DC/DC converter | 1 | $7.75 | $7.75 | [Product](https://www.aliexpress.us/item/3256806469175071.html) |  |
| Electrical | SN65HVD230 CAN transceiver module | 3 | $1.18 | $3.55 | [Product](https://www.aliexpress.us/item/3256813102806492.html) |  |
| Electrical | Encoder magnets, 6 x 2 mm, 10-pack | 1 | $3.55 | $3.55 | [Product](https://www.aliexpress.us/item/3256810578708839.html) |  |
| Mechanical | SANWAY 10x10 canopy, oval-tube stock | 1 | $79.99 | $79.99 | [Product](https://www.amazon.com/dp/B0GS4ZGF94) |  |
| Mechanical | PETG filament, price per kg | 7.73 | $8.00 | $61.83 | [Product](https://a.co/d/05x3dOF7) |  |
| Mechanical | KP08 8mm pillow block bearing | 12 | $1.58 | $19.00 | [Product](https://www.aliexpress.us/item/2255800723272765.html) |  |
| Mechanical | SI6 M6 right-hand female rod ends, ankles | 8 | $1.59 | $12.72 | [Product](https://www.aliexpress.us/item/3256805716018286.html) |  |
| Mechanical | M6x1 threaded rod, price per metre | 0.9759666 m | $5.00 | $4.88 | [Product](https://www.albanycountyfasteners.com/metric-zinc-threaded-rod-m6-100-x-1-meter-8408-026-0012) |  |
| Mechanical | 8mm smooth steel shaft stock, 330mm | 2 | $5.62 | $11.24 | [Product](https://www.aliexpress.us/item/3256803408580273.html) |  |
| Electrical | 26AWG signal wire, black, 20m roll | 1 | $5.02 | $5.02 | [Product](https://www.aliexpress.us/item/3256810592963671.html) |  |
| Electrical | 22AWG silicone wire, 5m red + 5m black | 1 | $4.05 | $4.05 | [Product](https://www.aliexpress.us/item/3256807281772727.html) |  |
| Electrical | 12AWG silicone wire, 5m red + 5m black | 1 | $19.89 | $19.89 | [Product](https://www.aliexpress.us/item/3256807281772727.html) |  |
| Mechanical | Fgruh M2.5 screw, nut and washer kit, 1520pcs | 1 | $9.99 | $9.99 | [Product](https://www.amazon.com/dp/B0FGV561HZ) |  |
| Mechanical | Fgruh M3 screw, nut and washer kit, 1120pcs | 1 | $9.99 | $9.99 | [Product](https://www.amazon.com/dp/B0FGV561HZ) |  |
| Mechanical | Fgruh M5 screw, nut and washer kit, 272pcs | 1 | $9.99 | $9.99 | [Product](https://www.amazon.com/dp/B0FGV561HZ) |  |
| Mechanical | DFDU M6 screw, nut and washer kit, 190pcs | 1 | $9.99 | $9.99 | [Product](https://www.amazon.com/dp/B0GY2XRV1F) |  |
| Mechanical | CNC parts, 7075 aluminum (allowance) | 6.07 kg |  | $100.00 |  |  |

**Total: $3,759.62**

[Previous README](archive/README-2026-10-30.md)
