---
chunk_id: "book-ca4fca8dd8-chunk-0906"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 906
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
547
Summary
This chapter shows how to combine utility theory with probability to enable an agent to select
actions that will maximize its expected performance.
• Probability theory describes what an agent should believe on the basis of evidence,
utility theory describes what an agent wants, and decision theory puts the two together
to describe what an agent should do.
• We can use decision theory to build a system that makes decisions by considering all
possible actions and choosing the one that leads to the best expected outcome. Such a
system is known as a rational agent.
• Utility theory shows that an agent whose preferences between lotteries are consistent
with a set of simple axioms can be described as possessing a utility function; further-
more, the agent selects actions as if maximizing its expected utility.
• Multiattribute utility theory deals with utilities that depend on several distinct at-
tributes of states. Stochastic dominance is a particularly useful technique for making
unambiguous decisions, even without precise utility values for attributes.
• Decision networks provide a simple formalism for expressing and solving decision
problems. They are a natural extension of Bayesian networks, containing decision and
utility nodes in addition to chance nodes.
• Sometimes, solving a problem involves ﬁnding more information before making a de-
cision. The value of information is deﬁned as the expected improvement in utility
compared with making a decision without the information; it is particularly useful for
guiding the process of information-gathering prior to making a ﬁnal decision.
• When, as is often the case, it is impossible to specify the human’s utility function com-
pletely and correctly, machines must operate under uncertainty about the true objective.
This makes a signiﬁcant difference when the possibility exists for the machine to ac-
quire more information about human preferences. We showed by a simple argument
that uncertainty about preferences ensures that the machine defers to the human, to the
point of allowing itself to be switched off.
Bibliographical and Historical Notes
In the 17th century treatise L’art de Penser, or Port-Royal Logic, Arnauld (1662) states:
To judge what one must do to obtain a good or avoid an evil, it is necessary to consider
not only the good and the evil in itself, but also the probability that it happens or does not
happen; and to view geometrically the proportion that all these things have together.
Modern texts talk of utility rather than good and evil, but this statement correctly notes that
one should multiply utility by probability (“view geometrically”) to give expected utility,
and maximize that over all outcomes (“all these things”) to “judge what one must do.” It is
remarkable how much Arnauld got right, more than 350 years ago, and only 8 years after
Pascal and Fermat ﬁrst showed how to use probability correctly.
Daniel Bernoulli (1738), investigating the St. Petersburg paradox (see Exercise 15.STPT),
was the ﬁrst to realize the importance of preference measurement for lotteries, writing “the
