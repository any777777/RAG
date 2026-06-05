---
chunk_id: "book-ca4fca8dd8-chunk-0300"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 300
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 5.5
The Structure of Problems
185
Q
NT
WA
SA
V
NSW
T
Q
NT
WA
V
NSW
T
(a)
(b)
Figure 5.12 (a) The original constraint graph from Figure 5.1. (b) After the removal of SA,
the constraint graph becomes a forest of two trees.
given above and thus solve the whole problem. Of course, in the general case (as opposed to
map coloring), the value chosen for SA could be the wrong one, so we would need to try each
possible value. The general algorithm is as follows:
1. Choose a subset S of the CSP’s variables such that the constraint graph becomes a tree
after removal of S. S is called a cycle cutset.
Cycle cutset
2. For each possible assignment to the variables in S that satisﬁes all constraints on S,
(a) remove from the domains of the remaining variables any values that are inconsis-
tent with the assignment for S, and
(b) if the remaining CSP has a solution, return it together with the assignment for S.
If the cycle cutset has size c, then the total run time is O(dc ·(n−c)d2): we have to try each of
the dc combinations of values for the variables in S, and for each combination we must solve
a tree problem of size n−c. If the graph is “nearly a tree,” then c will be small and the savings
over straight backtracking will be huge—for our 100-Boolean-variable example, if we could
ﬁnd a cutset of size c=20, this would get us down from the lifetime of the Universe to a few
minutes. In the worst case, however, c can be as large as (n−2). Finding the smallest cycle
cutset is NP-hard, but several efﬁcient approximation algorithms are known. The overall
algorithmic approach is called cutset conditioning; it comes up again in Chapter 13, where
Cutset conditioning
it is used for reasoning about probabilities.
5.5.2 Tree decomposition
The second way to reduce a constraint graph to a tree is based on constructing a tree decom-
position of the constraint graph: a transformation of the original graph into a tree where each
Tree decomposition
node in the tree consists of a set of variables, as in Figure 5.13. A tree decomposition must
satisfy these three requirements:
• Every variable in the original problem appears in at least one of the tree nodes.
• If two variables are connected by a constraint in the original problem, they must appear
together (along with the constraint) in at least one of the tree nodes.
• If a variable appears in two nodes in the tree, it must appear in every node along the
path connecting those nodes.

## Page 186
