---
chunk_id: "book-ca4fca8dd8-chunk-0759"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 759
confidence: "first-pass"
extraction_method: "structured-local"
---

458
Chapter 13
Probabilistic Reasoning
function LIKELIHOOD-WEIGHTING(X,e,bn,N) returns an estimate of P(X |e)
inputs: X, the query variable
e, observed values for variables E
bn, a Bayesian network specifying joint distribution P(X1,...,Xn)
N, the total number of samples to be generated
local variables: W, a vector of weighted counts for each value of X, initially zero
for j = 1 to N do
x,w←WEIGHTED-SAMPLE(bn,e)
W[j]←W[j]+w where xj is the value of X in x
return NORMALIZE(W)
function WEIGHTED-SAMPLE(bn,e) returns an event and a weight
w←1; x←an event with n elements, with values ﬁxed from e
for i = 1 to n do
if Xi is an evidence variable with value xij in e
then w←w× P(Xi = xij | parents(Xi))
else x[i]←a random sample from P(Xi | parents(Xi))
return x, w
Figure 13.18 The likelihood-weighting algorithm for inference in Bayesian networks. In
WEIGHTED-SAMPLE, each nonevidence variable is sampled according to the conditional
distribution given the values already sampled for the variable’s parents, while a weight is
accumulated based on the likelihood for each evidence variable.
because each variable is sampled conditioned on its parents. In order to complete the algo-
rithm, we need to know how to compute the weight for each sample generated from QWS.
According to the general scheme for importance sampling, the weight should be
w(z) = P(z|e)/QWS(z) = αP(z,e)/QWS(z)
where the normalizing factor α=1/P(e) is the same for all samples. Now z and e together
cover all the variables in the Bayes net, so P(z,e) is just the product of all the conditional prob-
abilities (Equation (13.2) page 433); and we can write this as the product of the conditional
probabilities for the nonevidence variables times the product of the conditional probabilities
for the evidence variables:
w(z) = α P(z,e)
QWS(z) = α ∏l
i=1 P(zi | parents(Zi)) ∏m
i=1 P(ei | parents(Ei))
∏l
i=1 P(zi | parents(Zi))
= α
m
∏
i=1
P(ei | parents(Ei)).
(13.9)
Thus the weight is the product of the conditional probabilities for the evidence variables
given their parents. (Probabilities of evidence are generally called likelihoods, hence the
name.) The weight calculation is implemented incrementally in WEIGHTED-SAMPLE, mul-
tiplying by the conditional probability each time an evidence variable is encountered. The
normalization is done at the end before the query result is returned.
Let us apply the algorithm to the network shown in Figure 13.15(a), with the query
P(Rain|Cloudy=true,WetGrass=true) and the ordering Cloudy, Sprinkler, Rain, WetGrass.
