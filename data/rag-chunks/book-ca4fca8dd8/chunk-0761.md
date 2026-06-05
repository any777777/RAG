---
chunk_id: "book-ca4fca8dd8-chunk-0761"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 761
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 13.4
Approximate Inference for Bayesian Networks
459
(Any topological ordering will do.) The process goes as follows: First, the weight w is set to
1.0. Then an event is generated:
1. Cloudy is an evidence variable with value true. Therefore, we set
w ←w×P(Cloudy=true) = 0.5.
2. Sprinkler is not an evidence variable, so sample from P(Sprinkler|Cloudy=true) =
⟨0.1,0.9⟩; suppose this returns false.
3. Rain is not an evidence variable, so sample from P(Rain|Cloudy=true) = ⟨0.8,0.2⟩;
suppose this returns true.
4. WetGrass is an evidence variable with value true. Therefore, we set
w ←w×P(WetGrass=true|Sprinkler=false,Rain=true)
= 0.5×0.9 = 0.45.
Here WEIGHTED-SAMPLE returns the event [true,false,true,true] with weight 0.45, and this
is tallied under Rain=true.
Notice that Parents(Zi) can include both nonevidence variables and evidence variables.
Unlike the prior distribution P(z), the distribution QWS pays some attention to the evidence:
the sampled values for each Zi will be inﬂuenced by evidence among Zi’s ancestors. For
example, when sampling Sprinkler the algorithm pays attention to the evidence Cloudy=true
in its parent variable. On the other hand, QWS pays less attention to the evidence than does
the true posterior distribution P(z|e), because the sampled values for each Zi ignore evidence
among Zi’s non-ancestors. For example, when sampling Sprinkler and Rain the algorithm
ignores the evidence in the child variable WetGrass=true; this means it will generate many
samples with Sprinkler=false and Rain=false despite the fact that the evidence actually
rules out this case. Those samples will have zero weight.
Because likelihood weighting uses all the samples generated, it can be much more efﬁ-
cient than rejection sampling. It will, however, suffer a degradation in performance as the
number of evidence variables increases. This is because most samples will have very low
weights and hence the weighted estimate will be dominated by the tiny fraction of samples
that accord more than an inﬁnitesimal likelihood to the evidence. The problem is exacerbated
if the evidence variables occur “downstream”—that is, late in the variable ordering—because
then the nonevidence variables will have no evidence in their parents and ancestors to guide
the generation of samples. This means the samples will be mere hallucinations—simulations
that bear little resemblance to the reality suggested by the evidence.
When applied to the discrete version of the car insurance network in Figure 13.9, like-
lihood weighting is considerably more efﬁcient than rejection sampling (see Figure 13.19).
The insurance network is a relatively benign case for likelihood weighting because much of
the evidence is “upstream” and the query variables are leaf nodes of the network.
13.4.2 Inference by Markov chain simulation
Markov chain Monte Carlo (MCMC) algorithms work differently from rejection sampling
Markov chain Monte
Carlo
and likelihood weighting. Instead of generating each sample from scratch, MCMC algorithms
generate a sample by making a random change to the preceding sample. Think of an MCMC
algorithm as being in a particular current state that speciﬁes a value for every variable and
generating a next state by making random changes to the current state.
