---
chunk_id: "chapter-03-2-d1bd0d2931-chunk-0004"
source_id: "chapter-03-2-d1bd0d2931"
source_file: "Chapter 03 (2).pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 4
confidence: "first-pass"
extraction_method: "structured-local"
---

17
Toy problem: Ex
The 8-queens
States: Any arrangement of 0 to 8 queens
Possible states: 64×63×…×57 = 1.8×1014
Initial state: Empty board
Actions: Add a queen to any empty square
Goal test: 8 queens on the board, none attacked
Path cost: N/A because only the final state counts
20

## Page 19

3.2.2 Real-world problems
• The route-finding problem, 
• Consider the airline travel problems that must be solved by a travel-planning 
Web site. (single goal)
• Touring problems describe a set of locations (many sequential goals) 
that must be visited, 
• rather than a single goal destination. 
• The traveling salesperson problem (TSP) is a touring problem in 
which every city on a map must be visited. 
• The aim is to find a tour with cost < C
• (or in the optimization version, to find a tour with the lowest cost possible). 
21

## Page 20

• An enormous amount of effort has been expended to improve the 
capabilities of TSP algorithms. 
• The algorithms can also be extended to handle fleets (groups) of vehicles. 
• For example, a search and optimization algorithm for routing school buses in Boston 
saved $5 million, cut traffic and air pollution, and saved time for drivers and students.
• Search algorithms have been used for tasks such as:
• planning the movements of automatic circuit-board drills 
• stocking machines on shop floors.
22
… Real-world problems

## Page 21

• A VLSI layout problem requires positioning millions of components 
and connections on a chip to minimize area, minimize circuit delays, 
minimize lost capacitances, and maximize manufacturing yield. 
• Robot navigation is a generalization of the route-finding problem. 
• Automatic assembly sequencing of complex objects (such as electric 
motors) by a robot has been standard industry practice since the 
1970s.
23
… Real-world problems

## Page 22

• A search algorithm takes a search problem as input and returns a 
solution, 
• or an indication of failure. 
• In this chapter we consider algorithms that superimpose a search 
tree:
• forming various paths from the initial state, 
• trying to find a path that reaches a goal state. 
• Each node in the search tree corresponds to a state in the state space 
• and the edges in the search tree correspond to actions. 
• The root of the tree corresponds to the initial state of the problem.
24

## Page 23

… Search Algorithms
25

## Page 24

… Search Algorithms
26

## Page 25
