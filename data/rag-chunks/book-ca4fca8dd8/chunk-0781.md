---
chunk_id: "book-ca4fca8dd8-chunk-0781"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 781
confidence: "first-pass"
extraction_method: "structured-local"
---

Summary
471
The probability terms in the sum are obtained by computation on the original network, by
any of the standard inference algorithms. This equation is known as an adjustment formula;
Adjustment formula
it is a probability-weighted average of the inﬂuence of Xj and its parents on Xi, where the
weights are the priors on the parent values. The effects of intervening on multiple variables
can be computed by imagining that the individual interventions happen in sequence, each one
in turn deleting the causal inﬂuences on a variable and yielding a new, mutilated model.
13.5.2 The back-door criterion
The ability to predict the effect of any intervention is a remarkable result, but it does re-
quire accurate knowledge of the necessary conditional distributions in the model, particularly
P(xj | parents(Xj)). In many real-world settings, however, this is too much to ask. For exam-
ple, we know that “genetic factors” play a role in obesity, but we do not know which genes
play a role or the precise nature of their effects. Even in the simple story of Mary’s sprin-
kler decisions (Figure 13.15, which also applies in Figure 13.23(a)), we might know that she
checks the weather before deciding whether to turn on the sprinkler, but we might not know
how she makes her decision.
The speciﬁc reason this is problematic in this instance is that we would like to predict
the effect of turning on the sprinkler on a downstream variable such as GreenerGrass, but the
adjustment formula (Equation (13.20)) must take into account not only the direct route from
Sprinkler, but also the “back door” route via Cloudy and Rain. If we knew the value of Rain,
this back-door path would be blocked—which suggests that there might be a way to write an
adjustment formula that conditions on Rain instead of Cloudy. And indeed this is possible:
P(g|do(S=true)) = ∑
r
P(g|S=true,r)P(r)
(13.21)
In general, if we wish to ﬁnd the effect of do(Xj =xjk) on a variable Xi, the back-door
criterion allows us to write an adjustment formula that conditions on any set of variables Z
Back-door criterion
that closes the back door, so to speak. In more technical language, we want a set Z such
that Xi is conditionally independent of Parents(Xj) given Xj and Z. This is a straightforward
application of d-separation (see page 437).
The back-door criterion is a basic building block for a theory of causal reasoning that has
emerged in the past two decades. It provides a way to argue against a century of statistical
dogma asserting that only a randomized controlled trial can provide causal information.
Randomized
controlled trial
The theory has provided conceptual tools and algorithms for causal analysis in a wide range
of non-experimental and quasi-experimental settings; for computing probabilities on counter-
factual statements (“if this had happened instead, what would the probability have been?”);
for determining when ﬁndings in one population can be transferred to another; and for han-
dling all forms of missing data when learning probability models.
Summary
This chapter has described Bayesian networks, a well-developed representation for uncertain
knowledge. Bayesian networks play a role roughly analogous to that of propositional logic
for deﬁnite knowledge.
