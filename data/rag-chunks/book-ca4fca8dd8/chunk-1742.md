---
chunk_id: "book-ca4fca8dd8-chunk-1742"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1742
confidence: "first-pass"
extraction_method: "structured-local"
---

1060
Chapter 28
Philosophy, Ethics, and Safety of AI
Privacy: Latanya Sweeney (Sweeney, 2002b) presents the k-anonymity model and the
idea of generalizing ﬁelds (Sweeney, 2002a). Achieving k-anonymity with minimal loss of
data is an NP-hard problem, but Bayardo and Agrawal (2005) give an approximation algo-
rithm. Cynthia Dwork (2008) describes differential privacy, and in subsequent work gives
practical examples of clever ways to apply differential privacy to get better results than the
naive approach (Dwork et al., 2014). Guo et al. (2019) describe a process for certiﬁed data
removal: if you train a model on some data, and then there is a request to delete some of the
data, this extension of differential privacy lets you modify the model and prove that it does
not make use of the deleted data. Ji et al. (2014) gives a review of the ﬁeld of privacy. Etzioni
(2004) argues for a balancing of privacy and security; individual rights and community. Fung
et al. (2018), Bagdasaryan et al. (2018) discuss the various attacks on federated learning pro-
tocols. Narayanan et al. (2011) describe how they were able to de-anonymize the obfuscated
connection graph from the 2011 Social Network Challenge by crawling the site where the
data was obtained (Flickr), and matching nodes with unusually high in-degree or out-degree
between the provided data and the crawled data. This allowed them to gain additional infor-
mation to win the challenge, and it also allowed them to uncover the true identity of nodes
in the data. Tools for user privacy are becoming available; for example, TensorFlow provides
modules for federated learning and privacy (McMahan and Andrew, 2018).
Fairness: Cathy O’Neil’s book Weapons of Math Destruction (2017) describes how var-
ious black box machine learning models inﬂuence our lives, often in unfair ways. She calls
on model builders to take responsibility for fairness, and for policy makers to impose appro-
priate regulation. Dwork et al. (2012) showed the ﬂaws with the simplistic “fairness through
unawareness” approach. Bellamy et al. (2018) present a toolkit for mitigating bias in machine
learning systems. Tram`er et al. (2016) show how an adversary can “steal” a machine learning
model by making queries against an API, Hardt et al. (2017) describe equal opportunity as
a metric for fairness. Chouldechova and Roth (2018) give an overview of the frontiers of
fairness, and Verma and Rubin (2018) give an exhaustive survey of fairness deﬁnitions.
Kleinberg et al. (2016) show that, in general, an algorithm cannot be both well-calibrated
and equal opportunity. Berk et al. (2017) give some additional deﬁnitions of types of fairness,
and again conclude that it is impossible to satisfy all aspects at once. Beutel et al. (2019) give
advice for how to put fairness metrics into practice.
Dressel and Farid (2018) report on the COMPAS recidivism scoring model. Christin
et al. (2015) and Eckhouse et al. (2019) discuss the use of predictive algorithms in the le-
gal system. Corbett-Davies et al. (2017) show that that there is a tension between ensuring
fairness and optimizing public safety, and Corbett-Davies and Goel (2018) discuss the dif-
ferences between fairness frameworks. Chouldechova (2017) advocates for fair impact: all
classes should have the same expected utility. Liu et al. (2018a) advocate for a long-term
measure of impact, pointing out that, for example, if we change the decision point for ap-
proving a loan in order to be more fair in the short run, this could have negative effect in the
long run on people who end up defaulting on a loan and thus have their credit score reduced.
Since 2014 there has been an annual conference on Fairness, Accountability, and Trans-
parency in Machine Learning. Mehrabi et al. (2019) give a comprehensive survey of bias and
fairness in machine learning, cataloging 23 kinds of bias and 10 deﬁnitions of fairness.
Trust: Explainable AI was an important topic going back to the early days of expert
systems (Neches et al., 1985), and has been making a resurgence in recent years (Biran and
