---
chunk_id: "book-ca4fca8dd8-chunk-0765"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 765
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 13.4
Approximate Inference for Bayesian Networks
461
function GIBBS-ASK(X,e,bn,N) returns an estimate of P(X |e)
local variables: C, a vector of counts for each value of X, initially zero
Z, the nonevidence variables in bn
x, the current state of the network, initialized from e
initialize x with random values for the variables in Z
for k = 1 to N do
choose any variable Zi from Z according to any distribution ρ(i)
set the value of Zi in x by sampling from P(Zi |mb(Zi))
C[j]←C[j]+1 where xj is the value of X in x
return NORMALIZE(C)
Figure 13.20 The Gibbs sampling algorithm for approximate inference in Bayes nets; this
version chooses variables at random, but cycling through the variables but also works.
2. Rain is chosen and then sampled, given the current values of its Markov blanket: in
this case, we sample from P(Rain|Cloudy=false,Sprinkler=true,WetGrass=true).
Suppose this yields Rain=true. The new current state is [false,true,true,true].
The one remaining detail concerns the method of calculating the Markov blanket distribu-
tion P(Xi |mb(Xi)), where mb(Xi) denotes the values of the variables in Xi’s Markov blan-
ket, MB(Xi). Fortunately, this does not involve any complex inference. As shown in Exer-
cise 13.MARB, the distribution is given by
P(xi |mb(Xi)) = αP(xi | parents(Xi))
∏
Yj∈Children(Xi)
P(yj | parents(Yj)).
(13.10)
In other words, for each value xi, the probability is given by multiplying probabilities from the
CPTs of Xi and its children. For example, in the ﬁrst sampling step shown above, we sampled
from P(Cloudy|Sprinkler=true,Rain=false). By Equation (13.10), and abbreviating the
variable names, we have
P(c|s,¬r) = αP(c)P(s|c)P(¬r|c) = α0.5·0.1·0.2
P(¬c|s,¬r) = αP(¬c)P(s|¬c)P(¬r|¬c) = α0.5·0.5·0.8,
so the sampling distribution is α⟨0.001,0.020⟩≈⟨0.048,0.952⟩.
Figure 13.21(a) shows the complete Markov chain for the case where variables are chosen
uniformly, i.e., ρ(Cloudy)=ρ(Rain)=0.5. The algorithm is simply wandering around in this
graph, following links with the stated probabilities. Each state visited during this process is
a sample that contributes to the estimate for the query variable Rain. If the process visits 20
states where Rain is true and 60 states where Rain is false, then the answer to the query is
NORMALIZE(⟨20,60⟩) = ⟨0.25,0.75⟩.
Analysis of Markov chains
We have said that Gibbs sampling works by wandering randomly around the state space to
generate samples. To explain why Gibbs sampling works correctly—that is, why its estimates
converge to correct values in the limit—we will need some careful analysis. (This section is
somewhat mathematical and can be skipped on ﬁrst reading.)
