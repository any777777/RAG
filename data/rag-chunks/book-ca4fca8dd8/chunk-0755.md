---
chunk_id: "book-ca4fca8dd8-chunk-0755"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 755
confidence: "first-pass"
extraction_method: "structured-local"
---

456
Chapter 13
Probabilistic Reasoning
function REJECTION-SAMPLING(X,e,bn,N) returns an estimate of P(X |e)
inputs: X, the query variable
e, observed values for variables E
bn, a Bayesian network
N, the total number of samples to be generated
local variables: C, a vector of counts for each value of X, initially zero
for j = 1 to N do
x←PRIOR-SAMPLE(bn)
if x is consistent with e then
C[j]←C[j]+1 where xj is the value of X in x
return NORMALIZE(C)
Figure 13.17 The rejection-sampling algorithm for answering queries given evidence in a
Bayesian network.
From Equation (13.7), this becomes
ˆP(X |e) ≈P(X,e)
P(e)
= P(X |e).
That is, rejection sampling produces a consistent estimate of the true probability.
Continuing with our example from Figure 13.15(a), let us assume that we wish to estimate
P(Rain|Sprinkler=true), using 100 samples. Of the 100 that we generate, suppose that 73
have Sprinkler=false and are rejected, while 27 have Sprinkler=true; of the 27, 8 have
Rain=true and 19 have Rain=false. Hence,
P(Rain|Sprinkler=true) ≈NORMALIZE(⟨8,19⟩) = ⟨0.296,0.704⟩.
The true answer is ⟨0.3,0.7⟩. As more samples are collected, the estimate will converge to
the true answer. The standard deviation of the error in each probability will be proportional
to 1/√n, where n is the number of samples used in the estimate.
Now we know that rejection sampling converges to the correct answer, the next ques-
tion is, how fast does that happen? More precisely, how many samples are required before
we know that the resulting estimates are close to the correct answers with high probability?
Whereas the complexity of exact algorithms depends to a large extent on the topology of the
network—trees are easy, densely connected networks are hard—the complexity of rejection
sampling depends primarily on the fraction of samples that are accepted. This fraction is
exactly equal to the prior probability of the evidence, P(e). Unfortunately, for complex prob-
lems with many evidence variables, this fraction is vanishingly small. When applied to the
discrete version of the car insurance network in Figure 13.9, the fraction of samples consis-
tent with a typical evidence case sampled from the network itself is usually between one in a
thousand and one in ten thousand. Convergence is extremely slow (see Figure 13.19 below).
We expect the fraction of samples consistent with the evidence e to drop exponentially as
the number of evidence variables grows, so the procedure is unusable for complex problems.
It also has difﬁculties with continuous-valued evidence variables, because the probability of
producing a sample consistent with such evidence is zero (if it is really continuous-valued) or
inﬁnitesimal (if it is merely a ﬁnite-precision ﬂoating-point number).
