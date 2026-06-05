---
chunk_id: "book-ca4fca8dd8-chunk-1567"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1567
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 948

948
Chapter 26
Robotics
shou
elb
s
e
e
table
table
left wall
vertical
obstacle
s
w
w
(a)
(b)
Figure 26.12 (a) Workspace representation of a robot arm with two degrees of freedom. The
workspace is a box with a ﬂat obstacle hanging from the ceiling. (b) Conﬁguration space of
the same robot. Only white regions in the space are conﬁgurations that are free of collisions.
The dot in this diagram corresponds to the conﬁguration of the robot shown on the left.
For the two-link arm, simple obstacles in the workspace, like a vertical line, have very
complex C-space counterparts, as shown in Figure 26.12(b). The different shadings of the
occupied space correspond to the different objects in the robot’s workspace: the dark region
surrounding the entire free space corresponds to conﬁgurations in which the robot collides
with itself. It is easy to see that extreme values of the shoulder or elbow angles cause such a
violation. The two oval-shaped regions on both sides of the robot correspond to the table on
which the robot is mounted. The third oval region corresponds to the left wall.
Finally, the most interesting object in conﬁguration space is the vertical obstacle that
hangs from the ceiling and impedes the robot’s motions. This object has a funny shape in
conﬁguration space: it is highly nonlinear and at places even concave. With a little bit of
imagination the reader will recognize the shape of the gripper at the upper left end.
We encourage the reader to pause for a moment and study this diagram. The shape of this
obstacle in C-space is not at all obvious! The dot inside Figure 26.12(b) marks the conﬁgu-
ration of the robot in Figure 26.12(a). Figure 26.13 depicts three additional conﬁgurations,
both in workspace and in conﬁguration space. In conﬁguration conf-1, the gripper is grasping
the vertical obstacle.
We see that even if the robot’s workspace is represented by ﬂat polygons, the shape of
the free space can be very complicated. In practice, therefore, one usually probes a conﬁgu-
ration space instead of constructing it explicitly. A planner may generate a conﬁguration and
then test to see if it is in free space by applying the robot kinematics and then checking for
collisions in workspace coordinates.

## Page 949
