---
chunk_id: "book-ca4fca8dd8-chunk-1071"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1071
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 18
PROBABILISTIC PROGRAMMING
In which we explain the idea of universal languages for probabilistic knowledge represen-
tation and inference in uncertain domains.
The spectrum of representations—atomic, factored, and structured—has been a persistent
theme in AI. For deterministic models, search algorithms assume only an atomic represen-
tation; CSPs and propositional logic provide factored representations; and ﬁrst-order logic
and planning systems take advantage of structured representations. The expressive power
afforded by structured representations yields models that are vastly more concise than the
equivalent factored or atomic descriptions.
For probabilistic models, Bayesian networks as described in Chapters 13 and 14 are fac-
tored representations: the set of random variables is ﬁxed and ﬁnite, and each has a ﬁxed
range of possible values. This fact limits the applicability of Bayesian networks, because the
Bayesian network representation for a complex domain is simply too large. This makes it
infeasible to construct such representations by hand and infeasible to learn them from any
reasonable amount of data.
The problem of creating an expressive formal language for probabilistic information has
taxed some of the greatest minds in history, including Gottfried Leibniz (the co-inventor of
calculus), Jacob Bernoulli (discoverer of e, the calculus of variations, and the Law of Large
Numbers), Augustus De Morgan, George Boole, Charles Sanders Peirce (one of the principal
logicians of the 19th century), John Maynard Keynes (the leading economist of the 20th
century), and Rudolf Carnap (one of the greatest analytical philosophers of the 20th century).
The problem resisted these and many other efforts until the 1990s.
Thanks in part to the development of Bayesian networks, there are now mathematically
elegant and eminently practical formal languages that allow the creation of probabilistic mod-
els for very complex domains. These languages are universal in the same sense that Turing
machines are universal: they can represent any computable probability model, just as Turing
machines can represent any computable function. In addition, these languages come with
general-purpose inference algorithms, roughly analogous to sound and complete logical in-
ference algorithms such as resolution.
There are two routes to introducing expressive power into probability theory. The ﬁrst
is via logic: to devise a language that deﬁnes probabilities over ﬁrst-order possible worlds,
rather than the propositional possible worlds of Bayes nets. This route is covered in Sec-
tions 18.1 and 18.2, with Section 18.3 covering the speciﬁc case of temporal reasoning. The
second route is via traditional programming languages: we introduce stochastic elements—
random choices, for example—into such languages, and view programs as deﬁning probabil-
ity distributions over their own execution traces. This approach is covered in Section 18.4.
