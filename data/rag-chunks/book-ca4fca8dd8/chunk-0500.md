---
chunk_id: "book-ca4fca8dd8-chunk-0500"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 500
confidence: "first-pass"
extraction_method: "structured-local"
---

304
Chapter 9
Inference in First-Order Logic
Employs(x,y)
Employs(x,Richard)
Employs(IBM,y)
Employs(IBM,Richard)
Employs(x,y)
Employs(John,John)
Employs(x,x)
Employs(x,John)
Employs(John,y)
(a)
(b)
Figure 9.2 (a) The subsumption lattice whose lowest node is Employs(IBM,Richard). (b)
The subsumption lattice for the sentence Employs(John,John).
interesting properties. The child of any node in the lattice is obtained from its parent by a
single substitution; and the “highest” common descendant of any two nodes is the result of
applying their most general uniﬁer. A sentence with repeated constants has a slightly different
lattice, as shown in Figure 9.2(b). Although function symbols are not shown in the ﬁgure,
they too can be incorporated into the lattice structure.
For predicates with a small number of arguments, it is a good tradeoff to create an index
for every point in the subsumption lattice. That requires a little more work at storage time,
but speeds up retrieval time. However, for a predicate with n arguments, the lattice contains
O(2n) nodes. If function symbols are allowed, the number of nodes is also exponential in the
size of the terms in the sentence to be stored. This can lead to a huge number of indices.
We have to somehow limit the indices to ones that are likely to be used frequently in
queries; otherwise we will waste more time in creating the indices than we save by having
them. We could adopt a ﬁxed policy, such as maintaining indices only on keys composed of
a predicate plus a single argument. Or we could learn an adaptive policy that creates indices
to meet the demands of the kinds of queries being asked. For commercial databases where
facts number in the billions, the problem has been the subject of intensive study, technology
development, and continual optimization.
9.3 Forward Chaining
In Section 7.5 we showed a forward-chaining algorithm for knowledge bases of propositional
deﬁnite clauses. Here we expand that idea to cover ﬁrst-order deﬁnite clauses.
Of course there are some logical sentences that cannot be stated as a deﬁnite clause, and
thus cannot be handled by this approach. But rules of the form Antecedent ⇒Consequent
are sufﬁcient to cover a wide variety of interesting real-world systems.
9.3.1 First-order deﬁnite clauses
First-order deﬁnite clauses are disjunctions of literals of which exactly one is positive. That
means a deﬁnite clause is either atomic, or is an implication whose antecedent is a conjunction
of positive literals and whose consequent is a single positive literal. Existential quantiﬁers are
not allowed, and universal quantiﬁers are left implicit: if you see an x in a deﬁnite clause, that
means there is an implicit ∀x quantiﬁer. A typical ﬁrst-order deﬁnite clause looks like this:
King(x)∧Greedy(x) ⇒Evil(x),
but the literals King(John) and Greedy(y) also count as deﬁnite clauses. First-order liter-
