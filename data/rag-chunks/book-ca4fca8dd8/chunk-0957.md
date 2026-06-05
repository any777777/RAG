---
chunk_id: "book-ca4fca8dd8-chunk-0957"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 957
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 16.4
Partially Observable MDPs
579
perceives evidence e, then the new belief state is obtained by calculating the probability of
now being in state s′, for each s′, with the following formula:
b′(s′) = αP(e|s′)∑
s
P(s′ |s,a)b(s),
where α is a normalizing constant that makes the belief state sum to 1. By analogy with the
update operator for ﬁltering (page 485), we can write this as
b′ = αFORWARD(b,a,e).
(16.16)
In the 4×3 POMDP, suppose the agent moves Left and its sensor reports one adjacent wall;
then it’s quite likely (although not guaranteed, because both the motion and the sensor are
noisy) that the agent is now in (3,1). Exercise 16.POMD asks you to calculate the exact
probability values for the new belief state.
The fundamental insight required to understand POMDPs is this: the optimal action ◀
depends only on the agent’s current belief state. That is, an optimal policy can be described
by a mapping π∗(b) from belief states to actions. It does not depend on the actual state the
agent is in. This is a good thing, because the agent does not know its actual state; all it knows
is the belief state. Hence, the decision cycle of a POMDP agent can be broken down into the
following three steps:
1. Given the current belief state b, execute the action a=π∗(b).
2. Observe the percept e.
3. Set the current belief state to FORWARD(b,a,e) and repeat.
We can think of POMDPs as requiring a search in belief-state space, just like the methods for
sensorless and contingency problems in Chapter 4. The main difference is that the POMDP
belief-state space is continuous, because a POMDP belief state is a probability distribution.
For example, a belief state for the 4×3 world is a point in an 11-dimensional continuous
space. An action changes the belief state, not just the physical state, because it affects the
percept that is received. Hence, the action is evaluated at least in part according to the in-
formation the agent acquires as a result. POMDPs therefore include the value of information
(Section 15.6) as one component of the decision problem.
Let’s look more carefully at the outcome of actions. In particular, let’s calculate the
probability that an agent in belief state b reaches belief state b′ after executing action a. Now,
if we knew the action and the subsequent percept, then Equation (16.16) would provide a
deterministic update to the belief state: b′ = FORWARD(b,a,e). Of course, the subsequent
percept is not yet known, so the agent might arrive in one of several possible belief states b′,
depending on the percept that is received. The probability of perceiving e, given that a was
performed starting in belief state b, is given by summing over all the actual states s′ that the
agent might reach:
P(e|a,b) = ∑
s′
P(e|a,s′,b)P(s′|a,b)
= ∑
s′
P(e|s′)P(s′|a,b)
= ∑
s′
P(e|s′)∑
s
P(s′ |s,a)b(s).
