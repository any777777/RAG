---
chunk_id: "book-ca4fca8dd8-chunk-1577"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1577
confidence: "first-pass"
extraction_method: "structured-local"
---

958
Chapter 26
Robotics
Figure 26.21 The task of reaching to grasp a bottle solved with a trajectory optimizer. Left:
the initial trajectory, plotted for the end effector. Middle: the ﬁnal trajectory after optimiza-
tion. Right: the goal conﬁguration. Courtesy of Anca Dragan. See Ratliff et al. (2009).
a mathematical description of a path into a sequence of actions in the real world (open-loop
control), and how do we make sure that we are staying on track (closed-loop control)?
From conﬁgurations to torques for open-loop tracking: Our path τ(t) gives us conﬁg-
urations. The robot starts at rest at qs = τ(0). From there the robot’s motors will turn currents
into torques, leading to motion. But what torques should the robot aim for, such that it ends
up at qg = τ(1)?
This is where the idea of a dynamics model (or transition model) comes in. We can give
Dynamics model
the robot a function f that computes the effects torques have on the conﬁguration. Remem-
ber F = ma from physics? Well, there is something like that for torques too, in the form
u = f −1(q, ˙q, ¨q), with u a torque, ˙q a velocity, and ¨q an acceleration.2 If the robot is at conﬁg-
uration q and velocity ˙q, and applied torque u, that would lead to acceleration ¨q = f(q, ˙q,u).
The tuple (q, ˙q) is a dynamic state, because it includes velocity, whereas q is the kinematic
Dynamic state
state and is not sufﬁcient for computing exactly what torque to apply. f is a deterministic
Kinematic state
dynamics model in the MDP over dynamic states with torques as actions. f −1 is the inverse
dynamics, telling us what torque to apply if we want a particular acceleration, which leads
Inverse dynamics
to a change in velocity and thus a change in dynamic state.
Now, naively, we could think of t ∈[0,1] as “time” on a scale from 0 to 1 and select our
torque using inverse dynamics:
u(t) = f −1(τ(t), ˙τ(t), ¨τ(t))
(26.2)
assuming that the robot starts at (τ(0), ˙τ(0)). In reality though, things are not that easy.
The path τ was created as a sequence of points, without taking velocities and accelera-
tions into account. As such, the path may not satisfy ˙τ(0) = 0 (the robot starts at 0 velocity),
or even that τ is differentiable (let alone twice differentiable). Further, the meaning of the
endpoint “1” is unclear: how many seconds does that map to?
In practice, before we even think of tracking a reference path, we usually retime it, that
Retiming
is, transform it into a trajectory ξ(t) that maps the interval [0,T] for some time duration T
into points in the conﬁguration space C. (The symbol ξ is the Greek letter Xi.) Retiming is
trickier than you might think, but there are approximate ways to do it, for instance by picking
a maximum velocity and acceleration, and using a proﬁle that accelerates to that maximum
2
We omit the details of f −1 here, but they involve mass, inertia, gravity, and Coriolis and centrifugal forces.
