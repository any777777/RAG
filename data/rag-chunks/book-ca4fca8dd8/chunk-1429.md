---
chunk_id: "book-ca4fca8dd8-chunk-1429"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1429
confidence: "first-pass"
extraction_method: "structured-local"
---

864
Chapter 23
Reinforcement Learning
is the behavior of agents who are already optimizing (or, let’s say, nearly optimizing) that
reward function—in this case, expert human drivers.
The general ﬁeld of apprenticeship learning studies the process of learning how to be-
Apprenticeship
learning
have well given observations of expert behavior. We show the algorithm examples of expert
driving and tell it to “do it like that.” There are (at least) two ways to approach the appren-
ticeship learning problem. The ﬁrst is the one we discussed brieﬂy at the beginning of the
chapter: assuming the environment is observable, we apply supervised learning to the ob-
served state–action pairs to learn a policy π(s). This is called imitation learning. It has
Imitation learning
had some success in robotics (see page 973) but suffers from the the problem of brittleness:
even small deviations from the training set lead to errors that grow over time and eventually
to failure. Moreover, imitation learning will at best duplicate the teacher’s performance, not
exceed it. When humans learn by imitation, we sometimes use the pejorative term “aping” to
describe what they are doing. (It’s quite possible that apes use the term “humaning” amongst
themselves, perhaps in an even more pejorative sense.) The implication is that the imitation
learner doesn’t understand why it should perform any given action.
The second approach to apprenticeship learning is to understand why: to observe the
expert’s actions (and resulting states) and try to work out what reward function the expert is
maximizing. Then we could derive an optimal policy with respect to that reward function.
One expects that this approach will produce robust policies from relatively few examples of
expert behavior; after all, the ﬁeld of reinforcement learning is predicated on the idea that the
reward function, rather than the policy or the value function, is the most succinct, robust, and
transferable deﬁnition of the task. Furthermore, if the learner makes appropriate allowances
for possible suboptimality on the part of the expert, then it may be able to do better than
the expert by optimizing an accurate approximation to the true reward function. We call this
approach inverse reinforcement learning (IRL): learning rewards by observing a policy,
Inverse
reinforcement
learning
rather than learning a policy by observing rewards.
How do we ﬁnd the expert’s reward function, given the expert’s actions? Let us begin by
assuming that the expert was acting rationally. In that case, it seems we should be looking for
a reward function R∗such that the total expected discounted reward under the expert’s policy
is higher than (or at least the same as) under any other possible policy.
Unfortunately, there will be many reward functions that satisfy this constraint; one of
them is R∗(s,a,s′) = 0, because any policy is rational when there are no rewards at all.7
Another problem with this approach is that the assumption of a rational expert is unrealistic.
It means, for example, that a robot observing Lee Sedol making what eventually turns out to
be a losing move against ALPHAGO would have to assume that Lee Sedol was trying to lose
the game.
To avoid the problem that R∗(s,a,s′)=0 explains any observed behavior, it helps to think
in a Bayesian way. (See Section 21.1 for a reminder of what this means.) Suppose we
observe data d and let hR be the hypothesis that R is the true reward function. Then according
to Bayes’ rule, we have
P(hR |d) = αP(d|hR)P(hR).
7
According to Equation (16.9) on page 559, a reward function R′(s,a,s′)=R(s,a,s′) + γΦ(s′) −Φ(s) has ex-
actly the same optimal policies as R(s,a,s′), so we can recover the reward function only up to the possible addition
of any shaping function Φ(s). This is not such a serious problem, because a robot using R′ will behave just like a
robot using the “correct” R.
