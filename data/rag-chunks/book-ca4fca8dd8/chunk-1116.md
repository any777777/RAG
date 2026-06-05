---
chunk_id: "book-ca4fca8dd8-chunk-1116"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1116
confidence: "first-pass"
extraction_method: "structured-local"
---

668
Chapter 18
Probabilistic Programming
languages such as BUGS, LIBBI (Murray, 2013), and STAN (Carpenter et al., 2017) generally
operate by constructing the full equivalent Bayesian network and then running inference on
it—Gibbs sampling in the case of BUGS, sequential Monte Carlo in the case of LIBBI, and
Hamiltonian Monte Carlo in the case of STAN. Programs in these languages can be read as
instructions for building the ground Bayes net. Breese (1992) showed how to generate only
the relevant fragment of the full network, given the query and the evidence.
Working with a grounded Bayes net means that the possible worlds visited by MCMC
are represented by a vector of values for variables in the Bayes net. The idea of directly
sampling ﬁrst-order possible worlds is due to Russell (1999). In the FACTORIE language
(McCallum et al., 2009), possible worlds in the MCMC process are represented within a
standard relational database system. The same two papers propose incremental query re-
evaluation as a way to avoid full query evaluation on each possible world.
Inference methods based on grounding are analogous to the earliest propositionalization
methods for ﬁrst-order logical inference (Davis and Putnam, 1960). For logical inference,
both resolution theorem provers and logic programming systems rely on lifting (Section 9.2)
to avoid instantiating logical variables unnecessarily.
Pfeffer et al. (1999) introduced a variable elimination algorithm that cached each com-
puted factor for reuse by later computations involving the same relations but different objects,
thereby realizing some of the computational gains of lifting. The ﬁrst truly lifted probabilistic
inference algorithm was a form of variable elimination described by Poole (2003) and sub-
sequently improved by de Salvo Braz et al. (2007). Further advances, including cases where
certain aggregate probabilities can be computed in closed form, are described by Milch et al.
(2008) and Kisynski and Poole (2009). There is now a fairly good understanding of when
lifting is possible and of its complexity (Gribkoff et al., 2014; Kazemi et al., 2017).
Methods of speeding up inference come in several ﬂavors, as noted in the chapter. Several
projects have explored more sophisticated algorithms, combined with compiler techniques
and/or learned proposals. LIBBI (Murray, 2013) introduced the ﬁrst particle Gibbs inference
for probabilistic programs; one of the ﬁrst inference compilers, with GPU support for mas-
sively parallel SMC; and use of the modeling language to deﬁne custom MCMC proposals.
Compilation of probabilistic inference is also studied by Wingate et al. (2011), Paige and
Wood (2014), Wu et al. (2016a). Claret et al. (2013), Hur et al. (2014), and Cusumano-
Towner et al. (2019) demonstrate static analysis methods for transforming probabilistic pro-
grams into more efﬁcient forms. PICTURE (Kulkarni et al., 2015) is the ﬁrst PPL that let users
apply learning from forward executions of the generative program to train fast bottom-up pro-
posals. Le et al. (2017) describe the use of deep learning techniques for efﬁcient importance
sampling in a PPL. In practice, inference algorithms for complex probability models often
use a mixture of techniques for different subsets of variables in the model. Mansinghka et al.
(2013) emphasized the idea of inference programs that apply diverse inference tactics to sub-
sets of variables chosen during inference runtime.
The collection edited by Getoor and Taskar (2007) includes many important papers on
ﬁrst-order probability models and their use in machine learning. Probabilistic programming
papers appear in all the major conferences on machine learning and probabilistic reasoning,
including NeurIPS, ICML, UAI, and AISTATS. Regular PPL workshops have been attached
to the NeurIPS and POPL (Principles of Programming Languages) conferences, and the ﬁrst
International Conference on Probabilistic Programming was held in 2018.
