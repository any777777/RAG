---
chunk_id: "book-ca4fca8dd8-chunk-1566"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1566
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 26.5
Planning and Control
947
For now we’ll stick with the simple two-dimensional C-space of the non-rotating triangle
robot. The next task is to ﬁgure out where the points in the obstacle are in C-space. Consider
the ﬁve dashed-line triangles on the left of Figure 26.11 and notice where the right-angle
vertex is on each of these. Then imagine all the ways that the triangle could slide about.
Obviously, the right-angle vertex can’t go inside the obstacle, and neither can it get any
closer than it is on any of the ﬁve dashed-line triangles. So you can see that the area where
the right-angle vertex can’t go—the C-space obstacle—is the ﬁve-sided polygon on the right
C-space obstacle
of Figure 26.11 labeled Cobs
In everyday language we speak of there being multiple obstacles for the robot—a table, a
chair, some walls. But the math notation is a bit easier if we think of all of these as combining
into one “obstacle” that happens to have disconnected components. In general, the C-space
obstacle is the set of all points q in C such that, if the robot were placed in that conﬁguration,
its workspace geometry would intersect the workspace obstacle.
Let the obstacles in the workspace be the set of points O, and let the set of all points on
the robot in conﬁguration q be A(q). Then the C-space obstacle is deﬁned as
Cobs = {q : q ∈C andA(q)∩O ̸= {}}
and the free space is Cfree = C −Cobs.
Free space
The C-space becomes more interesting for robots with moving parts. Consider the two-
link arm from Figure 26.12(a). It is bolted to a table so the base does not move, but the arm
has two joints that move independently—we call these degrees of freedom (DOF). Moving
Degrees of freedom
(DOF)
the joints alters the (x,y) coordinates of the elbow, the gripper, and every point on the arm.
The arm’s conﬁguration space is two-dimensional: (θshou,θelb), where θshou is the angle of
the shoulder joint, and θelb is the angle of the elbow joint.
Knowing the conﬁguration for our two-link arm means we can determine where each
point on the arm is through simple trigonometry. In general, the forward kinematics map-
Forward kinematics
ping is a function
φb : C →W
that takes in a conﬁguration and outputs the location of a particular point b on the robot when
the robot is in that conﬁguration. A particularly useful forward kinematics mapping is that for
the robot’s end effector, φEE. The set of all points on the robot in a particular conﬁguration q
is denoted by A(q) ⊂W:
A(q) =
[
b
{φb(q)}.
The inverse problem, of mapping a desired location for a point on the robot to the conﬁg-
uration(s) the robot needs to be in for that to happen, is known as inverse kinematics:
Inverse kinematics
IKb : x ∈W 7→{q ∈C s.t. φb(q) = x}.
Sometimes the inverse kinematics mapping might take not just a position, but also a desired
orientation as input. When we want a manipulator to grasp an object, for instance, we can
compute a desired position and orientation for its gripper, and use inverse kinematics to de-
termine a goal conﬁguration for the robot. Then a planner needs to ﬁnd a way to get the robot
from its current conﬁguration to the goal conﬁguration without intersecting obstacles.
Workspace obstacles are often depicted as simple geometric forms—especially in robotics
textbooks, which tend to focus on polygonal obstacles. But how do the obstacles look in con-
ﬁguration space?
