---
chunk_id: "chapter-03-2-d1bd0d2931-chunk-0011"
source_id: "chapter-03-2-d1bd0d2931"
source_file: "Chapter 03 (2).pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 11
confidence: "first-pass"
extraction_method: "structured-local"
---

Complete?? Yes, unless there are infinitely many nodes with f ≤f (G)
Time?? For most problems, the number of nodes within the goal search space 
is still exponential in the length of the solution
Space?? Keeps all nodes in memory (to test)
A* usually runs out of space long before it runs out of time.

It is not practical for many large-scale problems
Optimal?? Yes, (HW, giving the two conditions)
Properties of A*
How to overcome the space problem without scarifying the optimality and
completeness? Use: Memory-bounded heuristic search

## Page 83

• A∗search has many good qualities (complete, cost-optimal, and 
optimally efficient), but it expands a lot of nodes. 
• We can explore fewer nodes (taking less time and space) if 
we are willing to accept solutions that are suboptimal, but are 
“good enough”—what we call satisficing solutions. 
• If we allow A∗search to use an inadmissible heuristic—one 
that may overestimate—then we risk missing the optimal 
solution, but the heuristic can potentially be more accurate, 
thereby reducing the number of nodes expanded.
87
3.5.4 Satisficing search: Inadmissible heuristics 
and weighted A∗

## Page 84

Weighted A∗search:
f(n) = g(n)+W ×h(n), 
for some W > 1
88
… Satisficing search: Inadmissible heuristics 
and weighted A∗

## Page 85

• A weighted A∗search will find a solution that costs somewhere 
between C ∗and W × C∗
• but in practice we usually get results much closer to C ∗than W × C∗
• There are a variety of suboptimal search algorithms, which can 
be characterized by the criteria for what counts as “good 
enough”:
• In bounded suboptimal search, we look for a solution that is 
guaranteed to be within a constant factor W of the optimal cost. 
• Weighted A∗provides this guarantee. 
• In bounded-cost search, we look for a solution whose cost is less 
than some constant C. 
• And in unbounded-cost search, we accept a solution of any cost, 
• as long as we can find it quickly, (e.g. speedy search).
89
… Satisficing search: Inadmissible heuristics 
and weighted A∗

## Page 86
