---
chunk_id: "book-ca4fca8dd8-chunk-1112"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1112
confidence: "first-pass"
extraction_method: "structured-local"
---

666
Chapter 18
Probabilistic Programming
Attaching probabilities to sentences makes it very difﬁcult to deﬁne complete and consis-
tent probability models. Each inequality constrains the underlying probability model to lie in
a half-space in the high-dimensional space of probability models. Conjoining assertions cor-
responds to intersecting the constraints. Ensuring that the intersection yields a single point is
not easy. In fact, the principal result in Gaifman (1964a) is the construction of a single prob-
ability model requiring 1) a probability for every possible ground sentence and 2) probability
constraints for inﬁnitely many existentially quantiﬁed sentences.
One solution to this problem is to write a partial theory and then “complete” it by picking
out one canonical model in the allowed set. Nilsson (1986) proposed choosing the max-
imum entropy model consistent with the speciﬁed constraints. Paskin (2002) developed a
“maximum-entropy probabilistic logic” with constraints expressed as weights (relative prob-
abilities) attached to ﬁrst-order clauses. Such models are often called Markov logic net-
works or MLNs (Richardson and Domingos, 2006) and have become a popular technique for
applications involving relational data. Maximum-entropy approaches, including MLNs, can
produce unintuitive results in some cases (Milch, 2006; Jain et al., 2007, 2010).
Beginning in the early 1990s, researchers working on complex applications noticed the
expressive limitations of Bayesian networks and developed various languages for writing
“templates” with logical variables, from which large networks could be constructed automat-
ically for each problem instance (Breese, 1992; Wellman et al., 1992). The most important
such language was BUGS (Bayesian inference Using Gibbs Sampling) (Gilks et al., 1994;
Lunn et al., 2013), which combined Bayesian networks with the indexed random variable
Indexed random
variable
notation common in statistics. (In BUGS, an indexed random variable looks like X[i], where
i has a deﬁned integer range.)
These closed-universe languages inherited the key property of Bayesian networks: every
well-formed knowledge base deﬁnes a unique, consistent probability model. Other closed-
universe languages drew on the representational and inferential capabilities of logic program-
ming (Poole, 1993; Sato and Kameya, 1997; Kersting et al., 2000) and semantic networks
(Koller and Pfeffer, 1998; Pfeffer, 2000).
Research on open-universe probability models has several origins. In statistics, the prob-
lem of record linkage arises when data records do not contain standard unique identiﬁers—
Record linkage
for example, various citations of this book might name its ﬁrst author “Stuart J. Russell” or
“S. Russell” or even “Stewart Russel.” Other authors share the name “S. Russell.”
Hundreds of companies exist solely to solve record linkage problems in ﬁnancial, med-
ical, census, and other data. Probabilistic analysis goes back to work by Dunn (1946); the
Fellegi–Sunter model (1969), which is essentially naive Bayes applied to matching, still dom-
inates current practice. Identity uncertainty is also considered in multitarget tracking (Sittler,
1964), whose history is sketched in Chapter 14.
In AI, the working assumption until the 1990s was that sensors could supply logical sen-
tences with unique identiﬁers for objects, as was the case with Shakey. In the area of natural
language understanding, Charniak and Goldman (1992) proposed a probabilistic analysis of
coreference, where two linguistic expressions (say, “Obama” and “the president”) may refer
to the same entity. Huang and Russell (1998) and Pasula et al. (1999) developed a Bayesian
analysis of identity uncertainty for trafﬁc surveillance. Pasula et al. (2003) developed a com-
plex generative model for authors, papers, and citation strings, involving both relational and
identity uncertainty, and demonstrated high accuracy for citation information extraction.
