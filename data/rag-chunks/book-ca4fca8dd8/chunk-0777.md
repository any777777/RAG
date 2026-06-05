---
chunk_id: "book-ca4fca8dd8-chunk-0777"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 777
confidence: "first-pass"
extraction_method: "structured-local"
---

468
Chapter 13
Probabilistic Reasoning
a consistent construction of the network to represent the joint distribution function. This
was demonstrated in Figure 13.3, where changing the node ordering produced networks that
were bushier and a lot less natural than the original network in Figure 13.2 but enabled us,
nevertheless, to represent the same distribution on all variables.
This section describes causal networks, a restricted class of Bayesian networks that for-
Causal network
bids all but causally compatible orderings. We will explore how to construct such networks,
what is gained by such construction, and how to leverage this gain in decision-making tasks.
Consider the simplest Bayesian network imaginable, a single arrow, Fire →Smoke. It
tells us that variables Fire and Smoke may be dependent, so one needs to specify the prior
P(Fire) and the conditional probability P(Smoke|Fire) in order to specify the joint distri-
bution P(Fire,Smoke). However, this distribution can be represented equally well by the
reverse arrow Fire ←Smoke, using the appropriate P(Smoke) and P(Fire|Smoke) computed
from Bayes’ rule. The idea that these two networks are equivalent, hence convey the same
information, evokes discomfort and even resistance in most people. How could they convey
the same information when we know that Fire causes Smoke and not the other way around?
In other words, we know from our experience and scientiﬁc understanding that clearing
the smoke would not stop the ﬁre and extinguishing the ﬁre will stop the smoke. We ex-
pect therefore to represent this asymmetry through the directionality of the arrow between
them. But if arrow reversal only makes things equivalent, how can we hope to represent this
important information formally?
Causal Bayesian networks, sometimes called Causal Diagrams, were devised to permit
us to represent causal asymmetries and to leverage the asymmetries towards reasoning with
causal information. The idea is to decide on arrow directionality by considerations that go
beyond probabilistic dependence and invoke a totally different type of judgment. Instead of
asking an expert whether Smoke and Fire are probabilistically dependent, as we do in ordinary
Bayesian networks, we now ask which responds to which, Smoke to Fire or Fire to Smoke?
This may sound a bit mystical, but it can be made precise through the notion of “as-
signment,” similar to the assignment operator in programming languages. If nature assigns a
value to Smoke on the basis of what nature learns about Fire, we draw an arrow from Fire to
Smoke. More importantly, if we judge that nature assigns Fire a truth value that depends on
other variables, not Smoke, we refrain from drawing the arrow Fire ←Smoke. In other words,
the value xi of each variable Xi is determined by an equation xi = fi(OtherVariables), and an
arrow Xj →Xi is drawn if and only if Xj is one of the arguments of fi.
The equation xi = fi(·) is called a structural equation, because it describes a stable
Structural equation
mechanism in nature which, unlike the probabilities that quantify a Bayesian network, re-
mains invariant to measurements and local changes in the environment.
To appreciate this stability to local changes, consider Figure 13.23(a), which depicts a
slightly modiﬁed version of the lawn sprinkler story of Figure 13.15. To represent a disabled
sprinkler, for example, we simply delete from the network all links incident to the Sprinkler
node. To represent a lawn covered by a tent, we simply delete the arrow Rain →WetGrass.
Any local reconﬁguration of the mechanisms in the environment can thus be translated, with
only minor modiﬁcation, into an isomorphic reconﬁguration of the network topology. A much
more elaborate transformation would be required had the network been constructed contrary
to causal ordering. This local stability is particularly important for representing actions or
interventions, our next topic of discussion.
