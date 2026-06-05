---
chunk_id: "book-ca4fca8dd8-chunk-0159"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 159
confidence: "first-pass"
extraction_method: "structured-local"
---

94
Chapter 3
Solving Problems by Searching
the number of edges (distinct state/action pairs). This is appropriate when the graph is an
explicit data structure, such as the map of Romania. But in many AI problems, the graph is
represented only implicitly by the initial state, actions, and transition model. For an implicit
state space, complexity can be measured in terms of d, the depth or number of actions in
Depth
an optimal solution; m, the maximum number of actions in any path; and b, the branching
factor or number of successors of a node that need to be considered.
Branching factor
3.4 Uninformed Search Strategies
An uninformed search algorithm is given no clue about how close a state is to the goal(s).
For example, consider our agent in Arad with the goal of reaching Bucharest. An uninformed
agent with no knowledge of Romanian geography has no clue whether going to Zerind or
Sibiu is a better ﬁrst step. In contrast, an informed agent (Section 3.5) who knows the location
of each city knows that Sibiu is much closer to Bucharest and thus more likely to be on the
shortest path.
3.4.1 Breadth-ﬁrst search
When all actions have the same cost, an appropriate strategy is breadth-ﬁrst search, in which
Breadth-ﬁrst search
the root node is expanded ﬁrst, then all the successors of the root node are expanded next,
then their successors, and so on. This is a systematic search strategy that is therefore com-
plete even on inﬁnite state spaces. We could implement breadth-ﬁrst search as a call to
BEST-FIRST-SEARCH where the evaluation function f(n) is the depth of the node—that is,
the number of actions it takes to reach the node.
However, we can get additional efﬁciency with a couple of tricks. A ﬁrst-in-ﬁrst-out
queue will be faster than a priority queue, and will give us the correct order of nodes: new
nodes (which are always deeper than their parents) go to the back of the queue, and old nodes,
which are shallower than the new nodes, get expanded ﬁrst. In addition, reached can be a set
of states rather than a mapping from states to nodes, because once we’ve reached a state,
we can never ﬁnd a better path to the state. That also means we can do an early goal test,
Early goal test
checking whether a node is a solution as soon as it is generated, rather than the late goal test
Late goal test
that best-ﬁrst search uses, waiting until a node is popped off the queue. Figure 3.8 shows the
progress of a breadth-ﬁrst search on a binary tree, and Figure 3.9 shows the algorithm with
the early-goal efﬁciency enhancements.
Breadth-ﬁrst search always ﬁnds a solution with a minimal number of actions, because
when it is generating nodes at depth d, it has already generated all the nodes at depth d −1,
so if one of them were a solution, it would have been found. That means it is cost-optimal
A
B
C
D
E
F
G
A
B
C
D
E
F
G
A
B
C
D
E
F
G
A
B
C
D
E
F
G
Figure 3.8 Breadth-ﬁrst search on a simple binary tree. At each stage, the node to be ex-
panded next is indicated by the triangular marker.
