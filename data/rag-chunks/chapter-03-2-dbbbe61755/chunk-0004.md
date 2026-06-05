---
chunk_id: "chapter-03-2-dbbbe61755-chunk-0004"
source_id: "chapter-03-2-dbbbe61755"
source_file: "New folder/Chapter 03 (2).pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 4
confidence: "first-pass"
extraction_method: "structured-local"
---

states??: integer dirt and robot locations (ignore dirt amounts etc.) actions??: Left, Right, Suck, NoOp
goal test??: no dirt
path cost??: 1 per action (0 for NoOp)

## Slide 17

17

… Standardized problems: Ex

The sokoban puzzle
For a world with n non-obstacle cells and b boxes, 
there are n × n!/(b!(n − b)!) states; 
for example, on an 8 × 8 grid with a dozen boxes, there are over 200 trillion states.

## Slide 18

Sliding-tile puzzle
Rush Hour puzzle
8-puzzle
15-puzzle

18

… Standardized problems : Ex

Start State	Goal State

states??: integer locations of tiles (ignore intermediate positions) actions??: move blank left, right, up, down (ignore unjamming etc.) goal test??: = goal state (given)
path cost??: 1 per move

Possible states: 9!/2

## Slide 19

Toy problem: Ex

The 8-queens
Place 8 queens on a chessboard such that no queen attacks any other. (A queen attacks any piece in the same row, column or diagonal.)

19

## Slide 20

17

Toy problem: Ex

The 8-queens
States: Any arrangement of 0 to 8 queens
Possible states: 64×63×…×57 = 1.8×1014
Initial state: Empty board
Actions: Add a queen to any empty square
Goal test: 8 queens on the board, none attacked
Path cost: N/A because only the final state counts

20

## Slide 21

3.2.2 Real-world problems

The route-finding problem, 
Consider the airline travel problems that must be solved by a travel-planning Web site. (single goal)
Touring problems describe a set of locations (many sequential goals) that must be visited, 
rather than a single goal destination. 
The traveling salesperson problem (TSP) is a touring problem in which every city on a map must be visited. 
The aim is to find a tour with cost < C 
(or in the optimization version, to find a tour with the lowest cost possible).

21

## Slide 22

An enormous amount of effort has been expended to improve the capabilities of TSP algorithms. 
The algorithms can also be extended to handle fleets (groups) of vehicles. 
For example, a search and optimization algorithm for routing school buses in Boston saved $5 million, cut traffic and air pollution, and saved time for drivers and students.
Search algorithms have been used for tasks such as:
planning the movements of automatic circuit-board drills 
stocking machines on shop floors.

22

… Real-world problems

## Slide 23
