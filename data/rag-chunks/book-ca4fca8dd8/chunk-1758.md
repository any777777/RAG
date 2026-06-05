---
chunk_id: "book-ca4fca8dd8-chunk-1758"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1758
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 29.2
AI Architectures
1069
ﬁeld programmable gate arrays (FPGAs) are hundreds of times faster than conventional CPUs
for machine learning training (Vasilache et al., 2014; Jouppi et al., 2017). In 2014 it took a
full day to train an ImageNet model; in 2018 it takes just 2 minutes (Ying et al., 2018).
The OpenAI Institute reports that the amount of compute power used to train the largest
machine learning models doubled every 3.5 months from 2012 to 2018, reaching over an
exaﬂop/second-day for ALPHAZERO (although they also report that some very inﬂuential
work used 100 million times less computing power (Amodei and Hernandez, 2018)). The
same economic trends that have made cell-phone cameras cheaper and better also apply to
processors—we will see continued progress in low-power, high-performance computing that
beneﬁts from economies of scale.
There is a possibility that quantum computers could accelerate AI. Currently there are
some fast quantum algorithms for the linear algebra operations used in machine learning
(Harrow et al., 2009; Dervovic et al., 2018), but no quantum computer capable of running
them. We have some example applications of tasks such as image classiﬁcation (Mott et al.,
2017) where quantum algorithms are as good as classical algorithms on small problems.
Current quantum computers handle only a few tens of bits, whereas machine learning
algorithms often handle inputs with millions of bits and create models with hundreds of mil-
lions of parameters. So we need breakthroughs in both quantum hardware and software to
make quantum computing practical for large-scale machine learning. Alternatively, there may
be a division of labor—perhaps a quantum algorithm to efﬁciently search the space of hyper-
parameters while the normal training process runs on conventional computers—but we don’t
know how to do that yet. Research on quantum algorithms can sometimes inspire new and
better algorithms on classical computers (Tang, 2018).
We have also seen exponential growth in the number of publications, people, and dollars
in AI/machine learning/data science. Dean et al. (2018) show that the number of papers
about “machine learning” on arXiv doubled every two years from 2009 to 2017. Investors are
funding startup companies in these ﬁelds, large companies are hiring and spending as they
determine their AI strategy, and governments are investing to make sure their country doesn’t
fall too far behind.
29.2 AI Architectures
It is natural to ask, “Which of the agent architectures in Chapter 2 should an agent use?” The
answer is, “All of them!” Reﬂex responses are needed for situations in which time is of the
essence, whereas knowledge-based deliberation allows the agent to plan ahead. Learning is
convenient when we have lots of data, and necessary when the environment is changing, or
when human designers have insufﬁcient knowledge of the domain.
AI has long had a split between symbolic systems (based on logical and probabilistic
inference) and connectionist systems (based on loss minimization over a large number of
uninterpreted parameters). A continuing challenge for AI is to bring these two together,
to capture the best of both. Symbolic systems allow us to string together long chains of
reasoning and to take advantage of the expressive power of structured representations, while
connectionist systems can recognize patterns even in the face of noisy data. One line of
research aims to combine probabilistic programming with deep learning, although as yet the
various proposals are limited in the extent to which the approaches are truly merged.
