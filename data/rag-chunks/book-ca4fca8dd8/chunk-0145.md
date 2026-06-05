---
chunk_id: "book-ca4fca8dd8-chunk-0145"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 145
confidence: "first-pass"
extraction_method: "structured-local"
---

86
Chapter 3
Solving Problems by Searching
2
Start State
Goal State
1
3
4
6
7
5
1
2
3
4
6
7
8
5
8
Figure 3.3 A typical instance of the 8-puzzle.
The agent can’t push a box into another box or a wall. For a world with n non-obstacle cells
and b boxes, there are n × n!/(b!(n −b)!) states; for example on an 8 × 8 grid with a dozen
boxes, there are over 200 trillion states.
In a sliding-tile puzzle, a number of tiles (sometimes called blocks or pieces) are ar-
Sliding-tile puzzle
ranged in a grid with one or more blank spaces so that some of the tiles can slide into the
blank space. One variant is the Rush Hour puzzle, in which cars and trucks slide around a
6 ×6 grid in an attempt to free a car from the trafﬁc jam. Perhaps the best-known variant is
the 8-puzzle (see Figure 3.3), which consists of a 3 × 3 grid with eight numbered tiles and
8-puzzle
one blank space, and the 15-puzzle on a 4 × 4 grid. The object is to reach a speciﬁed goal
15-puzzle
state, such as the one shown on the right of the ﬁgure. The standard formulation of the 8
puzzle is as follows:
• States: A state description speciﬁes the location of each of the tiles.
• Initial state: Any state can be designated as the initial state. Note that a parity prop-
erty partitions the state space—any given goal can be reached from exactly half of the
possible initial states (see Exercise 3.PART).
• Actions: While in the physical world it is a tile that slides, the simplest way of describ-
ing an action is to think of the blank space moving Left, Right, Up, or Down. If the
blank is at an edge or corner then not all actions will be applicable.
• Transition model: Maps a state and action to a resulting state; for example, if we apply
Left to the start state in Figure 3.3, the resulting state has the 5 and the blank switched.
• Goal state: Although any state could be the goal, we typically specify a state with the
numbers in order, as in Figure 3.3.
• Action cost: Each action costs 1.
Note that every problem formulation involves abstractions. The 8-puzzle actions are ab-
stracted to their beginning and ﬁnal states, ignoring the intermediate locations where the tile
is sliding. We have abstracted away actions such as shaking the board when tiles get stuck
and ruled out extracting the tiles with a knife and putting them back again. We are left with a
description of the rules, avoiding all the details of physical manipulations.
Our ﬁnal standardized problem was devised by Donald Knuth (1964) and illustrates how
inﬁnite state spaces can arise. Knuth conjectured that starting with the number 4, a sequence
