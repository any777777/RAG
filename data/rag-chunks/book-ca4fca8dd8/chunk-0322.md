---
chunk_id: "book-ca4fca8dd8-chunk-0322"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 322
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 199

Section 6.2
Optimal Decisions in Games
199
(a)
(b)
(c)
(d)
(e)
(f)
3
3
12
3
12
8
3
12
8
2
3
12
8
2
14
3
12
8
2
14
5
2
A
B
A
B
A
B
C
D
A
B
C
D
A
B
A
B
C
[– 
, +
]
[– 
, 3]
[3, +
]
[3, 3]
[– 
, 2]
[3, 3]
[3, 14]
[–
, 2]
[– 
, 14]
[3, 3]
[3, 3]
[2, 2]
[3, + 
]
[3, 3]
[– 
, 3]
[– 
, + 
]
[– 
, 2]
Figure 6.5 Stages in the calculation of the optimal decision for the game tree in Figure 6.2.
At each point, we show the range of possible values for each node. (a) The ﬁrst leaf below B
has the value 3. Hence, B, which is a MIN node, has a value of at most 3. (b) The second leaf
below B has a value of 12; MIN would avoid this move, so the value of B is still at most 3.
(c) The third leaf below B has a value of 8; we have seen all B’s successor states, so the value
of B is exactly 3. Now we can infer that the value of the root is at least 3, because MAX has
a choice worth 3 at the root. (d) The ﬁrst leaf below C has the value 2. Hence, C, which is
a MIN node, has a value of at most 2. But we know that B is worth 3, so MAX would never
choose C. Therefore, there is no point in looking at the other successor states of C. This is an
example of alpha–beta pruning. (e) The ﬁrst leaf below D has the value 14, so D is worth at
most 14. This is still higher than MAX’s best alternative (i.e., 3), so we need to keep exploring
D’s successor states. Notice also that we now have bounds on all of the successors of the root,
so the root’s value is also at most 14. (f) The second successor of D is worth 5, so again we
need to keep exploring. The third successor is worth 2, so now D is worth exactly 2. MAX’s
decision at the root is to move to B, giving a value of 3.
Alpha–beta search updates the values of α and β as it goes along and prunes the remaining
branches at a node (i.e., terminates the recursive call) as soon as the value of the current
node is known to be worse than the current α or β value for MAX or MIN, respectively. The
complete algorithm is given in Figure 6.7. Figure 6.5 traces the progress of the algorithm on
a game tree.
6.2.4 Move ordering
The effectiveness of alpha–beta pruning is highly dependent on the order in which the states
are examined. For example, in Figure 6.5(e) and (f), we could not prune any successors of D
at all because the worst successors (from the point of view of MIN) were generated ﬁrst. If the

## Page 200
