---
chunk_id: "chapter-03-2-dbbbe61755-chunk-0003"
source_id: "chapter-03-2-dbbbe61755"
source_file: "New folder/Chapter 03 (2).pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 3
confidence: "first-pass"
extraction_method: "structured-local"
---

What are irrelevant details for the case of Fig 3.2 we can think of?
States: traveling companions, current radio program,
condition of the road, the weather, and so on.
Actions: turning on the radio, looking out of the window, turn steering wheel to the left by x degrees, and so on.

## Slide 11

The abstraction is valid if we can elaborate any abstract solution into a solution in the more detailed world
The abstraction is useful if carrying out each of the actions in the solution is easier than the original problem (without further search or planning)

11

… Formulating problems

## Slide 12

A standardized (Toy)  problem is intended to illustrate or exercise various problem-solving methods. 
It can be given a concise, exact description 
and hence is suitable as a benchmark for researchers to compare the performance of algorithms. 
If it does not work , we have reasons to believe that it won’t work for real-world problems.
A real-world problem, such as robot navigation, is one whose solutions people actually use, and whose formulation is distinctive, not standardized, 
because, for example, each robot has different sensors that produce different data.

12

## Slide 13

3.2.1 Standardized problems

A grid world problem is a two-dimensional rectangular array of square cells in which agents can move from cell to cell. 
Typically, the agent can move to any obstacle-free adjacent cell—
horizontally or vertically 
and in some problems diagonally . 
Cells can contain objects, which the agent can pick up, push, or otherwise act upon; 
a wall or other impassible obstacle in a cell prevents an agent from moving into that cell.

13

## Slide 14

The vacuum world can be formulated as a grid world problem as follows:
States: A state of the world says which objects are in which cells.
In general, a vacuum environment with n cells has n · 2n states.
Initial state: Any state can be designated as the initial state.
Actions:
absolute movement actions: Suck, move Left, move Right, Upward, and Downward
egocentric actions: Forward, Backward, TurnRight, and TurnLeft
Transition model (how the world changes over time): e.g. Suck removes any dirt from the agent’s cell
Goal states: The states in which every cell is clean
Action cost: Each action costs 1

14

… Standardized problems

## Slide 15

15

… Standardized problems

## Slide 16

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

Example:	vacuum world state space graph
