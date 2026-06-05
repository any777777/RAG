---
chunk_id: "book-ca4fca8dd8-chunk-1293"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1293
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 21.3
Learning with Hidden Variables: The EM Algorithm
789
Symptom1
Symptom2
Symptom3
(a)
(b)
HeartDisease
Symptom1
Symptom2
Symptom3
54
6
6
6
54
162
486
Smoking
Diet
Exercise
2
2
2
Smoking
Diet
Exercise
2
2
2
Figure 21.11 (a) A simple diagnostic network for heart disease, which is assumed to be
a hidden variable. Each variable has three possible values and is labeled with the number
of independent parameters in its conditional distribution; the total number is 78. (b) The
equivalent network with HeartDisease removed. Note that the symptom variables are no
longer conditionally independent given their parents. This network requires 708 parameters.
the network in (a) yields the network in (b); the total number of parameters increases from 78
to 708. Thus, latent variables can dramatically reduce the number of parameters required to ◀
specify a Bayesian network. This, in turn, can dramatically reduce the amount of data needed
to learn the parameters.
Hidden variables are important, but they do complicate the learning problem. In Fig-
ure 21.11(a), for example, it is not obvious how to learn the conditional distribution for
HeartDisease, given its parents, because we do not know the value of HeartDisease in each
case; the same problem arises in learning the distributions for the symptoms. This section
describes an algorithm called expectation–maximization, or EM, that solves this problem
Expectation–
maximization
in a very general way. We will show three examples and then provide a general description.
The algorithm seems like magic at ﬁrst, but once the intuition has been developed, one can
ﬁnd applications for EM in a huge range of learning problems.
21.3.1 Unsupervised clustering: Learning mixtures of Gaussians
Unsupervised clustering is the problem of discerning multiple categories in a collection of
Unsupervised
clustering
objects. The problem is unsupervised because the category labels are not given. For example,
suppose we record the spectra of a hundred thousand stars; are there different types of stars
revealed by the spectra, and, if so, how many types and what are their characteristics? We are
all familiar with terms such as “red giant” and “white dwarf,” but the stars do not carry these
labels on their hats—astronomers had to perform unsupervised clustering to identify these
categories. Other examples include the identiﬁcation of species, genera, orders, phylum, and
so on in the Linnaean taxonomy and the creation of natural kinds for ordinary objects (see
Chapter 10).
Unsupervised clustering begins with data. Figure 21.12(b) shows 500 data points, each of
which speciﬁes the values of two continuous attributes. The data points might correspond to
stars, and the attributes might correspond to spectral intensities at two particular frequencies.
