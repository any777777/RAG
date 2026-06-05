---
chunk_id: "book-ca4fca8dd8-chunk-1178"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1178
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.7
Nonparametric Models
709
19.7.4 Nonparametric regression
Now we’ll look at nonparametric approaches to regression rather than classiﬁcation. Fig-
ure 19.20 shows an example of some different models. In (a), we have perhaps the simplest
method of all, known informally as “connect-the-dots,” and superciliously as “piecewise-
linear nonparametric regression.” This model creates a function h(x) that, when given a query
xq, considers the training examples immediately to the left and right of xq, and interpolates
between them. When noise is low, this trivial method is actually not too bad, which is why
it is a standard feature of charting software in spreadsheets. But when the data are noisy, the
resulting function is spiky and does not generalize well.
k-nearest-neighbors regression improves on connect-the-dots. Instead of using just the
Nearest-neighbors
regression
two examples to the left and right of a query point xq, we use the k nearest neighbors. (Here
we are using k=3.). A larger value of k tends to smooth out the magnitude of the spikes,
although the resulting function has discontinuities. Figure 19.20 shows two versions of k-
nearest-neighbors regression. In (b), we have the k-nearest-neighbors average: h(x) is the
mean value of the k points, ∑yj/k. Notice that at the outlying points, near x=0 and x=14,
the estimates are poor because all the evidence comes from one side (the interior), and ignores
the trend. In (c), we have k-nearest-neighbor linear regression, which ﬁnds the best line
through the k examples. This does a better job of capturing trends at the outliers, but is still
discontinuous. In both (b) and (c), we’re left with the question of how to choose a good value
for k. The answer, as usual, is cross-validation.
Locally weighted regression (Figure 19.20(d)) gives us the advantages of nearest neigh-
Locally weighted
regression
bors, without the discontinuities. To avoid discontinuities in h(x), we need to avoid disconti-
nuities in the set of examples we use to estimate h(x). The idea of locally weighted regression
is that at each query point xq, the examples that are close to xq are weighted heavily, and the
examples that are farther away are weighted less heavily, and the farthest not at all. The
decrease in weight over distance is typically gradual, not sudden.
We decide how much to weight each example with a function known as a kernel, whose
Kernel
input is a distance between the query point and the example. A kernel function K is a de-
creasing function of distance with a maximum at 0, so that K(Distance(xj,xq)) gives higher
weight to examples xj that are closer to the query point xq for which we are trying to predict
the function value. The integral of the kernel value over the entire input space for x must be
ﬁnite—and if we choose to make the integral 1, certain calculations are easier.
Figure 19.20(d) was generated with a quadratic kernel, K(d)= max(0,1 −(2|d|/w)2),
with kernel width w=10. Other shapes, such as Gaussians, are also used. Typically, the
width matters more than the exact shape: this is a hyperparameter of the model that is best
chosen by cross-validation. If the kernels are too wide we’ll get underﬁtting and if they are
too narrow we’ll get overﬁtting. In Figure 19.20(d), a kernel width of 10 gives a smooth curve
that looks just about right.
Doing locally weighted regression with kernels is now straightforward. For a given query
point xq we solve the following weighted regression problem:
w∗= argmin
w
∑
j
K(Distance(xq,xj))(yj −w·xj)2 ,
where Distance is any of the distance metrics discussed for nearest neighbors. Then the
answer is h(xq)=w∗·xq.
