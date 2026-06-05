---
chunk_id: "book-ca4fca8dd8-chunk-0605"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 605
confidence: "first-pass"
extraction_method: "structured-local"
---

368
Chapter 11
Automated Planning
the same airport). On average, let’s say there are about 2000 possible actions per state, so the
search graph up to the depth of the 41-step solution has about 200041 nodes.
Clearly, even this relatively small problem instance is hopeless without an accurate heuris-
tic. Although many real-world applications of planning have relied on domain-speciﬁc heuris-
tics, it turns out (as we see in Section 11.3) that strong domain-independent heuristics can be
derived automatically; that is what makes forward search feasible.
11.2.2 Backward search for planning
In backward search (also called regression search) we start at the goal and apply the actions
Regression search
backward until we ﬁnd a sequence of steps that reaches the initial state. At each step we
consider relevant actions (in contrast to forward search, which considers actions that are
Relevant action
applicable). This reduces the branching factor signiﬁcantly, particularly in domains with
many possible actions.
A relevant action is one with an effect that uniﬁes with one of the goal literals, but with
no effect that negates any part of the goal. For example, with the goal ¬Poor ∧Famous, an
action with the sole effect Famous would be relevant, but one with the effect Poor ∧Famous
is not considered relevant: even though that action might be used at some point in the plan (to
establish Famous), it cannot appear at this point in the plan because then Poor would appear
in the ﬁnal state.
What does it mean to apply an action in the backward direction? Given a goal g and
an action a, the regression from g over a gives us a state description g′ whose positive and
Regression
negative literals are given by
POS(g′) = (POS(g)−ADD(a))∪POS(Precond(a))
NEG(g′) = (NEG(g)−DEL(a))∪NEG(Precond(a)).
That is, the preconditions must have held before, or else the action could not have been
executed, but the positive/negative literals that were added/deleted by the action need not
have been true before.
These equations are straightforward for ground literals, but some care is required when
there are variables in g and a. For example, suppose the goal is to deliver a speciﬁc piece
of cargo to SFO: At(C2,SFO). The Unload action schema has the effect At(c,a). When we
unify that with the goal, we get the substitution {c/C2,a/SFO}; applying that substitution to
the schema gives us a new schema which captures the idea of using any plane that is at SFO:
Action(Unload(C2, p′,SFO),
PRECOND:In(C2, p′)∧At(p′,SFO)∧Cargo(C2)∧Plane(p′)∧Airport(SFO)
EFFECT:At(C2,SFO)∧¬In(C2, p′)).
Here we replaced p with a new variable named p′. This is an instance of standardizing apart
variable names so there will be no conﬂict between different variables that happen to have the
same name (see page 302). The regressed state description gives us a new goal:
g′ = In(C2, p′)∧At(p′,SFO)∧Cargo(C2)∧Plane(p′)∧Airport(SFO).
As another example, consider the goal of owning a book with a speciﬁc ISBN number:
Own(9780134610993). Given a trillion 13-digit ISBNs and the single action schema
A = Action(Buy(i),PRECOND:ISBN(i),EFFECT:Own(i)).
a forward search without a heuristic would have to start enumerating the 10 billion ground
Buy actions. But with backward search, we would unify the goal Own(9780134610993) with
