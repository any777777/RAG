---
chunk_id: "book-ca4fca8dd8-chunk-0926"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 926
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 16.1
Sequential Decision Problems
559
Furthermore, the optimal policy can be extracted from the Q-function as follows:
π∗(s) = argmax
a
Q(s,a).
(16.7)
We can also develop a Bellman equation for Q-functions, noting that the expected total reward
for taking an action is its immediate reward plus the discounted utility of the outcome state,
which in turn can be expressed in terms of the Q-function:
Q(s,a) = ∑
s′
P(s′ |s,a)[R(s,a,s′)+γ U(s′)]
= ∑
s′
P(s′ |s,a)[R(s,a,s′)+γ max
a′ Q(s′,a′)]
(16.8)
Solving the Bellman equations for U (or for Q) gives us what we need to ﬁnd an optimal
policy. The Q-function shows up again and again in algorithms for solving MDPs, so we
shall use the following deﬁnition:
function Q-VALUE(mdp,s,a,U) returns a utility value
return ∑
s′
P(s′ |s,a)[R(s,a,s′) + γ U[s′]]
16.1.3 Reward scales
Chapter 15 noted that the scale of utilities is arbitrary: an afﬁne transformation leaves the op-
timal decision unchanged. We can replace U(s) by U′(s) = mU(s)+b where m and b are any
constants such that m > 0. It is easy to see, from the deﬁnition of utilities as discounted sums
of rewards, that a similar transformation of rewards will leave the optimal policy unchanged
in an MDP:
R′(s,a,s′) = mR(s,a,s′)+b.
It turns out, however, that the additive reward decomposition of utilities leads to signiﬁcantly
more freedom in deﬁning rewards. Let Φ(s) be any function of the state s. Then, according
to the shaping theorem, the following transformation leaves the optimal policy unchanged:
Shaping theorem
R′(s,a,s′) = R(s,a,s′)+γΦ(s′)−Φ(s).
(16.9)
To show that this is true, we need to prove that two MDPs, M and M′, have identical optimal
policies as long as they differ only in their reward functions as speciﬁed in Equation (16.9).
We start from the Bellman equation for Q, the Q-function for MDP M:
Q(s,a) = ∑
s′
P(s′ |s,a)[R(s,a,s′)+γ max
a′ Q(s′,a′)].
Now let Q′(s,a)=Q(s,a)−Φ(s) and plug it into this equation; we get
Q′(s,a)+Φ(s) = ∑
s′
P(s′ |s,a)[R(s,a,s′)+γ max
a′ (Q′(s′,a′)+Φ(s′))].
which then simpliﬁes to
Q′(s,a) = ∑
s′
P(s′ |s,a)[R(s,a,s′)+γΦ(s′)−Φ(s)+γ max
a′ Q′(s′,a′)]
= ∑
s′
P(s′ |s,a)[R′(s,a,s′)+γ max
a′ Q′(s′,a′)].

## Page 560
