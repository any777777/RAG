---
chunk_id: "book-ca4fca8dd8-chunk-1423"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1423
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 23.5
Policy Search
861
world. The physical state consists only of the positions, orientations, and velocities of the
players and the ball. There is no “passing” and no “recipient” in the physical world; these are
entirely internal constructs. This means that there is no way to provide such sensible advice
to a standard RL system.
The hierarchical structure of behavior also provides a natural additive decomposition
Additive
decomposition
of the overall utility function. Remember that utility is the sum of rewards over time, and
consider a sequence of, say, ten time steps with rewards [r1,r2,...,r10]. Suppose that for the
ﬁrst ﬁve time steps the agent is doing PASS-TO(Ali) and for the remaining ﬁve steps it is
doing MOVE-INTO-SPACE. Then the utility for the initial state is the sum of the total reward
during PASS-TO and the total reward during MOVE-INTO-SPACE. The former depends only
on whether the ball gets to Ali with enough time and space for Ali to retain possession, and
the latter depends only on whether the agent reaches a good location to receive the ball. In
other words, the overall utility decomposes into several terms, each of which depends on only
a few variables. This, in turns, means that learning occurs much more quickly than if we try
to learn a single utility function that depends on all the variables. This is somewhat analogous
to the representation theorems underlying the conciseness of Bayes nets (Chapter 13).
23.5 Policy Search
The ﬁnal approach we will consider for reinforcement learning problems is called policy
search. In some ways, policy search is the simplest of all the methods in this chapter: the
Policy search
idea is to keep twiddling the policy as long as its performance improves, then stop.
Let us begin with the policies themselves. Remember that a policy π is a function that
maps states to actions. We are interested primarily in parameterized representations of π that
have far fewer parameters than there are states in the state space (just as in the preceding
section). For example, we could represent π by a collection of parameterized Q-functions,
one for each action, and take the action with the highest predicted value:
π(s) = argmax
a
ˆQθ(s,a).
(23.13)
Each Q-function could be a linear function, as in Equation (23.9), or it could be a nonlinear
function such as a deep neural network. Policy search will then adjust the parameters θ to
improve the policy. Notice that if the policy is represented by Q-functions, then policy search
results in a process that learns Q-functions. This process is not the same as Q-learning!
◀
In Q-learning with function approximation, the algorithm ﬁnds a value of θ such that ˆQθ
is “close” to Q∗, the optimal Q-function. Policy search, on the other hand, ﬁnds a value of
θ that results in good performance; the values found by the two methods may differ very
substantially. (For example, the approximate Q-function deﬁned by ˆQθ(s,a)=Q∗(s,a)/100
gives optimal performance, even though it is not at all close to Q∗.) Another clear instance
of the difference is the case where π(s) is calculated using, say, depth-10 look-ahead search
with an approximate utility function ˆUθ. A value of θ that gives good results may be a long
way from making ˆUθ resemble the true utility function.
One problem with policy representations of the kind given in Equation (23.13) is that the
policy is a discontinuous function of the parameters when the actions are discrete. That is,
there will be values of θ such that an inﬁnitesimal change in θ causes the policy to switch
from one action to another. This means that the value of the policy may also change dis-
