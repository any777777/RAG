---
chunk_id: "book-ca4fca8dd8-chunk-1309"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1309
confidence: "first-pass"
extraction_method: "structured-local"
---

798
Chapter 21
Learning Probabilistic Models
• Nonparametric models represent a distribution using the collection of data points.
Thus, the number of parameters grows with the training set. Nearest-neighbors methods
look at the examples nearest to the point in question, whereas kernel methods form a
distance-weighted combination of all the examples.
Statistical learning continues to be a very active area of research. Enormous strides have been
made in both theory and practice, to the point where it is possible to learn almost any model
for which exact or approximate inference is feasible.
Bibliographical and Historical Notes
The application of statistical learning techniques in AI was an active area of research in the
early years (see Duda and Hart, 1973) but became separated from mainstream AI as the
latter ﬁeld concentrated on symbolic methods. A resurgence of interest occurred shortly after
the introduction of Bayesian network models in the late 1980s; at roughly the same time,
a statistical view of neural network learning began to emerge. In the late 1990s, there was
a noticeable convergence of interests in machine learning, statistics, and neural networks,
centered on methods for creating large probabilistic models from data.
The naive Bayes model is one of the oldest and simplest forms of Bayesian network,
dating back to the 1950s. Its origins were mentioned in Chapter 12. Its surprising success is
partially explained by Domingos and Pazzani (1997). A boosted form of naive Bayes learning
won the ﬁrst KDD Cup data mining competition (Elkan, 1997). Heckerman (1998) gives an
excellent introduction to the general problem of Bayes net learning. Bayesian parameter
learning with Dirichlet priors for Bayesian networks was discussed by Spiegelhalter et al.
(1993). The beta distribution as a conjugate prior for a Bernoulli variable was ﬁrst derived
by Thomas (Bayes, 1763) and later reintroduced by Karl Pearson (1895) as a model for
skewed data; for many years it was known as a “Pearson Type I distribution.” Bayesian linear
regression is discussed in the text by Box and Tiao (1973); Minka (2010) provides a concise
summary of the derivations for the general multivariate case.
Several software packages incorporate mechanisms for statistical learning with Bayes
net models. These include BUGS (Bayesian inference Using Gibbs Sampling) (Gilks et al.,
1994; Lunn et al., 2000, 2013), JAGS (Just Another Gibbs Sampler) (Plummer, 2003), and
STAN (Carpenter et al., 2017).
The ﬁrst algorithms for learning Bayes net structures used conditional independence
tests (Pearl, 1988; Pearl and Verma, 1991). Spirtes et al. (1993) implemented a compre-
hensive approach in the TETRAD package for Bayes net learning. Algorithmic improvements
since then led to a clear victory in the 2001 KDD Cup data mining competition for a Bayes
net learning method (Cheng et al., 2002). (The speciﬁc task here was a bioinformatics prob-
lem with 139,351 features!) A structure-learning approach based on maximizing likelihood
was developed by Cooper and Herskovits (1992) and improved by Heckerman et al. (1994).
More recent algorithms have achieved quite respectable performance in the complete-
data case (Moore and Wong, 2003; Teyssier and Koller, 2005). One important component is
an efﬁcient data structure, the AD-tree, for caching counts over all possible combinations of
variables and values (Moore and Lee, 1997). Friedman and Goldszmidt (1996) pointed out
the inﬂuence of the representation of local conditional distributions on the learned structure.
