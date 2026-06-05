---
chunk_id: "book-ca4fca8dd8-chunk-0150"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 150
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 89

Section 3.3
Search Algorithms
89
3.3 Search Algorithms
A search algorithm takes a search problem as input and returns a solution, or an indication of
Search algorithm
failure. In this chapter we consider algorithms that superimpose a search tree over the state-
space graph, forming various paths from the initial state, trying to ﬁnd a path that reaches a
goal state. Each node in the search tree corresponds to a state in the state space and the edges
Node
in the search tree correspond to actions. The root of the tree corresponds to the initial state of
the problem.
It is important to understand the distinction between the state space and the search tree.
The state space describes the (possibly inﬁnite) set of states in the world, and the actions
that allow transitions from one state to another. The search tree describes paths between
these states, reaching towards the goal. The search tree may have multiple paths to (and thus
multiple nodes for) any given state, but each node in the tree has a unique path back to the
root (as in all trees).
Figure 3.4 shows the ﬁrst few steps in ﬁnding a path from Arad to Bucharest. The root
node of the search tree is at the initial state, Arad. We can expand the node, by considering
Expand
Rimnicu Vilcea
Lugoj
Zerind
Sibiu
Arad
Fagaras
Oradea
Timisoara
Arad
Arad
Oradea
Arad
Arad
Fagaras
Oradea
Arad
Arad
Lugoj
Rimnicu Vilcea
Oradea
Zerind
Arad
Sibiu
Timisoara
Lugoj
Arad
Arad
Oradea
Rimnicu Vilcea
Zerind
Arad
Sibiu
Arad
Fagaras
Oradea
Timisoara
Figure 3.4 Three partial search trees for ﬁnding a route from Arad to Bucharest. Nodes
that have been expanded are lavender with bold letters; nodes on the frontier that have been
generated but not yet expanded are in green; the set of states corresponding to these two
types of nodes are said to have been reached. Nodes that could be generated next are shown
in faint dashed lines. Notice in the bottom tree there is a cycle from Arad to Sibiu to Arad;
that can’t be an optimal path, so search should not continue from there.

## Page 90
