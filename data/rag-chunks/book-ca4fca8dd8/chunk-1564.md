---
chunk_id: "book-ca4fca8dd8-chunk-1564"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1564
confidence: "first-pass"
extraction_method: "structured-local"
---

946
Chapter 26
Robotics
y
x
R
O
y
x
Cobs
O
Figure 26.11 A simple triangular robot that can translate, and needs to avoid a rectangular
obstacle. On the left is the workspace, on the right is the conﬁguration space.
Once we have a path, the task of executing a sequence of actions to follow the path is
called trajectory tracking control. A trajectory is a path that has a time associated with
Trajectory tracking
control
Trajectory
each point on the path. A path just says “go from A to B to C, etc.” and a trajectory says
“start at A, take 1 second to get to B, and another 1.5 seconds to get to C, etc.”
26.5.1 Conﬁguration space
Imagine a simple robot, R, in the shape of a right triangle as shown by the lavender triangle in
the lower left corner of Figure 26.11. The robot needs to plan a path that avoids a rectangular
obstacle, O. The physical space that a robot moves about in is called the workspace. This
Workspace
particular robot can move in any direction in the x −y plane, but cannot rotate. The ﬁgure
shows ﬁve other possible positions of the robot with dashed outlines; these are each as close
to the obstacle as the robot can get.
The body of the robot could be represented as a set of (x,y) points (or (x,y,z) points
for a three-dimensional robot), as could the obstacle. With this representation, avoiding the
obstacle means that no point on the robot overlaps any point on the obstacle. Motion planning
would require calculations on sets of points, which can be complicated and time-consuming.
We can simplify the calculations by using a representation scheme in which all the points
that comprise the robot are represented as a single point in an abstract multidimensional
space, which we call the conﬁguration space, or C-space. The idea is that the set of points
Conﬁguration space
C-space
that comprise the robot can be computed if we know (1) the basic measurements of the robot
(for our triangle robot, the length of the three sides will do) and (2) the current pose of the
robot—its position and orientation.
For our simple triangular robot, two dimensions sufﬁce for the C-space: if we know the
(x,y) coordinates of a speciﬁc point on the robot—we’ll use the right-angle vertex—then we
can calculate where every other point of the triangle is (because we know the size and shape of
the triangle and because the triangle cannot rotate). In the lower-left corner of Figure 26.11,
the lavender triangle can be represented by the conﬁguration (0,0).
If we change the rules so that the robot can rotate, then we will need three dimensions,
(x,y,θ), to be able to calculate where every point is. Here θ is the robot’s angle of rotation
in the plane. If the robot also had the ability to stretch itself, growing uniformly by a scaling
factor s, then the C-space would have four dimensions, (x,y,θ,s).
