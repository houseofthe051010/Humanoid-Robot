# Building it yourself

Prior to building, take a look at the Fabrication STLs folder and have all the parts there 3D printed and CNCd, along with everything else in the BOM. Each part has its own part number so make sure to organize accordingly.

The pictures show the left leg. Blue labels give the part number and whether it is 3D printed (FDM), CNC machined (CNC) or bought (BUY). Yellow labels show the screws.

## Foot

Attach the replaceable sole (558) to the bottom of the foot plate (557).

![Foot plate and sole](media/build-guide/01-foot-sole.png)

Bolt the front and rear roll pillow block bearings (559, 560) onto the foot plate with M5x20 screws, washers and nuts, two per bearing.

![Roll bearings on the foot plate](media/build-guide/02-foot-roll-bearings.png)

Slide the 8 mm roll shaft through the roll bearings and the cross axis block (551), then tighten the M3 pinch screws to lock the shafts.

![Cross axis block on the roll shaft](media/build-guide/03-foot-cross-block.png)

Bolt the two heel pillow block bearings (552, 554) to the back of the foot plate with M5x20 screws, washers and nuts. Slide the 6 mm heel shaft (561) through them with the printed axial spacers (556).

![Heel bearings and heel shaft](media/build-guide/04-foot-heel-shaft.png)

## Shin

Slide the two pitch pillow block bearings (513, 514) onto the pitch shaft of the cross axis block, then bolt them under the ankle adapter (507) with M5 screws and nuts.

![Pitch bearings under the ankle adapter](media/build-guide/05-shin-pitch-bearings.png)

Push the two oval tubes (501.1, 501.2) down into the ankle adapter.

![Oval tubes in the ankle adapter](media/build-guide/06-shin-oval-tubes.png)

Mount the ankle ODrive (508) to the TPU pad (505) between the tubes with the two TPU spacers (506.1, 506.2) and two M3x10 screws with washers.

![ODrive between the oval tubes](media/build-guide/07-shin-odrive.png)

Slide the calf mid shell (528) down over the tubes so it covers the ODrive.

![Calf mid shell over the ODrive](media/build-guide/08-shin-mid-shell.png)

Screw the two AS5047P encoders (509, 510) into the calf top piece (502) with M2.5x6 screws, four per encoder.

![Encoders in the calf top piece](media/build-guide/09-shin-encoders.png)

Bolt each GWK 7010 ankle motor to its motor plate with M3x12 flat head screws: motor A (511) on plate A (504) and motor B (512) on plate B (503).

![Ankle motors on their plates](media/build-guide/10-shin-motors-on-plates.png)

Press the M3 heat-set inserts into the calf top piece, slide it down the tubes onto the mid shell, and fasten both motor plates to it with M3x12 screws.

![Motor plates fastened to the calf top piece](media/build-guide/11-shin-close.png)

## Ankle linkage

Bolt an aluminium crank onto each ankle motor output with M3 screws and washers.

![Cranks on the ankle motor outputs](media/build-guide/12-link-cranks.png)

Thread the printed oval plugs onto both ends of the 6 mm threaded rod and put the rod guide between them. The rod ends go on the threads past the plugs.

![Threaded rod, plugs and rod guide](media/build-guide/13-link-rod-core.png)

Slide the oval steel tube over the plugs and the rod guide. Build rod B the same way.

![Oval steel tube over the rod](media/build-guide/14-link-rod-tube.png)

Fit the lower rod ends onto the ends of the 6 mm heel shaft, and bolt the upper rod ends to the cranks with an M6 screw.

![Linkage rods connecting the cranks to the heel](media/build-guide/15-link-connect.png)

## Knee

Stack the four aluminium knee plates (458.1 to 458.4) on top of the shin tubes with the sprocket standoff hub (459) and the knee sprocket (515), using the 6 mm dowels and M3 screws. Slide the 8 mm knee shaft (468) through.

