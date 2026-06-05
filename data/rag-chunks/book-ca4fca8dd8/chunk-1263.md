---
chunk_id: "book-ca4fca8dd8-chunk-1263"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1263
confidence: "first-pass"
extraction_method: "structured-local"
---

766
Chapter 20
Knowledge in Learning
{x/George}
Father(x,y)
P(x,y)
>
Father(George,y)
Ancestor(George,y)
>
P(George,y)
Ancestor(George,y)
>
¬
¬
Figure 20.14 An inverse resolution step that generates a new predicate P.
One thing that inverse resolution systems will do for you is invent new predicates. This
ability is often seen as somewhat magical, because computers are often thought of as “merely
working with what they are given.” In fact, new predicates fall directly out of the inverse
resolution step. The simplest case arises in hypothesizing two new clauses C1 and C2, given
a clause C. The resolution of C1 and C2 eliminates a literal that the two clauses share; hence,
it is quite possible that the eliminated literal contained a predicate that does not appear in C.
Thus, when working backward, one possibility is to generate a new predicate from which to
reconstruct the missing literal.
Figure 20.14 shows an example in which the new predicate P is generated in the process
of learning a deﬁnition for Ancestor. Once generated, P can be used in later inverse resolution
steps. For example, a later step might hypothesize that Mother(x,y) ⇒P(x,y). Thus, the
new predicate P has its meaning constrained by the generation of hypotheses that involve it.
Another example might lead to the constraint Father(x,y) ⇒P(x,y). In other words, the
predicate P is what we usually think of as the Parent relationship. As we mentioned earlier,
the invention of new predicates can signiﬁcantly reduce the size of the deﬁnition of the goal
predicate. Hence, by including the ability to invent new predicates, inverse resolution systems
can often solve learning problems that are infeasible with other techniques.
Some of the deepest revolutions in science come from the invention of new predicates and
functions—for example, Galileo’s invention of acceleration or Joule’s invention of thermal
energy. Once these terms are available, the discovery of new laws becomes (relatively) easy.
The difﬁcult part lies in realizing that some new entity, with a speciﬁc relationship to existing
entities, will allow an entire body of observations to be explained with a much simpler and
more elegant theory than previously existed.
As yet, ILP systems have not made discoveries on the level of Galileo or Joule, but their
discoveries have been deemed publishable in the scientiﬁc literature. For example, in the
Journal of Molecular Biology, Turcotte et al. (2001) describe the automated discovery of rules
for protein folding by the ILP program PROGOL. Many of the rules discovered by PROGOL
could have been derived from known principles, but most had not been previously published
as part of a standard biological database. (See Figure 20.10 for an example.). In related
work, Srinivasan et al. (1994) dealt with the problem of discovering molecular-structure-
based rules for the mutagenicity of nitroaromatic compounds. These compounds are found in
automobile exhaust fumes. For 80% of the compounds in a standard database, it is possible to
identify four important features, and linear regression on these features outperforms ILP. For
the remaining 20%, the features alone are not predictive, and ILP identiﬁes relationships that
