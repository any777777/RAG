---
chunk_id: "book-ca4fca8dd8-chunk-1585"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1585
confidence: "first-pass"
extraction_method: "structured-local"
---

962
Chapter 26
Robotics
In this section, we are looking more directly at the underlying MDP the robot works
in. We’re switching from the familiar discrete MDPs to continuous ones. We will denote
our dynamic state of the world by x, as is common practice—the equivalent of s in discrete
MDPs. Let xs and xg be the starting and goal states.
We want to ﬁnd a sequence of actions that, when executed by the robot, result in state-
action pairs with low cumulative cost. The actions are torques which we denote with u(t)
for t starting at 0 and ending at T. Formally, we want to ﬁnd the sequence of torques u that
minimize a cumulative cost J:
min
u
R T
0 J(x(t),u(t))dt
(26.7)
subject to the constraints
∀t, ˙x(t) = f(x(t),u(t))
x(0) = xs, x(T) = xg .
How is this connected to motion planning and trajectory tracking control? Well, imagine
we take the notion of efﬁciency and clearance away from the obstacles and put it into the cost
function J, just as we did before in trajectory optimization over kinematic state. The dynamic
state is the conﬁguration and velocity, and torques u change it via the dynamics f from open-
loop trajectory tracking. The difference is that now we’re thinking about the conﬁgurations
and the torques at the same time. Sometimes, we might want to treat collision avoidance as a
hard constraint as well, something we’ve also mentioned before when we looked at trajectory
optimization for the kinematic state only.
To solve this optimization problem, we can take gradients of J—not with respect to the
sequence τ of conﬁgurations anymore, but directly with respect to the controls u. It is some-
times helpful to include the state sequence x as a decision variable too, and use the dynamics
constraints to ensure that x and u are consistent. There are various trajectory optimization
techniques using this approach; two of them go by the names multiple shooting and direct
collocation. None of these techniques will ﬁnd the global optimal solution, but in practice
they can effectively make humanoid robots walk and make autonomous cars drive.
Magic happens when in the problem above, J is quadratic and f is linear in x and u. We
want to minimize
min
Z ∞
0 xTQx+uTRudt
subject to
∀t, ˙x(t) = Ax(t)+Bu(t).
We can optimize over an inﬁnite horizon rather than a ﬁnite one, and we obtain a policy
from any state rather than just a sequence of controls. Q and R need to be positive deﬁnite
matrices for this to work. This gives us the linear quadratic regulator (LQR). With LQR,
Linear quadratic
regulator (LQR)
the optimal value function (called cost to go) is quadratic, and the optimal policy is linear.
The policy looks like u = −Kx, where ﬁnding the matrix K requires solving an algebraic
Riccati equation—no local optimization, no value iteration, no policy iteration are needed!
Riccati equation
Because of the ease of ﬁnding the optimal policy, LQR ﬁnds many uses in practice de-
spite the fact that real problems seldom actually have quadratic costs and linear dynamics. A
really useful method is called iterative LQR (ILQR), which works by starting with a solu-
Iterative LQR
(ILQR)
tion and then iteratively computing a linear approximation of the dynamics and a quadratic
approximation of the cost around it, then solving the resulting LQR system to arrive at a new
solution. Variants of LQR are also often used for trajectory tracking.
