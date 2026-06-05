---
chunk_id: "book-ca4fca8dd8-chunk-0490"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 490
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 9.1
Propositional vs. First-Order Inference
299
Similarly, the rule of Existential Instantiation replaces an existentially quantiﬁed vari-
Existential
Instantiation
able with a single new constant symbol. The formal statement is as follows: for any sentence
α, variable v, and constant symbol k that does not appear elsewhere in the knowledge base,
∃v α
SUBST({v/k},α) .
For example, from the sentence
∃x Crown(x)∧OnHead(x,John)
we can infer the sentence
Crown(C1)∧OnHead(C1,John)
as long as C1 does not appear elsewhere in the knowledge base. Basically, the existential
sentence says there is some object satisfying a condition, and applying the existential instan-
tiation rule just gives a name to that object. Of course, that name must not already belong
to another object. Mathematics provides a nice example: suppose we discover that there is a
number that is a little bigger than 2.71828 and that satisﬁes the equation d(xy)/dy=xy for x.
We can give this number the name e, but it would be a mistake to give it the name of an
existing object, such as π. In logic, the new name is called a Skolem constant.
Skolem constant
Whereas Universal Instantiation can be applied many times to the same axiom to pro-
duce many different consequences, Existential Instantiation need only be applied once, and
then the existentially quantiﬁed sentence can be discarded. For example, we no longer need
∃x Kill(x,Victim) once we have added the sentence Kill(Murderer,Victim).
9.1.1 Reduction to propositional inference
We now show how to convert any ﬁrst-order knowledge base into a propositional knowledge
base. The ﬁrst idea is that, just as an existentially quantiﬁed sentence can be replaced by
one instantiation, a universally quantiﬁed sentence can be replaced by the set of all possible
instantiations. For example, suppose our knowledge base contains just the sentences
∀x King(x)∧Greedy(x) ⇒Evil(x)
King(John)
Greedy(John)
Brother(Richard,John).
(9.1)
and that the only objects are John and Richard. We apply UI to the ﬁrst sentence using all
possible substitutions, {x/John} and {x/Richard}. We obtain
King(John)∧Greedy(John) ⇒Evil(John)
King(Richard)∧Greedy(Richard) ⇒Evil(Richard).
Next replace ground atomic sentences, such as King(John), with proposition symbols, such
as JohnIsKing. Finally, apply any of the complete propositional algorithms in Chapter 7 to
obtain conclusions such as JohnIsEvil, which is equivalent to Evil(John).
This technique of propositionalization can be made completely general, as we show
Propositionalization
in Section 9.5. However, there is a problem: when the knowledge base includes a func-
tion symbol, the set of possible ground-term substitutions is inﬁnite! For example, if the
knowledge base mentions the Father symbol, then inﬁnitely many nested terms such as
Father(Father(Father(John))) can be constructed.
