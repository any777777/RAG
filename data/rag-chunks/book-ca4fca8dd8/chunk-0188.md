---
chunk_id: "book-ca4fca8dd8-chunk-0188"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 188
confidence: "first-pass"
extraction_method: "structured-local"
---

114
Chapter 3
Solving Problems by Searching
3.5.6 Bidirectional heuristic search
With unidirectional best-ﬁrst search, we saw that using f(n) = g(n)+h(n) as the evaluation
function gives us an A∗search that is guaranteed to ﬁnd optimal-cost solutions (assuming an
admissible h) while being optimally efﬁcient in the number of nodes expanded.
With bidirectional best-ﬁrst search we could also try using f(n) = g(n) + h(n), but un-
fortunately there is no guarantee that this would lead to an optimal-cost solution, nor that it
would be optimally efﬁcient, even with an admissible heuristic. With bidirectional search, it
turns out that it is not individual nodes but rather pairs of nodes (one from each frontier) that
can be proved to be surely expanded, so any proof of efﬁciency will have to consider pairs of
nodes (Eckerle et al., 2017).
We’ll start with some new notation. We use fF(n) = gF(n)+hF(n) for nodes going in the
forward direction (with the initial state as root) and fB(n) = gB(n) + hB(n) for nodes in the
backward direction (with a goal state as root). Although both forward and backward searches
are solving the same problem, they have different evaluation functions because, for example,
the heuristics are different depending on whether you are striving for the goal or for the initial
state. We’ll assume admissible heuristics.
Consider a forward path from the initial state to a node m and a backward path from the
goal to a node n. We can deﬁne a lower bound on the cost of a solution that follows the path
from the initial state to m, then somehow gets to n, then follows the path to the goal as
lb(m,n) = max(gF(m)+gB(n), fF(m), fB(n))
In other words, the cost of such a path must be at least as large as the sum of the path costs of
the two parts (because the remaining connection between them must have nonnegative cost),
and the cost must also be at least as much as the estimated f cost of either part (because the
heuristic estimates are optimistic). Given that, the theorem is that for any pair of nodes m,n
with lb(m,n) less than the optimal cost C∗, we must expand either m or n, because the path
that goes through both of them is a potential optimal solution. The difﬁculty is that we don’t
know for sure which node is best to expand, and therefore no bidirectional search algorithm
can be guaranteed to be optimally efﬁcient—any algorithm might expand up to twice the
minimum number of nodes if it always chooses the wrong member of a pair to expand ﬁrst.
Some bidirectional heuristic search algorithms explicitly manage a queue of (m,n) pairs, but
we will stick with bidirectional best-ﬁrst search (Figure 3.14), which has two frontier priority
queues, and give it an evaluation function that mimics the lb criteria:
f2(n) = max(2g(n),g(n)+h(n))
The node to expand next will be the one that minimizes this f2 value; the node can come
from either frontier. This f2 function guarantees that we will never expand a node (from
either frontier) with g(n) > C∗
2 . We say the two halves of the search “meet in the middle” in
the sense that when the two frontiers touch, no node inside of either frontier has a path cost
greater than the bound C∗
2 . Figure 3.24 works through an example bidirectional search.
We have described an approach where the hF heuristic estimates the distance to the goal
(or, when the problem has multiple goal states, the distance to the closest goal) and hB esti-
mates the distance to the start. This is called a front-to-end search. An alternative, called
Front-to-end
front-to-front search, attempts to estimate the distance to the other frontier. Clearly, if a
Front-to-front
frontier has millions of nodes, it would be inefﬁcient to apply the heuristic function to every
