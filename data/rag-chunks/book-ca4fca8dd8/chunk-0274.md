---
chunk_id: "book-ca4fca8dd8-chunk-0274"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 274
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 5.2
Constraint Propagation: Inference in CSPs
169
T
W
O
F O
U
R
T
W
O
F
T
U
W
R
O
C3
C2
C1
Figure 5.2 (a) A cryptarithmetic problem. Each letter stands for a distinct digit; the aim is
to ﬁnd a substitution of digits for letters such that the resulting sum is arithmetically correct,
with the added restriction that no leading zeroes are allowed. (b) The constraint hypergraph
for the cryptarithmetic problem, showing the Alldiff constraint (square box at the top) as well
as the column addition constraints (four square boxes in the middle). The variables C1, C2,
and C3 represent the carry digits for the three columns from right to left.
There are however two reasons why we might prefer a global constraint such as Alldiff
rather than a set of binary constraints. First, it is easier and less error-prone to write the
problem description using Alldiff. Second, it is possible to design special-purpose inference
algorithms for global constraints that are more efﬁcient than operating with primitive con-
straints. We describe these inference algorithms in Section 5.2.5.
The constraints we have described so far have all been absolute constraints, violation of
which rules out a potential solution. Many real-world CSPs include preference constraints
Preference
constraints
indicating which solutions are preferred. For example, in a university class-scheduling prob-
lem there are absolute constraints that no professor can teach two classes at the same time.
But we also may allow preference constraints: Prof. R might prefer teaching in the morning,
whereas Prof. N prefers teaching in the afternoon. A schedule that has Prof. R teaching at
2 p.m. would still be an allowable solution (unless Prof. R happens to be the department chair)
but would not be an optimal one.
Preference constraints can often be encoded as costs on individual variable assignments—
for example, assigning an afternoon slot for Prof. R costs 2 points against the overall objective
function, whereas a morning slot costs 1. With this formulation, CSPs with preferences can be
solved with optimization search methods, either path-based or local. We call such a problem
a constrained optimization problem, or COP. Linear programs are one class of COPs.
Constrained
optimization
problem
5.2 Constraint Propagation: Inference in CSPs
An atomic state-space search algorithm makes progress in only one way: by expanding a
node to visit the successors. A CSP algorithm has choices. It can generate successors by
choosing a new variable assignment, or it can do a speciﬁc type of inference called constraint
propagation: using the constraints to reduce the number of legal values for a variable, which
Constraint
propagation
