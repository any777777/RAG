---
chunk_id: "book-ca4fca8dd8-chunk-0751"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 751
confidence: "first-pass"
extraction_method: "structured-local"
---

454
Chapter 13
Probabilistic Reasoning
Monte Carlo algorithms, of which simulated annealing (page 133) is an example, are used
in many branches of science to estimate quantities that are difﬁcult to calculate exactly. In this
section, we are interested in sampling applied to the computation of posterior probabilities
in Bayes nets. We describe two families of algorithms: direct sampling and Markov chain
sampling. Several other approaches for approximate inference are mentioned in the notes at
the end of the chapter.
13.4.1 Direct sampling methods
The primitive element in any sampling algorithm is the generation of samples from a known
probability distribution. For example, an unbiased coin can be thought of as a random vari-
able Coin with values ⟨heads,tails⟩and a prior distribution P(Coin) = ⟨0.5,0.5⟩. Sampling
from this distribution is exactly like ﬂipping the coin: with probability 0.5 it will return heads,
and with probability 0.5 it will return tails. Given a source of random numbers r uniformly
distributed in the range [0,1], it is a simple matter to sample any distribution on a single
variable, whether discrete or continuous. This is done by constructing the cumulative distri-
bution for the variable and returning the ﬁrst value whose cumulative probability exceeds r
(see Exercise 13.PRSA).
We begin with a random sampling process for a Bayes net that has no evidence associated
with it. The idea is to sample each variable in turn, in topological order. The probability
distribution from which the value is sampled is conditioned on the values already assigned to
the variable’s parents. (Because we sample in topological order, the parents are guaranteed
to have values already.) This algorithm is shown in Figure 13.16. Applying it to the network
in Figure 13.15(a) with the ordering Cloudy, Sprinkler, Rain, WetGrass, we might produce a
random event as follows:
1. Sample from P(Cloudy) = ⟨0.5,0.5⟩, value is true.
2. Sample from P(Sprinkler|Cloudy=true) = ⟨0.1,0.9⟩, value is false.
3. Sample from P(Rain|Cloudy=true) = ⟨0.8,0.2⟩, value is true.
4. Sample from P(WetGrass|Sprinkler=false,Rain=true) = ⟨0.9,0.1⟩, value is true.
In this case, PRIOR-SAMPLE returns the event [true,false,true,true].
It is easy to see that PRIOR-SAMPLE generates samples from the prior joint distribution
speciﬁed by the network. First, let SPS(x1,...,xn) be the probability that a speciﬁc event is
function PRIOR-SAMPLE(bn) returns an event sampled from the prior speciﬁed by bn
inputs: bn, a Bayesian network specifying joint distribution P(X1,...,Xn)
x←an event with n elements
for each variable Xi in X1,...,Xn do
x[i]←a random sample from P(Xi | parents(Xi))
return x
Figure 13.16 A sampling algorithm that generates events from a Bayesian network. Each
variable is sampled according to the conditional distribution given the values already sampled
for the variable’s parents.
