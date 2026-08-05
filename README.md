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

Look at the BOM CSV for the BOM. I have requested a grant in macondo for the things I require, but this is the current cost of all the items.

Current estimated total: **$644.38 USD**

## Notes

This is a long project, and I don't think macondo runs long enough for me to complete it, which is why i'm completing the lower leg first, and then will add on in different hack club events.