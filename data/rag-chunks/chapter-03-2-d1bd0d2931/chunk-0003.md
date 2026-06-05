---
chunk_id: "chapter-03-2-d1bd0d2931-chunk-0003"
source_id: "chapter-03-2-d1bd0d2931"
source_file: "Chapter 03 (2).pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 3
confidence: "first-pass"
extraction_method: "structured-local"
---

3.2.1 Standardized problems
• A grid world problem is a two-dimensional rectangular array of 
square cells in which agents can move from cell to cell. 
• Typically, the agent can move to any obstacle-free adjacent cell—
• horizontally or vertically 
• and in some problems diagonally . 
• Cells can contain objects, which the agent can pick up, push, or 
otherwise act upon; 
• a wall or other impassible obstacle in a cell prevents an agent from moving 
into that cell.
13

## Page 12

• The vacuum world can be formulated as a grid world problem as 
follows:
• States: A state of the world says which objects are in which cells.
• In general, a vacuum environment with n cells has n · 2n states.
• Initial state: Any state can be designated as the initial state.
• Actions:
• absolute movement actions: Suck, move Left, move Right, Upward, and Downward
• egocentric actions: Forward, Backward, TurnRight, and TurnLeft
• Transition model (how the world changes over time): e.g. Suck removes any 
dirt from the agent’s cell
• Goal states: The states in which every cell is clean
• Action cost: Each action costs 1
14
… Standardized problems

## Page 13

15
… Standardized problems

## Page 14

16
S
S
R
L
S
S
S
S
R
L
R
L
R
L
S
S
S
S
L
L
L
L
R
R
R
R
Example: vacuum world state space graph
states??: integer dirt and robot locations (ignore dirt amounts etc.) 
actions??: Left, Right, Suck, NoOp
goal test??: no dirt
path cost??: 1 per action (0 for NoOp)

## Page 15

17
… Standardized problems: Ex
• The sokoban puzzle
• For a world with n non-obstacle cells and b boxes, 
• there are n × n!/(b!(n − b)!) states; 
• for example, on an 8 × 8 grid with a dozen boxes, there are over 200 trillion states.

## Page 16

• Sliding-tile puzzle
• Rush Hour puzzle
• 8-puzzle
• 15-puzzle
18
… Standardized problems : Ex
Start State
Goal State
states??: integer locations of tiles (ignore intermediate positions) 
actions??: move blank left, right, up, down (ignore unjamming etc.) 
goal test??: = goal state (given)
path cost??: 1 per move
Possible states: 9!/2

## Page 17

Toy problem: Ex
The 8-queens
Place 8 queens on a chessboard such that no 
queen attacks any other. (A queen attacks any 
piece in the same row, column or diagonal.)

## Page 18
