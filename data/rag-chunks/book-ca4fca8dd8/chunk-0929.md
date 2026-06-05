---
chunk_id: "book-ca4fca8dd8-chunk-0929"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 929
confidence: "first-pass"
extraction_method: "structured-local"
---

562
Chapter 16
Making Complex Decisions
At
NextPiecet
CurrentPiecet
Rt
Filledt
At+1
NextPiecet+1
CurrentPiecet+1
Rt+1
Filledt+1
(a)
(b)
Next
Figure 16.5 (a) The game of Tetris. The T-shaped piece at the top center can be dropped
in any orientation and in any horizontal position. If a row is completed, that row disappears
and the rows above it move down, and the agent receives one point. The next piece (here, the
L-shaped piece at top right) becomes the current piece, and a new next piece appears, chosen
at random from the seven piece types. The game ends if the board ﬁlls up to the top. (b) The
DDN for the Tetris MDP.
is because the agent must maximize the (discounted) sum of all future rewards, and U(Xt+3)
represents the reward for all rewards from t +3 onwards. If a heuristic approximation to U is
available, it can be included in the MDP representation in this way and used in lieu of further
expansion. This approach is closely related to the use of bounded-depth search and heuristic
evaluation functions for games in Chapter 6.
Another interesting and well-studied MDP is the game of Tetris (Figure 16.5(a)). The
state variables for the game are the CurrentPiece, the NextPiece, and a bit-vector-valued
variable Filled with one bit for each of the 10×20 board locations. Thus, the state space has
7×7×2200 ≈1062 states. The DDN for Tetris is shown in Figure 16.5(b). Note that Filledt+1
is a deterministic function of Filledt and At. It turns out that every policy for Tetris is proper
(reaches a terminal state): eventually the board ﬁlls despite one’s best efforts to empty it.
16.2 Algorithms for MDPs
In this section, we present four different algorithms for solving MDPs. The ﬁrst three, value
iteration, policy iteration, and linear programming, generate exact solutions ofﬂine. The
fourth is a family of online approximate algorithms that includes Monte Carlo planning.
Monte Carlo
planning
16.2.1 Value Iteration
The Bellman equation (Equation (16.5)) is the basis of the value iteration algorithm for solv-
Value iteration
ing MDPs. If there are n possible states, then there are n Bellman equations, one for each

## Page 563
