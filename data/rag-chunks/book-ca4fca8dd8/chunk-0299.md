---
chunk_id: "book-ca4fca8dd8-chunk-0299"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 299
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 184

184
Chapter 5
Constraint Satisfaction Problems
Figure 5.10 (a) The constraint graph of a tree-structured CSP. (b) A linear ordering of the
variables consistent with the tree with A as the root. This is known as a topological sort of
the variables.
function TREE-CSP-SOLVER(csp) returns a solution, or failure
inputs: csp, a CSP with components X, D, C
n←number of variables in X
assignment←an empty assignment
root←any variable in X
X ←TOPOLOGICALSORT(X,root)
for j = n down to 2 do
MAKE-ARC-CONSISTENT(PARENT(Xj), Xj)
if it cannot be made consistent then return failure
for i = 1 to n do
assignment[Xi]←any consistent value from Di
if there is no consistent value then return failure
return assignment
Figure 5.11 The TREE-CSP-SOLVER algorithm for solving tree-structured CSPs. If the
CSP has a solution, we will ﬁnd it in linear time; if not, we will detect a contradiction.
have to backtrack; we can move linearly through the variables. The complete algorithm is
shown in Figure 5.11.
Now that we have an efﬁcient algorithm for trees, we can consider whether more gen-
eral constraint graphs can be reduced to trees somehow. There are two ways to do this: by
removing nodes (Section 5.5.1) or by collapsing nodes together (Section 5.5.2).
5.5.1 Cutset conditioning
The ﬁrst way to reduce a constraint graph to a tree involves assigning values to some variables
so that the remaining variables form a tree. Consider the constraint graph for Australia, shown
again in Figure 5.12(a). Without South Australia, the graph would become a tree, as in (b).
Fortunately, we can delete South Australia (in the graph, not the country) by ﬁxing a value
for SA and deleting from the domains of the other variables any values that are inconsistent
with the value chosen for SA.
Now, any solution for the CSP after SA and its constraints are removed will be consistent
with the value chosen for SA. (This works for binary CSPs; the situation is more complicated
with higher-order constraints.) Therefore, we can solve the remaining tree with the algorithm

## Page 185
