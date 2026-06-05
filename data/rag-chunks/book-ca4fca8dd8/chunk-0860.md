---
chunk_id: "book-ca4fca8dd8-chunk-0860"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 860
confidence: "first-pass"
extraction_method: "structured-local"
---

520
Chapter 15
Making Simple Decisions
15.2.1 Constraints on rational preferences
These questions can be answered by writing down some constraints on the preferences that a
rational agent should have and then showing that the MEU principle can be derived from the
constraints. We use the following notation to describe an agent’s preferences:
A ≻B
the agent prefers A over B.
A ∼B
the agent is indifferent between A and B.
A ≻∼B
the agent prefers A over B or is indifferent between them.
Now the obvious question is, what sorts of things are A and B? They could be states of the
world, but more often than not there is uncertainty about what is really being offered. For
example, an airline passenger who is offered “the pasta dish or the chicken” does not know
what lurks beneath the tinfoil cover.1 The pasta could be delicious or congealed, the chicken
juicy or overcooked beyond recognition. We can think of the set of outcomes for each action
as a lottery—think of each action as a ticket. A lottery L with possible outcomes S1,...,Sn
Lottery
that occur with probabilities p1,..., pn is written
L = [p1,S1; p2,S2; ... pn,Sn].
In general, each outcome Si of a lottery can be either an atomic state or another lottery. The
primary issue for utility theory is to understand how preferences between complex lotteries
are related to preferences between the underlying states in those lotteries. To address this
issue we list six constraints that we require any reasonable preference relation to obey:
• Orderability: Given any two lotteries, a rational agent must either prefer one or else
Orderability
rate them as equally preferable. That is, the agent cannot avoid deciding. As noted on
page 412, refusing to bet is like refusing to allow time to pass.
Exactly one of (A ≻B), (B ≻A), or (A ∼B) holds.
• Transitivity: Given any three lotteries, if an agent prefers A to B and prefers B to C,
Transitivity
then the agent must prefer A to C.
(A ≻B)∧(B ≻C) ⇒(A ≻C).
• Continuity: If some lottery B is between A and C in preference, then there is some
Continuity
probability p for which the rational agent will be indifferent between getting B for sure
and the lottery that yields A with probability p and C with probability 1−p.
A ≻B ≻C ⇒∃p [p,A; 1−p,C] ∼B.
• Substitutability: If an agent is indifferent between two lotteries A and B, then the
Substitutability
agent is indifferent between two more complex lotteries that are the same except that
B is substituted for A in one of them. This holds regardless of the probabilities and the
other outcome(s) in the lotteries.
A ∼B ⇒[p,A; 1−p,C] ∼[p,B;1−p,C].
This also holds if we substitute ≻for ∼in this axiom.
• Monotonicity: Suppose two lotteries have the same two possible outcomes, A and
Monotonicity
B. If an agent prefers A to B, then the agent must prefer the lottery that has a higher
probability for A (and vice versa).
A ≻B ⇒(p > q ⇔[p,A; 1−p,B] ≻[q,A; 1−q,B]).
1
We apologize to readers whose local airlines no longer offer food on long ﬂights.
