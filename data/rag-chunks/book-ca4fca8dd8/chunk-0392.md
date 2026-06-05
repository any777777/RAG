---
chunk_id: "book-ca4fca8dd8-chunk-0392"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 392
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 241

Section 7.5
Propositional Theorem Proving
241
(α∧β) ≡(β ∧α)
commutativity of ∧
(α∨β) ≡(β ∨α)
commutativity of ∨
((α∧β)∧γ) ≡(α∧(β ∧γ))
associativity of ∧
((α∨β)∨γ) ≡(α∨(β ∨γ))
associativity of ∨
¬(¬α) ≡α
double-negation elimination
(α ⇒β) ≡(¬β ⇒¬α)
contraposition
(α ⇒β) ≡(¬α∨β)
implication elimination
(α ⇔β) ≡((α ⇒β)∧(β ⇒α))
biconditional elimination
¬(α∧β) ≡(¬α∨¬β)
De Morgan
¬(α∨β) ≡(¬α∧¬β)
De Morgan
(α∧(β ∨γ)) ≡((α∧β)∨(α∧γ))
distributivity of ∧over ∨
(α∨(β ∧γ)) ≡((α∨β)∧(α∨γ))
distributivity of ∨over ∧
Figure 7.11 Standard logical equivalences. The symbols α, β, and γ stand for arbitrary
sentences of propositional logic.
in propositional logic—the SAT problem—was the ﬁrst problem proved to be NP-complete.
SAT
Many problems in computer science are really satisﬁability problems. For example, all the
constraint satisfaction problems in Chapter 5 ask whether the constraints are satisﬁable by
some assignment.
Validity and satisﬁability are of course connected: α is valid iff ¬α is unsatisﬁable; con-
trapositively, α is satisﬁable iff ¬α is not valid. We also have the following useful result:
◀
α |= β if and only if the sentence (α∧¬β) is unsatisﬁable.
Proving β from α by checking the unsatisﬁability of (α ∧¬β) corresponds exactly to the
standard mathematical proof technique of reductio ad absurdum (literally, “reduction to an
Reductio ad
absurdum
absurd thing”). It is also called proof by refutation or proof by contradiction. One assumes a
Refutation
Contradiction
sentence β to be false and shows that this leads to a contradiction with known axioms α. This
contradiction is exactly what is meant by saying that the sentence (α∧¬β) is unsatisﬁable.
7.5.1 Inference and proofs
This section covers inference rules that can be applied to derive a proof—a chain of conclu-
Inference rules
Proof
sions that leads to the desired goal. The best-known rule is called Modus Ponens (Latin for
Modus Ponens
mode that afﬁrms) and is written
α ⇒β,
α
β
The notation means that, whenever any sentences of the form α ⇒β and α are given, then
the sentence β can be inferred. For example, if (WumpusAhead ∧WumpusAlive) ⇒Shoot
and (WumpusAhead ∧WumpusAlive) are given, then Shoot can be inferred.
Another useful inference rule is And-Elimination, which says that, from a conjunction,
And-Elimination
any of the conjuncts can be inferred:
α∧β
α
.
For example, from (WumpusAhead ∧WumpusAlive), WumpusAlive can be inferred.

## Page 242
