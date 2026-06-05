---
chunk_id: "book-ca4fca8dd8-chunk-0324"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 324
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 6.2
Optimal Decisions in Games
201
third successor of D had been generated ﬁrst, with value 2, we would have been able to prune
the other two successors. This suggests that it might be worthwhile to try to ﬁrst examine the
successors that are likely to be best.
If this could be done perfectly, alpha–beta would need to examine only O(bm/2) nodes to
pick the best move, instead of O(bm) for minimax. This means that the effective branching
factor becomes
√
b instead of b—for chess, about 6 instead of 35. Put another way, alpha–
beta with perfect move ordering can solve a tree roughly twice as deep as minimax in the
same amount of time. With random move ordering, the total number of nodes examined
will be roughly O(b3m/4) for moderate b. Now, obviously we cannot achieve perfect move
ordering—in that case the ordering function could be used to play a perfect game! But we
can often get fairly close. For chess, a fairly simple ordering function (such as trying captures
ﬁrst, then threats, then forward moves, and then backward moves) gets you to within about a
factor of 2 of the best-case O(bm/2) result.
Adding dynamic move-ordering schemes, such as trying ﬁrst the moves that were found
to be best in the past, brings us quite close to the theoretical limit. The past could be the
previous move—often the same threats remain—or it could come from previous exploration
of the current move through a process of iterative deepening (see page 98). First, search one
ply deep and record the ranking of moves based on their evaluations. Then search one ply
deeper, using the previous ranking to inform move ordering; and so on. The increased search
time from iterative deepening can be more than made up from better move ordering. The best
moves are known as killer moves, and to try them ﬁrst is called the killer move heuristic.
Killer moves
In Section 3.3.3, we noted that redundant paths to repeated states can cause an exponential
increase in search cost, and that keeping a table of previously reached states can address this
problem. In game tree search, repeated states can occur because of transpositions—different
Transposition
permutations of the move sequence that end up in the same position, and the problem can be
addressed with a transposition table that caches the heuristic value of states.
Transposition table
For example, suppose White has a move w1 that can be answered by Black with b1 and
an unrelated move w2 on the other side of the board that can be answered by b2, and that we
search the sequence of moves [w1,b1,w2,b2]; let’s call the resulting state s. After exploring a
large subtree below s, we ﬁnd its backed-up value, which we store in the transposition table.
When we later search the sequence of moves [w2,b2,w1,b1], we end up in s again, and we
can look up the value instead of repeating the search. In chess, use of transposition tables is
very effective, allowing us to double the reachable search depth in the same amount of time.
Even with alpha–beta pruning and clever move ordering, minimax won’t work for games
like chess and Go, because there are still too many states to explore in the time available. In
the very ﬁrst paper on computer game-playing, Programming a Computer for Playing Chess
(Shannon, 1950), Claude Shannon recognized this problem and proposed two strategies: a
Type A strategy considers all possible moves to a certain depth in the search tree, and then
Type A strategy
uses a heuristic evaluation function to estimate the utility of states at that depth. It explores
a wide but shallow portion of the tree. A Type B strategy ignores moves that look bad, and
Type B strategy
follows promising lines “as far as possible.” It explores a deep but narrow portion of the tree.
Historically, most chess programs have been Type A (which we cover in the next section),
whereas Go programs are more often Type B (covered in Section 6.4), because the branching
factor is much higher in Go. More recently, Type B programs have shown world-champion-
level play across a variety of games, including chess (Silver et al., 2018).
