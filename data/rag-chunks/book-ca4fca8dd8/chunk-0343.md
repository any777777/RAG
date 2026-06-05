---
chunk_id: "book-ca4fca8dd8-chunk-0343"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 343
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 211

Section 6.5
Stochastic Games
211
1
2
3
4
5
6
7
8
9
10
11
12
24
23
22
21
20
19
18
17
16
15
14
13
0
25
Figure 6.12 A typical backgammon position. The goal of the game is to move all one’s
pieces off the board. Black moves clockwise toward 25, and White moves counterclockwise
toward 0. A piece can move to any position unless multiple opponent pieces are there; if there
is one opponent, it is captured and must start over. In the position shown, Black has rolled
6–5 and must choose among four legal moves: (5–11,5–10), (5–11,19–24), (5–10,10–16),
and (5–11,11–16), where the notation (5–11,11–16) means move one piece from position 5
to 11, and then move a piece from 11 to 16.
At this point Black knows what moves can be made, but does not know what White is
going to roll and thus does not know what White’s legal moves will be. That means Black
cannot construct a standard game tree of the sort we saw in chess and tic-tac-toe. A game
tree in backgammon must include chance nodes in addition to MAX and MIN nodes. Chance
Chance nodes
nodes are shown as circles in Figure 6.13. The branches leading from each chance node
denote the possible dice rolls; each branch is labeled with the roll and its probability. There
are 36 ways to roll two dice, each equally likely; but because a 6–5 is the same as a 5–6, there
are only 21 distinct rolls. The six doubles (1–1 through 6–6) each have a probability of 1/36,
so we say P(1–1) = 1/36. The other 15 distinct rolls each have a 1/18 probability.
The next step is to understand how to make correct decisions. Obviously, we still want to
pick the move that leads to the best position. However, positions do not have deﬁnite minimax
values. Instead, we can only calculate the expected value of a position: the average over all
Expected value
possible outcomes of the chance nodes.
This leads us to the expectiminimax value for games with chance nodes, a generalization
Expectiminimax
value
of the minimax value for deterministic games. Terminal nodes and MAX and MIN nodes work
exactly the same way as before (with the caveat that the legal moves for MAX and MIN will
depend on the outcome of the dice roll in the previous chance node). For chance nodes we

## Page 212
