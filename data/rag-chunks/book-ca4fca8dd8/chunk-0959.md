---
chunk_id: "book-ca4fca8dd8-chunk-0959"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 959
confidence: "first-pass"
extraction_method: "structured-local"
---

580
Chapter 16
Making Complex Decisions
Let us write the probability of reaching b′ from b, given action a, as P(b′ |b,a). This proba-
bility can be calculated as follows:
P(b′ |b,a) = ∑
e
P(b′|e,a,b)P(e|a,b)
= ∑
e
P(b′|e,a,b)∑
s′
P(e|s′)∑
s
P(s′ |s,a)b(s),
(16.17)
where P(b′|e,a,b) is 1 if b′ =FORWARD(b,a,e) and 0 otherwise.
Equation (16.17) can be viewed as deﬁning a transition model for the belief-state space.
We can also deﬁne a reward function for belief-state transitions, which is derived from the
expected reward of the real state transitions that might be occurring. Here, we use the simple
form ρ(b,a), the expected reward if the agent does a in belief state b:
ρ(b,a) = ∑
s
b(s)∑
s′
P(s′ |s,a)R(s,a,s′).
Together, P(b′ |b,a) and ρ(b,a) deﬁne an observable MDP on the space of belief states.
Furthermore, it can be shown that an optimal policy for this MDP, π∗(b), is also an optimal
policy for the original POMDP. In other words, solving a POMDP on a physical state space
▶
can be reduced to solving an MDP on the corresponding belief-state space. This fact is
perhaps less surprising if we remember that the belief state is always observable to the agent,
by deﬁnition.
16.5 Algorithms for Solving POMDPs
We have shown how to reduce POMDPs to MDPs, but the MDPs we obtain have a contin-
uous (and usually high-dimensional) state space. This means we will have to redesign the
dynamic programming algorithms from Sections 16.2.1 and 16.2.2, which assumed a ﬁnite
state space and a ﬁnite number of actions. Here we describe a value iteration algorithm de-
signed speciﬁcally for POMDPs, followed by an online decision-making algorithm similar to
those developed for games in Chapter 6.
16.5.1 Value iteration for POMDPs
Section 16.2.1 described a value iteration algorithm that computed one utility value for each
state. With inﬁnitely many belief states, we need to be more creative. Consider an optimal
policy π∗and its application in a speciﬁc belief state b: the policy generates an action, then,
for each subsequent percept, the belief state is updated and a new action is generated, and so
on. For this speciﬁc b, therefore, the policy is exactly equivalent to a conditional plan, as de-
ﬁned in Chapter 4 for nondeterministic and partially observable problems. Instead of thinking
about policies, let us think about conditional plans and how the expected utility of executing
a ﬁxed conditional plan varies with the initial belief state. We make two observations:
1. Let the utility of executing a ﬁxed conditional plan p starting in physical state s be αp(s).
Then the expected utility of executing p in belief state b is just ∑s b(s)αp(s), or b·αp if
we think of them both as vectors. Hence, the expected utility of a ﬁxed conditional plan
varies linearly with b; that is, it corresponds to a hyperplane in belief space.
2. At any given belief state b, an optimal policy will choose to execute the conditional plan
with highest expected utility; and the expected utility of b under an optimal policy is just
