---
chunk_id: "book-ca4fca8dd8-chunk-0922"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 922
confidence: "first-pass"
extraction_method: "structured-local"
---

556
Chapter 16
Making Complex Decisions
case of purely additive rewards. Notice that additivity was used implicitly in our use of path
Additive reward
cost functions in heuristic search algorithms (Chapter 3).
There are several reasons why additive discounted rewards make sense. One is empirical:
both humans and animals appear to value near-term rewards more highly than rewards in the
distant future. Another is economic: if the rewards are monetary, then it really is better to
get them sooner rather than later because early rewards can be invested and produce returns
while you’re waiting for the later rewards. In this context, a discount factor of γ is equivalent
to an interest rate of (1/γ)−1. For example, a discount factor of γ =0.9 is equivalent to an
interest rate of 11.1%.
A third reason is uncertainty about the true rewards: they may never arrive for all sorts of
reasons that are not taken into account in the transition model. Under certain assumptions, a
discount factor of gamma is equivalent to adding a probability 1−γ of accidental termination
at every time step, independent of the action taken.
A fourth justiﬁcation arises from a natural property of preferences over histories. In the
terminology of multiattribute utility theory (see Section 15.4), each transition st
at
−→st+1
can be viewed as an attribute of the history [s0,a0,s1,a1,s2 ...]. In principle, the utility
function could depend in arbitrarily complex ways on these attributes. There is, however,
a highly plausible preference-independence assumption that can be made, namely that the
agent’s preferences between state sequences are stationary.
Stationary
preference
Assume two histories [s0,a0,s1,a1,s2,...] and [s′
0,a′
0,s′
1,a′
1,s′
2,...] begin with the same
transition (i.e., s0 =s′
0, a0 =a′
0, and s1 =s′
1). Then stationarity for preferences means that
the two histories should be preference-ordered the same way as the histories [s1,a1,s2,...]
and [s′
1,a′
1,s′
2,...]. In English, this means that if you prefer one future to another starting
tomorrow, then you should still prefer that future if it were to start today instead. Stationarity
is a fairly innocuous-looking assumption, but additive discounting is the only form of utility
on histories that satisﬁes it.
A ﬁnal justiﬁcation for discounted rewards is that it conveniently makes some nasty in-
ﬁnities go away. With inﬁnite horizons there is a potential difﬁculty: if the environment does
not contain a terminal state, or if the agent never reaches one, then all environment histories
will be inﬁnitely long, and utilities with additive undiscounted rewards will generally be inﬁ-
nite. While we can agree that +∞is better than −∞, comparing two state sequences with +∞
utility is more difﬁcult. There are three solutions, two of which we have seen already:
1. With discounted rewards, the utility of an inﬁnite sequence is ﬁnite. In fact, if γ < 1
and rewards are bounded by ±Rmax, we have
Uh([s0,a0,s1,...]) =
∞
∑
t =0
γtR(st,at,st+1) ≤
∞
∑
t =0
γtRmax = Rmax
1−γ ,
(16.1)
using the standard formula for the sum of an inﬁnite geometric series.
2. If the environment contains terminal states and if the agent is guaranteed to get to one
eventually, then we will never need to compare inﬁnite sequences. A policy that is
guaranteed to reach a terminal state is called a proper policy. With proper policies,
Proper policy
we can use γ =1 (i.e., additive undiscounted rewards). The ﬁrst three policies shown
in Figure 16.2(b) are proper, but the fourth is improper. It gains inﬁnite total reward
by staying away from the terminal states when the reward for transitions between non-
terminal states is positive. The existence of improper policies can cause the standard
