---
chunk_id: "book-ca4fca8dd8-chunk-1108"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1108
confidence: "first-pass"
extraction_method: "structured-local"
---

664
Chapter 18
Probabilistic Programming
Likelihood weighting works well only when the data are reasonably likely according
to the model. In more difﬁcult cases, MCMC is usually the method of choice. MCMC
applied to probabilistic programs involves sampling and modifying execution traces. Many
of the considerations arising with OUPMs also apply here; in addition, the algorithm has to
be careful about modiﬁcations to an execution trace, such as changing the outcome of an
if-statement, that may invalidate the remainder of the trace.
Further improvements in inference come from several lines of work. Some improvements
can produce fundamental shifts in the class of problems that are tractable with a given PPL,
even in principle; lifted inference, described earlier for RPMs, can have this effect. In many
cases, generic MCMC is too slow, and special-purpose proposals are needed to enable the
inference process to mix quickly.
An important focus of recent work in PPLs has been to make it easy for users to deﬁne and
use such proposals so that the efﬁciency of PPL inference matches that of custom inference
algorithms devised for speciﬁc models.
Many promising approaches are aimed at reducing the overhead of probabilistic infer-
ence. The compilation idea described for Bayes nets in Section 13.4.3 can be applied to
inference in OUPMs and PPLs, and typically yields speedups of two to three orders of mag-
nitude. There have also been proposals for special-purpose hardware for algorithms such
as message-passing and MCMC. For example, Monte Carlo hardware exploits low-precision
probability representations and massive ﬁne-grained parallelism to deliver 100–10,000x im-
provements in speed and energy efﬁciency.
Methods based on learning can also give substantial improvements in speed. For exam-
ple, adaptive proposal distributions can gradually learn how to generate MCMC proposals
Adaptive proposal
distribution
that are reasonably likely to be accepted and reasonably effective in exploring the probabil-
ity landscape of the model to ensure rapid mixing. It is also possible to train deep learning
models (see Chapter 22) to represent proposal distributions for importance sampling, using
synthetic data that was generated from the underlying model.
In general, one expects that any formalism built on top of general programming languages
will run up against the barrier of computability, and this is the case for PPLs. If we assume,
however, that the underlying program halts for all inputs and all random choices, does the
additional requirement of doing probabilistic inference still render the problem undecidable?
It turns out that the answer is yes, but only for a computational model with inﬁnite-precision
continuous random variables. In that case, it becomes possible to write a computable proba-
bility model in which inference encodes the halting problem. On the other hand, with ﬁnite-
precision numbers and with the smooth probability distributions typically used in real appli-
cations, inference remains decidable.
Summary
This chapter has explored expressive representations for probability models based on both
logic and programs.
• Relational probability models (RPMs) deﬁne probability models on worlds derived
from the database semantics for ﬁrst-order languages; they are appropriate when all
the objects and their identities are known with certainty.
