---
chunk_id: "chapter-03-2-d1bd0d2931-chunk-0010"
source_id: "chapter-03-2-d1bd0d2931"
source_file: "Chapter 03 (2).pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 10
confidence: "first-pass"
extraction_method: "structured-local"
---

3.5.2 A∗search
• The most common informed search algorithm is A∗search, a 
best-first search that uses the evaluation function
• f(n) = g(n)  +h(n)
• where g(n) is the path cost from the initial state to node n, 
• and h(n) is the estimated cost of the shortest path from n to a goal state, 
• So, we have f(n) = estimated cost of the best path that 
continues from n to a goal.
76
Idea: Avoid expanding paths that are already expensive

## Page 75

A* Search
How it works

## Page 76

78
… A∗search

## Page 77

79
… A∗search

## Page 78

• An admissible heuristic is one that never overestimates the 
cost to reach a goal. 
• (An admissible heuristic is therefore optimistic.)
• With an admissible heuristic, A∗is cost-optimal
80
… A∗search
A∗search uses an admissible heuristic
i.e., h(n) ≤h∗(n) where h∗(n) is the true cost from n. 
(Also require h(n) ≥0, so h(G) = 0 for any goal G.)
E.g., hSLD(n) never overestimates the actual road distance 
Theorem: A∗search is optimal if: 

Admissibility h(n)

Consistency (or Monotonicity)

## Page 79

Optimality of A* (Admissible ): ex
81
Start State
Goal State
51
2
3
4
5
6
7
8
7
2
4
5
6
8
3
1
h1(S) =?? 6
h2(S) =?? 4+0+3+3+1+0+2+1 = 14
With an admissible heuristic, A∗is cost-optimal
E.g., for the 8-puzzle:
h1(n) = number of misplaced tiles
h2(n) = total Manhattan distance
(i.e., no. of squares from desired location of each tile)

## Page 80

Optimality of A*(Consistency )
• Every consistent heuristic is admissible (but not vice versa),
• So, with a consistent heuristic, A∗is cost-optimal.
A heuristic is consistent if
h(n) ≤c(n, a, nJ) + h(nJ)
If h is consistent, we have
f (nJ) = g(nJ) + h(nJ)
= g(n) + c(n, a, nJ) + h(nJ)
≥g(n) + h(n)
= f (n)
I.e., f (n) is nondecreasing along any
path.

## Page 81

Example
Uniform-cost orders by path cost, or backward cost  g(n)
Greedy orders by goal proximity, or forward cost  h(n)
A* Search orders by the sum: f(n) = g(n) + h(n)
S
a
d
b
G
h=5
h=6
h=2
1
8
1
1
2
h=6
h=0
c
h=7
3
e
h=1
1
S
a
b
c
e
d
d
G
G
g = 0 
h=6
g = 1 
h=5
g = 2 
h=6
g = 3 
h=7
g = 4 
h=2
g = 6 
h=0
g = 9 
h=1
g = 10 
h=2
g = 12 
h=0
83

## Page 82
