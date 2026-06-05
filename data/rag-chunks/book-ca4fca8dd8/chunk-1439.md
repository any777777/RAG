---
chunk_id: "book-ca4fca8dd8-chunk-1439"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1439
confidence: "first-pass"
extraction_method: "structured-local"
---

Summary
869
Summary
This chapter has examined the reinforcement learning problem: how an agent can become
proﬁcient in an unknown environment, given only its percepts and occasional rewards. Re-
inforcement learning is a very broadly applicable paradigm for creating intelligent systems.
The major points of the chapter are as follows.
• The overall agent design dictates the kind of information that must be learned:
– A model-based reinforcement learning agent acquires (or is equipped with) a
transition model P(s′ |s,a) for the environment and learns a utility function U(s).
– A model-free reinforcement learning agent may learn an action-utility function
Q(s,a) or a policy π(s).
• Utilities can be learned using several different approaches:
– Direct utility estimation uses the total observed reward-to-go for a given state as
direct evidence for learning its utility.
– Adaptive dynamic programming (ADP) learns a model and a reward function
from observations and then uses value or policy iteration to obtain the utilities or
an optimal policy. ADP makes optimal use of the local constraints on utilities of
states imposed through the neighborhood structure of the environment.
– Temporal-difference (TD) methods adjust utility estimates to be more consistent
with those of successor states. They can be viewed as simple approximations of the
ADP approach that can learn without requiring a transition model. Using a learned
model to generate pseudoexperiences can, however, result in faster learning.
• Action-utility functions, or Q-functions, can be learned by an ADP approach or a TD
approach. With TD, Q-learning requires no model in either the learning or action-
selection phase. This simpliﬁes the learning problem but potentially restricts the ability
to learn in complex environments, because the agent cannot simulate the results of
possible courses of action.
• When the learning agent is responsible for selecting actions while it learns, it must
trade off the estimated value of those actions against the potential for learning useful
new information. An exact solution for the exploration problem is infeasible, but some
simple heuristics do a reasonable job. An exploring agent must also take care to avoid
premature death.
• In large state spaces, reinforcement learning algorithms must use an approximate func-
tional representation of U(s) or Q(s,a) in order to generalize over states. Deep re-
inforcement learning—using deep neural networks as function approximators—has
achieved considerable success on hard problems.
• Reward shaping and hierarchical reinforcement learning are helpful for learning
complex behaviors, particularly when rewards are sparse and long action sequences are
required to obtain them.
• Policy-search methods operate directly on a representation of the policy, attempting
to improve it based on observed performance. The variation in the performance in a
stochastic domain is a serious problem; for simulated domains this can be overcome by
ﬁxing the randomness in advance.
