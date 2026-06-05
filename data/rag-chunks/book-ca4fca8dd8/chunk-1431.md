---
chunk_id: "book-ca4fca8dd8-chunk-1431"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1431
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 23.6
Apprenticeship and Inverse Reinforcement Learning
865
Now, if the prior P(hR) is based on simplicity, then the hypothesis that R=0 scores fairly
well, because 0 is certainly simple. On the other hand, the term P(d|hR) is inﬁnitesimal
for the hypothesis that R=0, because it doesn’t explain why the expert chose that particular
behavior out of the vast space of behaviors that would be optimal if the hypothesis were true.
On the other hand, for a reward function R that has a unique optimal policy or a relatively
small equivalence class of optimal policies, P(d|hR) will be far higher.
To allow for the occasional mistake by the expert, we simply allow P(d|hR) to be nonzero
even when d comes from behavior that is a little bit suboptimal according to R. A typical
assumption—made, it must be said, more for mathematical convenience than faithfulness to
actual human data—is that an agent whose true Q-function is Q(s,a) chooses not accord-
ing to the deterministic policy π(s)= argmaxa Q(s,a) but instead according to a stochastic
policy deﬁned by the softmax distribution from Equation (23.14). This is sometimes called
Boltzmann rationality because, in statistical mechanics, the state occupation probabilities
Boltzmann
rationality
in a Boltzmann distribution depend exponentially on their energy levels.
There are dozens of inverse RL algorithms in the literature. One of the simplest is called
feature matching. It assumes that the reward function can be written as a weighted linear
Feature matching
combination of features:
Rθ(s,a,s′) =
n
∑
i=1
θi fi(s,a,s′) = θ ·f.
For example, the features in the driving domain might include speed, speed in excess of the
speed limit, acceleration, proximity to nearest obstacle, etc.
Recall from Equation (16.2) on page 557 that the utility of executing a policy π, starting
in state s0, is deﬁned to be
Uπ(s) = E
"
∞
∑
t =0
γtR(St,π(St),St+1)
#
,
where the expectation E is with respect to the probability distribution over state sequences
determined by s and π. Because R is assumed to be a linear combination of feature values,
we can rewrite this as follows:
Uπ(s) = E
"
∞
∑
t =0
γt
n
∑
i=1
θi fi(St,π(St),St+1)
#
=
n
∑
i=1
θiE
"
∞
∑
t =0
γt fi(St,π(St),St+1)
#
=
n
∑
i=1
θiµi(π) = θ ·µ(π)
where we have deﬁned the feature expectation µi(π) as the expected discounted value of
Feature expectation
the feature fi when policy π is executed. For example, if fi is the excess speed of the vehicle
(above the speed limit), then µi(π) is the (time-discounted) average excess speed over the
entire trajectory. The key point about feature expectations is the following: if a policy π ◀
produces feature expectations µi(π) that match those of the expert’s policy πE, then π is
as good as the expert’s policy according to the expert’s own reward function. Now, we
cannot measure the exact values for the feature expectations of the expert’s policy, but we
can approximate them using the average values on the observed trajectories. Thus, we need
