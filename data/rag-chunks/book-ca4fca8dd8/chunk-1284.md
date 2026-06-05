---
chunk_id: "book-ca4fca8dd8-chunk-1284"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1284
confidence: "first-pass"
extraction_method: "structured-local"
---

782
Chapter 21
Learning Probabilistic Models
Θ
Θ1
Θ2
Flavor1
Flavor2
Flavor3
Wrapper1
Wrapper2
Wrapper3
Figure 21.6 A Bayesian network that corresponds to a Bayesian learning process. Poste-
rior distributions for the parameter variables Θ, Θ1, and Θ2 can be inferred from their prior
distributions and the evidence in Flavori and Wrapperi.
Besides its ﬂexibility, the beta family has another wonderful property: if Θ has a prior
Beta(a,b), then, after a data point is observed, the posterior distribution for Θ is also a beta
distribution. In other words, Beta is closed under update. The beta family is called the
conjugate prior for the family of distributions for a Boolean variable.4 Let’s see how this
Conjugate prior
works. Suppose we observe a cherry candy; then we have
P(θ|D1 =cherry) = α P(D1 =cherry|θ)P(θ)
= α′ θ ·Beta(θ;a,b) = α′ θ ·θa−1(1−θ)b−1
= α′ θa(1−θ)b−1 = α′ Beta(θ;a+1,b).
Thus, after seeing a cherry candy, we simply increment the a parameter to get the posterior;
similarly, after seeing a lime candy, we increment the b parameter. Thus, we can view the a
and b hyperparameters as virtual counts, in the sense that a prior Beta(a,b) behaves exactly
Virtual count
as if we had started out with a uniform prior Beta(1,1) and seen a−1 actual cherry candies
and b−1 actual lime candies.
By examining a sequence of beta distributions for increasing values of a and b, keeping
the proportions ﬁxed, we can see vividly how the posterior distribution over the parameter
Θ changes as data arrive. For example, suppose the actual bag of candy is 75% cherry. Fig-
ure 21.5(b) shows the sequence Beta(3,1), Beta(6,2), Beta(30,10). Clearly, the distribution
is converging to a narrow peak around the true value of Θ. For large data sets, then, Bayesian
learning (at least in this case) converges to the same answer as maximum-likelihood learning.
Now let us consider a more complicated case. The network in Figure 21.2(b) has three
parameters, θ, θ1, and θ2, where θ1 is the probability of a red wrapper on a cherry candy and
4
Other conjugate priors include the Dirichlet family for the parameters of a discrete multivalued distribution
and the Normal–Wishart family for the parameters of a Gaussian distribution. See Bernardo and Smith (1994).

## Page 783
