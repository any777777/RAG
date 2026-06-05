---
chunk_id: "book-ca4fca8dd8-chunk-1579"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1579
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 26.5
Planning and Control
959
(a)
(b)
(c)
Figure 26.22 Robot arm control using (a) proportional control with gain factor 1.0, (b) pro-
portional control with gain factor 0.1, and (c) PD (proportional derivative) control with gain
factors 0.3 for the proportional component and 0.8 for the differential component. In all cases
the robot arm tries to follow the smooth line path, but in (a) and (b) deviates substantially from
the path.
velocity, stays there as long as it can, and then decelerates back to 0. Assuming we can do
this, Equation (26.2) above can be rewritten as
u(t) = f −1(ξ(t), ˙ξ(t), ¨ξ(t)).
(26.3)
Even with the change from τ to ξ, an actual trajectory, the equation of applying torques from
above (called a control law) has a problem in practice. Thinking back to the reinforcement
Control law
learning section, you might guess what it is. The equation works great in the situation where
f is exact, but pesky reality gets in the way as usual: in real systems, we can’t measure masses
and inertias exactly, and f might not properly account for physical phenomena like stiction in
Stiction
the motors (the friction that tends to prevent stationary surfaces from being set in motion—to
make them stick). So, when the robot arm starts applying those torques but f is wrong, the
errors accumulate and you deviate further and further from the reference path.
Rather than just letting those errors accumulate, a robot can use a control process that
looks at where it thinks it is, compares that to where it wanted to be, and applies a torque to
minimize the error.
A controller that provides force in negative proportion to the observed error is known as
a proportional controller or P controller for short. The equation for the force is:
P controller
u(t) = KP(ξ(t)−qt)
where qt is the current conﬁguration, and KP is a constant representing the gain factor of the
Gain factor
controller. KP regulates how strongly the controller corrects for deviations between the actual
state qt and the desired state ξ(t).
Figure 26.22(a) illustrates what can go wrong with proportional control. Whenever a de-
viation occurs—whether due to noise or to constraints on the forces the robot can apply—the
robot provides an opposing force whose magnitude is proportional to this deviation. Intu-
itively, this might appear plausible, since deviations should be compensated by a counterforce
to keep the robot on track. However, as Figure 26.22(a) illustrates, a proportional controller
can cause the robot to apply too much force, overshooting the desired path and zig-zagging
