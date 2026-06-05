---
chunk_id: "book-ca4fca8dd8-chunk-1311"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1311
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
799
The general problem of learning probability models with hidden variables and missing
data was addressed by Hartley (1958), who described the general idea of what was later
called EM and gave several examples. Further impetus came from the Baum–Welch algo-
rithm for HMM learning (Baum and Petrie, 1966), which is a special case of EM. The paper
by Dempster, Laird, and Rubin (1977), which presented the EM algorithm in general form
and analyzed its convergence, is one of the most cited papers in both computer science and
statistics. (Dempster himself views EM as a schema rather than an algorithm, since a good
deal of mathematical work may be required before it can be applied to a new family of dis-
tributions.) McLachlan and Krishnan (1997) devote an entire book to the algorithm and its
properties. The speciﬁc problem of learning mixture models, including mixtures of Gaus-
sians, is covered by Titterington et al. (1985).
Within AI, AUTOCLASS (Cheeseman et al., 1988; Cheeseman and Stutz, 1996) was the
ﬁrst successful system that used EM for mixture modeling. AUTOCLASS was applied to
a number of real-world scientiﬁc classiﬁcation tasks, including the discovery of new types
of stars from spectral data (Goebel et al., 1989) and new classes of proteins and introns in
DNA/protein sequence databases (Hunter and States, 1992).
For maximum-likelihood parameter learning in Bayes nets with hidden variables, EM
and gradient-based methods were introduced around the same time by Lauritzen (1995) and
Russell et al. (1995). The structural EM algorithm was developed by Friedman (1998) and
applied to maximum-likelihood learning of Bayes net structures with latent variables. Fried-
man and Koller (2003) describe Bayesian structure learning. Daly et al. (2011) review the
ﬁeld of Bayes net learning, providing extensive citations to the literature.
The ability to learn the structure of Bayesian networks is closely connected to the issue
of recovering causal information from data. That is, is it possible to learn Bayes nets in
such a way that the recovered network structure indicates real causal inﬂuences? For many
years, statisticians avoided this question, believing that observational data (as opposed to data
generated from experimental trials) could yield only correlational information—after all, any
two variables that appear related might in fact be inﬂuenced by a third, unknown causal
factor rather than inﬂuencing each other directly. Pearl (2000) has presented convincing
arguments to the contrary, showing that there are in fact many cases where causality can be
ascertained and developing the causal network formalism to express causes and the effects
of intervention as well as ordinary conditional probabilities.
Nonparametric density estimation, also called Parzen window density estimation, was
investigated initially by Rosenblatt (1956) and Parzen (1962). Since that time, a huge litera-
ture has developed investigating the properties of various estimators. Devroye (1987) gives a
thorough introduction. There is also a rapidly growing literature on nonparametric Bayesian
methods, originating with the seminal work of Ferguson (1973) on the Dirichlet process,
Dirichlet process
which can be thought of as a distribution over Dirichlet distributions. These methods are par-
ticularly useful for mixtures with unknown numbers of components. Ghahramani (2005) and
Jordan (2005) provide useful tutorials on the many applications of these ideas to statistical
learning. The text by Rasmussen and Williams (2006) covers the Gaussian process, which
Gaussian process
gives a way of deﬁning prior distributions over the space of continuous functions.
The material in this chapter brings together work from the ﬁelds of statistics and pattern
recognition, so the story has been told many times in many ways. Good texts on Bayesian
statistics include those by DeGroot (1970), Berger (1985), and Gelman et al. (1995). Bishop
