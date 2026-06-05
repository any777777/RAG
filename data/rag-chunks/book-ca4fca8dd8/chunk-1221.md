---
chunk_id: "book-ca4fca8dd8-chunk-1221"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1221
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
735
used instead and have produced excellent results in practice. The text by Li and Vitanyi (2008)
is the best source for Kolmogorov complexity.
The theory of PAC learning was inaugurated by Leslie Valiant (1984), stressing the
importance of computational and sample complexity. With Michael Kearns (1990), Valiant
showed that several concept classes cannot be PAC-learned tractably, even though sufﬁcient
information is available in the examples. Some positive results were obtained for classes such
as decision lists (Rivest, 1987).
An independent tradition of sample-complexity analysis has existed in statistics, begin-
ning with the work on uniform convergence theory (Vapnik and Chervonenkis, 1971). The
so-called VC dimension provides a measure roughly analogous to, but more general than, the
VC dimension
ln|H| measure obtained from PAC analysis. The VC dimension can be applied to continuous
function classes, to which standard PAC analysis does not apply. PAC-learning theory and
VC theory were ﬁrst connected by the “four Germans” (none of whom actually is German):
Blumer, Ehrenfeucht, Haussler, and Warmuth (1989).
Linear regression with squared error loss goes back to Legendre (1805) and Gauss
(1809), who were both working on predicting orbits around the sun. (Gauss claimed to be us-
ing the technique since 1795, but delayed in publishing it.) The modern use of multivariable
regression for machine learning is covered in texts such as Bishop (2007). The differences
between L1 and L2 regularization are analyzed by Ng (2004) and Moore and DeNero (2011).
The term logistic function comes from Pierre-Franc¸ois Verhulst (1804–1849), a statisti-
cian who used the curve to model population growth with limited resources, a more realis-
tic model than the unconstrained geometric growth proposed by Thomas Malthus. Verhulst
called it the courbe logistique, because of its relation to the logarithmic curve. The term curse
of dimensionality comes from Richard Bellman (1961).
Logistic regression can be solved with gradient descent or with the Newton–Raphson
method (Newton, 1671; Raphson, 1690). A variant of the Newton method called L-BFGS
is often used for large-dimensional problems; the L stands for “limited memory,” meaning
that it avoids creating the full matrices all at once, and instead creates parts of them on the
ﬂy. BFGS are the authors’ initials (Byrd et al., 1995). The idea of gradient descent goes
back to Cauchy (1847); stochastic gradient descent (SGD) was introduced in the statistical
optimization community by Robbins and Monro (1951), rediscovered for neural networks by
Rosenblatt (1960), and popularized for large-scale machine learning by Bottou and Bousquet
(2008). Bottou et al. (2018) reconsider the topic of large-scale learning with a decade of
additional experience.
Nearest-neighbors models date back at least to Fix and Hodges (1951) and have been a
standard tool in statistics and pattern recognition ever since. Within AI, they were popularized
by Stanﬁll and Waltz (1986), who investigated methods for adapting the distance metric to the
data. Hastie and Tibshirani (1996) developed a way to localize the metric to each point in the
space, depending on the distribution of data around that point. Gionis et al. (1999) introduced
locality-sensitive hashing (LSH), which revolutionized the retrieval of similar objects in high-
dimensional spaces. Andoni and Indyk (2006) provide a survey of LSH and related methods,
and Samet (2006) covers properties of high-dimensional spaces. The technique is particularly
useful for genomic data, where each record has millions of attributes (Berlin et al., 2015).
The ideas behind kernel machines come from Aizerman et al. (1964) (who also in-
troduced the kernel trick), but the full development of the theory is due to Vapnik and his
