---
chunk_id: "book-ca4fca8dd8-chunk-0429"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 429
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 7.7
Agents Based on Propositional Logic
263
prove L1
2,1 if, say, Shoot0 is asserted instead. Now, SATPLAN will ﬁnd the plan [Forward0];
so far, so good.
Unfortunately, SATPLAN also ﬁnds the plan [Shoot0]. How could this be? To ﬁnd out,
we inspect the model that SATPLAN constructs: it includes the assignment L0
2,1, that is, the
agent can be in [2,1] at time 1 by being there at time 0 and shooting. One might ask, “Didn’t
we say the agent is in [1,1] at time 0?” Yes, we did, but we didn’t tell the agent that it can’t
be in two places at once! For entailment, L0
2,1 is unknown and cannot, therefore, be used in
a proof; for satisﬁability, on the other hand, L0
2,1 is unknown and can, therefore, be set to
whatever value helps to make the goal true.
SATPLAN is a good debugging tool for knowledge bases because it reveals places where
knowledge is missing. In this particular case, we can ﬁx the knowledge base by asserting
that, at each time step, the agent is in exactly one location, using a collection of sentences
similar to those used to assert the existence of exactly one wumpus. Alternatively, we can
assert ¬L0
x,y for all locations other than [1,1]; the successor-state axiom for location takes care
of subsequent time steps. The same ﬁxes also work to make sure the agent has one and only
one orientation at a time.
SATPLAN has more surprises in store, however. The ﬁrst is that it ﬁnds models with
impossible actions, such as shooting with no arrow. To understand why, we need to look more
carefully at what the successor-state axioms (such as Equation (7.3)) say about actions whose
preconditions are not satisﬁed. The axioms do predict correctly that nothing will happen when
such an action is executed (see Exercise 7.SATP), but they do not say that the action cannot be
executed! To avoid generating plans with illegal actions, we must add precondition axioms
Precondition axioms
stating that an action occurrence requires the preconditions to be satisﬁed.14 For example, we
need to say, for each time t, that
Shoott ⇒HaveArrowt .
This ensures that if a plan selects the Shoot action at any time, it must be the case that the
agent has an arrow at that time.
SATPLAN’s second surprise is the creation of plans with multiple simultaneous actions.
For example, it may come up with a model in which both Forward0 and Shoot0 are true,
which is not allowed. To eliminate this problem, we introduce action exclusion axioms: for
Action exclusion
axiom
every pair of actions At
i and At
j we add the axiom
¬At
i ∨¬At
j .
It might be pointed out that walking forward and shooting at the same time is not so hard to
do, whereas, say, shooting and grabbing at the same time is rather impractical. By imposing
action exclusion axioms only on pairs of actions that really do interfere with each other, we
can allow for plans that include multiple simultaneous actions—and because SATPLAN ﬁnds
the shortest legal plan, we can be sure that it will take advantage of this capability.
To summarize, SATPLAN ﬁnds models for a sentence containing the initial state, the
goal, the successor-state axioms, the precondition axioms, and the action exclusion axioms.
It can be shown that this collection of axioms is sufﬁcient, in the sense that there are no
longer any spurious “solutions.” Any model satisfying the propositional sentence will be a
14 Notice that the addition of precondition axioms means that we need not include preconditions for actions in
the successor-state axioms.
