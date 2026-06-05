---
chunk_id: "book-ca4fca8dd8-chunk-0846"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 846
confidence: "first-pass"
extraction_method: "structured-local"
---

510
Chapter 14
Probabilistic Reasoning over Time
function PARTICLE-FILTERING(e,N,dbn) returns a set of samples for the next time step
inputs: e, the new incoming evidence
N, the number of samples to be maintained
dbn, a DBN deﬁned by P(X0), P(X1 |X0), and P(E1 |X1)
persistent: S, a vector of samples of size N, initially generated from P(X0)
local variables: W, a vector of weights of size N
for i = 1 to N do
S[i]←sample from P(X1 |X0 = S[i])
// step 1
W[i]←P(e|X1 = S[i])
// step 2
S←WEIGHTED-SAMPLE-WITH-REPLACEMENT(N,S,W)
// step 3
return S
Figure 14.17 The particle ﬁltering algorithm implemented as a recursive update oper-
ation with state (the set of samples).
Each of the sampling operations involves sam-
pling the relevant slice variables in topological order, much as in PRIOR-SAMPLE. The
WEIGHTED-SAMPLE-WITH-REPLACEMENT operation can be implemented to run in O(N)
expected time. The step numbers refer to the description in the text.
Clearly, we need a better solution. The second key innovation is to focus the set of
▶
samples on the high-probability regions of the state space. This can be done by throwing
away samples that have very low weight, according to the observations, while replicating
those that have high weight. In that way, the population of samples will stay reasonably close
to reality. If we think of samples as a resource for modeling the posterior distribution, then it
makes sense to use more samples in regions of the state space where the posterior is higher.
A family of algorithms called particle ﬁltering is designed to do just that. (Another early
Particle ﬁltering
name was sequential importance sampling with resampling, but for some reason it failed
on catch on.) Particle ﬁltering works as follows: First, we generate a population of N samples
from the prior distribution P(X0). Then the update cycle is repeated for each time step:
1. Each sample is propagated forward by sampling the next state value xt+1 given the
current value xt for the sample, based on the transition model P(Xt+1 |xt).
2. Each sample is weighted by the likelihood it assigns to the new evidence, P(et+1 |xt+1).
3. The population is resampled to generate a new population of N samples. Each new
sample is selected from the current population; the probability that a particular sample
is selected is proportional to its weight. The new samples are unweighted.
The algorithm is shown in detail in Figure 14.17, and its operation for the umbrella DBN is
illustrated in Figure 14.18.
We can show that this algorithm is consistent—gives the correct probabilities as N tends
to inﬁnity—by examining the operations in one update cycle. We assume that the sample pop-
ulation starts with a correct representation of the forward message—that is, f1:t =P(Xt |e1:t)
at time t. Writing N(xt |e1:t) for the number of samples occupying state xt after observations
e1:t have been processed, we therefore have
N(xt |e1:t)/N = P(xt |e1:t)
(14.23)
for large N. Now we propagate each sample forward by sampling the state variables at t +1,
