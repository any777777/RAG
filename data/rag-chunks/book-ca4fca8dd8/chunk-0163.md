---
chunk_id: "book-ca4fca8dd8-chunk-0163"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 163
confidence: "first-pass"
extraction_method: "structured-local"
---

96
Chapter 3
Solving Problems by Searching
Sibiu
Fagaras
Pitesti
Rimnicu Vilcea
Bucharest
99
80
97
101
211
Figure 3.10 Part of the Romania state space, selected to illustrate uniform-cost search.
Consider Figure 3.10, where the problem is to get from Sibiu to Bucharest. The succes-
sors of Sibiu are Rimnicu Vilcea and Fagaras, with costs 80 and 99, respectively. The least-
cost node, Rimnicu Vilcea, is expanded next, adding Pitesti with cost 80 + 97=177. The
least-cost node is now Fagaras, so it is expanded, adding Bucharest with cost 99+211=310.
Bucharest is the goal, but the algorithm tests for goals only when it expands a node, not when
it generates a node, so it has not yet detected that this is a path to the goal.
The algorithm continues on, choosing Pitesti for expansion next and adding a second path
to Bucharest with cost 80 + 97 + 101=278. It has a lower cost, so it replaces the previous
path in reached and is added to the frontier. It turns out this node now has the lowest cost,
so it is considered next, found to be a goal, and returned. Note that if we had checked for a
goal upon generating a node rather than when expanding the lowest-cost node, then we would
have returned a higher-cost path (the one through Fagaras).
The complexity of uniform-cost search is characterized in terms of C∗, the cost of the
optimal solution,8 and ϵ, a lower bound on the cost of each action, with ϵ > 0. Then the
algorithm’s worst-case time and space complexity is O(b1+⌊C∗/ϵ⌋), which can be much greater
than bd. This is because uniform-cost search can explore large trees of actions with low costs
before exploring paths involving a high-cost and perhaps useful action. When all action costs
are equal, b1+⌊C∗/ϵ⌋is just bd+1, and uniform-cost search is similar to breadth-ﬁrst search.
Uniform-cost search is complete and is cost-optimal, because the ﬁrst solution it ﬁnds
will have a cost that is at least as low as the cost of any other node in the frontier. Uniform-
cost search considers all paths systematically in order of increasing cost, never getting caught
going down a single inﬁnite path (assuming that all action costs are > ϵ > 0).
3.4.3 Depth-ﬁrst search and the problem of memory
Depth-ﬁrst search always expands the deepest node in the frontier ﬁrst. It could be imple-
Depth-ﬁrst search
mented as a call to BEST-FIRST-SEARCH where the evaluation function f is the negative
of the depth. However, it is usually implemented not as a graph search but as a tree-like
search that does not keep a table of reached states. The progress of the search is illustrated
in Figure 3.11; search proceeds immediately to the deepest level of the search tree, where the
nodes have no successors. The search then “backs up” to the next deepest node that still has
8
Here, and throughout the book, the “star” in C∗means an optimal value for C.
