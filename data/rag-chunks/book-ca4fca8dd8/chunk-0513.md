---
chunk_id: "book-ca4fca8dd8-chunk-0513"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 513
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 314

314
Chapter 9
Inference in First-Order Logic
(a)
(b)
A
B
C
A1
J4
Figure 9.8 (a) Finding a path from A to C can lead Prolog into an inﬁnite loop. (b) A graph
in which each node is connected to two random successors in the next layer. Finding a path
from A1 to J4 requires 877 inferences.
path(a,c)
fail
{
}
/
Y b
{ }
link(a,c)
path(a,Y)
link(a,Y)
link(b,c)
path(a,c)
path(a,Y)
link(Y,c)
path(a,Y’)
link(Y’,Y)
(a)
(b)
Figure 9.9 (a) Proof that a path exists from A to C. (b) Inﬁnite proof tree generated when
the clauses are in the “wrong” order.
path(X,Z) :- link(X,Z).
path(X,Z) :- path(X,Y), link(Y,Z).
A simple three-node graph, described by the facts link(a,b) and link(b,c), is shown in
Figure 9.8(a). With this program, the query path(a,c) generates the proof tree shown in
Figure 9.9(a). On the other hand, if we put the two clauses in the order
path(X,Z) :- path(X,Y), link(Y,Z).
path(X,Z) :- link(X,Z).
then Prolog follows the inﬁnite path shown in Figure 9.9(b). Prolog is therefore incomplete as
a theorem prover for deﬁnite clauses—even for Datalog programs, as this example shows—
because, for some knowledge bases, it fails to prove sentences that are entailed. Notice
that forward chaining does not suffer from this problem: once path(a,b), path(b,c), and
path(a,c) are inferred, forward chaining halts.
Depth-ﬁrst backward chaining also has problems with redundant computations. For ex-
ample, when ﬁnding a path from A1 to J4 in Figure 9.8(b), Prolog performs 877 inferences,
most of which involve ﬁnding all possible paths to nodes from which the goal is unreachable.
This is similar to the repeated-state problem discussed in Chapter 3. The total amount of

## Page 315
