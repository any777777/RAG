---
chunk_id: "chapter-03-2-d1bd0d2931-chunk-0009"
source_id: "chapter-03-2-d1bd0d2931"
source_file: "Chapter 03 (2).pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 9
confidence: "first-pass"
extraction_method: "structured-local"
---

• An informed search strategy uses domain-specific hints about 
the location of goals—
• can find solutions more efficiently than an uninformed 
strategy.
• The hints come in the form of a heuristic function, denoted 
h(n):
• h(n) = estimated cost of the cheapest path from the state at node n to a 
goal state.
67
Know whether one non-goal state is “more promising” than another

## Page 66

3.5.1 Greedy best-first search
• Greedy best-first search is a form of best-first search that 
expands first the node with the lowest h(n) value—
• the node that appears to be closest to the goal—
• So, the evaluation function f(n) = h(n).
• For route-finding problems, we use the straight-line distance 
heuristic, hSLD
• it takes a certain amount of world knowledge to know that hSLD is 
correlated with actual road distances and is, therefore, a useful 
heuristic.
68

## Page 67

69
… Greedy best-first search

## Page 68

Romania with step costs in km
Straight−line distance 
to Bucharest
Arad
366
Bucharest
0
Craiova
160
Dobreta
242
Eforie
161
Fagaras
178
Giurgiu
77
Hirsova
151
Iasi
226
Lugoj
244
Mehadia
241
Neamt
234
Oradea
380
Pitesti
98
Rimnicu Vilcea
193
Sibiu
253
Timisoara
329
Urziceni
80
Vaslui
199
Zerind
374
Urziceni
Hirsova
Eforie
Neamt
Oradea
Zerind
Arad
Timisoara
Lugoj
Mehadia
Dobreta
Craiova
Sibiu
Fagaras
Pitesti
Vaslui
Iasi
Rimnicu Vilcea
71
75
118
111
70
75
120
151
140
99
80
97
101
211
138
146
85
Bucharest
90
Giurgiu
98
142
92
87
86

## Page 69

Greedy Best-First Search
Finding the route using greedy search

## Page 70

72
… Greedy best-
first search
•
The solution it found does 
not have optimal cost. 
•
This is why the algorithm is 
called “greedy”—on each 
iteration it tries to get as 
close to a goal as it can,
•
but greediness can 
lead to worse results 
than being careful.

## Page 71

Video of Demo Contours Greedy (Empty)
73

## Page 72

Video of Demo Contours Greedy (Pacman Small Maze)
74

## Page 73

Complete?? No. Can get stuck in loops
Time?? O(bm), but a good heuristiccan give dramatic improvement
Space?? O(bm)—keeps all nodes in memory
Optimal?? No
Properties of Greedy Search

The path via Sibiu and Fagaras to Bucharest is 32 kilometers
longer than the path through Rimnicu Vilcea and Pitesti

Consider the problem of getting from Iasi to Oradea.

## Page 74
