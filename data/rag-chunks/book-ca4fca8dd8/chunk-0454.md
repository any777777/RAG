---
chunk_id: "book-ca4fca8dd8-chunk-0454"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 454
confidence: "first-pass"
extraction_method: "structured-local"
---

278
Chapter 8
First-Order Logic
that John must have one) without ever providing a deﬁnition of LeftLeg. This is something
that cannot be done with subroutines in programming languages.
The formal semantics of terms is straightforward. Consider a term f(t1,...,tn). The
function symbol f refers to some function in the model (call it F); the argument terms refer
to objects in the domain (call them d1,...,dn); and the term as a whole refers to the object that
is the value of the function F applied to d1,...,dn. For example, suppose the LeftLeg function
symbol refers to the function shown in Equation (8.2) and John refers to King John, then
LeftLeg(John) refers to King John’s left leg. In this way, the interpretation ﬁxes the referent
of every term.
8.2.4 Atomic sentences
Now that we have terms for referring to objects and predicate symbols for referring to rela-
tions, we can combine them to make atomic sentences that state facts. An atomic sentence
Atomic sentence
(or atom for short) is formed from a predicate symbol optionally followed by a parenthesized
Atom
list of terms, such as
Brother(Richard,John).
This states, under the intended interpretation given earlier, that Richard the Lionheart is the
brother of King John.4 Atomic sentences can have complex terms as arguments. Thus,
Married(Father(Richard),Mother(John))
states that Richard the Lionheart’s father is married to King John’s mother (again, under a
suitable interpretation).5
An atomic sentence is true in a given model if the relation referred to by the predicate
▶
symbol holds among the objects referred to by the arguments.
8.2.5 Complex sentences
We can use logical connectives to construct more complex sentences, with the same syntax
and semantics as in propositional calculus. Here are four sentences that are true in the model
of Figure 8.2 under our intended interpretation:
¬Brother(LeftLeg(Richard),John)
Brother(Richard,John)∧Brother(John,Richard)
King(Richard)∨King(John)
¬King(Richard) ⇒King(John).
8.2.6 Quantiﬁers
Once we have a logic that allows objects, it is only natural to want to express properties of
entire collections of objects, instead of enumerating the objects by name. Quantiﬁers let us
Quantiﬁer
do this. First-order logic contains two standard quantiﬁers, called universal and existential.
Universal quantiﬁcation (∀)
Recall the difﬁculty we had in Chapter 7 with the expression of general rules in proposi-
tional logic. Rules such as “Squares neighboring the wumpus are smelly” and “All kings
4
We usually follow the argument-ordering convention that P(x,y) is read as “x is a P of y.”
5
This ontology only recognizes one father and one mother for each person. A more complex ontology could
recognize biological mother, birth mother, adoptive mother, etc.
