---
chunk_id: "book-ca4fca8dd8-chunk-0615"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 615
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 11.3
Heuristics for Planning
373
of consideration all symmetric branches of the search tree except for one. For many domains,
this makes the difference between intractable and efﬁcient solving.
Another possibility is to do forward pruning, accepting the risk that we might prune
away an optimal solution, in order to focus the search on promising branches. We can deﬁne
a preferred action as follows: First, deﬁne a relaxed version of the problem, and solve it to
Preferred action
get a relaxed plan. Then a preferred action is either a step of the relaxed plan, or it achieves
some precondition of the relaxed plan.
Sometimes it is possible to solve a problem efﬁciently by recognizing that negative in-
teractions can be ruled out. We say that a problem has serializable subgoals if there exists
Serializable subgoals
an order of subgoals such that the planner can achieve them in that order without having to
undo any of the previously achieved subgoals. For example, in the blocks world, if the goal
is to build a tower (e.g., A on B, which in turn is on C, which in turn is on the Table, as in
Figure 11.3 on page 365), then the subgoals are serializable bottom to top: if we ﬁrst achieve
C on Table, we will never have to undo it while we are achieving the other subgoals. A
planner that uses the bottom-to-top trick can solve any problem in the blocks world without
backtracking (although it might not always ﬁnd the shortest plan). As another example, if
there is a room with n light switches, each controlling a separate light, and the goal is to have
them all on, then we don’t have to consider permutations of the order; we could arbitrarily
restrict ourselves to plans that ﬂip switches in, say, ascending order.
For the Remote Agent planner that commanded NASA’s Deep Space One spacecraft, it
was determined that the propositions involved in commanding a spacecraft are serializable.
This is perhaps not too surprising, because a spacecraft is designed by its engineers to be as
easy as possible to control (subject to other constraints). Taking advantage of the serialized
ordering of goals, the Remote Agent planner was able to eliminate most of the search. This
meant that it was fast enough to control the spacecraft in real time, something previously
considered impossible.
11.3.2 State abstraction in planning
A relaxed problem leaves us with a simpliﬁed planning problem just to calculate the value
of the heuristic function. Many planning problems have 10100 states or more, and relaxing
the actions does nothing to reduce the number of states, which means that it may still be
expensive to compute the heuristic. Therefore, we now look at relaxations that decrease the
number of states by forming a state abstraction—a many-to-one mapping from states in the
State abstraction
ground representation of the problem to the abstract representation.
The easiest form of state abstraction is to ignore some ﬂuents. For example, consider an
air cargo problem with 10 airports, 50 planes, and 200 pieces of cargo. Each plane can be
at one of 10 airports and each package can be either in one of the planes or unloaded at one
of the airports. So there are 1050 × (50 + 10)200 ≈10405 states. Now consider a particular
problem in that domain in which it happens that all the packages are at just 5 of the airports,
and all packages at a given airport have the same destination. Then a useful abstraction of the
problem is to drop all the At ﬂuents except for the ones involving one plane and one package
at each of the 5 airports. Now there are only 105 ×(5+10)5 ≈1011 states. A solution in this
abstract state space will be shorter than a solution in the original space (and thus will be an
admissible heuristic), and the abstract solution is easy to extend to a solution to the original
problem (by adding additional Load and Unload actions).
