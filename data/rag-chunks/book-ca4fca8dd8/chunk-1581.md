---
chunk_id: "book-ca4fca8dd8-chunk-1581"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1581
confidence: "first-pass"
extraction_method: "structured-local"
---

960
Chapter 26
Robotics
back and forth. This is the result of the natural inertia of the robot: once driven back to its
reference position the robot has a velocity that can’t instantaneously be stopped.
In Figure 26.22(a), the parameter KP = 1. At ﬁrst glance, one might think that choosing
a smaller value for KP would remedy the problem, giving the robot a gentler approach to
the desired path. Unfortunately, this is not the case. Figure 26.22(b) shows a trajectory for
KP = .1, still exhibiting oscillatory behavior. The lower value of the gain parameter helps, but
does not solve the problem. In fact, in the absence of friction, the P controller is essentially a
spring law; so it will oscillate indeﬁnitely around a ﬁxed target location.
There are a number of controllers that are superior to the simple proportional control law.
A controller is said to be stable if small perturbations lead to a bounded error between the
Stable
robot and the reference signal. It is said to be strictly stable if it is able to return to and then
Strictly stable
stay on its reference path upon such perturbations. Our P controller appears to be stable but
not strictly stable, since it fails to stay anywhere near its reference trajectory.
The simplest controller that achieves strict stability in our domain is a PD controller.
PD controller
The letter ‘P’ stands again for proportional, and ‘D’ stands for derivative. PD controllers are
described by the following equation:
u(t) = KP(ξ(t)−qt)+KD( ˙ξ(t)−˙qt).
(26.4)
As this equation suggests, PD controllers extend P controllers by a differential component,
which adds to the value of u(t) a term that is proportional to the ﬁrst derivative of the error
ξ(t) −qt over time. What is the effect of such a term? In general, a derivative term damp-
ens the system that is being controlled. To see this, consider a situation where the error is
changing rapidly over time, as is the case for our P controller above. The derivative of this
error will then counteract the proportional term, which will reduce the overall response to
the perturbation. However, if the same error persists and does not change, the derivative will
vanish and the proportional term dominates the choice of control.
Figure 26.22(c) shows the result of applying this PD controller to our robot arm, using as
gain parameters KP = .3 and KD = .8. Clearly, the resulting path is much smoother, and does
not exhibit any obvious oscillations.
PD controllers do have failure modes, however. In particular, PD controllers may fail to
regulate an error down to zero, even in the absence of external perturbations. Often such a
situation is the result of a systematic external force that is not part of the model. For example,
an autonomous car driving on a banked surface may ﬁnd itself systematically pulled to one
side. Wear and tear in robot arms causes similar systematic errors. In such situations, an
over-proportional feedback is required to drive the error closer to zero. The solution to this
problem lies in adding a third term to the control law, based on the integrated error over time:
u(t) = KP(ξ(t)−qt)+KI
Z t
0 (ξ(s)−qs)ds+KD( ˙ξ(t)−˙qt).
(26.5)
Here KI is a third gain parameter. The term
R t
0(ξ(s) calculates the integral of the error over
time. The effect of this term is that long-lasting deviations between the reference signal and
the actual state are corrected. Integral terms, then, ensure that a controller does not exhibit
systematic long-term error, although they do pose a danger of oscillatory behavior.
A controller with all three terms is called a PID controller (for proportional integral
PID controller
derivative). PID controllers are widely used in industry, for a variety of control problems.
Think of the three terms as follows—proportional: try harder the farther away you are from
