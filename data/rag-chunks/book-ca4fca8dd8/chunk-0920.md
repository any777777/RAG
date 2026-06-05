---
chunk_id: "book-ca4fca8dd8-chunk-0920"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 920
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 16.1
Sequential Decision Problems
555
Figure 16.2 (a) The optimal policies for the stochastic environment with r= −0.04 for
transitions between nonterminal states. There are two policies because in state (3,1) both
Left and Up are optimal. (b) Optimal policies for four different ranges of r.
The ﬁrst question to answer is whether there is a ﬁnite horizon or an inﬁnite horizon
Finite horizon
Inﬁnite horizon
for decision making. A ﬁnite horizon means that there is a ﬁxed time N after which nothing
matters—the game is over, so to speak. Thus,
Uh([s0,a0,s1,a1,...,sN+k]) = Uh([s0,a0,s1,a1,...,sN])
for all k > 0. For example, suppose an agent starts at (3,1) in the 4×3 world of Figure 16.1,
and suppose that N =3. Then, to have any chance of reaching the +1 state, the agent must
head directly for it, and the optimal action is to go Up. On the other hand, if N =100, then
there is plenty of time to take the safe route by going Left. So, with a ﬁnite horizon, an optimal ◀
action in a given state may depend on how much time is left. A policy that depends on the
time is called nonstationary.
Nonstationary policy
With no ﬁxed time limit, on the other hand, there is no reason to behave differently in the
same state at different times. Hence, an optimal action depends only on the current state, and
the optimal policy is stationary. Policies for the inﬁnite-horizon case are therefore simpler
Stationary policy
than those for the ﬁnite-horizon case, and we deal mainly with the inﬁnite-horizon case in
this chapter. (We will see later that for partially observable environments, the inﬁnite-horizon
case is not so simple.) Note that “inﬁnite horizon” does not necessarily mean that all state
sequences are inﬁnite; it just means that there is no ﬁxed deadline. There can be ﬁnite state
sequences in an inﬁnite-horizon MDP that contains a terminal state.
The next question we must decide is how to calculate the utility of state sequences.
Throughout this chapter, we will additive discounted rewards: the utility of a history is
Additive discounted
reward
Uh([s0,a0,s1,a1,s2,...]) = R(s0,a0,s1)+γR(s1,a1,s2)+γ2R(s2,a2,s3)+··· ,
where the discount factor γ is a number between 0 and 1. The discount factor describes the
Discount factor
preference of an agent for current rewards over future rewards. When γ is close to 0, rewards
in the distant future are viewed as insigniﬁcant. When γ is close to 1, an agent is more willing
to wait for long-term rewards. When γ is exactly 1, discounted rewards reduce to the special
