---
chunk_id: "book-ca4fca8dd8-chunk-1548"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1548
confidence: "first-pass"
extraction_method: "structured-local"
---

934
Chapter 26
Robotics
(a)
(b)
Figure 26.2 (a) NASA’s Curiosity rover taking a selﬁe on Mars. Image courtesy of NASA.
(b) A Skydio drone accompanying a family on a bike ride. Image courtesy of Skydio.
Mobile robots are those that use wheels, legs, or rotors to move about the environment.
Mobile robot
Quadcopter drones are a type of unmanned aerial vehicle (UAV); autonomous underwa-
Quadcopter drone
UAV
ter vehicles (AUVs) roam the oceans. But many mobile robots stay indoors and move on
AUV
wheels, like a vacuum cleaner or a towel delivery robot in a hotel. Their outdoor counterparts
include autonomous cars or rovers that explore new terrain, even on the surface of Mars
Autonomous car
Rover
(Figure 26.2). Finally, legged robots are meant to traverse rough terrain that is inaccessible
Legged robot
with wheels. The downside is that controlling legs to do the right thing is more challenging
than spinning wheels.
Other kinds of robots include prostheses, exoskeletons, robots with wings, swarms, and
intelligent environments in which the robot is the entire room.
26.2.2 Sensing the world
Sensors are the perceptual interface between robot and environment. Passive sensors, such
Passive sensor
as cameras, are true observers of the environment: they capture signals that are generated
by other sources in the environment. Active sensors, such as sonar, send energy into the
Active sensor
environment. They rely on the fact that this energy is reﬂected back to the sensor. Active
sensors tend to provide more information than passive sensors, but at the expense of increased
power consumption and with a danger of interference when multiple active sensors are used
at the same time. We also distinguish whether a sensor is directed at sensing the environment,
the robot’s location, or the robot’s internal conﬁguration.
Range ﬁnders are sensors that measure the distance to nearby objects. Sonar sensors
Range ﬁnder
Sonar
are active range ﬁnders that emit directional sound waves, which are reﬂected by objects,
with some of the sound making it back to the sensor. The time and intensity of the returning
signal indicates the distance to nearby objects. Sonar is the technology of choice for au-
tonomous underwater vehicles, and was popular in the early days of indoor robotics. Stereo
vision (see Section 27.6) relies on multiple cameras to image the environment from slightly
Stereo vision

## Page 935
