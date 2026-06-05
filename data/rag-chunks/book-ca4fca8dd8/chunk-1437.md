---
chunk_id: "book-ca4fca8dd8-chunk-1437"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1437
confidence: "first-pass"
extraction_method: "structured-local"
---

868
Chapter 23
Reinforcement Learning
x
θ
(a)
(b)
Figure 23.9 (a) Setup for the problem of balancing a long pole on top of a moving cart.
The cart can be jerked left or right by a controller that observes the cart’s position x and
velocity ˙x, as well as the pole’s angle θ and rate of change of angle ˙θ. (b) Six superimposed
time-lapse images of a single autonomous helicopter performing a very difﬁcult “nose-in
circle” maneuver. The helicopter is under the control of a policy developed by the PEGASUS
policy-search algorithm (Ng et al., 2003). A simulator model was developed by observing
the effects of various control manipulations on the real helicopter; then the algorithm was
run on the simulator model overnight. A variety of controllers were developed for different
maneuvers. In all cases, performance far exceeded that of an expert human pilot using remote
control. (Image courtesy of Andrew Ng.)
to balance the pole for over an hour after 30 trials. The algorithm ﬁrst discretized the four-
dimensional state space into boxes—hence the name. It then ran trials until the pole fell over.
Negative reinforcement was associated with the ﬁnal action in the ﬁnal box and then propa-
gated back through the sequence. Improved generalization and faster learning can be obtained
using an algorithm that adaptively partitions the state space according to the observed varia-
tion in the reward, or by using a continuous-state, nonlinear function approximator such as a
neural network. Nowadays, balancing a triple inverted pendulum (three poles joined together
end to end) is a common exercise—a feat far beyond the capabilities of most humans, but
achievable using reinforcement learning.
Still more impressive is the application of reinforcement learning to radio-controlled
helicopter ﬂight (Figure 23.9(b)). This work has generally used policy search over large
MDPs (Bagnell and Schneider, 2001; Ng et al., 2003), often combined with imitation learn-
ing and inverse RL given observations of a human expert pilot (Coates et al., 2009).
Inverse RL has also been applied successfully to interpret human behavior, including
destination prediction and route selection by taxi drivers based on 100,000 miles of GPS
data (Ziebart et al., 2008) and detailed physical movements by pedestrians in complex envi-
ronments based on hours of video observation (Kitani et al., 2012). In the area of robotics,
a single expert demonstration was enough for the LittleDog quadruped to learn a 25-feature
reward function and nimbly traverse a previously unseen area of rocky terrain (Kolter et al.,
2008). For more on how RL and inverse RL are used in robotics, see Sections 26.7 and 26.8.
