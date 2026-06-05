---
chunk_id: "chapter-03-2-dbbbe61755-chunk-0011"
source_id: "chapter-03-2-dbbbe61755"
source_file: "New folder/Chapter 03 (2).pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 11
confidence: "first-pass"
extraction_method: "structured-local"
---

How to overcome the space problem without scarifying the optimality and completeness? Use: Memory-bounded heuristic search

## Slide 85

3.5.3 Search contours

85

A useful way to visualize
a search is to draw contours
in the state space

## Slide 86

If C∗ is the cost of the optimal solution path, then:
A∗ expands all nodes that can be reached from the initial state on a path where every node on the path has f (n) <C∗. We say these are surely expanded nodes.
A∗ might then expand some of the nodes right on the “goal contour” (where f (n) =C∗) before selecting a goal node.
A∗ expands no nodes with f (n) >C∗.
We say that A∗ with a consistent heuristic is optimally efficient
A∗ is efficient because it prunes away search tree nodes that are not necessary for finding an optimal solution.
The concept of pruning—eliminating possibilities from consideration without having to examine them—is important for many areas of AI.

86

… Search contours

## Slide 87

A∗ search has many good qualities (complete, cost-optimal, and optimally efficient), but it expands a lot of nodes. 
We can explore fewer nodes (taking less time and space) if we are willing to accept solutions that are suboptimal, but are “good enough”—what we call satisficing solutions. 
If we allow A∗ search to use an inadmissible heuristic—one that may overestimate—then we risk missing the optimal solution, but the heuristic can potentially be more accurate, thereby reducing the number of nodes expanded.

87

3.5.4 Satisficing search: Inadmissible heuristics and weighted A∗

## Slide 88

Weighted A∗ search:
f(n) = g(n)+W ×h(n), 
for some W > 1

88

… Satisficing search: Inadmissible heuristics and weighted A∗

## Slide 89

A weighted A∗ search will find a solution that costs somewhere between C ∗ and W × C∗
but in practice we usually get results much closer to C ∗ than W × C∗
There are a variety of suboptimal search algorithms, which can be characterized by the criteria for what counts as “good enough”:
In bounded suboptimal search, we look for a solution that is guaranteed to be within a constant factor W of the optimal cost. 
Weighted A∗ provides this guarantee. 
In bounded-cost search, we look for a solution whose cost is less than some constant C. 
And in unbounded-cost search, we accept a solution of any cost, 
as long as we can find it quickly, (e.g. speedy search).

89

… Satisficing search: Inadmissible heuristics and weighted A∗

## Slide 90

3.5.5 Memory-bounded search
