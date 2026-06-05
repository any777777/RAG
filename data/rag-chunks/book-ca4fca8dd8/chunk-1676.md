---
chunk_id: "book-ca4fca8dd8-chunk-1676"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1676
confidence: "first-pass"
extraction_method: "structured-local"
---

1024
Chapter 27
Computer Vision
27.7.6 Controlling movement with vision
One of the principal uses of vision is to provide information both for manipulating objects—
picking them up, grasping them, twirling them, and so on—and for navigating while avoiding
obstacles. The ability to use vision for these purposes is present in the most primitive of
animal visual systems. In many cases, the visual system is minimal, in the sense that it
extracts from the available light ﬁeld just the information the animal needs to inform its
behavior. Quite probably, modern vision systems evolved from early, primitive organisms
that used a photosensitive spot at one end in order to orient themselves toward (or away from)
the light. We saw in Section 27.6 that ﬂies use a very simple optical ﬂow detection system to
land on walls.
Suppose that, rather than landing on walls, we want to build a self-driving car. This is
a project that places much greater demands on the perceptual system. Perception in a self-
driving car has to support the following tasks:
• Lateral control: Ensure that the vehicle remains securely within its lane or changes
lanes smoothly when required.
• Longitudinal control: Ensure that there is a safe distance to the vehicle in front.
• Obstacle avoidance: Monitor vehicles in neighboring lanes and be prepared for evasive
maneuvers. Detect pedestrians and allow them to cross safely.
• Obey trafﬁc signals: These include trafﬁc lights, stop signs, speed limit signs, and
police hand signals.
The problem for a driver (human or computer) is to generate appropriate steering, accelera-
tion, and braking actions to best accomplish these tasks.
To make good decisions, the driver should construct a model of the world and the objects
in it. Figure 27.28 shows some of the visual inferences that are necessary to build this model.
For lateral control, the driver needs to maintain a representation of the position and orientation
of the car relative to the lane. For longitudinal control, the driver needs to keep a safe distance
from the vehicle in front (which may not be easy to identify on, say, curving multilane roads).
Obstacle avoidance and following trafﬁc signals require additional inferences.
Roads were designed for humans who navigate using vision, so it should in principle be
possible to drive using vision alone. However, in practice, commercial self-driving cars use
a variety of sensors, including cameras, lidars, radars, and microphones. A lidar or radar en-
ables direct measurement of depth, which can be more accurate than the vision-only methods
of Section 27.6. Having multiple sensors increases performance in general, and is particu-
larly important in conditions of poor visibility; for example, radar can cut through fog that
blocks cameras and lidars. Microphones can detect approaching vehicles (especially ones
with sirens) before they become visible.
There has also been much research on mobile robots navigating in indoor and outdoor
environments. Applications abound, such as the last mile of package or pizza delivery. Tra-
ditional approaches break this task up into two stages as shown in Figure 27.29:
• Map building: Simultaneous Localization and Mapping or SLAM (see page 942) is
the task of constructing a 3D model of the world, including the location of the robot in
the world (or more speciﬁcally, the location of each of the robot’s cameras). This model
(typically represented as a point cloud of obstacles) can be built from a series of images
from different camera positions.
