---
chunk_id: "book-ca4fca8dd8-chunk-1549"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1549
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 26.2
Robot Hardware
935
(a)
(b)
Figure 26.3 (a) Time-of-ﬂight camera; image courtesy of Mesa Imaging GmbH. (b) 3D
range image obtained with this camera. The range image makes it possible to detect obstacles
and objects in a robot’s vicinity. Image courtesy of Willow Garage, LLC.
different viewpoints, analyzing the resulting parallax in these images to compute the range of
surrounding objects.
For mobile ground robots, sonar and stereo vision are now rarely used, because they are
not reliably accurate. The Kinect is a popular low-cost sensor that combines a camera and a
structured light projector, which projects a pattern of grid lines onto a scene. The camera
Structured light
sees how the grid lines bend, giving the robot information about the shape of the objects in
the scene. If desired, the projection can be infrared light, so as not to interfere with other
sensors (such as human eyes).
Most ground robots are now equipped with active optical range ﬁnders. Just like sonar
sensors, optical range sensors emit active signals (light) and measure the time until a reﬂection
of this signal arrives back at the sensor. Figure 26.3(a) shows a time-of-ﬂight camera. This
Time-of-ﬂight
camera
camera acquires range images like the one shown in Figure 26.3(b) at up to 60 frames per
second. Autonomous cars often use scanning lidars (short for light detection and ranging)—
Scanning lidar
active sensors that emit laser beams and sense the reﬂected beam, giving range measurements
accurate to within a centimeter at a range of 100 meters. They use complex arrangements of
mirrors or rotating elements to sweep the beam across the environment and build a map.
Scanning lidars tend to work better than time-of-ﬂight cameras at longer ranges, and tend to
perform better in bright daylight.
Radar is often the range ﬁnding sensor of choice for air vehicles (autonomous or not).
Radar
Radar sensors can measure distances up to kilometers, and have an advantage over optical
sensors in that they can see through fog. On the close end of range sensing are tactile sensors
Tactile sensor
such as whiskers, bump panels, and touch-sensitive skin. These sensors measure range based
on physical contact, and can be deployed only for sensing objects very close to the robot.
A second important class is location sensors. Most location sensors use range sensing
Location sensor
as a primary component to determine location. Outdoors, the Global Positioning System
Global Positioning
System
(GPS) is the most common solution to the localization problem. GPS measures the distance to
