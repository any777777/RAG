---
chunk_id: "book-ca4fca8dd8-chunk-0175"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 175
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 3.5
Informed (Heuristic) Search Strategies
103
Urziceni
Neamt
Oradea
Zerind
Timisoara
Mehadia
Sibiu
Pitesti
Rimnicu Vilcea
Vaslui
Bucharest
Giurgiu
Hirsova
Eforie
Arad
Lugoj
Drobeta
Craiova
Fagaras
Iasi
 0
160
242
161
77
151
366
244
226
176
241
253
329
80
199
380
234
374
100
193
Figure 3.16 Values of hSLD—straight-line distances to Bucharest.
3.5.1 Greedy best-ﬁrst search
Greedy best-ﬁrst search is a form of best-ﬁrst search that expands ﬁrst the node with the
Greedy best-ﬁrst
search
lowest h(n) value—the node that appears to be closest to the goal—on the grounds that this
is likely to lead to a solution quickly. So the evaluation function f(n) = h(n).
Let us see how this works for route-ﬁnding problems in Romania; we use the straight-
line distance heuristic, which we will call hSLD. If the goal is Bucharest, we need to know
Straight-line
distance
the straight-line distances to Bucharest, which are shown in Figure 3.16.
For example,
hSLD(Arad)=366. Notice that the values of hSLD cannot be computed from the problem
description itself (that is, the ACTIONS and RESULT functions). Moreover, it takes a certain
amount of world knowledge to know that hSLD is correlated with actual road distances and is,
therefore, a useful heuristic.
Figure 3.17 shows the progress of a greedy best-ﬁrst search using hSLD to ﬁnd a path
from Arad to Bucharest. The ﬁrst node to be expanded from Arad will be Sibiu because the
heuristic says it is closer to Bucharest than is either Zerind or Timisoara. The next node to be
expanded will be Fagaras because it is now closest according to the heuristic. Fagaras in turn
generates Bucharest, which is the goal. For this particular problem, greedy best-ﬁrst search
using hSLD ﬁnds a solution without ever expanding a node that is not on the solution path.
The solution it found does not have optimal cost, however: the path via Sibiu and Fagaras to
Bucharest is 32 miles longer than the path through Rimnicu Vilcea and Pitesti. This is why
the algorithm is called “greedy”—on each iteration it tries to get as close to a goal as it can,
but greediness can lead to worse results than being careful.
Greedy best-ﬁrst graph search is complete in ﬁnite state spaces, but not in inﬁnite ones.
The worst-case time and space complexity is O(|V|). With a good heuristic function, however,
the complexity can be reduced substantially, on certain problems reaching O(bm).
3.5.2 A∗search
The most common informed search algorithm is A∗search (pronounced “A-star search”), a
A∗search
best-ﬁrst search that uses the evaluation function
f(n) = g(n)+h(n)
where g(n) is the path cost from the initial state to node n, and h(n) is the estimated cost of
the shortest path from n to a goal state, so we have
f(n) = estimated cost of the best path that continues from n to a goal.