![Knee plate stack, sprocket and shaft](media/build-guide/16-knee-stack.png)

Put the knee pillow block bearing (452) on the shaft and mount it to the knee side rail seats (453, 454) with M5 screws.

![Knee rail seats and pillow block](media/build-guide/17-knee-seats-bearings.png)

Push the two thigh oval tubes (451.1, 451.2) into the rail seats and lock them with the M4 screws and crush sleeves.

![Thigh oval tubes in the rail seats](media/build-guide/18-knee-thigh-tubes.png)

Put the DJI 10018 knee motor (462) into the round motor holder (455) with M4x12 screws, close it with the front cover (456) using M3 screws and nuts, and fit the motor output sprocket (464) with its flange (465).

![Knee motor in its holder](media/build-guide/19-knee-motor.png)

Mount the knee FOC-68 driver (461) on the motor holder.

![Knee motor driver](media/build-guide/20-knee-driver.png)

Loop the knee chain (467) over the motor sprocket (464) and the knee sprocket (515). Leave the thigh shell off for now.

![Knee chain](media/build-guide/21-knee-chain.png)

## Hip

Fit the rail-to-yaw crosshead (407) on top of the thigh tubes with the 6007 yaw bearing (418) and its retainer (408). Mount the GWK 7010 hip yaw motor (414), its FOC-68 driver (411) and the yaw output hub (406).

![Hip yaw motor and crosshead](media/build-guide/22-hip-yaw.png)

Bolt the yaw-to-roll cradle (405) onto the yaw output hub.

![Yaw to roll cradle](media/build-guide/23-hip-cradle.png)

Put the DJI 10018 hip roll motor (413) and its 61810 bearings (417) into the 110 mm roll tube (402) on the cradle.

![Hip roll motor in the roll tube](media/build-guide/24-hip-roll-motor.png)

Close the roll tube with the end caps (403) and front cap (420), mount the hip roll FOC-68 driver (410), and fasten the clamp spacers (404) with the M4 bolts and nuts.

![Roll tube caps, driver and bolts](media/build-guide/25-hip-roll-caps.png)

Bolt the roll-to-pitch fork (401) onto the roll output.

![Roll to pitch fork](media/build-guide/26-hip-fork.png)

## Thigh casing

Fit the front and rear thigh casings (469, 470) around the thigh, from the hip roll down to the knee. They close around the knee motor and chain.

![Thigh casings](media/build-guide/26b-thigh-casing.png)

## Waist

Join the waist front and rear covers (224, 225) with the M4 bolts and nuts.

![Waist casing](media/build-guide/27-waist-casing.png)

Mount both DJI 10018 hip pitch motors (415) in their gearbox shells (416) with the end caps (409), and fit the hip pitch FOC-68 drivers (412). The hip pitch motor output takes the roll-to-pitch fork (401) of each leg.

![Hip pitch motors and drivers](media/build-guide/28-hip-pitch-motors.png)

Build the right leg the same way. It is a mirror of the left leg and uses the same part numbers with `-R` instead of `-L`.

![Both legs on the waist](media/build-guide/29-both-legs.png)

Mount the GWK 7010 waist yaw motor (214) in its round holder (210) with the M3x8 button screws, fit the four metal risers (207.1 to 207.4) and the waist yaw FOC-68 driver (212), and bolt it down with the M4 bolts.

![Waist yaw motor and driver](media/build-guide/30-waist-yaw.png)

## Torso

Put the 6808 waist bearing on top of the yaw motor: the bearing seat (208), the outer race (222) with its seal, the inner race (217) on the 40 mm bearing journal (218), and the outer race retainer (209) held down with M2.5x6 flat head screws.

![Waist bearing](media/build-guide/31-waist-bearing.png)

Bolt the lower pitch base (201) to the yaw output with M3x18 screws. Fit the waist pitch joint (203) on it with the lower pitch pin (215) and its bushings, and the 6 mm base cross pin (216) with the pin spacers (202).

