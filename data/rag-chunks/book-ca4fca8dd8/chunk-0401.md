---
chunk_id: "book-ca4fca8dd8-chunk-0401"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 401
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 7.5
Propositional Theorem Proving
247
¬P2,1 
B1,1
¬B1,1 
P1,2 
P2,1
¬P1,2 
B1,1
¬B1,1
P1,2
¬P2,1
¬P1,2
P1,2 
P2,1 
¬P2,1
¬B1,1 
P2,1 
B1,1
P1,2 
P2,1 
¬P1,2
¬B1,1 
P1,2 
B1,1
^
^
^
^
^
^
^
^
^
^
^
^
Figure 7.14 Partial application of PL-RESOLUTION to a simple inference in the wumpus
world to prove the query ¬P1,2. Each of the leftmost four clauses in the top row is paired with
each of the other three, and the resolution rule is applied to yield the clauses on the bottom
row. We see that the third and fourth clauses on the top row combine to yield the clause ¬P1,2,
which is then resolved with P1,2 to yield the empty clause, meaning that the query is proven.
This theorem is proved by demonstrating its contrapositive: if the closure RC(S) does not
contain the empty clause, then S is satisﬁable. In fact, we can construct a model for S with
suitable truth values for P1,...,Pk. The construction procedure is as follows:
For i from 1 to k,
– If a clause in RC(S) contains the literal ¬Pi and all its other literals are false under
the assignment chosen for P1,...,Pi−1, then assign false to Pi.
– Otherwise, assign true to Pi.
This assignment to P1,...,Pk is a model of S. To see this, assume the opposite—that, at some
stage i in the sequence, assigning symbol Pi causes some clause C to become false. For this
to happen, it must be the case that all the other literals in C must already have been falsiﬁed
by assignments to P1,...,Pi−1. Thus, C must now look like either (false∨false∨···false∨Pi)
or like (false∨false∨···false∨¬Pi). If just one of these two is in RC(S), then the algorithm
will assign the appropriate truth value to Pi to make C true, so C can only be falsiﬁed if both
of these clauses are in RC(S).
Now, since RC(S) is closed under resolution, it will contain the resolvent of these two
clauses, and that resolvent will have all of its literals already falsiﬁed by the assignments to
P1,...,Pi−1. This contradicts our assumption that the ﬁrst falsiﬁed clause appears at stage
i. Hence, we have proved that the construction never falsiﬁes a clause in RC(S); that is, it
produces a model of RC(S). Finally, because S is contained in RC(S), any model of RC(S) is
a model of S itself.
7.5.3 Horn clauses and deﬁnite clauses
The completeness of resolution makes it a very important inference method. In many practical
situations, however, the full power of resolution is not needed. Some real-world knowledge
bases satisfy certain restrictions on the form of sentences they contain, which enables them
to use a more restricted and efﬁcient inference algorithm.
One such restricted form is the deﬁnite clause, which is a disjunction of literals of which
Deﬁnite clause
exactly one is positive. For example, the clause (¬L1,1 ∨¬Breeze∨B1,1) is a deﬁnite clause,
whereas (¬B1,1 ∨P1,2 ∨P2,1) is not, because it has two positive clauses.
Slightly more general is the Horn clause, which is a disjunction of literals of which at
Horn clause
