---
chunk_id: "book-ca4fca8dd8-chunk-1591"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1591
confidence: "first-pass"
extraction_method: "structured-local"
---

966
Chapter 26
Robotics
(a)
(b)
(c)
Figure 26.26 Training a robust policy. (a) Multiple simulations are run of a robot hand ma-
nipulating objects, with different randomized parameters for physics and lighting. Courtesy
of Wojciech Zaremba. (b) The real-world environment, with a single robot hand in the center
of a cage, surrounded by cameras and range ﬁnders. (c) Simulation and real-world train-
ing yields multiple different policies for grasping objects; here a pinch grasp and a quadpod
grasp. Courtesy of OpenAI. See Andrychowicz et al. (2018a).
break!), and we have to accept that progress will be slower than in a simulation because the
world refuses to move faster than one second per second. Much of what is interesting about
using reinforcement learning in robotics boils down to how we might reduce the real world
sample complexity—the number of interactions with the physical world that the robot needs
before it has learned how to do the task.
26.7.1 Exploiting models
A natural way to avoid the need for many real-world samples is to use as much knowledge
of the world’s dynamics as possible. For instance, we might not know exactly what the
coefﬁcient of friction or the mass of an object is, but we might have equations that describe
the dynamics as a function of these parameters.
In such a case, model-based reinforcement learning (Chapter 23) is appealing, where
the robot can alternate between ﬁtting the dynamics parameters and computing a better pol-
icy. Even if the equations are incorrect because they fail to model every detail of physics,
researchers have experimented with learning an error term, in addition to the parameters, that
can compensate for the inaccuracy of the physical model. Or, we can abandon the equations
and instead ﬁt locally linear models of the world that each approximate the dynamics in a
region of the state space, an approach that has been successful in getting robots to master
complex dynamic tasks like juggling.
A model of the world can also be useful in reducing the sample complexity of model-free
reinforcement learning methods by doing sim-to-real transfer: transferring policies that work
Sim-to-real

## Page 967
