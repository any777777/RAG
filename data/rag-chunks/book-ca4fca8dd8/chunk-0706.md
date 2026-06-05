---
chunk_id: "book-ca4fca8dd8-chunk-0706"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 706
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 424

424
Chapter 12
Quantifying Uncertainty
the known, frontier, and query variables. To use this insight, we manipulate the query formula
into a form in which the breezes are conditioned on all the other variables, and then we apply
conditional independence:
P(P1,3 |known,b)
= α ∑
unknown
P(P1,3,known,b,unknown)
(from Equation (12.23))
= α ∑
unknown
P(b|P1,3,known,unknown)P(P1,3,known,unknown) (product rule)
= α ∑
frontier ∑
other
P(b|known,P1,3,frontier,other)P(P1,3,known,frontier,other)
= α ∑
frontier ∑
other
P(b|known,P1,3,frontier)P(P1,3,known,frontier,other),
where the ﬁnal step uses conditional independence: b is independent of other given known,
P1,3, and frontier. Now, the ﬁrst term in this expression does not depend on the Other vari-
ables, so we can move the summation inward:
P(P1,3 |known,b)
= α ∑
frontier
P(b|known,P1,3,frontier) ∑
other
P(P1,3,known,frontier,other).
By independence, as in Equation (12.22), the term on the right can be factored, and then the
terms can be reordered:
P(P1,3 |known,b)
= α ∑
frontier
P(b|known,P1,3,frontier) ∑
other
P(P1,3)P(known)P(frontier)P(other)
= αP(known)P(P1,3) ∑
frontier
P(b|known,P1,3,frontier)P(frontier) ∑
other
P(other)
= α′ P(P1,3) ∑
frontier
P(b|known,P1,3,frontier)P(frontier),
where the last step folds P(known) into the normalizing constant and uses the fact that
∑other P(other) equals 1.
Now, there are just four terms in the summation over the frontier variables, P2,2 and P3,1.
The use of independence and conditional independence has completely eliminated the other
squares from consideration.
Notice that the probabilities in P(b|known,P1,3,frontier) are 1 when the breeze observa-
tions are consistent with the other variables and 0 otherwise. Thus, for each value of P1,3,
we sum over the logical models for the frontier variables that are consistent with the known
facts. (Compare with the enumeration over models in Figure 7.5 on page 233.) The models
and their associated prior probabilities—P(frontier)—are shown in Figure 12.6. We have
P(P1,3 |known,b) = α′ ⟨0.2(0.04+0.16+0.16), 0.8(0.04+0.16)⟩≈⟨0.31,0.69⟩.
That is, [1,3] (and [3,1] by symmetry) contains a pit with roughly 31% probability. A similar
calculation, which the reader might wish to perform, shows that [2,2] contains a pit with
roughly 86% probability. The wumpus agent should deﬁnitely avoid [2,2]! Note that our
logical agent from Chapter 7 did not know that [2,2] was worse than the other squares. Logic

## Page 425
