---
chunk_id: "book-ca4fca8dd8-chunk-1072"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1072
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 642

642
Chapter 18
Probabilistic Programming
. . .
. . .
. . .
R
J
R
R
R
R
R
J
J
J
J
J
. . .
R
J
J
R
R
J
R
J
R
J
R
J
R
J
R
J
R
J
R
J
Figure 18.1 Top: Some members of the set of all possible worlds for a language with two
constant symbols, R and J, and one binary relation symbol, under the standard semantics for
ﬁrst-order logic. Bottom: the possible worlds under database semantics. The interpretation
of the constant symbols is ﬁxed, and there is a distinct object for each constant symbol.
Both routes lead to a probabilistic programming language (PPL). The ﬁrst route leads
Probabilistic
programming
language (PPL)
to declarative PPLs, which bear roughly the same relationship to general PPLs as logic pro-
gramming (Chapter 9) does to general programming languages.
18.1 Relational Probability Models
Recall from Chapter 12 that a probability model deﬁnes a set Ωof possible worlds with
a probability P(ω) for each world ω. For Bayesian networks, the possible worlds are as-
signments of values to variables; for the Boolean case in particular, the possible worlds are
identical to those of propositional logic.
For a ﬁrst-order probability model, then, it seems we need the possible worlds to be those
of ﬁrst-order logic—that is, a set of objects with relations among them and an interpretation
that maps constant symbols to objects, predicate symbols to relations, and function symbols to
functions on those objects. (See Section 8.2.) The model also needs to deﬁne a probability for
each such possible world, just as a Bayesian network deﬁnes a probability for each assignment
of values to variables.
Let us suppose, for a moment, that we have ﬁgured out how to do this. Then, as usual
(see page 407), we can obtain the probability of any ﬁrst-order logical sentence φ (phi) as a
sum over the possible worlds where it is true:
P(φ) =
∑
ω:φ is true in ω
P(ω).
(18.1)
Conditional probabilities P(φ|e) can be obtained similarly, so we can, in principle, ask any
question we want of our model—and get an answer. So far, so good.
There is, however, a problem: the set of ﬁrst-order models is inﬁnite. We saw this ex-
plicitly in Figure 8.4 on page 277, which we show again in Figure 18.1 (top). This means
that (1) the summation in Equation (18.1) could be infeasible, and (2) specifying a complete,
consistent distribution over an inﬁnite set of worlds could be very difﬁcult.

## Page 643
