---
chunk_id: "book-ca4fca8dd8-chunk-0538"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 538
confidence: "first-pass"
extraction_method: "structured-local"
---

328
Chapter 9
Inference in First-Order Logic
• A lifted version of Modus Ponens uses uniﬁcation to provide a natural and powerful
inference rule, generalized Modus Ponens. The forward-chaining and backward-
chaining algorithms apply this rule to sets of deﬁnite clauses.
• Generalized Modus Ponens is complete for deﬁnite clauses, although the entailment
problem is semidecidable. For Datalog knowledge bases consisting of function-free
deﬁnite clauses, entailment is decidable.
• Forward chaining is used in deductive databases, where it can be combined with re-
lational database operations. It is also used in production systems, which perform
efﬁcient updates with very large rule sets. Forward chaining is complete for Datalog
and runs in polynomial time.
• Backward chaining is used in logic programming systems, which employ sophisti-
cated compiler technology to provide very fast inference. Backward chaining suffers
from redundant inferences and inﬁnite loops; these can be alleviated by memoization.
• Prolog, unlike ﬁrst-order logic, uses a closed world with the unique names assumption
and negation as failure. These make Prolog a more practical programming language,
but bring it further from pure logic.
• The generalized resolution inference rule provides a complete proof system for ﬁrst-
order logic, using knowledge bases in conjunctive normal form.
• Several strategies exist for reducing the search space of a resolution system without
compromising completeness. One of the most important issues is dealing with equality;
we showed how demodulation and paramodulation can be used.
• Efﬁcient resolution-based theorem provers have been used to prove interesting mathe-
matical theorems and to verify and synthesize software and hardware.
Bibliographical and Historical Notes
Gottlob Frege, who developed full ﬁrst-order logic in 1879, based his system of inference
on a collection of valid schemas plus a single inference rule, Modus Ponens. Whitehead
and Russell (1910) expounded the so-called rules of passage (the actual term is from Her-
brand (1930)) that are used to move quantiﬁers to the front of formulas. Skolem constants
and Skolem functions were introduced, appropriately enough, by Thoralf Skolem (1920).
Oddly enough, it was Skolem who introduced the Herbrand universe (Skolem, 1928).
Herbrand’s theorem (Herbrand, 1930) has played a vital role in the development of au-
tomated reasoning. Herbrand is also the inventor of uniﬁcation. G¨odel (1930) built on the
ideas of Skolem and Herbrand to show that ﬁrst-order logic has a complete proof proce-
dure. Alan Turing (1936) and Alonzo Church (1936) simultaneously showed, using very
different proofs, that validity in ﬁrst-order logic was not decidable. The excellent text by
Enderton (1972) explains all of these results in a rigorous yet understandable fashion.
Abraham Robinson proposed that an automated reasoner could be built using proposition-
alization and Herbrand’s theorem, and Paul Gilmore (1960) wrote the ﬁrst program. Davis
and Putnam (1960) introduced the propositionalization method of Section 9.1. Prawitz (1960)
developed the key idea of letting the quest for propositional inconsistency drive the search,
and generating terms from the Herbrand universe only when they were necessary to estab-
