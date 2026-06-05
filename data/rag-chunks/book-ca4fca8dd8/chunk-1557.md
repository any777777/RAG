---
chunk_id: "book-ca4fca8dd8-chunk-1557"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1557
confidence: "first-pass"
extraction_method: "structured-local"
---

940
Chapter 26
Robotics
xi, yi
vt ¢t
xt11
h(xt)
xt
t11
t ¢t
ut
u
v
Z1
Z2
Z3
Z4
(a)
(b)
Figure 26.5 (a) A simpliﬁed kinematic model of a mobile robot. The robot is shown as a
circle with an interior radius line marking the forward direction. The state xt consists of the
(xt,yt) position (shown implicitly) and the orientation θt. The new state xt+1 is obtained by
an update in position of vt∆t and in orientation of ωt∆t. Also shown is a landmark at (xi,yi)
observed at time t. (b) The range-scan sensor model. Two possible robot poses are shown for
a given range scan (z1,z2,z3,z4). It is much more likely that the pose on the left generated
the range scan than the pose on the right.
The notation ˆX refers to a deterministic state prediction. Of course, physical robots are
somewhat unpredictable. This is commonly modeled by a Gaussian distribution with mean
f(Xt,vt,ωt) and covariance Σx. (See Appendix A for a mathematical deﬁnition.)
P(Xt+1 | Xt,vt,ωt) = N( ˆXt+1,Σx).
This probability distribution is the robot’s motion model. It models the effects of the motion
at on the location of the robot.
Next, we need a sensor model. We will consider two kinds of sensor models. The ﬁrst
assumes that the sensors detect stable, recognizable features of the environment called land-
marks. For each landmark, the range and bearing are reported. Suppose the robot’s state
Landmark
is xt =(xt,yt,θt)⊤and it senses a landmark whose location is known to be (xi,yi)⊤. With-
out noise, a prediction of the range and bearing can be calculated by simple geometry (see
Figure 26.5(a)):
ˆzt = h(xt) =
 p
(xt −xi)2 +(yt −yi)2
arctan yi−yt
xi−xt −θt
!
.
Again, noise distorts our measurements. To keep things simple, assume Gaussian noise with
covariance Σz, giving us the sensor model
P(zt | xt) = N(ˆzt,Σz).
A somewhat different sensor model is used for a sensor array of range sensors, each of
Sensor array
which has a ﬁxed bearing relative to the robot. Such sensors produce a vector of range values
zt = (z1,...,zM)⊤.
Given a pose xt, let ˆzj be the computed range along the jth beam direction from xt to the
nearest obstacle. As before, this will be corrupted by Gaussian noise. Typically, we assume

## Page 941
