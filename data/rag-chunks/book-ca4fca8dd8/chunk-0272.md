---
chunk_id: "book-ca4fca8dd8-chunk-0272"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 272
confidence: "first-pass"
extraction_method: "structured-local"
---

168
Chapter 5
Constraint Satisfaction Problems
In addition to examining the types of variables that can appear in CSPs, it is useful to
look at the types of constraints. The simplest type is the unary constraint, which restricts
Unary constraint
the value of a single variable. For example, in the map-coloring problem it could be the case
that South Australians won’t tolerate the color green; we can express that with the unary
constraint ⟨(SA),SA ̸= green⟩. (The initial speciﬁcation of the domain of a variable can also
be seen as a unary constraint.)
A binary constraint relates two variables. For example, SA ̸= NSW is a binary constraint.
Binary constraint
A binary CSP is one with only unary and binary constraints; it can be represented as a
Binary CSP
constraint graph, as in Figure 5.1(b).
We can also deﬁne higher-order constraints. The ternary constraint Between(X,Y,Z), for
example, can be deﬁned as ⟨(X,Y,Z),X < Y < Z or X > Y > Z⟩.
A constraint involving an arbitrary number of variables is called a global constraint.
Global constraint
(The name is traditional but confusing because a global constraint need not involve all the
variables in a problem). One of the most common global constraints is Alldiff, which says
that all of the variables involved in the constraint must have different values. In Sudoku
problems (see Section 5.2.6), all variables in a row, column, or 3×3 box must satisfy an
Alldiff constraint.
Another example is provided by cryptarithmetic puzzles (Figure 5.2(a)). Each letter in
Cryptarithmetic
a cryptarithmetic puzzle represents a different digit. For the case in Figure 5.2(a), this would
be represented as the global constraint Alldiff(F,T,U,W,R,O). The addition constraints on
the four columns of the puzzle can be written as the following n-ary constraints:
O+O = R+10·C1
C1 +W +W = U +10·C2
C2 +T +T = O+10·C3
C3 = F ,
where C1, C2, and C3 are auxiliary variables representing the digit carried over into the tens,
hundreds, or thousands column. These constraints can be represented in a constraint hy-
pergraph, such as the one shown in Figure 5.2(b). A hypergraph consists of ordinary nodes
Constraint
hypergraph
(the circles in the ﬁgure) and hypernodes (the squares), which represent n-ary constraints—
constraints involving n variables.
Alternatively, as Exercise 5.NARY asks you to prove, every ﬁnite-domain constraint can
be reduced to a set of binary constraints if enough auxiliary variables are introduced. This
means that we could transform any CSP into one with only binary constraints—which cer-
tainly makes the life of the algorithm designer simpler. Another way to convert an n-ary CSP
to a binary one is the dual graph transformation: create a new graph in which there will be
Dual graph
one variable for each constraint in the original graph, and one binary constraint for each pair
of constraints in the original graph that share variables.
For example, consider a CSP with the variables X = {X,Y,Z}, each with the domain
{1,2,3,4,5}, and with the two constraints C1 : ⟨(X,Y,Z),X +Y = Z⟩and C2 : ⟨(X,Y),X +1 =
Y⟩. Then the dual graph would have the variables X = {C1,C2}, where the domain of the C1
variable in the dual graph is the set of {(xi,y j,zk)} tuples from the C1 constraint in the original
problem, and similarly the domain of C2 is the set of {(xi,yj)} tuples. The dual graph has the
binary constraint ⟨(C1,C2),R1⟩, where R1 is a new relation that deﬁnes the constraint between
C1 and C2; in this case it would be R1 = {((1,2,3),(1,2)),((2,3,5),(2,3))}.
