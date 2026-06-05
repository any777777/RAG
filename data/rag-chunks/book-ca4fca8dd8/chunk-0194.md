---
chunk_id: "book-ca4fca8dd8-chunk-0194"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 194
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 3.6
Heuristic Functions
117
Search Cost (nodes generated)
Effective Branching Factor
d
BFS
A∗(h1)
A∗(h2)
BFS
A∗(h1)
A∗(h2)
6
128
24
19
2.01
1.42
1.34
8
368
48
31
1.91
1.40
1.30
10
1033
116
48
1.85
1.43
1.27
12
2672
279
84
1.80
1.45
1.28
14
6783
678
174
1.77
1.47
1.31
16
17270
1683
364
1.74
1.48
1.32
18
41558
4102
751
1.72
1.49
1.34
20
91493
9905
1318
1.69
1.50
1.34
22
175921
22955
2548
1.66
1.50
1.34
24
290082
53039
5733
1.62
1.50
1.36
26
395355
110372
10080
1.58
1.50
1.35
28
463234
202565
22055
1.53
1.49
1.36
Figure 3.26 Comparison of the search costs and effective branching factors for 8-puzzle
problems using breadth-ﬁrst search, A∗with h1 (misplaced tiles), and A∗with h2 (Manhattan
distance). Data are averaged over 100 puzzles for each solution length d from 6 to 28.
One might ask whether h2 is always better than h1. The answer is “Essentially, yes.” It
is easy to see from the deﬁnitions of the two heuristics that for any node n, h2(n) ≥h1(n).
We thus say that h2 dominates h1. Domination translates directly into efﬁciency: A∗using h2
Domination
will never expand more nodes than A∗using h1 (except in the case of breaking ties unluckily).
The argument is simple. Recall the observation on page 108 that every node with f(n) < C∗
will surely be expanded. This is the same as saying that every node with h(n) < C∗−g(n)
is surely expanded when h is consistent. But because h2 is at least as big as h1 for all nodes,
every node that is surely expanded by A∗search with h2 is also surely expanded with h1, and
h1 might cause other nodes to be expanded as well. Hence, it is generally better to use a
heuristic function with higher values, provided it is consistent and that the computation time
for the heuristic is not too long.
3.6.2 Generating heuristics from relaxed problems
We have seen that both h1 (misplaced tiles) and h2 (Manhattan distance) are fairly good
heuristics for the 8-puzzle and that h2 is better. How might one have come up with h2? Is it
possible for a computer to invent such a heuristic mechanically?
h1 and h2 are estimates of the remaining path length for the 8-puzzle, but they are also
perfectly accurate path lengths for simpliﬁed versions of the puzzle. If the rules of the puzzle
were changed so that a tile could move anywhere instead of just to the adjacent empty square,
then h1 would give the exact length of the shortest solution. Similarly, if a tile could move one
square in any direction, even onto an occupied square, then h2 would give the exact length
of the shortest solution. A problem with fewer restrictions on the actions is called a relaxed
problem. The state-space graph of the relaxed problem is a supergraph of the original state
Relaxed problem
space because the removal of restrictions creates added edges in the graph.
Because the relaxed problem adds edges to the state-space graph, any optimal solution in
the original problem is, by deﬁnition, also a solution in the relaxed problem; but the relaxed
