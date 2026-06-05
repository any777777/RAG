---
chunk_id: "book-ca4fca8dd8-chunk-0317"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 317
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 6.2
Optimal Decisions in Games
195
MAX
A
B
C
D
3
12
8
2
4
6
14
5
2
3
2
2
3
a1
a2
a3
b1
b2
b3
c1
c2
c3
d1
d2
d3
MIN
Figure 6.2 A two-ply game tree. The △nodes are “MAX nodes,” in which it is MAX’s turn
to move, and the ▽nodes are “MIN nodes.” The terminal nodes show the utility values for
MAX; the other nodes are labeled with their minimax values. MAX’s best move at the root is
a1, because it leads to the state with the highest minimax value, and MIN’s best reply is b1,
because it leads to the state with the lowest minimax value.
move, and MIN prefers a state of minimum value (that is, minimum value for MAX and thus
maximum value for MIN). So we have:
MINIMAX(s) =



UTILITY(s, MAX)
if IS-TERMINAL(s)
maxa∈Actions(s) MINIMAX(RESULT(s,a))
if TO-MOVE(s)= MAX
mina∈Actions(s) MINIMAX(RESULT(s,a))
if TO-MOVE(s)= MIN
Let us apply these deﬁnitions to the game tree in Figure 6.2. The terminal nodes on the bottom
level get their utility values from the game’s UTILITY function. The ﬁrst MIN node, labeled
B, has three successor states with values 3, 12, and 8, so its minimax value is 3. Similarly,
the other two MIN nodes have minimax value 2. The root node is a MAX node; its successor
states have minimax values 3, 2, and 2; so it has a minimax value of 3. We can also identify
the minimax decision at the root: action a1 is the optimal choice for MAX because it leads to
Minimax decision
the state with the highest minimax value.
This deﬁnition of optimal play for MAX assumes that MIN also plays optimally. What if
MIN does not play optimally? Then MAX will do at least as well as against an optimal player,
possibly better. However, that does not mean that it is always best to play the minimax optimal
move when facing a suboptimal opponent. Consider a situation where optimal play by both
sides will lead to a draw, but there is one risky move for MAX that leads to a state in which
there are 10 possible response moves by MIN that all seem reasonable, but 9 of them are a
loss for MIN and one is a loss for MAX. If MAX believes that MIN does not have sufﬁcient
computational power to discover the optimal move, MAX might want to try the risky move,
on the grounds that a 9/10 chance of a win is better than a certain draw.
6.2.1 The minimax search algorithm
Now that we can compute MINIMAX(s), we can turn that into a search algorithm that ﬁnds
the best move for MAX by trying all actions and choosing the one whose resulting state has
the highest MINIMAX value. Figure 6.3 shows the algorithm. It is a recursive algorithm
that proceeds all the way down to the leaves of the tree and then backs up the minimax
values through the tree as the recursion unwinds. For example, in Figure 6.2, the algorithm
