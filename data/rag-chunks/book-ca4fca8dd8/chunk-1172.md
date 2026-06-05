---
chunk_id: "book-ca4fca8dd8-chunk-1172"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1172
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.7
Nonparametric Models
705
2.5
3
3.5
4
4.5
5
5.5
6
6.5
7
7.5
4.5
5
5.5
6
6.5
7
x1
x2
2.5
3
3.5
4
4.5
5
5.5
6
6.5
7
7.5
4.5
5
5.5
6
6.5
7
x1
x2
(k=1)
(k=5)
Figure 19.19 (a) A k-nearest-neighbors model showing the extent of the explosion class for
the data in Figure 19.15, with k=1. Overﬁtting is apparent. (b) With k=5, the overﬁtting
problem goes away for this data set.
lookup: take all the training examples, put them in a lookup table, and then when asked for
Table lookup
h(x), see if x is in the table; if it is, return the corresponding y.
The problem with this method is that it does not generalize well: when x is not in the
table we have no information about a plausible value.
19.7.1 Nearest-neighbor models
We can improve on table lookup with a slight variation: given a query xq, instead of ﬁnding
an example that is equal to xq, ﬁnd the k examples that are nearest to xq. This is called k-
nearest-neighbors lookup. We’ll use the notation NN(k,xq) to denote the set of k neighbors
Nearest neighbors
nearest to xq.
To do classiﬁcation, ﬁnd the set of neighbors NN(k,xq) and take the most common output
value—for example, if k=3 and the output values are ⟨Yes,No,Yes⟩, then the classiﬁcation
will be Yes. To avoid ties on binary classiﬁcation, k is usually chosen to be an odd number.
To do regression, we can take the mean or median of the k neighbors, or we can solve a
linear regression problem on the neighbors. The piecewise linear function from Figure 19.1
solves a (trivial) linear regression problem with the two data points to the right and left of xq.
(When the xi data points are equally spaced, these will be the two nearest neighbors.)
In Figure 19.19, we show the decision boundary of k-nearest-neighbors classiﬁcation for
k= 1 and 5 on the earthquake data set from Figure 19.15. Nonparametric methods are still
subject to underﬁtting and overﬁtting, just like parametric methods. In this case 1-nearest-
neighbors is overﬁtting; it reacts too much to the black outlier in the upper right and the white
outlier at (5.4, 3.7). The 5-nearest-neighbors decision boundary is good; higher k would
underﬁt. As usual, cross-validation can be used to select the best value of k.
The very word “nearest” implies a distance metric. How do we measure the distance from
a query point xq to an example point xj? Typically, distances are measured with a Minkowski
distance or Lp norm, deﬁned as
Minkowski distance
Lp(xj,xq) = (∑
i
|xj,i −xq,i|p)1/p .
With p=2 this is Euclidean distance and with p=1 it is Manhattan distance. With Boolean
