---
chunk_id: "book-ca4fca8dd8-chunk-1433"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1433
confidence: "first-pass"
extraction_method: "structured-local"
---

866
Chapter 23
Reinforcement Learning
to ﬁnd values for the parameters θi such that the feature expectations of the policy induced
by the parameter values match those of the expert policy on the observed trajectories. The
following algorithm achieves this with any desired error bound.
• Pick an initial default policy π(0).
• For j=1,2,... until convergence:
– Find parameters θ(j) such that the expert’s policy maximally outperforms the poli-
cies π(0),...,π(j−1) according to the expected utility θ(j) ·µ(π).
– Let π(j) be the optimal policy for the reward function R(j) =θ(j) ·f.
This algorithm converges to a policy that is close in value to the expert’s, according to the
expert’s own reward function. It requires only O(nlogn) iterations and O(nlogn) expert
demonstrations, where n is the number of features.
A robot can use inverse reinforcement learning to learn a good policy for itself, by under-
standing the actions of an expert. In addition, the robot can learn the policies used by other
agents in a multiagent domain, whether they be adversarial or cooperative. And ﬁnally, in-
verse reinforcement learning can be used for scientiﬁc inquiry (without any thought of agent
design), to better understand the behavior of humans and other animals.
A key assumption in inverse RL is that the “expert” is behaving optimally, or nearly
optimally, with respect to some reward function in a single-agent MDP. This is a reasonable
assumption if the learner is watching the expert through a one-way mirror while the expert
goes about his or her business unawares. It is not a reasonable assumption if the expert is
aware of the learner. For example, suppose a robot is in medical school, learning to be a
surgeon by watching a human expert. An inverse RL algorithm would assume that the human
performs the surgery in the usual optimal way, as if the robot were not there. But that’s not
what would happen: the human surgeon is motivated to have the robot (like any other medical
student) learn quickly and well, and so she will modify her behavior considerably. She might
explain what she is doing as she goes along; she might point out mistakes to avoid, such as
making the incision too deep or the stitches too tight; she might describe the contingency
plans in case something goes wrong during surgery. None of these behaviors make sense
when performing surgery in isolation, so inverse RL algorithms will not be able to interpret
the underlying reward function. Instead, we need to understand this kind of situation as a
two-person assistance game, as described in Section 17.2.5.
23.7 Applications of Reinforcement Learning
We now turn to applications of reinforcement learning. These include game playing, where
the transition model is known and the goal is to learn the utility function, and robotics, where
the model is initially unknown.
23.7.1 Applications in game playing
In Chapter 1 we described Arthur Samuel’s early work on reinforcement learning for check-
ers, which began in 1952. A few decades passed before the challenge was taken up again, this
time by Gerry Tesauro in his work on backgammon. Tesauro’s ﬁrst attempt (1990) was a sys-
tem called NEUROGAMMON. The approach was an interesting variant on imitation learning.
The input was a set of 400 games played by Tesauro against himself. Rather than learn a pol-
