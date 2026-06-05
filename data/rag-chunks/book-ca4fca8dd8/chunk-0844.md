---
chunk_id: "book-ca4fca8dd8-chunk-0844"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 844
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 14.5
Dynamic Bayesian Networks
509
we cannot reason efﬁciently and exactly about those processes. The DBN model itself, which
represents the prior joint distribution over all the variables, is factorable into its constituent
CPTs, but the posterior joint distribution conditioned on an observation sequence—that is,
the forward message—is generally not factorable. The problem is intractable in general, so
we must fall back on approximate methods.
14.5.3 Approximate inference in DBNs
Section 13.4 described two approximation algorithms: likelihood weighting (Figure 13.18)
and Markov chain Monte Carlo (MCMC, Figure 13.20). Of the two, the former is most easily
adapted to the DBN context. (An MCMC ﬁltering algorithm is described brieﬂy in the notes
at the end of this chapter.) We will see, however, that several improvements are required over
the standard likelihood weighting algorithm before a practical method emerges.
Recall that likelihood weighting works by sampling the nonevidence nodes of the net-
work in topological order, weighting each sample by the likelihood it accords to the observed
evidence variables. As with the exact algorithms, we could apply likelihood weighting di-
rectly to an unrolled DBN, but this would suffer from the same problems of increasing time
and space requirements per update as the observation sequence grows. The problem is that
the standard algorithm runs each sample in turn, all the way through the network.
Instead, we can simply run all N samples together through the DBN, one slice at a time.
The modiﬁed algorithm ﬁts the general pattern of ﬁltering algorithms, with the set of N sam-
ples as the forward message. The ﬁrst key innovation, then, is to use the samples themselves ◀
as an approximate representation of the current state distribution.
This meets the require-
ment of a “constant” time per update, although the constant depends on the number of samples
required to maintain an accurate approximation. There is also no need to unroll the DBN, be-
cause we need to have in memory only the current slice and the next slice. This approach is
called sequential importance sampling or SIS.
Sequential
importance sampling
In our discussion of likelihood weighting in Chapter 13, we pointed out that the algo-
rithm’s accuracy suffers if the evidence variables are “downstream” from the variables being
sampled, because in that case the samples are generated without any inﬂuence from the evi-
dence and will nearly all have very low weights.
Now if we look at the typical structure of a DBN—say, the umbrella DBN in Fig-
ure 14.16—we see that indeed the early state variables will be sampled without the beneﬁt of
the later evidence. In fact, looking more carefully, we see that none of the state variables have
any evidence variables among its ancestors! Hence, although the weight of each sample will
depend on the evidence, the actual set of samples generated will be completely independent
of the evidence. For example, even if the boss brings in the umbrella every day, the sampling
process could still hallucinate endless days of sunshine.
What this means in practice is that the fraction of samples that remain reasonably close
to the actual series of events (and therefore have non-negligible weights) drops exponentially
with t, the length of the sequence. In other words, to maintain a given level of accuracy, we
need to increase the number of samples exponentially with t. Given that a real-time ﬁltering
algorithm can use only a bounded number of samples, what happens in practice is that the
error blows up after a very small number of update steps. Figure 14.19 on page 512 shows
this effect for SIS applied to the grid-world localization problem from Section 14.3: even
with 100,000 samples, the SIS approximation fails completely after about 20 steps.
