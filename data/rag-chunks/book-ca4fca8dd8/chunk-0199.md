---
chunk_id: "book-ca4fca8dd8-chunk-0199"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 199
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 120

120
Chapter 3
Solving Problems by Searching
Figure 3.28 A Web service providing driving directions, computed by a search algorithm.
milliseconds—the number of nodes generated is reduced by a factor of 10,000 compared with
the use of Manhattan distance. For 24-puzzles, a speedup of roughly a factor of a million can
be obtained. Disjoint pattern databases work for sliding-tile puzzles because the problem can
be divided up in such a way that each move affects only one subproblem—because only one
tile is moved at a time.
3.6.4 Generating heuristics with landmarks
There are online services that host maps with tens of millions of vertices and ﬁnd cost-optimal
driving directions in milliseconds (Figure 3.28). How can they do that, when the best search
algorithms we have considered so far are about a million times slower? There are many tricks,
but the most important one is precomputation of some optimal path costs. Although the
Precomputation
precomputation can be time-consuming, it need only be done once, and then can be amortized
over billions of user search requests.
We could generate a perfect heuristic by precomputing and storing the cost of the optimal
path between every pair of vertices. That would take O(|V|2) space, and O(|E|3) time—
practical for graphs with 10 thousand vertices, but not 10 million.
A better approach is to choose a few (perhaps 10 or 20) landmark points16 from the
Landmark point
vertices. Then for each landmark L and for each other vertex v in the graph, we compute
and store C∗(v,L), the exact cost of the optimal path from v to L. (We also need C∗(L,v);
on an undirected graph this is the same as C∗(v,L); on a directed graph—e.g., with one-way
streets—we need to compute this separately.) Given the stored C∗tables, we can easily create
an efﬁcient (although inadmissible) heuristic: the minimum, over all landmarks, of the cost
of getting from the current node to the landmark, and then to the goal:
hL(n) =
min
L∈LandmarksC∗(n,L)+C∗(L,goal)
If the optimal path happens to go through a landmark, this heuristic will be exact; if not it
is inadmissible—it overestimates the cost to the goal. In an A∗search, if you have exact
heuristics, then once you reach a node that is on an optimal path, every node you expand
16 Landmark points are sometimes called “pivots” or “anchors.”

## Page 121
