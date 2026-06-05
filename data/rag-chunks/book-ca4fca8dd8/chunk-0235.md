---
chunk_id: "book-ca4fca8dd8-chunk-0235"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 235
confidence: "first-pass"
extraction_method: "structured-local"
---

142
Chapter 4
Search in Complex Environments
Left
Suck
Right
Suck
Right
Suck
6 
GOAL
8 
GOAL
7 
1 
2 
5 
1 
LOOP
5 
LOOP
5 
LOOP
Left
Suck
1 
LOOP
GOAL
8 
4 
Figure 4.10 The ﬁrst two levels of the search tree for the erratic vacuum world. State nodes
are OR nodes where some action must be chosen. At the AND nodes, shown as circles, every
outcome must be handled, as indicated by the arc linking the outgoing branches. The solution
found is shown in bold lines.
A solution for an AND–OR search problem is a subtree of the complete search tree that
(1) has a goal node at every leaf, (2) speciﬁes one action at each of its OR nodes, and (3)
includes every outcome branch at each of its AND nodes. The solution is shown in bold lines
in the ﬁgure; it corresponds to the plan given in Equation (4.3).
Figure 4.11 gives a recursive, depth-ﬁrst algorithm for AND–OR graph search. One key
aspect of the algorithm is the way in which it deals with cycles, which often arise in nonde-
terministic problems (e.g., if an action sometimes has no effect or if an unintended effect can
be corrected). If the current state is identical to a state on the path from the root, then it re-
turns with failure. This doesn’t mean that there is no solution from the current state; it simply
means that if there is a noncyclic solution, it must be reachable from the earlier incarnation of
the current state, so the new incarnation can be discarded. With this check, we ensure that the
algorithm terminates in every ﬁnite state space, because every path must reach a goal, a dead
end, or a repeated state. Notice that the algorithm does not check whether the current state is
a repetition of a state on some other path from the root, which is important for efﬁciency.
AND–OR graphs can be explored either breadth-ﬁrst or best-ﬁrst. The concept of a heuris-
tic function must be modiﬁed to estimate the cost of a contingent solution rather than a se-
quence, but the notion of admissibility carries over and there is an analog of the A∗algorithm
for ﬁnding optimal solutions. (See the bibliographical notes at the end of the chapter.)

## Page 143
