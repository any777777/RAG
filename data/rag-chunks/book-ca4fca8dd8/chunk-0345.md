---
chunk_id: "book-ca4fca8dd8-chunk-0345"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 345
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 6.5
Stochastic Games
213
CHANCE
MIN
MAX
2
2
3
3
1
1
4
4
2
3
1
4
.9
.1
.9
.1
2.1
1.3
20
20
30
30
1
1
400
400
20
30
1
400
.9
.1
.9
.1
21
40.9
a1
a2
a1
a2
Figure 6.14 An order-preserving transformation on leaf values changes the best move.
and general property of situations in which uncertainty is involved, and we discuss it further
in Chapter 15.
If the program knew in advance all the dice rolls that would occur for the rest of the game,
solving a game with dice would be just like solving a game without dice, which minimax does
in O(bm) time, where b is the branching factor and m is the maximum depth of the game tree.
Because expectiminimax is also considering all the possible dice-roll sequences, it will take
O(bmnm), where n is the number of distinct rolls.
Even if the search is limited to some small depth d, the extra cost compared with that of
minimax makes it unrealistic to consider looking ahead very far in most games of chance. In
backgammon n is 21 and b is usually around 20, but in some situations can be as high as 4000
for dice rolls that are doubles. We could probably only manage three ply of search.
Another way to think about the problem is this: the advantage of alpha–beta is that it
ignores future developments that just are not going to happen, given best play. Thus, it
concentrates on likely occurrences. But in a game where a throw of two dice precedes each
move, there are no likely sequences of moves; even the most likely move occurs only 2/36
of the time, because for the move to take place, the dice would ﬁrst have to come out the
right way to make it legal. This is a general problem whenever uncertainty enters the picture:
the possibilities are multiplied enormously, and forming detailed plans of action becomes
pointless because the world probably will not play along.
It may have occurred to you that something like alpha–beta pruning could be applied to
game trees with chance nodes. It turns out that it can. The analysis for MIN and MAX nodes
is unchanged, but we can also prune chance nodes, using a bit of ingenuity. Consider the
chance node C in Figure 6.13 and what happens to its value as we evaluate its children. Is it
possible to ﬁnd an upper bound on the value of C before we have looked at all its children?
(Recall that this is what alpha–beta needs in order to prune a node and its subtree.)
At ﬁrst sight, it might seem impossible because the value of C is the average of its chil-
dren’s values, and in order to compute the average of a set of numbers, we must look at all
the numbers. But if we put bounds on the possible values of the utility function, then we can
