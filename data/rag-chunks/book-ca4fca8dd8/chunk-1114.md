---
chunk_id: "book-ca4fca8dd8-chunk-1114"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1114
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
667
The ﬁrst formal language for open-universe probability models was BLOG (Milch et al.,
2005; Milch, 2006), which came with a (very slow) general-purpose MCMC inference en-
gine. Laskey (2008) describes another open-universe modeling language called multi-entity
Bayesian networks. The NET-VISA global seismic monitoring system described in the text
is due to Arora et al. (2013). The Elo rating system was developed in 1959 by Arpad Elo
(1978) but is essentially the same at Thurstone’s Case V model (Thurstone, 1927). Mi-
crosoft’s TrueSkill model (Herbrich et al., 2007; Minka et al., 2018) is based on Mark Glick-
man’s (1999) Bayesian version of Elo and now runs on the infer.NET PPL.
Data association for multitarget tracking was ﬁrst described in a probabilistic setting by
Sittler (1964). The ﬁrst practical algorithm for large-scale problems was the “multiple hy-
pothesis tracker” or MHT algorithm (Reid, 1979). Important papers are collected by Bar-
Shalom and Fortmann (1988) and Bar-Shalom (1992). The development of an MCMC algo-
rithm for data association is due to Pasula et al. (1999), who applied it to trafﬁc surveillance
problems. Oh et al. (2009) provide a formal analysis and experimental comparisons to other
methods. Schulz et al. (2003) describe a data association method based on particle ﬁltering.
Ingemar Cox analyzed the complexity of data association (Cox, 1993; Cox and Hingo-
rani, 1994) and brought the topic to the attention of the vision community. He also noted
the applicability of the polynomial-time Hungarian algorithm to the problem of ﬁnding most-
likely assignments, which had long been considered an intractable problem in the tracking
community. The algorithm itself was published by Kuhn (1955), based on translations of pa-
pers published in 1931 by two Hungarian mathematicians, D´enes K¨onig and Jen¨o Egerv´ary.
The basic theorem had been derived previously, however, in an unpublished Latin manuscript
by the famous mathematician Carl Gustav Jacobi (1804–1851).
The idea that probabilistic programs could also represent complex probability models is
due to Koller et al. (1997). The ﬁrst working PPL was Avi Pfeffer’s IBAL (2001, 2007), based
on a simple functional language. BLOG can be thought of as a declarative PPL. The con-
nection between declarative and functional PPLs was explored by McAllester et al. (2008).
CHURCH (Goodman et al., 2008), a PPL built on the Scheme language, pioneered the idea
of piggybacking on an existing programming language. CHURCH also introduced the ﬁrst
MCMC inference algorithm for models with random higher-order functions and generated
interest in the cognitive science community as a way to model complex forms of human
learning (Lake et al., 2015). PPLs also connect in interesting ways to computability the-
ory (Ackerman et al., 2013) and programming language research.
In the 2010s, dozens of PPLs emerged based on a wide range of underlying programming
languages. Figaro, based on the Scala language, has been used for a wide variety of applica-
tions (Pfeffer, 2016). Gen (Cusumano-Towner et al., 2019), based on Julia and TensorFlow,
has been used for real-time machine perception as well as Bayesian structure learning for time
series data analysis. PPLs built on top of deep learning frameworks include Pyro (Bingham
et al., 2019) (built on PyTorch) and Edward (Tran et al., 2017) (built on TensorFlow).
There have been efforts to make probabilistic programming accessible to more people,
such as database and spreadsheet users. Tabular (Gordon et al., 2014) provides a spreadsheet-
like relational schema language on top of infer.NET. BayesDB (Saad and Mansinghka, 2017)
lets users combine and query probabilistic programs using an SQL-like language.
Inference in probabilistic programs has generally relied on approximate methods because
exact algorithms do not scale to the kinds of models that PPLs can represent. Closed-universe
