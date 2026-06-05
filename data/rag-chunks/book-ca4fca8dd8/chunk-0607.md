---
chunk_id: "book-ca4fca8dd8-chunk-0607"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 607
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 11.2
Algorithms for Classical Planning
369
the effect Own(i′), yielding the substitution θ = {i′/9780134610993}. Then we would regress
over the action Subst(θ,A) to yield the predecessor state description ISBN(9780134610993).
This is part of the initial state, so we have a solution and we are done, having considered just
one action, not a trillion.
More formally, assume a goal description g that contains a goal literal gi and an action
schema A. If A has an effect literal e′
j where Unify(gi,e′
j)=θ and where we deﬁne A′ =
SUBST(θ,A) and if there is no effect in A′ that is the negation of a literal in g, then A′ is a
relevant action towards g.
For most problem domains backward search keeps the branching factor lower than for-
ward search. However, the fact that backward search uses states with variables rather than
ground states makes it harder to come up with good heuristics. That is the main reason why
the majority of current systems favor forward search.
11.2.3 Planning as Boolean satisﬁability
In Section 7.7.4 we showed how some clever axiom-rewriting could turn a wumpus world
problem into a propositional logic satisﬁability problem that could be handed to an efﬁcient
satisﬁability solver. SAT-based planners such as SATPLAN operate by translating a PDDL
problem description into propositional form. The translation involves a series of steps:
• Propositionalize the actions: for each action schema, form ground propositions by sub-
stituting constants for each of the variables. So instead of a single Unload(c, p,a)
schema, we would have separate action propositions for each combination of cargo,
plane, and airport (here written with subscripts), and for each time step (here written as
a superscript).
• Add action exclusion axioms saying that no two actions can occur at the same time, e.g.
¬(FlyP1SFOJFK1 ∧FlyP1SFOBUH1).
• Add precondition axioms: For each ground action At, add the axiom At ⇒PRE(A)t,
that is, if an action is taken at time t, then the preconditions must have been true. For
example, FlyP1SFOJFK1 ⇒At(P1,SFO)∧Plane(P1)∧Airport(SFO)∧Airport(JFK).
• Deﬁne the initial state: assert F0 for every ﬂuent F in the problem’s initial state, and
¬F0 for every ﬂuent not mentioned in the initial state.
• Propositionalize the goal: the goal becomes a disjunction over all of its ground in-
stances, where variables are replaced by constants. For example, the goal of having
block A on another block, On(A,x)∧Block(x) in a world with objects A,B and C, would
be replaced by the goal
(On(A,A)∧Block(A))∨(On(A,B)∧Block(B))∨(On(A,C)∧Block(C)).
• Add successor-state axioms: For each ﬂuent F, add an axiom of the form
Ft+1 ⇔ActionCausesFt ∨(Ft ∧¬ActionCausesNotFt),
where ActionCausesF stands for a disjunction of all the ground actions that add F, and
ActionCausesNotF stands for a disjunction of all the ground actions that delete F.
The resulting translation is typically much larger than the original PDDL, but the efﬁciency
of modern SAT solvers often more than makes up for this.
