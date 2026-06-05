---
chunk_id: "book-ca4fca8dd8-chunk-0181"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 181
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 109

Section 3.5
Informed (Heuristic) Search Strategies
109
(a)
(b)
Figure 3.21 Two searches on the same grid: (a) an A∗search and (b) a weighted A∗search
with weight W = 2. The gray bars are obstacles, the purple line is the path from the green
start to red goal, and the small dots are states that were reached by each search. On this
particular problem, weighted A∗explores 7 times fewer states and ﬁnds a path that is 5%
more costly.
nodes expanded. For example, road engineers know the concept of a detour index, which is
Detour index
a multiplier applied to the straight-line distance to account for the typical curvature of roads.
A detour index of 1.3 means that if two cities are 10 miles apart in straight-line distance, a
good estimate of the best path between them is 13 miles. For most localities, the detour index
ranges between 1.2 and 1.6.
We can apply this idea to any problem, not just ones involving roads, with an approach
called weighted A∗search where we weight the heuristic value more heavily, giving us the
Weighted A∗search
evaluation function f(n) = g(n)+W ×h(n), for some W > 1.
Figure 3.21 shows a search problem on a grid world. In (a), an A∗search ﬁnds the optimal
solution, but has to explore a large portion of the state space to ﬁnd it. In (b), a weighted A∗
search ﬁnds a solution that is slightly costlier, but the search time is much faster. We see that
the weighted search focuses the contour of reached states towards a goal. That means that
fewer states are explored, but if the optimal path ever strays outside of the weighted search’s
contour (as it does in this case), then the optimal path will not be found. In general, if
the optimal solution costs C∗, a weighted A∗search will ﬁnd a solution that costs somewhere
between C∗and W ×C∗; but in practice we usually get results much closer to C∗than W ×C∗.
We have considered searches that evaluate states by combining g and h in various ways;
weighted A∗can be seen as a generalization of the others:
A∗search:
g(n)+h(n)
(W = 1)
Uniform-cost search:
g(n)
(W = 0)
Greedy best-ﬁrst search:
h(n)
(W = ∞)
Weighted A∗search: g(n)+W ×h(n) (1 < W < ∞)
You could call weighted A∗“somewhat-greedy search”: like greedy best-ﬁrst search, it fo-
cuses the search towards a goal; on the other hand, it won’t ignore the path cost completely,
and will suspend a path that is making little progress at great cost.

## Page 110
