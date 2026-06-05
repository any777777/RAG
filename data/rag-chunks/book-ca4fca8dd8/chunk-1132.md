---
chunk_id: "book-ca4fca8dd8-chunk-1132"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1132
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.3
Learning Decision Trees
681
19.3.4 Generalization and overﬁtting
We want our learning algorithms to ﬁnd a hypothesis that ﬁts the training data, but more
importantly, we want it to generalize well for previously unseen data. In Figure 19.1 we saw
that a high-degree polynomial can ﬁt all the data, but has wild swings that are not warranted
by the data: it ﬁts but can overﬁt. Overﬁtting becomes more likely as the number of attributes
grows, and less likely as we increase the number of training examples. Larger hypothesis
spaces (e.g., decision trees with more nodes or polynomials with high degree) have more
capacity both to ﬁt and to overﬁt; some model classes are more prone to overﬁtting than
others.
For decision trees, a technique called decision tree pruning combats overﬁtting. Pruning
Decision tree
pruning
works by eliminating nodes that are not clearly relevant. We start with a full tree, as gener-
ated by LEARN-DECISION-TREE. We then look at a test node that has only leaf nodes as
descendants. If the test appears to be irrelevant—detecting only noise in the data—then we
eliminate the test, replacing it with a leaf node. We repeat this process, considering each test
with only leaf descendants, until each one has either been pruned or accepted as is.
The question is, how do we detect that a node is testing an irrelevant attribute? Suppose
we are at a node consisting of p positive and n negative examples. If the attribute is irrel-
evant, we would expect that it would split the examples into subsets such that each subset
has roughly the same proportion of positive examples as the whole set, p/(p+n), and so the
information gain will be close to zero.3 Thus, a low information gain is a good clue that the
attribute is irrelevant. Now the question is, how large a gain should we require in order to
split on a particular attribute?
We can answer this question by using a statistical signiﬁcance test. Such a test begins
Signiﬁcance test
by assuming that there is no underlying pattern (the so-called null hypothesis). Then the ac-
Null hypothesis
tual data are analyzed to calculate the extent to which they deviate from a perfect absence of
pattern. If the degree of deviation is statistically unlikely (usually taken to mean a 5% prob-
ability or less), then that is considered to be good evidence for the presence of a signiﬁcant
pattern in the data. The probabilities are calculated from standard distributions of the amount
of deviation one would expect to see in random sampling.
In this case, the null hypothesis is that the attribute is irrelevant and, hence, that the infor-
mation gain for an inﬁnitely large sample would be zero. We need to calculate the probability
that, under the null hypothesis, a sample of size v=n + p would exhibit the observed devi-
ation from the expected distribution of positive and negative examples. We can measure the
deviation by comparing the actual numbers of positive and negative examples in each subset,
pk and nk, with the expected numbers, ˆpk and ˆnk, assuming true irrelevance:
ˆpk = p× pk +nk
p+n
ˆnk = n× pk +nk
p+n .
A convenient measure of the total deviation is given by
∆=
d
∑
k=1
(pk −ˆpk)2
ˆpk
+ (nk −ˆnk)2
ˆnk
.
Under the null hypothesis, the value of ∆is distributed according to the χ2 (chi-squared)
3
The gain will be strictly positive except for the unlikely case where all the proportions are exactly the same.
(See Exercise 19.NNGA.)
