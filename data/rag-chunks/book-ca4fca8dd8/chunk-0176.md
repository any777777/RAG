---
chunk_id: "book-ca4fca8dd8-chunk-0176"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 176
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 104

104
Chapter 3
Solving Problems by Searching
Rimnicu Vilcea
Zerind
Arad
Sibiu
Arad
Fagaras
Oradea
Timisoara
Sibiu
Bucharest
329
374
366
380
193
253
0
Rimnicu Vilcea
Arad
Sibiu
Arad
Fagaras
Oradea
Timisoara
329
Zerind
374
366
176
380
193
Zerind
Arad
Sibiu
Timisoara
253
329
374
Arad
366
(a) The initial state
(b) After expanding Arad
(c) After expanding Sibiu
(d) After expanding Fagaras
Figure 3.17 Stages in a greedy best-ﬁrst tree-like search for Bucharest with the straight-line
distance heuristic hSLD. Nodes are labeled with their h-values.
In Figure 3.18, we show the progress of an A∗search with the goal of reaching Bucharest.
The values of g are computed from the action costs in Figure 3.1, and the values of hSLD are
given in Figure 3.16. Notice that Bucharest ﬁrst appears on the frontier at step (e), but it is
not selected for expansion (and thus not detected as a solution) because at f =450 it is not the
lowest-cost node on the frontier—that would be Pitesti, at f =417. Another way to say this
is that there might be a solution through Pitesti whose cost is as low as 417, so the algorithm
will not settle for a solution that costs 450. At step (f), a different path to Bucharest is now
the lowest-cost node, at f =418, so it is selected and detected as the optimal solution.
A∗search is complete.11 Whether A∗is cost-optimal depends on certain properties of
the heuristic. A key property is admissibility: an admissible heuristic is one that never
Admissible heuristic
overestimates the cost to reach a goal. (An admissible heuristic is therefore optimistic.) With
11 Again, assuming all action costs are > ϵ > 0, and the state space either has a solution or is ﬁnite.

## Page 105
