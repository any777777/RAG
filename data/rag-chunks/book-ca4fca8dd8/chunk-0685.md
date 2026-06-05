---
chunk_id: "book-ca4fca8dd8-chunk-0685"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 685
confidence: "first-pass"
extraction_method: "structured-local"
---

410
Chapter 12
Quantifying Uncertainty
deﬁnition of P(x) is the probability that X falls within an arbitrarily small region beginning
at x, divided by the width of the region:
P(x) = lim
dx→0P(x ≤X ≤x+dx)/dx.
For NoonTemp we have
P(NoonTemp=x) = Uniform(x;18C,26C) =

1
8C if 18C ≤x ≤26C
0 otherwise
,
where C stands for centigrade (not for a constant). In P(NoonTemp=20.18C)= 1
8C, note that
1
8C is not a probability, it is a probability density. The probability that NoonTemp is exactly
20.18C is zero, because 20.18C is a region of width 0. Some authors use different symbols
for discrete probabilities and probability densities; we use P for speciﬁc probability values
and P for vectors of values in both cases, since confusion seldom arises and the equations
are usually identical. Note that probabilities are unitless numbers, whereas density functions
are measured with a unit, in this case reciprocal degrees centigrade. If the same temperature
interval were to be expressed in degrees Fahrenheit, it would have a width of 14.4 degrees,
and the density would be 1/14.4F.
In addition to distributions on single variables, we need notation for distributions on
multiple variables. Commas are used for this. For example, P(Weather,Cavity) denotes the
probabilities of all combinations of the values of Weather and Cavity. This is a 4×2 table of
probabilities called the joint probability distribution of Weather and Cavity. We can also
Joint probability
distribution
mix variables and speciﬁc values; P(sun,Cavity) would be a two-element vector giving the
probabilities of a cavity with a sunny day and no cavity with a sunny day.
The P notation makes certain expressions much more concise than they might otherwise
be. For example, the product rules (see Equation (12.4)) for all possible values of Weather
and Cavity can be written as a single equation:
P(Weather,Cavity) = P(Weather|Cavity)P(Cavity),
instead of as these 4×2=8 equations (using abbreviations W and C):
P(W =sun∧C=true) = P(W =sun|C=true)P(C=true)
P(W =rain∧C=true) = P(W =rain|C=true)P(C=true)
P(W =cloud ∧C=true) = P(W =cloud|C=true)P(C=true)
P(W =snow∧C=true) = P(W =snow|C=true)P(C=true)
P(W =sun∧C=false) = P(W =sun|C=false)P(C=false)
P(W =rain∧C=false) = P(W =rain|C=false)P(C=false)
P(W =cloud ∧C=false) = P(W =cloud|C=false)P(C=false)
P(W =snow∧C=false) = P(W =snow|C=false)P(C=false).
As a degenerate case, P(sun,cavity) has no variables and thus is a zero-dimensional vector,
which we can think of as a scalar value.
Now we have deﬁned a syntax for propositions and probability assertions and we have
given part of the semantics: Equation (12.2) deﬁnes the probability of a proposition as the sum
of the probabilities of worlds in which it holds. To complete the semantics, we need to say
what the worlds are and how to determine whether a proposition holds in a world. We borrow
this part directly from the semantics of propositional logic, as follows. A possible world is
▶
deﬁned to be an assignment of values to all of the random variables under consideration.
It is easy to see that this deﬁnition satisﬁes the basic requirement that possible worlds be
mutually exclusive and exhaustive (Exercise 12.EXEX). For example, if the random variables
