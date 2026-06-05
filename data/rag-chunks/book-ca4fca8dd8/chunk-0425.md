---
chunk_id: "book-ca4fca8dd8-chunk-0425"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 425
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 7.7
Agents Based on Propositional Logic
261
Figure 7.21 Depiction of a 1-CNF belief state (bold outline) as a simply representable, con-
servative approximation to the exact (wiggly) belief state (shaded region with dashed outline).
Each possible world is shown as a circle; the shaded ones are consistent with all the percepts.
represents the set of all states at time 1 in which the wumpus is alive, the agent is at [2,1],
that square is breezy, and there is a pit in [3,1] or [2,2] or both.
Maintaining an exact belief state as a logical formula turns out not to be easy. If there
are n ﬂuent symbols for time t, then there are 2n possible states—that is, assignments of truth
values to those symbols. Now, the set of belief states is the powerset (set of all subsets) of the
set of physical states. There are 2n physical states, hence 22n belief states. Even if we used
the most compact possible encoding of logical formulas, with each belief state represented
by a unique binary number, we would need numbers with log2(22n)=2n bits to label the
current belief state. That is, exact state estimation may require logical formulas whose size is
exponential in the number of symbols.
One very common and natural scheme for approximate state estimation is to represent
belief states as conjunctions of literals, that is, 1-CNF formulas. To do this, the agent program
simply tries to prove Xt and ¬Xt for each symbol Xt (as well as each atemporal symbol whose
truth value is not yet known), given the belief state at t −1. The conjunction of provable
literals becomes the new belief state, and the previous belief state is discarded.
It is important to understand that this scheme may lose some information as time goes
along. For example, if the sentence in Equation (7.4) were the true belief state, then neither
P3,1 nor P2,2 would be provable individually and neither would appear in the 1-CNF belief
state. (Exercise 7.HYBR explores one possible solution to this problem.) On the other hand,
because every literal in the 1-CNF belief state is proved from the previous belief state, and
the initial belief state is a true assertion, we know that the entire 1-CNF belief state must be
true. Thus the set of possible states represented by the 1-CNF belief state includes all states ◀
that are in fact possible given the full percept history. As illustrated in Figure 7.21, the 1-
CNF belief state acts as a simple outer envelope, or conservative approximation, around the
Conservative
approximation
exact belief state. We see this idea of conservative approximations to complicated sets as a
recurring theme in many areas of AI.
