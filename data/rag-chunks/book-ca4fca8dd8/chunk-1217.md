---
chunk_id: "book-ca4fca8dd8-chunk-1217"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1217
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
733
• Ensemble methods such as bagging and boosting often perform better than individual
methods. In online learning we can aggregate the opinions of experts to come arbi-
trarily close to the best expert’s performance, even when the distribution of the data are
constantly shifting.
• Building a good machine learning model requires experience in the complete develop-
ment process, from managing data to model selection and optimization, to continued
maintenance.
Bibliographical and Historical Notes
Chapter 1 covered the history of philosophical investigations into the topic of inductive learn-
ing. William of Ockham (1280–1349), the most inﬂuential philosopher of his century and a
major contributor to medieval epistemology, logic, and metaphysics, is credited with a state-
ment called “Ockham’s Razor”—in Latin, Entia non sunt multiplicanda praeter necessitatem,
and in English, “Entities are not to be multiplied beyond necessity.” Unfortunately, this laud-
able piece of advice is nowhere to be found in his writings in precisely these words (although
he did say “Pluralitas non est ponenda sine necessitate,” or “Plurality shouldn’t be posited
without necessity”). A similar sentiment was expressed by Aristotle in 350 BCE in Physics
book I, chapter VI: “For the more limited, if adequate, is always preferable.”
David Hume (1711–1776) formulated the problem of induction, recognizing that gener-
alizing from examples admits the possibility of errors, in a way that logical deduction does
not. He saw that there was no way to have a guaranteed correct solution to the problem,
but proposed the principle of uniformity of nature, which we have called stationarity. What
Ockham and Hume were getting at is that when we do induction, we are choosing from the
multitude of consistent models one that is more likely—because it is simpler and matches
our expectations. In modern day, the no free lunch theorem (Wolpert and Macready, 1997;
Wolpert, 2013) says that if a learning algorithm performs well on a certain set of problems, it
is only because it will perform poorly on a different set: if our decision tree correctly predicts
SR’s restaurant waiting behavior, it must perform poorly for some other hypothetical person
who has the opposite waiting behavior on the unobserved inputs.
Machine learning was one of the key ideas at the birth of computer science. Alan Turing
(1947) anticipated it, saying “Let us suppose we have set up a machine with certain initial
instruction tables, so constructed that these tables might on occasion, if good reason arose,
modify those tables.” Arthur Samuel (1959) deﬁned machine learning as the “ﬁeld of study
that gives computers the ability to learn without being explicitly programmed” while creating
his learning checkers program.
The ﬁrst notable use of decision trees was in EPAM, the “Elementary Perceiver And
Memorizer” (Feigenbaum, 1961), which was a simulation of human concept learning. ID3
(Quinlan, 1979) added the crucial idea of choosing the attribute with maximum entropy. The
concepts of entropy and information theory were developed by Claude Shannon to aid in the
study of communication (Shannon and Weaver, 1949). (Shannon also contributed one of the
earliest examples of machine learning, a mechanical mouse named Theseus that learned to
navigate through a maze by trial and error.) The χ2 method of tree pruning was described
by Quinlan (1986). A description of C4.5, an industrial-strength decision tree package, can
