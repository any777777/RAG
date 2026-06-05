---
chunk_id: "book-ca4fca8dd8-chunk-0771"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 771
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 13.4
Approximate Inference for Bayesian Networks
465
always reports a posterior probability for the query of ⟨1.0,0.0⟩; if it starts in [false,false] it
always reports a posterior probability for the query of ⟨0.0,1.0⟩.
Gibbs sampling fails in this case because the deterministic relationship between Cloudy
and Rain breaks the property of ergodicity that is required for convergence. If, however,
we make the relationship nearly deterministic, then convergence is restored, but happens
arbitrarily slowly. There are several ﬁxes that help MCMC algorithms mix more quickly.
One is block sampling: sampling multiple variables simultaneously. In this case, we could
Block sampling
sample Cloudy and Rain jointly, conditioned on their combined Markov blanket. Another is
to generate next states more intelligently, as we will see in the next section.
Metropolis–Hastings sampling
The Metropolis–Hastings or MH sampling method is perhaps the most broadly applicable
MCMC algorithm. Like Gibbs sampling, MH is designed to generate samples x (eventually)
according to target probabilities π(x); in the case of inference in Bayesian networks, we want
π(x)=P(x|e). Like simulated annealing (page 133), MH has two stages in each iteration of
the sampling process:
1. Sample a new state x′ from a proposal distribution q(x′ |x), given the current state x.
Proposal distribution
2. Probabilistically accept or reject x′ according to the acceptance probability
Acceptance
probability
a(x′ |x) = min

1, π(x′)q(x|x′)
π(x)q(x′ |x)

.
If the proposal is rejected, the state remains at x.
The transition kernel for MH consists of this two-step process. Note that if the proposal is
rejected, the chain stays in the same state.
The proposal distribution is responsible, as its name suggests, for proposing a next state
x′. For example, q(x′ |x) could be deﬁned as follows:
• With probability 0.95, perform a Gibbs sampling step to generate x′.
• Otherwise, generate x′ by running the WEIGHTED-SAMPLE algorithm from page 458.
This proposal distribution causes MH to do about 20 steps of Gibbs sampling then “restarts”
the process from a new state (assuming it is accepted) that is generated from scratch. By this
stratagem, it gets around the problem of Gibbs sampling getting stuck in one part of the state
space and being unable to reach the other parts.
You might ask how on Earth we know that MH with such a weird proposal actually con-
verges to the right answer. The remarkable thing about MH is that convergence to the correct ◀
stationary distribution is guaranteed for any proposal distribution, provided the resulting
transition kernel is ergodic.
This property follows from the way the acceptance probability is deﬁned. As with Gibbs
sampling, the self-loop with x=x′ automatically satisﬁes detailed balance, so we focus on
the case where x ̸= x′. This can occur only if the proposal is accepted. The probability of
such a transition occurring is
k(x →x′) = q(x′ |x)a(x′ |x).
As with Gibbs sampling, proving detailed balance means showing that the ﬂow from x to
x′, π(x)k(x →x′), matches the ﬂow from x′ to x, π(x′)k(x′ →x). After plugging in the
