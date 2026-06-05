---
chunk_id: "book-ca4fca8dd8-chunk-0727"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 727
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 13.2
The Semantics of Bayesian Networks
437
. . .
. . .
U1
X
Um
Yn
Znj
Y1
Z1j
. . .
. . .
U1
Um
Yn
Znj
Y1
Z1j
X
(a)
(b)
Figure 13.4 (a) A node X is conditionally independent of its non-descendants (e.g., the Zijs)
given its parents (the Uis shown in the lavender area). (b) A node X is conditionally indepen-
dent of all other nodes in the network given its Markov blanket (the lavender area).
For example, in Figure 13.2, the variable JohnCalls is independent of Burglary, Earthquake,
and MaryCalls given the value of Alarm. The deﬁnition is illustrated in Figure 13.4(a).
It turns out that the non-descendants property combined with interpretation of the net-
work parameters θ(Xi |Parents(Xi)) as conditional probabilities P(Xi |Parents(Xi)) sufﬁces to
reconstruct the full joint distribution given in Equation (13.2). In other words, one can view
the semantics of Bayes nets in a different way: instead of deﬁning the full joint distribution as
the product of conditional distributions, the network deﬁnes a set of conditional independence
properties. The full joint distribution can be derived from those properties.
Another important independence property is implied by the non-descendants property:
a variable is conditionally independent of all other nodes in the network, given its parents,
children, and children’s parents—that is, given its Markov blanket.
Markov blanket
(Exercise 13.MARB asks you to prove this.) For example, the variable Burglary is independent
of JohnCalls and MaryCalls, given Alarm and Earthquake. This property is illustrated in Fig-
ure 13.4(b). The Markov blanket property makes possible inference algorithms that use com-
pletely local and distributed stochastic sampling processes, as explained in Section 13.4.2.
The most general conditional independence question one might ask in a Bayes net is
whether a set of nodes X is conditionally independent of another set Y, given a third set Z.
This can be determined efﬁciently by examining the Bayes net to see whether Z d-separates
D-separation
X and Y. The process works as follows:
1. Consider just the ancestral subgraph consisting of X, Y, Z, and their ancestors.
Ancestral subgraph
2. Add links between any unlinked pair of nodes that share a common child; now we have
the so-called moral graph.
Moral graph
3. Replace all directed links by undirected links.
4. If Z blocks all paths between X and Y in the resulting graph, then Z d-separates X and
Y. In that case, X is conditionally independent of Y, given Z. Otherwise, the original
Bayes net does not require conditional independence.
