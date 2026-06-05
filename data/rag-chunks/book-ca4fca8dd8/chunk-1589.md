---
chunk_id: "book-ca4fca8dd8-chunk-1589"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1589
confidence: "first-pass"
extraction_method: "structured-local"
---

964
Chapter 26
Robotics
v
Cv
motion
envelope
initial
configuration
Figure 26.23 A two-dimensional environment, velocity uncertainty cone, and envelope of
possible robot motions. The intended velocity is v, but with uncertainty the actual velocity
could be anywhere in Cv, resulting in a ﬁnal conﬁguration somewhere in the motion envelope,
which means we wouldn’t know if we hit the hole or not.
and make sure the robot does that before coming up with a plan for reaching its actual goal.
Each guarded motion consists of (1) a motion command and (2) a termination condition,
which is a predicate on the robot’s sensor values saying when to stop.
Sometimes, the goal itself could be reached via a sequence of guarded moves guaranteed
to succeed regardless of uncertainty. As an example, Figure 26.23 shows a two-dimensional
conﬁguration space with a narrow vertical hole. It could be the conﬁguration space for inser-
tion of a rectangular peg into a hole or a car key into the ignition. The motion commands are
constant velocities. The termination conditions are contact with a surface. To model uncer-
tainty in control, we assume that instead of moving in the commanded direction, the robot’s
actual motion lies in the cone Cv about it.
The ﬁgure shows what would happen if the robot attempted to move straight down from
the initial conﬁguration. Because of the uncertainty in velocity, the robot could move any-
where in the conical envelope, possibly going into the hole, but more likely landing to one
side of it. Because the robot would not then know which side of the hole it was on, it would
not know which way to move.
A more sensible strategy is shown in Figures 26.24 and 26.25. In Figure 26.24, the robot
deliberately moves to one side of the hole. The motion command is shown in the ﬁgure,
and the termination test is contact with any surface. In Figure 26.25, a motion command is
given that causes the robot to slide along the surface and into the hole. Because all possible
velocities in the motion envelope are to the right, the robot will slide to the right whenever it
is in contact with a horizontal surface.
It will slide down the right-hand vertical edge of the hole when it touches it, because
all possible velocities are down relative to a vertical surface. It will keep moving until it
reaches the bottom of the hole, because that is its termination condition. In spite of the
control uncertainty, all possible trajectories of the robot terminate in contact with the bottom
of the hole—that is, unless surface irregularities cause the robot to stick in one place.
Other techniques beyond guarded movements change the cost function to incentivize ac-
tions we know will lead to information—like the coastal navigation heuristic which requires
Coastal navigation
the robot to stay near known landmarks. More generally, techniques can incorporate the ex-
pected information gain (reduction of entropy of the belief) as a term in the cost function,
