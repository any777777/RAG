---
chunk_id: "book-ca4fca8dd8-chunk-0604"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 604
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 367

Section 11.2
Algorithms for Classical Planning
367
apply the substitution to the action schema to yield a ground action with no variables. (It
is a requirement of action schemas that any variable in the effect must also appear in the
precondition; that way, we are guaranteed that no variables remain after the substitution.)
Each schema may unify in multiple ways. In the spare tire example (page 364), the
Remove action has the precondition At(obj,loc), which matches against the initial state in two
ways, resulting in the two substitutions {obj/Flat,loc/Axle} and {obj/Spare,loc/Trunk};
applying these substitutions yields two ground actions. If an action has multiple literals in
the precondition, then each of them can potentially be matched against the current state in
multiple ways.
At ﬁrst, it seems that the state space might be too big for many problems. Consider an
air cargo problem with 10 airports, where each airport initially has 5 planes and 20 pieces of
cargo. The goal is to move all the cargo at airport A to airport B. There is a 41-step solution
to the problem: load the 20 pieces of cargo into one of the planes at A, ﬂy the plane to B, and
unload the 20 pieces.
Finding this apparently straightforward solution can be difﬁcult because the average
branching factor is huge: each of the 50 planes can ﬂy to 9 other airports, and each of the 200
packages can be either unloaded (if it is loaded) or loaded into any plane at its airport (if it
is unloaded). So in any state there is a minimum of 450 actions (when all the packages are
at airports with no planes) and a maximum of 10,450 (when all packages and planes are at
(a)
(b)
At(P1, A)
Fly(P1, A, B)
Fly(P2, A, B)
Fly(P1, A, B)
Fly(P2, A, B)
At(P2, A)
At(P1, B)
At(P2, A)
At(P1, A)
At(P2, B)
At(P1, B)
At(P2, B)
At(P1, B)
At(P2, A)
At(P1, A)
At(P2, B)
Figure 11.5 Two approaches to searching for a plan.
(a) Forward (progression) search
through the space of ground states, starting in the initial state and using the problem’s ac-
tions to search forward for a member of the set of goal states. (b) Backward (regression)
search through state descriptions, starting at the goal and using the inverse of the actions to
search backward for the initial state.

## Page 368
