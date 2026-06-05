---
chunk_id: "book-ca4fca8dd8-chunk-0687"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 687
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 12.2
Basic Probability Notation
411
are Cavity, Toothache, and Weather, then there are 2×2×4=16 possible worlds. Further-
more, the truth of any given proposition can be determined easily in such worlds by the same
recursive truth calculation we used for propositional logic (see page 236).
Note that some random variables may be redundant, in that their values can be obtained in
all cases from the values of other variables. For example, the Doubles variable in the two-dice
world is true exactly when Die1 =Die2. Including Doubles as one of the random variables,
in addition to Die1 and Die2, seems to increase the number of possible worlds from 36 to 72,
but of course exactly half of the 72 will be logically impossible and will have probability 0.
From the preceding deﬁnition of possible worlds, it follows that a probability model is
completely determined by the joint distribution for all of the random variables—the so-called
full joint probability distribution. For example, given Cavity, Toothache, and Weather,
Full joint probability
distribution
the full joint distribution is P(Cavity,Toothache,Weather). This joint distribution can be
represented as a 2×2×4 table with 16 entries. Because every proposition’s probability is
a sum over possible worlds, a full joint distribution sufﬁces, in principle, for calculating the
probability of any proposition. We will see examples of how to do this in Section 12.3.
12.2.3 Probability axioms and their reasonableness
The basic axioms of probability (Equations (12.1) and (12.2)) imply certain relationships
among the degrees of belief that can be accorded to logically related propositions. For exam-
ple, we can derive the familiar relationship between the probability of a proposition and the
probability of its negation:
P(¬a) = ∑ω∈¬a P(ω)
by Equation (12.2)
= ∑ω∈¬a P(ω)+∑ω∈a P(ω)−∑ω∈a P(ω)
= ∑ω∈ΩP(ω)−∑ω∈a P(ω)
grouping the ﬁrst two terms
= 1−P(a)
by (12.1) and (12.2).
We can also derive the well-known formula for the probability of a disjunction, sometimes
called the inclusion–exclusion principle:
Inclusion–exclusion
principle
P(a∨b) = P(a)+P(b)−P(a∧b).
(12.5)
This rule is easily remembered by noting that the cases where a holds, together with the cases
where b holds, certainly cover all the cases where a ∨b holds; but summing the two sets of
cases counts their intersection twice, so we need to subtract P(a∧b).
Equations (12.1) and (12.5) are often called Kolmogorov’s axioms in honor of the math-
Kolmogorov’s
axioms
ematician Andrei Kolmogorov, who showed how to build up the rest of probability theory
from this simple foundation and how to handle the difﬁculties caused by continuous vari-
ables.4 While Equation (12.2) has a deﬁnitional ﬂavor, Equation (12.5) reveals that the ax-
ioms really do constrain the degrees of belief an agent can have concerning logically related
propositions. This is analogous to the fact that a logical agent cannot simultaneously believe
A, B, and ¬(A∧B), because there is no possible world in which all three are true. With prob-
abilities, however, statements refer not to the world directly, but to the agent’s own state of
knowledge. Why, then, can an agent not hold the following set of beliefs (even though they
violate Kolmogorov’s axioms)?
P(a)=0.4
P(b)=0.3
P(a∧b)=0.0
P(a∨b)=0.8.
(12.6)
4
The difﬁculties include the Vitali set, a well-deﬁned subset of the interval [0,1] with no well-deﬁned size.
