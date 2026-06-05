---
chunk_id: "book-ca4fca8dd8-chunk-0641"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 641
confidence: "first-pass"
extraction_method: "structured-local"
---

388
Chapter 11
Automated Planning
pockets to make sure we have the car keys, reading street signs as we navigate through a city)
to eliminate uncertainty and keep our belief state manageable.
There is another, quite different approach to the problem of unmanageably wiggly belief
states: don’t bother computing them at all. Suppose the initial belief state is b0 and we would
like to know the belief state resulting from the action sequence [a1,...,am]. Instead of com-
puting it explicitly, just represent it as “b0 then [a1,...,am].” This is a lazy but unambiguous
representation of the belief state, and it’s quite concise—O(n+m) where n is the size of the
initial belief state (assumed to be in 1-CNF) and m is the maximum length of an action se-
quence. As a belief-state representation, it suffers from one drawback, however: determining
whether the goal is satisﬁed, or an action is applicable, may require a lot of computation.
The computation can be implemented as an entailment test: if Am represents the collec-
tion of successor-state axioms required to deﬁne occurrences of the actions a1,...,am—as
explained for SATPLAN in Section 11.2.3—and Gm asserts that the goal is true after m steps,
then the plan achieves the goal if b0 ∧Am |= Gm—that is, if b0 ∧Am ∧¬Gm is unsatisﬁable.
Given a modern SAT solver, it may be possible to do this much more quickly than computing
the full belief state. For example, if none of the actions in the sequence has a particular goal
ﬂuent in its add list, the solver will detect this immediately. It also helps if partial results
about the belief state—for example, ﬂuents known to be true or false—are cached to simplify
subsequent computations.
The ﬁnal piece of the sensorless planning puzzle is a heuristic function to guide the
search. The meaning of the heuristic function is the same as for classical planning: an esti-
mate (perhaps admissible) of the cost of achieving the goal from the given belief state. With
belief states, we have one additional fact: solving any subset of a belief state is necessarily
easier than solving the belief state:
if b1 ⊆b2 then h∗(b1) ≤h∗(b2).
Hence, any admissible heuristic computed for a subset is admissible for the belief state itself.
The most obvious candidates are the singleton subsets, that is, individual physical states. We
can take any random collection of states s1,...,sN that are in the belief state b, apply any
admissible heuristic h, and return
H(b) = max{h(s1),...,h(sN)}
as the heuristic estimate for solving b. We can also use inadmissible heuristics such as the
ignore-delete-lists heuristic (page 372), which seems to work quite well in practice.
11.5.2 Contingent planning
We saw in Chapter 4 that contingency planning—the generation of plans with conditional
branching based on percepts—is appropriate for environments with partial observability, non-
determinism, or both. For the partially observable painting problem with the percept schemas
given earlier, one possible conditional solution is as follows:
[LookAt(Table),LookAt(Chair),
if Color(Table,c)∧Color(Chair,c) then NoOp
else [RemoveLid(Can1),LookAt(Can1),RemoveLid(Can2),LookAt(Can2),
if Color(Table,c)∧Color(can,c) then Paint(Chair,can)
else if Color(Chair,c)∧Color(can,c) then Paint(Table,can)
else [Paint(Chair,Can1),Paint(Table,Can1)]]]
