---
chunk_id: "book-ca4fca8dd8-chunk-0527"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 527
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 322

322
Chapter 9
Inference in First-Order Logic
Any set of sentences S is representable in clausal form
Assume S is unsatisfiable, and in clausal form
Some set S′ of ground instances is unsatisfiable
Resolution can find a contradiction in S′
There is a resolution proof for the contradiction in S′
Lifting lemma
Ground resolution
theorem
Herbrand’s theorem
Figure 9.12 Structure of a completeness proof for resolution.
For example, if S contains just the clause ¬P(x,F(x,A)) ∨¬Q(x,A) ∨R(x,B), then HS
is the following inﬁnite set of ground terms:
{A,B,F(A,A),F(A,B),F(B,A),F(B,B),F(A,F(A,A)),...}.
• Saturation: If S is a set of clauses and P is a set of ground terms, then P(S), the
Saturation
saturation of S with respect to P, is the set of all ground clauses obtained by applying
all possible consistent substitutions of ground terms in P for variables in S.
• Herbrand base: The saturation of a set S of clauses with respect to its Herbrand uni-
Herbrand base
verse is called the Herbrand base of S, written as HS(S). For example, if S contains
solely the clause given above, then HS(S) is the inﬁnite set of clauses
{¬P(A,F(A,A))∨¬Q(A,A)∨R(A,B),
¬P(B,F(B,A))∨¬Q(B,A)∨R(B,B),
¬P(F(A,A),F(F(A,A),A))∨¬Q(F(A,A),A)∨R(F(A,A),B),
¬P(F(A,B),F(F(A,B),A))∨¬Q(F(A,B),A)∨R(F(A,B),B),... }
These deﬁnitions allow us to state a form of Herbrand’s theorem (Herbrand, 1930):
Herbrand’s theorem
If a set S of clauses is unsatisﬁable, then there exists a ﬁnite subset of HS(S) that
is also unsatisﬁable.
Let S′ be this ﬁnite subset of ground sentences. Now, we can appeal to the ground resolution
theorem (page 246) to show that the resolution closure RC(S′) contains the empty clause.
That is, running propositional resolution to completion on S′ will derive a contradiction.
Now that we have established that there is always a resolution proof involving some ﬁnite
subset of the Herbrand base of S, the next step is to show that there is a resolution proof using
the clauses of S itself, which are not necessarily ground clauses. We start by considering a
single application of the resolution rule. Robinson stated this lemma:
Let C1 and C2 be two clauses with no shared variables, and let C′
1 and C′
2 be ground
instances of C1 and C2. If C′ is a resolvent of C′
1 and C′
2, then there exists a clause
C such that (1) C is a resolvent of C1 and C2 and (2) C′ is a ground instance of C.

## Page 323
