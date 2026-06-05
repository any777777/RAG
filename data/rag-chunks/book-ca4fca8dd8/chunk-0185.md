---
chunk_id: "book-ca4fca8dd8-chunk-0185"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 185
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 112

112
Chapter 3
Solving Problems by Searching
Zerind
Arad
Arad
Oradea
Craiova
Sibiu
Bucharest
Craiova
Rimnicu Vilcea
Fagaras
Sibiu
Zerind
Arad
Arad
Sibiu
Bucharest
Rimnicu Vilcea
Oradea
Zerind
Arad
Arad
Timisoara
Timisoara
Timisoara
Fagaras
Oradea
Rimnicu Vilcea
Craiova
Pitesti
Sibiu
646
415
671
526
553
646
671
450
591
646
671
526
553
418
615
607
447
449
447
447
449
449
366
393
366
393
413
413 417
415
366
393
415 450
417
Sibiu
Sibiu
Rimnicu Vilcea
Fagaras
447
415
447
447
417
(a) After expanding Arad, Sibiu, 
and Rimnicu Vilcea
(c) After switching back to Rimnicu Vilcea
and expanding Pitesti
(b) After unwinding back to Sibiu 
and expanding Fagaras
447
447
∞
∞
∞
417
417
Pitesti
Figure 3.23 Stages in an RBFS search for the shortest route to Bucharest. The f-limit value
for each recursive call is shown on top of each current node, and every node is labeled with
its f-cost. (a) The path via Rimnicu Vilcea is followed until the current best leaf (Pitesti)
has a value that is worse than the best alternative path (Fagaras). (b) The recursion unwinds
and the best leaf value of the forgotten subtree (417) is backed up to Rimnicu Vilcea; then
Fagaras is expanded, revealing a best leaf value of 450. (c) The recursion unwinds and the
best leaf value of the forgotten subtree (450) is backed up to Fagaras; then Rimnicu Vilcea is
expanded. This time, because the best alternative path (through Timisoara) costs at least 447,
the expansion continues to Bucharest.
“changes its mind” and tries Fagaras, and then changes its mind back again. These mind
changes occur because every time the current best path is extended, its f-value is likely to
increase—h is usually less optimistic for nodes closer to a goal. When this happens, the
second-best path might become the best path, so the search has to backtrack to follow it.
Each mind change corresponds to an iteration of IDA∗and could require many reexpansions
of forgotten nodes to recreate the best path and extend it one more node.

## Page 113
