---
chunk_id: "book-ca4fca8dd8-chunk-0639"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 639
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 11.5
Planning and Acting in Nondeterministic Domains
387
“when condition: effect,” where condition is a logical formula to be compared against the
current state, and effect is a formula describing the resulting state. For the vacuum world:
Action(Suck,
EFFECT:when AtL: CleanL∧when AtR: CleanR).
When applied to the initial belief state True, the resulting belief state is (AtL ∧CleanL) ∨
(AtR ∧CleanR), which is no longer in 1-CNF. (This transition can be seen in Figure 4.14
on page 147.) In general, conditional effects can induce arbitrary dependencies among the
ﬂuents in a belief state, leading to belief states of exponential size in the worst case.
It is important to understand the difference between preconditions and conditional effects.
All conditional effects whose conditions are satisﬁed have their effects applied to generate the
resulting belief state; if none are satisﬁed, then the resulting state is unchanged. On the other
hand, if a precondition is unsatisﬁed, then the action is inapplicable and the resulting state
is undeﬁned. From the point of view of sensorless planning, it is better to have conditional
effects than an inapplicable action. For example, we could split Suck into two actions with
unconditional effects as follows:
Action(SuckL,
PRECOND:AtL; EFFECT:CleanL)
Action(SuckR,
PRECOND:AtR; EFFECT:CleanR).
Now we have only unconditional schemas, so the belief states all remain in 1-CNF; unfortu-
nately, we cannot determine the applicability of SuckL and SuckR in the initial belief state.
It seems inevitable, then, that nontrivial problems will involve wiggly belief states, just
like those encountered when we considered the problem of state estimation for the wumpus
world (see Figure 7.21 on page 261). The solution suggested then was to use a conservative
approximation to the exact belief state; for example, the belief state can remain in 1-CNF
if it contains all literals whose truth values can be determined and treats all other literals as
unknown. While this approach is sound, in that it never generates an incorrect plan, it is
incomplete because it may be unable to ﬁnd solutions to problems that necessarily involve
interactions among literals. To give a trivial example, if the goal is for the robot to be on
a clean square, then [Suck] is a solution but a sensorless agent that insists on 1-CNF belief
states will not ﬁnd it.
Perhaps a better solution is to look for action sequences that keep the belief state as simple
as possible. In the sensorless vacuum world, the action sequence [Right,Suck,Left,Suck]
generates the following sequence of belief states:
b0 = True
b1 = AtR
b2 = AtR∧CleanR
b3 = AtL∧CleanR
b4 = AtL∧CleanR∧CleanL
That is, the agent can solve the problem while retaining a 1-CNF belief state, even though
some sequences (e.g., those beginning with Suck) go outside 1-CNF. The general lesson is
not lost on humans: we are always performing little actions (checking the time, patting our
