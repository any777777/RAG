---
chunk_id: "book-ca4fca8dd8-chunk-0319"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 319
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 6.2
Optimal Decisions in Games
197
to move
A
B
C
A
X
(1, 2, 6)
(1, 2, 6)
(1, 2, 6)
(6, 1, 2)
(0, 5, 2)
(0, 5, 2)
(5, 4, 5)
(1, 2, 6)
(4, 2, 3)
(6, 1, 2)
(7, 4, 1)
(5, 1, 1)
(0, 5, 2)
(7, 7, 1)
(5, 4, 5)
Figure 6.4 The ﬁrst three ply of a game tree with three players (A, B, C). Each node is
labeled with values from the viewpoint of each player. The best move is marked at the root.
6.2.2 Optimal decisions in multiplayer games
Many popular games allow more than two players. Let us examine how to extend the minimax
idea to multiplayer games. This is straightforward from the technical viewpoint, but raises
some interesting new conceptual issues.
First, we need to replace the single value for each node with a vector of values. For
example, in a three-player game with players A, B, and C, a vector ⟨vA,vB,vC⟩is associated
with each node. For terminal states, this vector gives the utility of the state from each player’s
viewpoint. (In two-player, zero-sum games, the two-element vector can be reduced to a single
value because the values are always opposite.) The simplest way to implement this is to have
the UTILITY function return a vector of utilities.
Now we have to consider nonterminal states. Consider the node marked X in the game
tree shown in Figure 6.4. In that state, player C chooses what to do. The two choices lead to
terminal states with utility vectors ⟨vA =1,vB =2,vC =6⟩and ⟨vA =4,vB =2,vC =3⟩. Since
6 is bigger than 3, C should choose the ﬁrst move. This means that if state X is reached,
subsequent play will lead to a terminal state with utilities ⟨vA =1,vB =2,vC =6⟩. Hence, the
backed-up value of X is this vector. In general, the backed-up value of a node n is the utility
vector of the successor state with the highest value for the player choosing at n.
Anyone who plays multiplayer games, such as Diplomacy or Settlers of Catan, quickly
becomes aware that much more is going on than in two-player games. Multiplayer games
usually involve alliances, whether formal or informal, among the players. Alliances are made
Alliance
and broken as the game proceeds. How are we to understand such behavior? Are alliances a
natural consequence of optimal strategies for each player in a multiplayer game? It turns out
that they can be.
For example, suppose A and B are in weak positions and C is in a stronger position. Then
it is often optimal for both A and B to attack C rather than each other, lest C destroy each of
them individually. In this way, collaboration emerges from purely selﬁsh behavior. Of course,
as soon as C weakens under the joint onslaught, the alliance loses its value, and either A or B
could violate the agreement.
In some cases, explicit alliances merely make concrete what would have happened any-
way. In other cases, a social stigma attaches to breaking an alliance, so players must balance
