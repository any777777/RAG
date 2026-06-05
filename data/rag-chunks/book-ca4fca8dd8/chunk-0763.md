---
chunk_id: "book-ca4fca8dd8-chunk-0763"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 763
confidence: "first-pass"
extraction_method: "structured-local"
---

460
Chapter 13
Probabilistic Reasoning
 0
 0.02
 0.04
 0.06
 0.08
 0.1
 0
 200000
 400000
 600000
 800000
 1x106
Error
Number of samples
Rejection sampling
Likelihood weighting
Figure 13.19 Performance of rejection sampling and likelihood weighting on the insurance
network. The x-axis shows the number of samples generated and the y-axis shows the maxi-
mum absolute error in any of the probability values for a query on PropertyCost.
The term Markov chain refers to a random process that generates a sequence of states.
Markov chain
(Markov chains also ﬁgure prominently in Chapters 14 and 16; the simulated annealing algo-
rithm in Chapter 4 and the WALKSAT algorithm in Chapter 7 are also members of the MCMC
family.) We begin by describing a particular form of MCMC called Gibbs sampling, which
Gibbs sampling
is especially well suited for Bayes nets. We then describe the more general Metropolis–
Hastings algorithm, which allows much greater ﬂexibility in generating samples.
Metropolis–Hastings
Gibbs sampling in Bayesian networks
The Gibbs sampling algorithm for Bayesian networks starts with an arbitrary state (with the
evidence variables ﬁxed at their observed values) and generates a next state by randomly
sampling a value for one of the nonevidence variables Xi. Recall from page 437 that Xi is in-
dependent of all other variables given its Markov blanket (its parents, children, and children’s
other parents); therefore, Gibbs sampling for Xi means sampling conditioned on the current
values of the variables in its Markov blanket. The algorithm wanders randomly around the
state space—the space of possible complete assignments—ﬂipping one variable at a time, but
keeping the evidence variables ﬁxed. The complete algorithm is shown in Figure 13.20.
Consider the query P(Rain|Sprinkler=true,WetGrass=true) for the network in Fig-
ure 13.15(a). The evidence variables Sprinkler and WetGrass are ﬁxed to their observed
values (both true), and the nonevidence variables Cloudy and Rain are initialized randomly
to, say, true and false respectively. Thus, the initial state is [true,true,false,true], where we
have marked the ﬁxed evidence values in bold. Now the nonevidence variables Zi are sam-
pled repeatedly in some random order according to a probability distribution ρ(i) for choosing
variables. For example:
1. Cloudy is chosen and then sampled, given the current values of its Markov blanket: in
this case, we sample from P(Cloudy|Sprinkler=true,Rain=false). Suppose the result
is Cloudy=false. Then the new current state is [false,true,false,true].
