---
chunk_id: "book-ca4fca8dd8-chunk-1592"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1592
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 26.7
Reinforcement Learning in Robotics
967
in simulation to the real world. The idea is to use the model as a simulator for a policy search
(Section 23.5). To learn a policy that transfers well, we can add noise to the model during
training, thereby making the policy more robust. Or, we can train policies that will work
with a variety of models by sampling different parameters in the simulations—sometimes
referred to as domain randomization. An example is in Figure 26.26, where a dexterous
Domain
randomization
manipulation task is trained in simulation by varying visual attributes, as well as physical
attributes like friction or damping.
Finally, hybrid approaches that borrow ideas from both model-based and model-free al-
gorithms are meant to give us the best of both. The hybrid approach originated with the Dyna
architecture, where the idea was to iterate between acting and improving the policy, but the
policy improvement would come in two complementary ways: 1) the standard model-free
way of using the experience to directly update the policy, and 2) the model-based way of
using the experience to ﬁt a model, then plan with it to generate a policy.
More recent techniques have experimented with ﬁtting local models, planning with them
to generate actions, and using these actions as supervision to ﬁt a policy, then iterating to get
better and better models around the areas that the policy needs. This has been successfully
applied in end-to-end learning, where the policy takes pixels as input and directly outputs
torques as actions—it enabled the ﬁrst demonstration of deep RL on physical robots.
Models can also be exploited for the purpose of ensuring safe exploration. Learning
slowly but safely may be better than learning quickly but crashing and burning half way
through. So arguably, more important than reducing real-world samples is reducing real-
world samples in dangerous states—we don’t want robots falling off cliffs, and we don’t
want them breaking our favorite mugs or, even worse, colliding with objects and people. An
approximate model, with uncertainty associated to it (for example by considering a range of
values for its parameters), can guide exploration and impose constraints on the actions that
the robot is allowed to take in order to avoid these dangerous states. This is an active area of
research in robotics and control.
26.7.2 Exploiting other information
Models are useful, but there is more we can do to further reduce sample complexity.
When setting up a reinforcement learning problem, we have to select the state and action
spaces, the representation of the policy or value function, and the reward function we’re using.
These decisions have a large impact on how easy or how hard we are making the problem.
One approach is to use higher-level motion primitives instead of low-level actions like
Motion primitive
torque commands. A motion primitive is a parameterized skill that the robot has. For exam-
ple, a robotic soccer player might have the skill of “pass the ball to the player at (x,y).” All
the policy needs to do is to ﬁgure out how to combine them and set their parameters, instead
of reinventing them. This approach often learns much faster than low-level approaches, but
does restrict the space of possible behaviors that the robot can learn.
Another way to reduce the number of real-world samples required for learning is to reuse
information from previous learning episodes on other tasks, rather than starting from scratch.
This falls under the umbrella of metalearning or transfer learning.
Finally, people are a great source of information. In the next section, we talk about how
to interact with people, and part of it is how to use their actions to guide the robot’s learning.
