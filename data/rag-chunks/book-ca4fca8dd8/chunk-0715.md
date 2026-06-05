---
chunk_id: "book-ca4fca8dd8-chunk-0715"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 715
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 13
PROBABILISTIC REASONING
In which we explain how to build efﬁcient network models to reason under uncertainty
according to the laws of probability theory, and how to distinguish between correlation
and causality.
Chapter 12 introduced the basic elements of probability theory and noted the importance of
independence and conditional independence relationships in simplifying probabilistic repre-
sentations of the world. This chapter introduces a systematic way to represent such relation-
ships explicitly in the form of Bayesian networks. We deﬁne the syntax and semantics of
these networks and show how they can be used to capture uncertain knowledge in a natu-
ral and efﬁcient way. We then show how probabilistic inference, although computationally
intractable in the worst case, can be done efﬁciently in many practical situations. We also
describe a variety of approximate inference algorithms that are often applicable when exact
inference is infeasible. Chapter 18 extends the basic ideas of Bayesian networks to more
expressive formal languages for deﬁning probability models.
13.1 Representing Knowledge in an Uncertain Domain
In Chapter 12, we saw that the full joint probability distribution can answer any question about
the domain, but can become intractably large as the number of variables grows. Furthermore,
specifying probabilities for possible worlds one by one is unnatural and tedious.
We also saw that independence and conditional independence relationships among vari-
ables can greatly reduce the number of probabilities that need to be speciﬁed in order to
deﬁne the full joint distribution. This section introduces a data structure called a Bayesian
network1 to represent the dependencies among variables. Bayesian networks can represent
Bayesian network
essentially any full joint probability distribution and in many cases can do so very concisely.
A Bayesian network is a directed graph in which each node is annotated with quantitative
probability information. The full speciﬁcation is as follows:
1. Each node corresponds to a random variable, which may be discrete or continuous.
2. Directed links or arrows connect pairs of nodes. If there is an arrow from node X to
node Y, X is said to be a parent of Y. The graph has no directed cycles and hence is a
directed acyclic graph, or DAG.
3. Each node Xi has associated probability information θ(Xi |Parents(Xi)) that quantiﬁes
the effect of the parents on the node using a ﬁnite number of parameters.
Parameter
1
Bayesian networks, often abbreviated to “Bayes net,” were called belief networks in the 1980s and 1990s. A
causal network is a Bayes net with additional constraints on the meaning of the arrows (see Section 13.5). The
term graphical model refers to a broader class that includes Bayesian networks.
