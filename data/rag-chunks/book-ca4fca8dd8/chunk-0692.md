---
chunk_id: "book-ca4fca8dd8-chunk-0692"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 692
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 414

414
Chapter 12
Quantifying Uncertainty
This process is called marginalization, or summing out—because we sum up the probabil-
Marginalization
ities for each possible value of the other variables, thereby taking them out of the equation.
We can write the following general marginalization rule for any sets of variables Y and Z:
P(Y) = ∑
z
P(Y,Z=z),
(12.7)
where ∑z sums over all the possible combinations of values of the set of variables Z. As
usual we can abbreviate P(Y,Z=z) in this equation by P(Y,z). For the Cavity example,
Equation (12.7) corresponds to the following equation:
P(Cavity) = P(Cavity,toothache,catch)+P(Cavity,toothache,¬catch)
+ P(Cavity,¬toothache,catch)+P(Cavity,¬toothache,¬catch)
= ⟨0.108,0.016⟩+⟨0.012,0.064⟩+⟨0.072,0.144⟩+⟨0.008,0.576⟩
= ⟨0.2,0.8⟩.
Using the product rule (Equation (12.4)), we can replace P(Y,z) in Equation (12.7) by
P(Y|z)P(z), obtaining a rule called conditioning:
Conditioning
P(Y) = ∑
z
P(Y|z)P(z).
(12.8)
Marginalization and conditioning turn out to be useful rules for all kinds of derivations in-
volving probability expressions.
In most cases, we are interested in computing conditional probabilities of some variables,
given evidence about others. Conditional probabilities can be found by ﬁrst using Equa-
tion (12.3) to obtain an expression in terms of unconditional probabilities and then evaluating
the expression from the full joint distribution. For example, we can compute the probability
of a cavity, given evidence of a toothache, as follows:
P(cavity|toothache) = P(cavity∧toothache)
P(toothache)
=
0.108+0.012
0.108+0.012+0.016+0.064 = 0.6.
Just to check, we can also compute the probability that there is no cavity, given a toothache:
P(¬cavity|toothache) = P(¬cavity∧toothache)
P(toothache)
=
0.016+0.064
0.108+0.012+0.016+0.064 = 0.4.
The two values sum to 1.0, as they should. Notice that the term P(toothache) is in the de-
nominator for both of these calculations. If the variable Cavity had more than two values, it
would be in the denominator for all of them. In fact, it can be viewed as a normalization
constant for the distribution P(Cavity|toothache), ensuring that it adds up to 1. Throughout
the chapters dealing with probability, we use α to denote such constants. With this notation,
we can write the two preceding equations in one:
P(Cavity|toothache) = αP(Cavity,toothache)
= α[P(Cavity,toothache,catch)+P(Cavity,toothache,¬catch)]
= α[⟨0.108,0.016⟩+⟨0.012,0.064⟩] = α⟨0.12,0.08⟩= ⟨0.6,0.4⟩.

## Page 415
