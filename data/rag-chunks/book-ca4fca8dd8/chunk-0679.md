---
chunk_id: "book-ca4fca8dd8-chunk-0679"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 679
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 12.2
Basic Probability Notation
407
possible world must be the case. For example, if we are about to roll two (distinguishable)
dice, there are 36 possible worlds to consider: (1,1), (1,2), ..., (6,6). The Greek letter Ω
(uppercase omega) is used to refer to the sample space, and ω (lowercase omega) refers to
elements of the space, that is, particular possible worlds.
A fully speciﬁed probability model associates a numerical probability P(ω) with each
Probability model
possible world.1 The basic axioms of probability theory say that every possible world has a
probability between 0 and 1 and that the total probability of the set of possible worlds is 1:
0 ≤P(ω) ≤1 for every ω and ∑
ω∈Ω
P(ω) = 1.
(12.1)
For example, if we assume that each die is fair and the rolls don’t interfere with each other,
then each of the possible worlds (1,1), (1,2), ..., (6,6) has probability 1/36. If the dice are
loaded then some worlds will have higher probabilities and some lower, but they will all still
sum to 1.
Probabilistic assertions and queries are not usually about particular possible worlds, but
about sets of them. For example, we might ask for the probability that the two dice add up
to 11, the probability that doubles are rolled, and so on. In probability theory, these sets
are called events—a term already used extensively in Chapter 10 for a different concept. In
Event
logic, a set of worlds corresponds to a proposition in a formal language; speciﬁcally, for each
proposition, the corresponding set contains just those possible worlds in which the proposi-
tion holds. (Hence, “event” and “proposition” mean roughly the same thing in this context,
except that a proposition is expressed in a formal language.) The probability associated with
a proposition is deﬁned to be the sum of the probabilities of the worlds in which it holds:
For any proposition φ, P(φ) = ∑
ω∈φ
P(ω).
(12.2)
For example, when rolling fair dice, we have P(Total=11) = P((5,6))+P((6,5)) = 1/36+
1/36 = 1/18. Note that probability theory does not require complete knowledge of the prob-
abilities of each possible world. For example, if we believe the dice conspire to produce
the same number, we might assert that P(doubles) = 1/4 without knowing whether the dice
prefer double 6 to double 2. Just as with logical assertions, this assertion constrains the
underlying probability model without fully determining it.
Probabilities such as P(Total=11) and P(doubles) are called unconditional or prior
Unconditional
probability
probabilities (and sometimes just “priors” for short); they refer to degrees of belief in propo-
Prior probability
sitions in the absence of any other information. Most of the time, however, we have some
information, usually called evidence, that has already been revealed. For example, the ﬁrst
Evidence
die may already be showing a 5 and we are waiting with bated breath for the other one to
stop spinning. In that case, we are interested not in the unconditional probability of rolling
doubles, but the conditional or posterior probability (or just “posterior” for short) of rolling
Conditional
probability
Posterior probability
doubles given that the ﬁrst die is a 5. This probability is written P(doubles|Die1 =5), where
the “|” is pronounced “given.”2
Similarly, if I am going to the dentist for a regularly scheduled checkup, then the prior
probability P(cavity)=0.2 might be of interest; but if I go to the dentist because I have a
toothache, it’s the conditional probability P(cavity|toothache)=0.6 that matters.
1
For now, we assume a discrete, countable set of worlds. The proper treatment of the continuous case brings in
certain complications that are less relevant for most purposes in AI.
2
Note that the precedence of “|” is such that any expression of the form P(... | ...) always means P((...)|(...)).
