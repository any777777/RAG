---
chunk_id: "book-ca4fca8dd8-chunk-1174"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1174
confidence: "first-pass"
extraction_method: "structured-local"
---

706
Chapter 19
Learning from Examples
attribute values, the number of attributes on which the two points differ is called the Ham-
ming distance. Often Euclidean distance is used if the dimensions are measuring similar
Hamming distance
properties, such as the width, height and depth of parts, and Manhattan distance is used if
they are dissimilar, such as age, weight, and gender of a patient. Note that if we use the raw
numbers from each dimension then the total distance will be affected by a change in units
in any dimension. That is, if we change the height dimension from meters to miles while
keeping the width and depth dimensions the same, we’ll get different nearest neighbors. And
how do we compare a difference in age to a difference in weight? A common approach is
to apply normalization to the measurements in each dimension. We can compute the mean
Normalization
µi and standard deviation σi of the values in each dimension, and rescale them so that xj,i
becomes (xj,i −µi)/σi. A more complex metric known as the Mahalanobis distance takes
Mahalanobis
distance
into account the covariance between dimensions.
In low-dimensional spaces with plenty of data, nearest neighbors works very well: we
are likely to have enough nearby data points to get a good answer. But as the number of
dimensions rises we encounter a problem: the nearest neighbors in high-dimensional spaces
are usually not very near! Consider k-nearest-neighbors on a data set of N points uniformly
distributed throughout the interior of an n-dimensional unit hypercube. We’ll deﬁne the k-
neighborhood of a point as the smallest hypercube that contains the k nearest neighbors. Let
ℓbe the average side length of a neighborhood. Then the volume of the neighborhood (which
contains k points) is ℓn and the volume of the full cube (which contains N points) is 1. So, on
average, ℓn =k/N. Taking nth roots of both sides we get ℓ= (k/N)1/n.
To be concrete, let k=10 and N =1,000,000. In two dimensions (n=2; a unit square),
the average neighborhood has ℓ=0.003, a small fraction of the unit square, and in 3 dimen-
sions ℓis just 2% of the edge length of the unit cube. But by the time we get to 17 dimensions,
ℓis half the edge length of the unit hypercube, and in 200 dimensions it is 94%. This problem
has been called the curse of dimensionality.
Curse of
dimensionality
Another way to look at it: consider the points that fall within a thin shell making up the
outer 1% of the unit hypercube. These are outliers; in general it will be hard to ﬁnd a good
value for them because we will be extrapolating rather than interpolating. In one dimension,
these outliers are only 2% of the points on the unit line (those points where x < .01 or x > .99),
but in 200 dimensions, over 98% of the points fall within this thin shell—almost all the points
are outliers. You can see an example of a poor nearest-neighbors ﬁt on outliers if you look
ahead to Figure 19.20(b).
The NN(k,xq) function is conceptually trivial: given a set of N examples and a query xq,
iterate through the examples, measure the distance to xq from each one, and keep the best k.
If we are satisﬁed with an implementation that takes O(N) execution time, then that is the
end of the story. But instance-based methods are designed for large data sets, so we would
like something faster. The next two subsections show how trees and hash tables can be used
to speed up the computation.
19.7.2 Finding nearest neighbors with k-d trees
A balanced binary tree over data with an arbitrary number of dimensions is called a k-d
tree, for k-dimensional tree. The construction of a k-d tree is similar to the construction of a
K-d tree
balanced binary tree. We start with a set of examples and at the root node we split them along
the ith dimension by testing whether xi ≤m, where m is the median of the examples along
