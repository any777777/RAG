---
chunk_id: "book-ca4fca8dd8-chunk-0908"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 908
confidence: "first-pass"
extraction_method: "structured-local"
---

548
Chapter 15
Making Simple Decisions
value of an item must not be based on its price, but rather on the utility that it yields” (ital-
ics his). Utilitarian philosopher Jeremy Bentham (1823) proposed the hedonic calculus for
Hedonic calculus
weighing “pleasures” and “pains,” arguing that all decisions (not just monetary ones) could
be reduced to utility comparisons.
Bernoulli’s introduction of utility—an internal, subjective quantity—to explain human
behavior via a mathematical theory was an utterly remarkable proposal for its time. It was all
the more remarkable for the fact that unlike monetary amounts, the utility values of various
bets and prizes are not directly observable; instead, utilities are to be inferred from the pref-
erences exhibited by an individual. It would be two centuries before the implications of the
idea were fully worked out and it became broadly accepted by statisticians and economists.
The derivation of numerical utilities from preferences was ﬁrst carried out by Ram-
sey (1931); the axioms for preference in the present text are closer in form to those rediscov-
ered in Theory of Games and Economic Behavior (von Neumann and Morgenstern, 1944).
Ramsey had derived subjective probabilities (not just utilities) from an agent’s preferences;
Savage (1954) and Jeffrey (1983) carry out more recent constructions of this kind. Beardon
et al. (2002) show that a utility function does not sufﬁce to represent nontransitive preferences
and other anomalous situations.
In the post-war period, decision theory became a standard tool in economics, ﬁnance,
and management science. A ﬁeld of decision analysis emerged to aid in making policy
Decision analysis
decisions more rational in areas such as military strategy, medical diagnosis, public health,
engineering design, and resource management. The process involves a decision maker who
Decision maker
states preferences between outcomes and a decision analyst who enumerates the possible
Decision analyst
actions and outcomes and elicits preferences from the decision maker to determine the best
course of action. Von Winterfeldt and Edwards (1986) provide a nuanced perspective on
decision analysis and its relationship to human preference structures. Smith (1988) gives an
overview of the methodology of decision analysis.
Until the 1980s, multivariate decision problems were handled by constructing “decision
trees” of all possible instantiations of the variables. Inﬂuence diagrams or decision networks,
which take advantage of the same conditional independence properties as Bayesian networks,
were introduced by Howard and Matheson (1984), based on earlier work at SRI (Miller et al.,
1976). Howard and Matheson’s algorithm constructed the complete (exponentially large)
decision tree from the decision network. Shachter (1986) developed a method for making
decisions based directly on a decision network, without the creation of an intermediate deci-
sion tree. This algorithm was also one of the ﬁrst to provide complete inference for multiply
connected Bayesian networks. Nilsson and Lauritzen (2000) link algorithms for decision
networks to ongoing developments in clustering algorithms for Bayesian networks. The col-
lection by Oliver and Smith (1990) has a number of useful early articles on decision networks,
as does the 1990 special issue of the journal Networks. The text by Fenton and Neil (2018)
provides a hands-on guide to solving real-world decision problems using decision networks.
Papers on decision networks and utility modeling also appear regularly in the journals Man-
agement Science and Decision Analysis.
Surprisingly few early AI researchers adopted decision-theoretic tools after the early ap-
plications in medical decision making described in Chapter 12. One of the few exceptions
was Jerry Feldman, who applied decision theory to problems in vision (Feldman and Yaki-
movsky, 1974) and planning (Feldman and Sproull, 1977). Rule-based expert systems of the
