---
chunk_id: "book-ca4fca8dd8-chunk-0635"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 635
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 11.5
Planning and Acting in Nondeterministic Domains
385
plan only for contingencies that have important consequences and a nonnegligible chance
of happening. Thus, a car driver contemplating a trip across the Sahara desert should make
explicit contingency plans for breakdowns, whereas a trip to the supermarket requires less
advance planning. We next look at each of the three approaches in more detail.
11.5.1 Sensorless planning
Section 4.4.1 (page 144) introduced the basic idea of searching in belief-state space to ﬁnd
a solution for sensorless problems. Conversion of a sensorless planning problem to a belief-
state planning problem works much the same way as it did in Section 4.4.1; the main dif-
ferences are that the underlying physical transition model is represented by a collection of
action schemas, and the belief state can be represented by a logical formula instead of by
an explicitly enumerated set of states. We assume that the underlying planning problem is
deterministic.
The initial belief state for the sensorless painting problem can ignore InView ﬂuents
because the agent has no sensors.
Furthermore, we take as given the unchanging facts
Object(Table)∧Object(Chair)∧Can(C1)∧Can(C2) because these hold in every belief state.
The agent doesn’t know the colors of the cans or the objects, or whether the cans are open
or closed, but it does know that objects and cans have colors: ∀x ∃c Color(x,c). After
Skolemizing (see Section 9.5.1), we obtain the initial belief state:
b0 = Color(x,C(x)).
In classical planning, where the closed-world assumption is made, we would assume that
any ﬂuent not mentioned in a state is false, but in sensorless (and partially observable) plan-
ning we have to switch to an open-world assumption in which states contain both positive
and negative ﬂuents, and if a ﬂuent does not appear, its value is unknown. Thus, the belief
state corresponds exactly to the set of possible worlds that satisfy the formula. Given this
initial belief state, the following action sequence is a solution:
[RemoveLid(Can1),Paint(Chair,Can1),Paint(Table,Can1)].
We now show how to progress the belief state through the action sequence to show that the
ﬁnal belief state satisﬁes the goal.
First, note that in a given belief state b, the agent can consider any action whose pre-
conditions are satisﬁed by b. (The other actions cannot be used because the transition model
doesn’t deﬁne the effects of actions whose preconditions might be unsatisﬁed.) According
to Equation (4.4) (page 145), the general formula for updating the belief state b given an
applicable action a in a deterministic world is as follows:
b′ = RESULT(b,a) = {s′ : s′ =RESULTP(s,a) and s ∈b}
where RESULTP deﬁnes the physical transition model. For the time being, we assume that the
initial belief state is always a conjunction of literals, that is, a 1-CNF formula. To construct
the new belief state b′, we must consider what happens to each literal ℓin each physical state
s in b when action a is applied. For literals whose truth value is already known in b, the truth
value in b′ is computed from the current value and the add list and delete list of the action.
(For example, if ℓis in the delete list of the action, then ¬ℓis added to b′.) What about a
literal whose truth value is unknown in b? There are three cases:
1. If the action adds ℓ, then ℓwill be true in b′ regardless of its initial value.
