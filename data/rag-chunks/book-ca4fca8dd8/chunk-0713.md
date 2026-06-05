---
chunk_id: "book-ca4fca8dd8-chunk-0713"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 713
confidence: "first-pass"
extraction_method: "structured-local"
---

428
Chapter 12
Quantifying Uncertainty
such logic rests on a subjective prior probability distribution whose effect is diminished as
more observations are collected.
The study of this relation was intended to constitute a mathematical discipline called
inductive logic, analogous to ordinary deductive logic (Carnap, 1948, 1950). Carnap was not
able to extend his inductive logic much beyond the propositional case, and Putnam (1963)
showed by adversarial arguments that some difﬁculties were inherent. More recent work by
Bacchus, Grove, Halpern, and Koller (1992) extends Carnap’s methods to ﬁrst-order theories.
The ﬁrst rigorously axiomatic framework for probability theory was proposed by Kol-
mogorov (1950, ﬁrst published in German in 1933). R´enyi (1970) later gave an axiomatic
presentation that took conditional probability, rather than absolute probability, as primitive.
In addition to de Finetti’s arguments for the validity of the axioms, Cox (1946) showed
that any system for uncertain reasoning that meets his set of assumptions is equivalent to
probability theory. This gave renewed conﬁdence to probability fans, but others were not
convinced, objecting to the assumption that belief must be represented by a single number.
Halpern (1999) describes the assumptions and shows some gaps in Cox’s original formu-
lation. Horn (2003) shows how to patch up the difﬁculties. Jaynes (2003) has a similar
argument that is easier to read.
The Rev. Thomas Bayes (1702–1761) introduced the rule for reasoning about conditional
probabilities that was posthumously named after him (Bayes, 1763). Bayes only considered
the case of uniform priors; it was Laplace who independently developed the general case.
Bayesian probabilistic reasoning has been used in AI since the 1960s, especially in medical
diagnosis. It was used not only to make a diagnosis from available evidence, but also to
select further questions and tests by using the theory of information value (Section 15.6)
when available evidence was inconclusive (Gorry, 1968; Gorry et al., 1973). One system
outperformed human experts in the diagnosis of acute abdominal illnesses (de Dombal et al.,
1974). Lucas et al. (2004) provide an overview.
These early Bayesian systems suffered from a number of problems. Because they lacked
any theoretical model of the conditions they were diagnosing, they were vulnerable to unrep-
resentative data occurring in situations for which only a small sample was available (de Dom-
bal et al., 1981). Even more fundamentally, because they lacked a concise formalism (such as
the one to be described in Chapter 13) for representing and using conditional independence
information, they depended on the acquisition, storage, and processing of enormous tables of
probabilistic data. Because of these difﬁculties, probabilistic methods for coping with uncer-
tainty fell out of favor in AI from the 1970s to the mid-1980s. Developments since the late
1980s are described in the next chapter.
The naive Bayes model for joint distributions has been studied extensively in the pat-
tern recognition literature since the 1950s (Duda and Hart, 1973). It has also been used,
often unwittingly, in information retrieval, beginning with the work of Maron (1961). The
probabilistic foundations of this technique, described further in Exercise 12.BAYS, were elu-
cidated by Robertson and Sparck Jones (1976). Domingos and Pazzani (1997) provide an
explanation for the surprising success of naive Bayesian reasoning even in domains where
the independence assumptions are clearly violated.
There are many good introductory textbooks on probability theory, including those by
Bertsekas and Tsitsiklis (2008), Ross (2015), and Grinstead and Snell (1997). DeGroot and
Schervish (2001) offer a combined introduction to probability and statistics from a Bayesian
