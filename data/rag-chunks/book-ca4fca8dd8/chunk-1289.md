---
chunk_id: "book-ca4fca8dd8-chunk-1289"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1289
confidence: "first-pass"
extraction_method: "structured-local"
---

786
Chapter 21
Learning Probabilistic Models
assert that CO2 concentrations have no effect on climate—so it is important to understand
how the structure of a Bayes net can be learned from data. This section gives a brief sketch
of the main ideas.
The most obvious approach is to search for a good model. We can start with a model
containing no links and begin adding parents for each node, ﬁtting the parameters with the
methods we have just covered and measuring the accuracy of the resulting model. Alterna-
tively, we can start with an initial guess at the structure and use hill climbing or simulated
annealing search to make modiﬁcations, retuning the parameters after each change in the
structure. Modiﬁcations can include reversing, adding, or deleting links. We must not in-
troduce cycles in the process, so many algorithms assume that an ordering is given for the
variables, and that a node can have parents only among those nodes that come earlier in the
ordering (just as in the construction process in Chapter 13). For full generality, we also need
to search over possible orderings.
There are two alternative methods for deciding when a good structure has been found.
The ﬁrst is to test whether the conditional independence assertions implicit in the structure are
actually satisﬁed in the data. For example, the use of a naive Bayes model for the restaurant
problem assumes that
P(Hungry,Bar|WillWait) = P(Hungry|WillWait)P(Bar|WillWait)
and we can check in the data whether the same equation holds between the corresponding
conditional frequencies. But even if the structure describes the true causal nature of the
domain, statistical ﬂuctuations in the data set mean that the equation will never be satisﬁed
exactly, so we need to perform a suitable statistical test to see if there is sufﬁcient evidence
that the independence hypothesis is violated. The complexity of the resulting network will
depend on the threshold used for this test—the stricter the independence test, the more links
will be added and the greater the danger of overﬁtting.
An approach more consistent with the ideas in this chapter is to assess the degree to
which the proposed model explains the data (in a probabilistic sense). We must be careful
how we measure this, however. If we just try to ﬁnd the maximum-likelihood hypothesis, we
will end up with a fully connected network, because adding more parents to a node cannot
decrease the likelihood (Exercise 21.MLPA). We are forced to penalize model complexity in
some way. The MAP (or MDL) approach simply subtracts a penalty from the likelihood of
each structure (after parameter tuning) before comparing different structures. The Bayesian
approach places a joint prior over structures and parameters. There are usually far too many
structures to sum over (superexponential in the number of variables), so most practitioners
use MCMC to sample over structures.
Penalizing complexity (whether by MAP or Bayesian methods) introduces an important
connection between the optimal structure and the nature of the representation for the con-
ditional distributions in the network. With tabular distributions, the complexity penalty for
a node’s distribution grows exponentially with the number of parents, but with, say, noisy-
OR distributions, it grows only linearly. This means that learning with noisy-OR (or other
compactly parameterized) models tends to produce learned structures with more parents than
does learning with tabular distributions.
