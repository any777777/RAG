---
chunk_id: "book-ca4fca8dd8-chunk-0144"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 144
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 85

Section 3.2
Example Problems
85
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
Figure 3.2 The state-space graph for the two-cell vacuum world. There are 8 states and three
actions for each state: L = Left, R = Right, S = Suck.
the agent can pick up, push, or otherwise act upon; a wall or other impassible obstacle in a
cell prevents an agent from moving into that cell. The vacuum world from Section 2.1 can
be formulated as a grid world problem as follows:
• States: A state of the world says which objects are in which cells. For the vacuum
world, the objects are the agent and any dirt. In the simple two-cell version, the agent
can be in either of the two cells, and each cell can either contain dirt or not, so there are
2 · 2 · 2 = 8 states (see Figure 3.2). In general, a vacuum environment with n cells has
n·2n states.
• Initial state: Any state can be designated as the initial state.
• Actions: In the two-cell world we deﬁned three actions: Suck, move Left, and move
Right. In a two-dimensional multi-cell world we need more movement actions. We
could add Upward and Downward, giving us four absolute movement actions, or we
could switch to egocentric actions, deﬁned relative to the viewpoint of the agent—for
example, Forward, Backward, TurnRight, and TurnLeft.
• Transition model: Suck removes any dirt from the agent’s cell; Forward moves the
agent ahead one cell in the direction it is facing, unless it hits a wall, in which case
the action has no effect. Backward moves the agent in the opposite direction, while
TurnRight and TurnLeft change the direction it is facing by 90◦.
• Goal states: The states in which every cell is clean.
• Action cost: Each action costs 1.
Another type of grid world is the sokoban puzzle, in which the agent’s goal is to push a
Sokoban puzzle
number of boxes, scattered about the grid, to designated storage locations. There can be at
most one box per cell. When an agent moves forward into a cell containing a box and there
is an empty cell on the other side of the box, then both the box and the agent move forward.

## Page 86
