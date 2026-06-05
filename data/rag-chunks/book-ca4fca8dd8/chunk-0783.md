---
chunk_id: "book-ca4fca8dd8-chunk-0783"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 783
confidence: "first-pass"
extraction_method: "structured-local"
---

472
Chapter 13
Probabilistic Reasoning
• A Bayesian network is a directed acyclic graph whose nodes correspond to random
variables; each node has a conditional distribution for the node, given its parents.
• Bayesian networks provide a concise way to represent conditional independence rela-
tionships in the domain.
• A Bayesian network speciﬁes a joint probability distribution over its variables. The
probability of any given assignment to all the variables is deﬁned as the product of the
corresponding entries in the local conditional distributions. A Bayesian network is often
exponentially smaller than an explicitly enumerated joint distribution.
• Many conditional distributions can be represented compactly by canonical families of
distributions. Hybrid Bayesian networks, which include both discrete and continuous
variables, use a variety of canonical distributions.
• Inference in Bayesian networks means computing the probability distribution of a set
of query variables, given a set of evidence variables. Exact inference algorithms, such
as variable elimination, evaluate sums of products of conditional probabilities as efﬁ-
ciently as possible.
• In polytrees (singly connected networks), exact inference takes time linear in the size
of the network. In the general case, the problem is intractable.
• Random sampling techniques such as likelihood weighting and Markov chain Monte
Carlo can give reasonable estimates of the true posterior probabilities in a network and
can cope with much larger networks than can exact algorithms.
• Whereas Bayes nets capture probabilistic inﬂuences, causal networks capture causal
relationships and allow prediction of the effects of interventions as well as observations.
Bibliographical and Historical Notes
The use of networks to represent probabilistic information began early in the 20th century,
with the work of Sewall Wright on the probabilistic analysis of genetic inheritance and an-
imal growth factors (Wright, 1921, 1934). I. J. Good (1961), in collaboration with Alan
Turing, developed probabilistic representations and Bayesian inference methods that could
be regarded as a forerunner of modern Bayesian networks—although the paper is not often
cited in this context.7 The same paper is the original source for the noisy-OR model.
The inﬂuence diagram representation for decision problems, which incorporated a DAG
representation for random variables, was used in decision analysis in the late 1970s (see Chap-
ter 15), but only enumeration was used for evaluation. Judea Pearl developed the message-
passing method for inference in tree networks (Pearl, 1982a) and polytree networks (Kim
and Pearl, 1983) and explained the importance of causal rather than diagnostic probability
models. The ﬁrst expert system using Bayesian networks was CONVINCE (Kim, 1983).
As chronicled in Chapter 1, the mid-1980s saw a boom in rule-based expert systems,
which incorporated ad hoc methods for handling uncertainty. Probability was considered both
impractical and “cognitively implausible” as a basis for reasoning. Peter Cheeseman’s (1985)
7
I. J. Good was chief statistician for Turing’s code-breaking team in World War II. In 2001: A Space Odyssey
(Clarke, 1968), Good and Minsky are credited with making the breakthrough that led to the development of the
HAL 9000 computer.
