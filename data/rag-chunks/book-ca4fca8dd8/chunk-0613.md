---
chunk_id: "book-ca4fca8dd8-chunk-0613"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 613
confidence: "first-pass"
extraction_method: "structured-local"
---

372
Chapter 11
Automated Planning
Figure 11.6 Two state spaces from planning problems with the ignore-delete-lists heuristic.
The height above the bottom plane is the heuristic score of a state; states on the bottom
plane are goals. There are no local minima, so search for the goal is straightforward. From
Hoffmann (2005).
Another possibility is the ignore-delete-lists heuristic. Assume for a moment that all
Ignore-delete-lists
heuristic
goals and preconditions contain only positive literals.2 We want to create a relaxed version
of the original problem that will be easier to solve, and where the length of the solution
will serve as a good heuristic. We can do that by removing the delete lists from all actions
(i.e., removing all negative literals from effects). That makes it possible to make monotonic
progress towards the goal—no action will ever undo progress made by another action. It turns
out it is still NP-hard to ﬁnd the optimal solution to this relaxed problem, but an approximate
solution can be found in polynomial time by hill climbing.
Figure 11.6 diagrams part of the state space for two planning problems using the ignore-
delete-lists heuristic. The dots represent states and the edges actions, and the height of each
dot above the bottom plane represents the heuristic value. States on the bottom plane are
solutions. In both of these problems, there is a wide path to the goal. There are no dead ends,
so no need for backtracking; a simple hill-climbing search will easily ﬁnd a solution to these
problems (although it may not be an optimal solution).
11.3.1 Domain-independent pruning
Factored representations make it obvious that many states are just variants of other states. For
example, suppose we have a dozen blocks on a table, and the goal is to have block A on top
of a three-block tower. The ﬁrst step in a solution is to place some block x on top of block y
(where x, y, and A are all different). After that, place A on top of x and we’re done. There are
11 choices for x, and given x, 10 choices for y, and thus 110 states to consider. But all these
states are symmetric: choosing one over another makes no difference, and thus a planner
should only consider one of them. This is the process of symmetry reduction: we prune out
Symmetry reduction
2
Many problems are written with this convention. For problems that aren’t, replace every negative literal ¬P in
a goal or precondition with a new positive literal, P′, and modify the initial state and the action effects accordingly.
