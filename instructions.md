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

## Waist

Join the waist front and rear covers (224, 225) with the M4 bolts and nuts.

![Waist casing](media/build-guide/27-waist-casing.png)

Mount both DJI 10018 hip pitch motors (415) in their gearbox shells (416) with the end caps (409), and fit the hip pitch FOC-68 drivers (412). The hip pitch motor output takes the roll-to-pitch fork (401) of each leg.

![Hip pitch motors and drivers](media/build-guide/28-hip-pitch-motors.png)

Build the right leg the same way. It is a mirror of the left leg and uses the same part numbers with `-R` instead of `-L`.

![Both legs on the waist](media/build-guide/29-both-legs.png)

Mount the GWK 7010 waist yaw motor (214) in its round holder (210) with the M3x8 button screws, fit the four metal risers (207.1 to 207.4) and the waist yaw FOC-68 driver (212), and bolt it down with the M4 bolts.

![Waist yaw motor and driver](media/build-guide/30-waist-yaw.png)
