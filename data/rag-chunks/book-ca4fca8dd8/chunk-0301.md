---
chunk_id: "book-ca4fca8dd8-chunk-0301"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 301
confidence: "first-pass"
extraction_method: "structured-local"
---

186
Chapter 5
Constraint Satisfaction Problems
NT
WA
SA
Q
NT
SA
Q
SA
NSW
SA
V
NSW
T
Figure 5.13 A tree decomposition of the constraint graph in Figure 5.12(a).
The ﬁrst two conditions ensure that all the variables and constraints are represented in the
tree decomposition. The third condition seems rather technical, but allows us to say that
any variable from the original problem must have the same value wherever it appears: the
constraints in the tree say that a variable in one node of the tree must have the same value as
the corresponding variable in the adjacent node in the tree. For example, SA appears in all
four of the connected nodes in Figure 5.13, so each edge in the tree decomposition therefore
includes the constraint that the value of SA in one node must be the same as the value of SA
in the next. You can verify from Figure 5.12 that this decomposition makes sense.
Once we have a tree-structured graph, we can apply TREE-CSP-SOLVER to get a solution
in O(nd2) time, where n is the number of tree nodes and d is the size of the largest domain.
But note that in the tree, a domain is a set of tuples of values, not just individual values.
For example, the top left node in Figure 5.13 represents, at the level of the original prob-
lem, a subproblem with variables {WA,NT,SA}, domain {red,green,blue}, and constraints
WA ̸= NT,SA ̸= NT,WA ̸= SA. At the level of the tree, the node represents a single vari-
able, which we can call SANTWA, whose value must be a three-tuple of colors, such as
(red,green,blue), but not (red,red,blue), because that would violate the constraint SA ̸= NT
from the original problem. We can then move from that node to the adjacent one, with the
variable we can call SANTQ, and ﬁnd that there is only one tuple, (red,green,blue), that is
consistent with the choice for SANTWA. The exact same process is repeated for the next two
nodes, and independently we can make any choice for T.
We can solve any tree decomposition problem in O(nd2) time with TREE-CSP-SOLVER,
which will be efﬁcient as long as d remains small. Going back to our example with 100
Boolean variables, if each node has 10 variables, then d =210 and we should be able to solve
the problem in seconds. But if there is a node with 30 variables, it would take centuries.
A given graph admits many tree decompositions; in choosing a decomposition, the aim
is to make the subproblems as small as possible. (Putting all the variables into one node is
technically a tree, but is not helpful.) The tree width of a tree decomposition of a graph is
Tree width
