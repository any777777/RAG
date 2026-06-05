---
chunk_id: "book-ca4fca8dd8-chunk-1283"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1283
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 21.2
Learning with Complete Data
781
 0
 0.5
 1
 1.5
 2
 2.5
 0
 0.2
 0.4
 0.6
 0.8
 1
[1,1]
[2,2]
[5,5]
P(Θ = θ)
Parameter θ
 0
 1
 2
 3
 4
 5
 6
 0
 0.2
 0.4
 0.6
 0.8
 1
[3,1]
[6,2]
[30,10]
P(Θ = θ)
Parameter θ
(a)
(b)
Figure 21.5 Examples of the Beta(a,b) distribution for different values of (a,b).
21.2.5 Bayesian parameter learning
Maximum-likelihood learning gives rise to simple procedures, but it has serious deﬁciencies
with small data sets. For example, after seeing one cherry candy, the maximum-likelihood
hypothesis is that the bag is 100% cherry (i.e., θ=1.0). Unless one’s hypothesis prior is that
bags must be either all cherry or all lime, this is not a reasonable conclusion. It is more likely
that the bag is a mixture of lime and cherry. The Bayesian approach to parameter learning
starts with a hypothesis prior and updates the distribution as data arrive.
The candy example in Figure 21.2(a) has one parameter, θ: the probability that a ran-
domly selected piece of candy is cherry-ﬂavored. In the Bayesian view, θ is the (unknown)
value of a random variable Θ that deﬁnes the hypothesis space; the hypothesis prior is the
prior distribution over P(Θ). Thus, P(Θ=θ) is the prior probability that the bag has a frac-
tion θ of cherry candies.
If the parameter θ can be any value between 0 and 1, then P(Θ) is a continuous probability
density function (see Section A.3). If we don’t know anything about the possible values of θ
we can use the uniform density function P(θ) = Uniform(θ;0,1), which says all values are
equally likely.
A more ﬂexible family of probability density functions is known as the beta distribu-
tions. Each beta distribution is deﬁned by two hyperparameters3 a and b such that
Beta distribution
Hyperparameter
Beta(θ;a,b) = α θa−1(1−θ)b−1 ,
(21.6)
for θ in the range [0,1]. The normalization constant α, which makes the distribution integrate
to 1, depends on a and b. Figure 21.5 shows what the distribution looks like for various
values of a and b. The mean value of the beta distribution is a/(a+b), so larger values of a
suggest a belief that Θ is closer to 1 than to 0. Larger values of a + b make the distribution
more peaked, suggesting greater certainty about the value of Θ. It turns out that the uniform
density function is the same as Beta(1,1): the mean is 1/2, and the distribution is ﬂat.
3
They are called hyperparameters because they parameterize a distribution over θ, which is itself a parameter.

## Page 782
