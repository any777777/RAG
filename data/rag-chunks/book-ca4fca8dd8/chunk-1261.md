---
chunk_id: "book-ca4fca8dd8-chunk-1261"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1261
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 20.5
Inductive Logic Programming
765
an inefﬁcient search) without additional controls. A number of approaches to taming the
search have been tried in implemented ILP systems:
1. Redundant choices can be eliminated—for example, by generating only the most spe-
ciﬁc hypotheses possible and by requiring that all the hypothesized clauses be consistent
with each other, and with the observations. This last criterion would rule out the clause
¬Parent(z,y)∨Grandparent(George,y), listed before.
2. The proof strategy can be restricted. For example, we saw in Chapter 9 that linear
resolution is a complete, restricted strategy. Linear resolution produces proof trees that
have a linear branching structure—the whole tree follows one line, with only single
clauses branching off that line (as in Figure 20.13).
3. The representation language can be restricted, for example by eliminating function sym-
bols or by allowing only Horn clauses. For instance, PROGOL operates with Horn
clauses using inverse entailment. The idea is to change the entailment constraint
Inverse entailment
Background ∧Hypothesis∧Descriptions |= Classiﬁcations
to the logically equivalent form
Background ∧Descriptions∧¬Classiﬁcations |= ¬Hypothesis.
From this, one can use a process similar to the normal Prolog Horn-clause deduction,
with negation-as-failure to derive Hypothesis. Because it is restricted to Horn clauses,
this is an incomplete method, but it can be more efﬁcient than full resolution. It is also
possible to apply complete inference with inverse entailment (Inoue, 2001).
4. Inference can be done with model checking rather than theorem proving. The PROGOL
system (Muggleton, 1995) uses a form of model checking to limit the search. That
is, like answer set programming, it generates possible values for logical variables, and
checks for consistency.
5. Inference can be done with ground propositional clauses rather than in ﬁrst-order logic.
The LINUS system (Lavrauc and Duzeroski, 1994) works by translating ﬁrst-order the-
ories into propositional logic, solving them with a propositional learning system, and
then translating back. Working with propositional formulas can be more efﬁcient on
some problems, as we saw with SATPLAN in Chapter 10.
20.5.4 Making discoveries with inductive logic programming
An inverse resolution procedure that inverts a complete resolution strategy is, in principle,
a complete algorithm for learning ﬁrst-order theories. That is, if some unknown Hypothesis
generates a set of examples, then an inverse resolution procedure can generate Hypothesis
from the examples. This observation suggests an interesting possibility: Suppose that the
available examples include a variety of trajectories of falling bodies. Would an inverse reso-
lution program be theoretically capable of inferring the law of gravity? The answer is clearly
yes, because the law of gravity allows one to explain the examples, given suitable background
mathematics. Similarly, one can imagine that electromagnetism, quantum mechanics, and the
theory of relativity are also within the scope of ILP programs. Of course, they are also within
the scope of a monkey with a typewriter; we still need better heuristics and new ways to
structure the search space.
