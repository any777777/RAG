---
chunk_id: "book-ca4fca8dd8-chunk-0190"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 190
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 3.6
Heuristic Functions
115
f2=10
f=9=4+5
f2=16
f=9=8+1
f2=14
f=9=7+2
f2=12
f=8=6+2
f2=14
f=8=7+1
f2=10
f=10=4+6
4
1
1
1
4
E
F
C
A
2
B
D
Goal
Start
66
Figure 3.24 Bidirectional search maintains two frontiers: on the left, nodes A and B are
successors of Start; on the right, node F is an inverse successor of Goal. Each node is labeled
with f =g + h values and the f2 = max(2g,g + h) value. (The g values are the sum of the
action costs as shown on each arrow; the h values are arbitrary and cannot be derived from
anything in the ﬁgure.) The optimal solution, Start-A-F-Goal, has cost C∗=4 + 2 + 4=10,
so that means that a meet-in-the-middle bidirectional algorithm should not expand any node
with g > C∗
2 =5; and indeed the next node to be expanded would be A or F (each with g=4),
leading us to an optimal solution. If we expanded the node with lowest f cost ﬁrst, then B
and C would come next, and D and E would be tied with A, but they all have g > C∗
2 and thus
are never expanded when f2 is the evaluation function.
one of them and take the minimum. But it can work to sample a few nodes from the frontier.
In certain speciﬁc problem domains it is possible to summarize the frontier—for example, in
a grid search problem, we can incrementally compute a bounding box of the frontier, and use
as a heuristic the distance to the bounding box.
Bidirectional search is sometimes more efﬁcient than unidirectional search, sometimes
not. In general, if we have a very good heuristic, then A∗search produces search contours
that are focused on the goal, and adding bidirectional search does not help much. With an
average heuristic, bidirectional search that meets in the middle tends to expand fewer nodes
and is preferred. In the worst case of a poor heuristic, the search is no longer focused on the
goal, and bidirectional search has the same asymptotic complexity as A∗. Bidirectional search
with the f2 evaluation function and an admissible heuristic h is complete and optimal.
3.6 Heuristic Functions
In this section, we look at how the accuracy of a heuristic affects search performance, and also
consider how heuristics can be invented. As our main example we’ll return to the 8-puzzle. As
mentioned in Section 3.2, the object of the puzzle is to slide the tiles horizontally or vertically
into the empty space until the conﬁguration matches the goal conﬁguration (Figure 3.25).
There are 9!/2=181,400 reachable states in an 8-puzzle, so a search could easily keep
them all in memory. But for the 15-puzzle, there are 16!/2 states—over 10 trillion—so to
search that space we will need the help of a good admissible heuristic function. There is a
long history of such heuristics for the 15-puzzle; here are two commonly used candidates:
• h1 = the number of misplaced tiles (blank not included). For Figure 3.25, all eight tiles
are out of position, so the start state has h1 = 8. h1 is an admissible heuristic because
any tile that is out of place will require at least one move to get it to the right place.