![Waist pitch base and joint](media/build-guide/32-waist-pitch-base.png)

Fit the pitch-to-roll bridge (204) on top with the upper roll pin (220) and its bushings.

![Pitch to roll bridge](media/build-guide/33-waist-roll-bridge.png)

Mount the upper roll spine carrier (205) on the bridge and push the spine oval tube (206) into it with the spine crossbolts. Mount the two GWK 6010 waist roll motors (213.1, 213.2) and their FOC-68 drivers (211-L, 211-R) on the carrier.

![Waist roll motors on the spine carrier](media/build-guide/34-waist-roll-motors.png)

Bolt a waist crank onto each waist roll motor output, and connect each crank to the end of the 6 mm base cross pin (216) with an M6 tie rod.

![Waist cranks and tie rods](media/build-guide/35-waist-linkage.png)

Put the TPU pad (102) in the battery lower cradle (101), set the 12S3P battery (106) on it, and close it with the upper restraint (103) using the M4 screws.

![Battery cradle](media/build-guide/36-torso-battery.png)

Clamp the internal shoulder spine frame (104) onto the spine tube with the two spine clamp caps (105.1, 105.2) and the M3 crossbolts and nuts.

![Spine frame](media/build-guide/37-torso-frame.png)

Mount the electronics box spine mount (152) and the electronics case (151). Screw the ESP32-P4 main board (153) in on 10 mm standoffs with M2.5x6 screws, and the BNO085 IMU (154) on 10 mm standoffs with M2x6 screws.

![Torso electronics](media/build-guide/38-torso-electronics.png)

Close the torso with the shell pieces (108 to 112, left and right), the USB-C service panels (115), the splices (113) and the blue identifier (107), using the torso shell screws.

![Torso casing](media/build-guide/39-torso-casing.png)

## Neck and head

Fit the neck yaw: the oval spine servo adapter (051) on top of the spine, the 6005 bearing (063) with its retainer (053), the Feetech yaw servo (057) held by the yaw servo clamp (052), and the head yaw output (054).

![Neck yaw](media/build-guide/40-neck-yaw.png)

Clamp the Feetech pitch servo (060) to the head yaw output with the pitch servo clamp (055) and M3 screws, fit the head pitch yoke (056) on it, and put the neck yaw collar (065) over the neck.

![Neck pitch](media/build-guide/41-neck-pitch.png)

Mount the depth camera (001) on the head pitch yoke, then close the head with the front shell (002), the camera visor bezel (003) and the removable rear shell (004) using the head shell screws.

![Head](media/build-guide/42-head.png)

## Arms

The pictures show the left arm. Build the right arm the same way: it is a mirror of the left arm and uses the same part numbers with `-R` instead of `-L`.

Mount the GWK 6010 shoulder pitch stator (256) on the pitch motor face mount (252) in the shoulder socket of the spine frame with its mount screws. Fit the 6810 pitch bearing (259) and hold it with the outer race retainer (251), then mount the shoulder pitch FOC-68 driver (254).

![Shoulder pitch](media/build-guide/50-shoulder-pitch.png)

Build the shoulder roll on the pitch carrier roll housing (253): the GWK 6010 pitch rotating hub (257) with the inner collar (260), and the GWK 6010 roll stator (258) with its mount screws. Mount the shoulder roll FOC-68 driver (255).

![Shoulder roll](media/build-guide/51-shoulder-roll.png)

Fit the roll driven output (301) and the 6005 rear support bearing (305) with the rear bearing cap (306), using the drive and retainer screws. Mount the upper-arm fork (302) on the roll output and put the elbow servo (304) in its cradle.

![Upper arm](media/build-guide/52-upper-arm.png)

Fit the forearm fork (351) onto the elbow servo outputs with the driven horn (355) and the rear horn (356).

![Forearm](media/build-guide/53-forearm.png)

