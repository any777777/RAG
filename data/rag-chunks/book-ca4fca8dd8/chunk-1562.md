---
chunk_id: "book-ca4fca8dd8-chunk-1562"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1562
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 26.5
Planning and Control
945
(a)
(b)
(c)
Figure 26.10 Sequence of “drivable surface” classiﬁcations using adaptive vision. (a) Only
the road is classiﬁed as drivable (pink area). The V-shaped blue line shows where the vehicle
is heading. (b) The vehicle is commanded to drive off the road, and the classiﬁer is beginning
to classify some of the grass as drivable. (c) The vehicle has updated its model of drivable
surfaces to correspond to grass as well as road. Courtesy of Sebastian Thrun.
the colors: neon light has a stronger component of green light than sunlight has. Yet somehow
we seem not to notice the change. If we walk together with people into a neon-lit room, we
don’t think that their faces suddenly turned green. Our perception quickly adapts to the new
lighting conditions, and our brain ignores the differences.
Adaptive perception techniques enable robots to adjust to such changes. One example
is shown in Figure 26.10, taken from the autonomous driving domain. Here an unmanned
ground vehicle adapts its classiﬁer of the concept “drivable surface.” How does this work?
The robot uses a laser to provide classiﬁcation for a small area immediately in front of the
robot. When this area is found to be ﬂat in the laser range scan, it is used as a positive training
example for the concept “drivable surface.” A mixture-of-Gaussians technique similar to the
EM algorithm discussed in Chapter 21 is then trained to recognize the speciﬁc color and
texture coefﬁcients of the small sample patch. The images in Figure 26.10 are the result of
applying this classiﬁer to the full image.
Methods that make robots collect their own training data (with labels!) are called self-
supervised. In this instance, the robot uses machine learning to leverage a short-range sensor
Self-supervised
learning
that works well for terrain classiﬁcation into a sensor that can see much farther. That allows
the robot to drive faster, slowing down only when the sensor model says there is a change in
the terrain that needs to be examined more carefully by the short-range sensors.
26.5 Planning and Control
The robot’s deliberations ultimately come down to deciding how to move, from the abstract
task level all the way down to the currents that are sent to its motors. In this section, we
simplify by assuming that perception (and, where needed, prediction) are given, so the world
is observable. We further assume deterministic transitions (dynamics) of the world.
We start by separating motion from control. We deﬁne a path as a sequence of points in
Path
geometric space that a robot (or a robot part, such as an arm) will follow. This is related to
the notion of path in Chapter 3, but here we mean a sequence of points in space rather than a
sequence of discrete actions. The task of ﬁnding a good path is called motion planning.
