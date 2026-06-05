---
chunk_id: "book-ca4fca8dd8-chunk-1360"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1360
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 828

828
Chapter 22
Deep Learning
Figure 22.9 A demonstration of how a generative model has learned to use different direc-
tions in z space to represent different aspects of faces. We can actually perform arithmetic in
z space. The images here are all generated from the learned model and show what happens
when we decode different points in z space. We start with the coordinates for the concept of
“man with glasses,” subtract off the coordinates for “man,” add the coordinates for “woman,”
and obtain the coordinates for “woman with glasses.” Images reproduced with permission
from (Radford et al., 2015).
is chosen from a zero-mean, spherical Gaussian, then x is generated from z by applying a
weight matrix W and adding spherical Gaussian noise:
P(z) = N(z;0,I)
PW(x|z) = N(x;Wz,σ2I).
The weights W (and optionally the noise parameter σ2) can be learned by maximizing the
likelihood of the data, given by
PW(x) =
Z
PW(x,z)dz = N(x;0,WW⊤+σ2I).
(22.16)
The maximization with respect to W can be done by gradient methods or by an efﬁcient
iterative EM algorithm (see Section 21.3). Once W has been learned, new data samples
can be generated directly from PW(x) using Equation (22.16). Moreover, new observations
x that have very low probability according to Equation (22.16) can be ﬂagged as potential
anomalies.
With PPCA, we usually assume that the dimensionality of z is much less than the dimen-
sionality of x, so that the model learns to explain the data as well as possible in terms of a
small number of features. These features can be extracted for use in standard classiﬁers by
computing ˆz, the expectation of PW(z|x).
Generating data from a probabilistic PCA model is straightforward: ﬁrst sample z from
its ﬁxed Gaussian prior, then sample x from a Gaussian with mean Wz. As we will see
shortly, many other generative models resemble this process, but use complicated mappings
deﬁned by deep models rather than linear mappings from z-space to x-space.
7
Standard PCA involves ﬁtting a multivariate Gaussian to the raw input data and then selecting out the longest
axes—the principal components—of that ellipsoidal distribution.

## Page 829
