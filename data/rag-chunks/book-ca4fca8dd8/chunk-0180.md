---
chunk_id: "book-ca4fca8dd8-chunk-0180"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 180
confidence: "first-pass"
extraction_method: "structured-local"
---

108
Chapter 3
Solving Problems by Searching
But it is not obvious whether the f = g+h cost will monotonically increase. As you ex-
tend a path from n to n′, the cost goes from g(n)+h(n) to g(n)+c(n,a,n′)+h(n′). Canceling
out the g(n) term, we see that the path’s cost will be monotonically increasing if and only if
h(n) ≤c(n,a,n′)+h(n′); in other words if and only if the heuristic is consistent.13 But note
that a path might contribute several nodes in a row with the same g(n)+h(n) score; this will
happen whenever the decrease in h is exactly equal to the action cost just taken (for example,
in a grid problem, when n is in the same row as the goal and you take a step towards the goal,
g is increased by 1 and h is decreased by 1). If C∗is the cost of the optimal solution path,
then we can say the following:
• A∗expands all nodes that can be reached from the initial state on a path where every
node on the path has f(n) < C∗. We say these are surely expanded nodes.
Surely expanded
nodes
• A∗might then expand some of the nodes right on the “goal contour” (where f(n) = C∗)
before selecting a goal node.
• A∗expands no nodes with f(n) > C∗.
We say that A∗with a consistent heuristic is optimally efﬁcient in the sense that any algorithm
Optimally eﬃcient
that extends search paths from the initial state, and uses the same heuristic information, must
expand all nodes that are surely expanded by A∗(because any one of them could have been
part of an optimal solution). Among the nodes with f(n)=C∗, one algorithm could get lucky
and choose the optimal one ﬁrst while another algorithm is unlucky; we don’t consider this
difference in deﬁning optimal efﬁciency.
A∗is efﬁcient because it prunes away search tree nodes that are not necessary for ﬁnding
Pruning
an optimal solution. In Figure 3.18(b) we see that Timisoara has f = 447 and Zerind has f =
449. Even though they are children of the root and would be among the ﬁrst nodes expanded
by uniform-cost or breadth-ﬁrst search, they are never expanded by A∗search because the
solution with f = 418 is found ﬁrst. The concept of pruning—eliminating possibilities from
consideration without having to examine them—is important for many areas of AI.
That A∗search is complete, cost-optimal, and optimally efﬁcient among all such algo-
rithms is rather satisfying. Unfortunately, it does not mean that A∗is the answer to all our
searching needs. The catch is that for many problems, the number of nodes expanded can
be exponential in the length of the solution. For example, consider a version of the vacuum
world with a super-powerful vacuum that can clean up any one square at a cost of 1 unit,
without even having to visit the square; in that scenario, squares can be cleaned in any order.
With N initially dirty squares, there are 2N states where some subset has been cleaned; all
of those states are on an optimal solution path, and hence satisfy f(n) < C∗, so all of them
would be visited by A∗.
3.5.4 Satisﬁcing search: Inadmissible heuristics and weighted A∗
A∗search has many good qualities, but it expands a lot of nodes. We can explore fewer
nodes (taking less time and space) if we are willing to accept solutions that are suboptimal,
but are “good enough”—what we call satisﬁcing solutions. If we allow A∗search to use
an inadmissible heuristic—one that may overestimate—then we risk missing the optimal
Inadmissible
heuristic
solution, but the heuristic can potentially be more accurate, thereby reducing the number of
13 In fact, the term “monotonic heuristic” is a synonym for “consistent heuristic.” The two ideas were developed
independently, and then it was proved that they are equivalent (Pearl, 1984).
