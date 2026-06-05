---
chunk_id: "book-ca4fca8dd8-chunk-0628"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 628
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 381

Section 11.4
Hierarchical Planning
381
(a)
(b)
Figure 11.10 Goal achievement for high-level plans with approximate descriptions. The set
of goal states is shaded in purple. For each plan, the pessimistic (solid lines, light blue) and
optimistic (dashed lines, light green) reachable sets are shown. (a) The plan indicated by the
black arrow deﬁnitely achieves the goal, while the plan indicated by the red arrow deﬁnitely
doesn’t. (b) A plan that possibly achieves the goal (the optimistic reachable set intersects
the goal) but does not necessarily achieve the goal (the pessimistic reachable set does not
intersect the goal). The plan would need to be reﬁned further to determine if it really does
achieve the goal.
with approximate descriptions, there is a middle ground: if the optimistic set intersects the
goal but the pessimistic set doesn’t, then we cannot tell if the plan works (Figure 11.10(b)).
When this circumstance arises, the uncertainty can be resolved by reﬁning the plan. This is
a very common situation in human reasoning. For example, in planning the aforementioned
two-week Hawaii vacation, one might propose to spend two days on each of seven islands.
Prudence would indicate that this ambitious plan needs to be reﬁned by adding details of
inter-island transportation.
An algorithm for hierarchical planning with approximate angelic descriptions is shown
in Figure 11.11. For simplicity, we have kept to the same overall scheme used previously
in Figure 11.8, that is, a breadth-ﬁrst search in the space of reﬁnements. As just explained,
the algorithm can detect plans that will and won’t work by checking the intersections of
the optimistic and pessimistic reachable sets with the goal. (The details of how to compute
the reachable sets of a plan, given approximate descriptions of each step, are covered in
Exercise 11.HLAP.)
When a workable abstract plan is found, the algorithm decomposes the original problem
into subproblems, one for each step of the plan. The initial state and goal for each subproblem
are obtained by regressing a guaranteed-reachable goal state through the action schemas for
each step of the plan. (See Section 11.2.2 for a discussion of how regression works.) Fig-
ure 11.9(b) illustrates the basic idea: the right-hand circled state is the guaranteed-reachable
goal state, and the left-hand circled state is the intermediate goal obtained by regressing the
goal through the ﬁnal action.

## Page 382
