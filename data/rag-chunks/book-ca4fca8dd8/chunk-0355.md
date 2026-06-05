---
chunk_id: "book-ca4fca8dd8-chunk-0355"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 355
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 6.7
Limitations of Game Search Algorithms
219
MAX
99
100
99
1000
1000
1000
100
101
102
100
MIN
Figure 6.16 A two-ply game tree for which heuristic minimax may make an error.
6.7 Limitations of Game Search Algorithms
Because calculating optimal decisions in complex games is intractable, all algorithms must
make some assumptions and approximations. Alpha–beta search uses the heuristic evaluation
function as an approximation, and Monte Carlo search computes an approximate average
over a random selection of playouts. The choice of which algorithm to use depends in part
on the features of each game: when the branching factor is high or it is difﬁcult to deﬁne
an evaluation function, Monte Carlo search is preferred. But both algorithms suffer from
fundamental limitations.
One limitation of alpha–beta search is its vulnerability to errors in the heuristic function.
Figure 6.16 shows a two-ply game tree for which minimax suggests taking the right-hand
branch because 100 > 99. That is the correct move if the evaluations are all exactly accurate.
But suppose that the evaluation of each node has an error that is independent of other nodes
and is randomly distributed with a standard deviation of σ. Then the left-hand branch is
actually better 71% of the time when σ = 5, and 58% of the time when σ = 2 (because
one of the four right-hand leaves is likely to slip below 99 in these cases). If errors in the
evaluation function are not independent, then the chance of a mistake rises. It is difﬁcult to
compensate for this because we don’t have a good model of the dependencies between the
values of sibling nodes.
A second limitation of both alpha–beta and Monte Carlo is that they are designed to
calculate (bounds on) the values of legal moves. But sometimes there is one move that is
obviously best (for example when there is only one legal move), and in that case, there is no
point wasting computation time to ﬁgure out the value of the move—it is better to just make
the move. A better search algorithm would use the idea of the utility of a node expansion,
selecting node expansions of high utility—that is, ones that are likely to lead to the discovery
of a signiﬁcantly better move. If there are no node expansions whose utility is higher than
their cost (in terms of time), then the algorithm should stop searching and make a move. This
works not only for clear-favorite situations but also for the case of symmetrical moves, for
which no amount of search will show that one move is better than another.
This kind of reasoning about what computations to do is called metareasoning (reason-
Metareasoning
ing about reasoning). It applies not just to game playing but to any kind of reasoning at all.
All computations are done in the service of trying to reach better decisions, all have costs,
and all have some likelihood of resulting in a certain improvement in decision quality. Monte
