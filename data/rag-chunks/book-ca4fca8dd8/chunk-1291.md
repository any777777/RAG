---
chunk_id: "book-ca4fca8dd8-chunk-1291"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1291
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 21.2
Learning with Complete Data
787
 0
 0.2  0.4  0.6  0.8
 1  0
 0.2
 0.4
 0.6
 0.8
 1
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
Density
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0.9
 1
 0
 0.2
 0.4
 0.6
 0.8
 1
(a)
(b)
Figure 21.8 (a) A 3D plot of the mixture of Gaussians from Figure 21.12(a). (b) A 128-point
sample of points from the mixture, together with two query points (small orange squares) and
their 10-nearest-neighborhoods (large circle and smaller circle to the right).
21.2.8 Density estimation with nonparametric models
It is possible to learn a probability model without making any assumptions about its structure
and parameterization by adopting the nonparametric methods of Section 19.7. The task of
nonparametric density estimation is typically done in continuous domains, such as that
Nonparametric
density estimation
shown in Figure 21.8(a). The ﬁgure shows a probability density function on a space deﬁned
by two continuous variables. In Figure 21.8(b) we see a sample of data points from this
density function. The question is, can we recover the model from the samples?
First we will consider k-nearest-neighbors models. (In Chapter 19 we saw nearest-
neighbor models for classiﬁcation and regression; here we see them for density estimation.)
Given a sample of data points, to estimate the unknown probability density at a query point x
we can simply measure the density of the data points in the neighborhood of x. Figure 21.8(b)
shows two query points (small squares). For each query point we have drawn the smallest
circle that encloses 10 neighbors—the 10-nearest-neighborhood. We can see that the central
circle is large, meaning there is a low density there, and the circle on the right is small,
meaning there is a high density there. In Figure 21.9 we show three plots of density estimation
using k-nearest-neighbors, for different values of k. It seems clear that (b) is about right, while
(a) is too spiky (k is too small) and (c) is too smooth (k is too big).
Another possibility is to use kernel functions, as we did for locally weighted regression.
To apply a kernel model to density estimation, assume that each data point generates its
own little density function. For example, we might use spherical Gaussians with standard
deviation w along each axis. Then estimated density at a query point x is the average of the
data kernels:
P(x) = 1
N
N
∑
j=1
K(x,xj)
where
K(x,xj) =
1
(w2√
2π)d e−
D(x,x j)2
2w2
,
where d is the number of dimensions in x and D is the Euclidean distance function. We
