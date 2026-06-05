---
chunk_id: "book-ca4fca8dd8-chunk-0315"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 315
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 6.1
Game Theory
193
6.1.1 Two-player zero-sum games
The games most commonly studied within AI (such as chess and Go) are what game theorists
call deterministic, two-player, turn-taking, perfect information, zero-sum games. “Perfect
Perfect information
Zero-sum games
information” is a synonym for “fully observable,”1 and “zero-sum” means that what is good
for one player is just as bad for the other: there is no “win-win” outcome. For games we often
use the term move as a synonym for “action” and position as a synonym for “state.”
Move
Position
We will call our two players MAX and MIN, for reasons that will soon become obvious.
MAX moves ﬁrst, and then the players take turns moving until the game is over. At the end
of the game, points are awarded to the winning player and penalties are given to the loser. A
game can be formally deﬁned with the following elements:
• S0: The initial state, which speciﬁes how the game is set up at the start.
• TO-MOVE(s): The player whose turn it is to move in state s.
• ACTIONS(s): The set of legal moves in state s.
• RESULT(s,a): The transition model, which deﬁnes the state resulting from taking ac-
Transition model
tion a in state s.
• IS-TERMINAL(s): A terminal test, which is true when the game is over and false
Terminal test
otherwise. States where the game has ended are called terminal states.
Terminal state
• UTILITY(s, p): A utility function (also called an objective function or payoff function),
which deﬁnes the ﬁnal numeric value to player p when the game ends in terminal state s.
In chess, the outcome is a win, loss, or draw, with values 1, 0, or 1/2.2 Some games
have a wider range of possible outcomes—for example, the payoffs in backgammon
range from 0 to 192.
Much as in Chapter 3, the initial state, ACTIONS function, and RESULT function deﬁne the
state space graph—a graph where the vertices are states, the edges are moves and a state
State space graph
might be reached by multiple paths. As in Chapter 3, we can superimpose a search tree over
Search tree
part of that graph to determine what move to make. We deﬁne the complete game tree as a
Game tree
search tree that follows every sequence of moves all the way to a terminal state. The game
tree may be inﬁnite if the state space itself is unbounded or if the rules of the game allow for
inﬁnitely repeating positions.
Figure 6.1 shows part of the game tree for tic-tac-toe (noughts and crosses). From the
initial state, MAX has nine possible moves. Play alternates between MAX’s placing an X and
MIN’s placing an O until we reach leaf nodes corresponding to terminal states such that one
player has three squares in a row or all the squares are ﬁlled. The number on each leaf node
indicates the utility value of the terminal state from the point of view of MAX; high values are
good for MAX and bad for MIN (which is how the players get their names).
For tic-tac-toe the game tree is relatively small—fewer than 9!=362,880 terminal nodes
(with only 5,478 distinct states). But for chess there are over 1040 nodes, so the game tree is
best thought of as a theoretical construct that we cannot realize in the physical world.
1
Some authors make a distinction, using “imperfect information game” for one like poker where the players get
private information about their own hands that the other players do not have, and “partially observable game” to
mean one like StarCraft II where each player can see the nearby environment, but not the environment far away.
2
Chess is considered a “zero-sum” game, even though the sum of the outcomes for the two players is +1 for
each game, not zero. “Constant-sum” would have been a more accurate term, but zero-sum is traditional and
makes sense if you imagine each player is charged an entry fee of 1/2.