Build the wrist on the end of the forearm fork: put the two STS3215 servos in the wrist cassette with their straps, then fit the wrist gears, the pitch yoke and the roll output gear.

![Wrist](media/build-guide/54-wrist.png)

Close the arm with the shoulder roll pods (261, 262), the upper arm shells (307, 308) and the forearm shells (357, 358).

![Arm covers](media/build-guide/56-arm-covers.png)

The finished robot:

![Finished robot](media/build-guide/57-full-robot.png)

## Wiring

The wires are not in the CAD. Follow the [schematic](Schematics/Humanoid_Electronics.pdf) for the connections. Wire sizes below come from the schematic.

### Power

The battery (106) comes assembled with its JBD 12S 60A BMS. Run the BMS output (P+, P−) to the electronics box with 12 AWG wire. This is VBAT.

The three DC-DC converters go in the electronics box (they are not in the CAD): 5 V / 25 A, 12 V / 20 A and 24 V / 10 A. Feed each from VBAT with 12 AWG wire.

- 5 V: ESP32-P4 (22 AWG), depth camera and the hand servos
- 12 V: STS3215 head and wrist servos
- 24 V: elbow servos

### Motor drivers

Every round FOC-68 motor driver and both ankle ODrives get two power wires (VBAT and GND), then CAN high and CAN low to their bus:

- CAN A, left leg: hip yaw, hip roll, hip pitch, knee and the left ankle ODrive
- CAN B, right leg: the same motors on the right leg
- CAN C, shoulders and waist: left and right shoulder pitch and roll, waist pitch, waist roll and waist yaw

Use 12 AWG for the leg motor phase wires and 22 AWG for the CAN C motor phase wires. Each ankle ODrive drives both ankle motors and reads both AS5047P encoders on its shin.

The three CAN buses connect to the ESP32-P4 through three SN65HVD230 CAN transceivers powered from 3.3 V: CAN A on GPIO 1/2, CAN B on GPIO 3/4 and CAN C on GPIO 5/6 (TX/RX).

### Servos

The servos get two power wires and one single-wire half-duplex UART data wire. Pull each data line up to 3.3 V.

- Head and wrist STS3215 servos: 12 V, GND, data to GPIO 20
- Hand SCS0009 servos: 5 V, GND, data to GPIO 21

The two elbow servos are the exception: they take 24 V, GND and a PWM signal, left elbow on GPIO 22 and right elbow on GPIO 23.

### Sensors

- BNO085 IMU (154): 3.3 V, GND, SDA to GPIO 7, SCL to GPIO 8, INT to GPIO 26, RST to GPIO 36, using 26 AWG
- Depth camera (001): USB to the ESP32-P4 USB host port

## Flashing the firmware

### ESP32-P4 main controller

The source is in [`firmware/ESP32-P4 Host controller/`](firmware/ESP32-P4%20Host%20controller/) and the compiled images are in its [`images/`](firmware/ESP32-P4%20Host%20controller/images/) folder. The images are built for chip revision 3.1 or newer.

Install [esptool](https://docs.espressif.com/projects/esptool/en/latest/esp32p4/installation.html), connect the ESP32-P4 and run:

```sh
cd "firmware/ESP32-P4 Host controller/images"
esptool --chip esp32p4 --port COM3 write-flash 0x2000 bootloader.bin 0x8000 partition-table.bin 0x10000 humanoid_p4.bin
```

Replace COM3 with the serial port your ESP32-P4 is on.

### Motor drivers

Set every motor driver and ODrive to 500 kbit/s CAN and give it the node ID listed for its motor in [`can_motors.c`](firmware/ESP32-P4%20Host%20controller/main/can_motors.c).

### Servos

The servo buses run at 1 Mbit/s. Give the head servos IDs 1 and 2 and the wrist servos IDs 3 to 6. The hand servos use IDs 1 to 16 on their own bus.
