---
chunk_id: "book-ca4fca8dd8-chunk-0173"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 173
confidence: "first-pass"
extraction_method: "structured-local"
---

102
Chapter 3
Solving Problems by Searching
function is the path cost, we get bidirectional uniform-cost search, and if the cost of the
optimal path is C∗, then no node with cost > C∗
2 will be expanded. This can result in a
considerable speedup.
The general best-ﬁrst bidirectional search algorithm is shown in Figure 3.14. We pass
in two versions of the problem and the evaluation function, one in the forward direction
(subscript F) and one in the backward direction (subscript B). When the evaluation function
is the path cost, we know that the ﬁrst solution found will be an optimal solution, but with
different evaluation functions that is not necessarily true. Therefore, we keep track of the best
solution found so far, and might have to update that several times before the TERMINATED
test proves that there is no possible better solution remaining.
3.4.6 Comparing uninformed search algorithms
Figure 3.15 compares uninformed search algorithms in terms of the four evaluation criteria set
forth in Section 3.3.4. This comparison is for tree-like search versions which don’t check for
repeated states. For graph searches which do check, the main differences are that depth-ﬁrst
search is complete for ﬁnite state spaces, and the space and time complexities are bounded
by the size of the state space (the number of vertices and edges, |V|+|E|).
Criterion
Breadth-
Uniform-
Depth-
Depth-
Iterative
Bidirectional
First
Cost
First
Limited
Deepening
(if applicable)
Complete?
Yes1
Yes1,2
No
No
Yes1
Yes1,4
Optimal cost?
Yes3
Yes
No
No
Yes3
Yes3,4
Time
O(bd)
O(b1+⌊C∗/ϵ⌋)
O(bm)
O(bℓ)
O(bd)
O(bd/2)
Space
O(bd)
O(b1+⌊C∗/ϵ⌋)
O(bm)
O(bℓ)
O(bd)
O(bd/2)
Figure 3.15 Evaluation of search algorithms. b is the branching factor; m is the maximum
depth of the search tree; d is the depth of the shallowest solution, or is m when there is
no solution; ℓis the depth limit. Superscript caveats are as follows: 1 complete if b is
ﬁnite, and the state space either has a solution or is ﬁnite. 2 complete if all action costs are
≥ϵ > 0; 3 cost-optimal if action costs are all identical; 4 if both directions are breadth-ﬁrst
or uniform-cost.
3.5 Informed (Heuristic) Search Strategies
This section shows how an informed search strategy—one that uses domain-speciﬁc hints
Informed search
about the location of goals—can ﬁnd solutions more efﬁciently than an uninformed strategy.
The hints come in the form of a heuristic function, denoted h(n):10
Heuristic function
h(n) = estimated cost of the cheapest path from the state at node n to a goal state.
For example, in route-ﬁnding problems, we can estimate the distance from the current state to
a goal by computing the straight-line distance on the map between the two points. We study
heuristics and where they come from in more detail in Section 3.6.
10 It may seem odd that the heuristic function operates on a node, when all it really needs is the node’s state. It is
traditional to use h(n) rather than h(s) to be consistent with the evaluation function f(n) and the path cost g(n).
