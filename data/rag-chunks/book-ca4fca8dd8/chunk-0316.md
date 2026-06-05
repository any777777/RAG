---
chunk_id: "book-ca4fca8dd8-chunk-0316"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 316
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 194

194
Chapter 6
Adversarial Search and Games
X
X
X
X
X
X
X
X
X
X
X
O
O
X O
O
X O
X O
X
. . .
. . .
. . .
. . .
. . .
. . .
. . .
X
X
–1
 0
+1
X
X
X
X
O
X
X
O
X
X
O
O
O
X
X
X
O
O
O
O O X
X
MAX (X)
MIN (O)
MAX (X)
MIN (O)
TERMINAL
Utility
Figure 6.1 A (partial) game tree for the game of tic-tac-toe. The top node is the initial state,
and MAX moves ﬁrst, placing an X in an empty square. We show part of the tree, giving
alternating moves by MIN (O) and MAX (X), until we eventually reach terminal states, which
can be assigned utilities according to the rules of the game.
6.2 Optimal Decisions in Games
MAX wants to ﬁnd a sequence of actions leading to a win, but MIN has something to say
about it. This means that MAX’s strategy must be a conditional plan—a contingent strategy
specifying a response to each of MIN’s possible moves. In games that have a binary outcome
(win or lose), we could use AND–OR search (page 143) to generate the conditional plan. In
fact, for such games, the deﬁnition of a winning strategy for the game is identical to the
deﬁnition of a solution for a nondeterministic planning problem: in both cases the desirable
outcome must be guaranteed no matter what the “other side” does. For games with multiple
outcome scores, we need a slightly more general algorithm called minimax search.
Minimax search
Consider the trivial game in Figure 6.2. The possible moves for MAX at the root node
are labeled a1, a2, and a3. The possible replies to a1 for MIN are b1, b2, b3, and so on. This
particular game ends after one move each by MAX and MIN. (Note: In some games, the
word “move” means that both players have taken an action; therefore the word ply is used to
Ply
unambiguously mean one move by one player, bringing us one level deeper in the game tree.)
The utilities of the terminal states in this game range from 2 to 14.
Given a game tree, the optimal strategy can be determined by working out the minimax
value of each state in the tree, which we write as MINIMAX(s). The minimax value is the
Minimax value
utility (for MAX) of being in that state, assuming that both players play optimally from there
to the end of the game. The minimax value of a terminal state is just its utility. In a non-
terminal state, MAX prefers to move to a state of maximum value when it is MAX’s turn to

## Page 195
