---
chunk_id: "book-ca4fca8dd8-chunk-1551"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1551
confidence: "first-pass"
extraction_method: "structured-local"
---

936
Chapter 26
Robotics
satellites that emit pulsed signals. At present, there are 31 operational GPS satellites in orbit,
and 24 GLONASS satellites, the Russian counterpart. GPS receivers can recover the distance
to a satellite by analyzing phase shifts. By triangulating signals from multiple satellites, GPS
receivers can determine their absolute location on Earth to within a few meters. Differential
GPS involves a second ground receiver with known location, providing millimeter accuracy
Diﬀerential GPS
under ideal conditions.
Unfortunately, GPS does not work indoors or underwater. Indoors, localization is often
achieved by attaching beacons in the environment at known locations. Many indoor environ-
ments are full of wireless base stations, which can help robots localize through the analysis of
the wireless signal. Underwater, active sonar beacons can provide a sense of location, using
sound to inform AUVs of their relative distances to those beacons.
The third important class is proprioceptive sensors, which inform the robot of its own
Proprioceptive
sensor
motion. To measure the exact conﬁguration of a robotic joint, motors are often equipped with
shaft decoders that accurately measure the angular motion of a shaft. On robot arms, shaft
Shaft decoder
decoders help track the position of joints. On mobile robots, shaft decoders report wheel rev-
olutions for odometry—the measurement of distance traveled. Unfortunately, wheels tend to
Odometry
drift and slip, so odometry is accurate only over short distances. External forces, such as wind
and ocean currents, increase positional uncertainty. Inertial sensors, such as gyroscopes, re-
Inertial sensor
duce uncertainty by relying on the resistance of mass to the change of velocity.
Other important aspects of robot state are measured by force sensors and torque sensors.
Force sensor
Torque sensor
These are indispensable when robots handle fragile objects or objects whose exact size and
shape are unknown. Imagine a one-ton robotic manipulator screwing in a light bulb. It would
be all too easy to apply too much force and break the bulb. Force sensors allow the robot
to sense how hard it is gripping the bulb, and torque sensors allow it to sense how hard it is
turning. High-quality sensors can measure forces in all three translational and three rotational
directions. They do this at a frequency of several hundred times a second so that a robot can
quickly detect unexpected forces and correct its actions before it breaks a light bulb. However,
it can be a challenge to outﬁt a robot with high-end sensors and the computational power to
monitor them.
26.2.3 Producing motion
The mechanism that initiates the motion of an effector is called an actuator; examples include
Actuator
transmissions, gears, cables, and linkages. The most common type of actuator is the electric
actuator, which uses electricity to spin up a motor. These are predominantly used in systems
that need rotational motion, like joints on a robot arm. Hydraulic actuators use pressurized
Hydraulic actuator
hydraulic ﬂuid (like oil or water) and pneumatic actuators use compressed air to generate
Pneumatic actuator
mechanical motion.
Actuators are often used to move joints, which connect rigid bodies (links). Arms and
legs have such joints. In revolute joints, one link rotates with respect to the other. In pris-
Revolute joint
matic joints, one link slides along the other. Both of these are single-axis joints (one axis
Prismatic joint
of motion). Other kinds of joints include spherical, cylindrical, and planar joints, which are
multi-axis joints.
To interact with objects in the environment, robots use grippers. The most basic type
of gripper is the parallel jaw gripper, with two ﬁngers and a single actuator that moves
Parallel jaw gripper
the ﬁngers together to grasp objects. This effector is both loved and hated for its simplicity.
