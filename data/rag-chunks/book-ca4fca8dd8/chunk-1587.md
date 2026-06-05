---
chunk_id: "book-ca4fca8dd8-chunk-1587"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1587
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 26.6
Planning Uncertain Movements
963
26.6 Planning Uncertain Movements
In robotics, uncertainty arises from partial observability of the environment and from the
stochastic (or unmodeled) effects of the robot’s actions. Errors can also arise from the use
of approximation algorithms such as particle ﬁltering, which does not give the robot an exact
belief state even if the environment is modeled perfectly.
The majority of today’s robots use deterministic algorithms for decision making, such
as the path-planning algorithms of the previous section, or the search algorithms that were
introduced in Chapter 3. These deterministic algorithms are adapted in two ways: ﬁrst, they
deal with the continuous state space by turning it into a discrete space (for example with
visibility graphs or cell decomposition). Second, they deal with uncertainty in the current
state by choosing the most likely state from the probability distribution produced by the
Most likely state
state estimation algorithm. That approach makes the computation faster and makes a better
ﬁt for the deterministic search algorithms. In this section we discuss methods for dealing with
uncertainty that are analogous to the more complex search algorithms covered in Chapter 4.
First, instead of deterministic plans, uncertainty calls for policies. We already discussed
how trajectory tracking control turns a plan into a policy to compensate for errors in dynamics.
Sometimes though, if the most likely hypothesis changes enough, tracking the plan designed
for a different hypothesis is too suboptimal. This is where online replanning comes in: we
Online replanning
can recompute a new plan based on the new belief. Many robots today use a technique called
model predictive control (MPC), where they plan for a shorter time horizon, but replan
Model predictive
control (MPC)
at every time step. (MPC is therefore closely related to real-time search and game-playing
algorithms.) This effectively results in a policy: at every step, we run a planner and take the
ﬁrst action in the plan; if new information comes along, or we end up not where we expected,
that’s OK, because we are going to replan anyway and that will tell us what to do next.
Second, uncertainty calls for information gathering actions. When we consider only the
information we have and make a plan based on it (this is called separating estimation from
control), we are effectively solving (approximately) a new MDP at every step, corresponding
to our current belief about where we are or how the world works. But in reality, uncertainty is
better captured by the POMDP framework: there is something we don’t directly observe, be
it the robot’s location or conﬁguration, the location of objects in the world, or the parameters
of the dynamics model itself—for example, where exactly is the center of mass of link two
on this arm?
What we lose when we don’t solve the POMDP is the ability to reason about future
information the robot will get: in MDPs we only plan with what we know, not with what we
might eventually know. Remember the value of information? Well, robots that plan using
their current belief as if they will never ﬁnd out anything more fail to account for the value of
information. They will never take actions that seem suboptimal right now according to what
they know, but that will actually result in a lot of information and enable the robot to do well.
What does such an action look like for a navigation robot? The robot could get close
to a landmark to get a better estimate of where it is, even if that landmark is out of the way
according to what it currently knows. This action is optimal only if the robot considers the
new observations it will get, as opposed to looking only at the information it already has.
To get around this, robotics techniques sometimes deﬁne information gathering actions
explicitly—such as moving a hand until it touches a surface (called guarded movements)—
Guarded movement
