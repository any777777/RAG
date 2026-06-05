---
chunk_id: "book-ca4fca8dd8-chunk-0757"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 757
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 13.4
Approximate Inference for Bayesian Networks
457
Notice that rejection sampling is very similar to the estimation of conditional probabilities
in the real world. For example, to estimate the conditional probability that any humans survive
after a 1km-diameter asteroid crashes into the Earth, one can simply count how often any
humans survive after a 1km-diameter asteroid crashes into the Earth, ignoring all those days
when no such event occurs. (Here, the universe itself plays the role of the sample-generation
algorithm.) To get a decent estimate, one might need to wait for 100 such events to occur.
Obviously, this could take a long time, and that is the weakness of rejection sampling.
Importance sampling
The general statistical technique of importance sampling aims to emulate the effect of sam-
Importance sampling
pling from a distribution P using samples from another distribution Q. We ensure that the
answers are correct in the limit by applying a correction factor P(x)/Q(x), also known as a
weight, to each sample x when counting up the samples.
The reason for using importance sampling in Bayes nets is simple: we would like to sam-
ple from the true posterior distribution conditioned on all the evidence, but usually this is too
hard;6 so instead, we sample from an easy distribution and apply the necessary corrections.
The reason why importance sampling works is also simple. Let the nonevidence variables be
Z. If we could sample directly from P(z|e), we could construct estimates like this:
ˆP(z|e) = NP(z)
N
≈P(z|e)
where NP(z) is the number of samples with Z=z when sampling from P. Now suppose
instead that we sample from Q(z). The estimate in this case includes the correction factors:
ˆP(z|e) = NQ(z)
N
P(z|e)
Q(z) ≈Q(z)P(z|e)
Q(z) = P(z|e).
Thus, the estimate converges to the correct value regardless of which sampling distribution
Q is used. (The only technical requirement is that Q(z) should not be zero for any z where
P(z|e) is nonzero.) Intuitively, the correction factor compensates for oversampling or under-
sampling. For example, if Q(z) is much bigger than P(z|e) for some z, then there will be
many more samples of that z than there should be, but each will have a small weight, so it
works out just as if there were the right number.
As for which Q to use, we want one that is easy to sample from and as close as possible
to the true posterior P(z|e). The most common approach is called likelihood weighting (for
Likelihood weighting
reasons we will see shortly). As shown in the WEIGHTED-SAMPLE function in Figure 13.18,
the algorithm ﬁxes the values for the evidence variables E and samples all the nonevidence
variables in topological order, each conditioned on its parents. This guarantees that each
event generated is consistent with the evidence.
Let’s call the sampling distribution produced by this algorithm QWS. If the nonevidence
variables are Z={Z1,...,Zl}, then we have
QWS(z) =
l
∏
i=1
P(zi | parents(Zi))
(13.8)
6
If it was easy, then we could approximate the desired probability to arbitrary accuracy with a polynomial
number of samples. It can be shown that no such polynomial-time approximation scheme can exist.
