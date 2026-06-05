---
chunk_id: "book-ca4fca8dd8-chunk-1183"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1183
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 713

Section 19.7
Nonparametric Models
713
-1.5
-1
-0.5
 0
 0.5
 1
 1.5
-1.5
-1
-0.5
 0
 0.5
 1
 1.5
x2
x1
 0
 0.5
 1
 1.5
 2
 2.5 0
 0.5
 1
 1.5
 2
 2.5
-3
-2
-1
 0
 1
 2
 3
x1
2
x2
2
√2x1x2
(a)
(b)
Figure 19.22 (a) A two-dimensional training set with positive examples as green ﬁlled cir-
cles and negative examples as orange open circles. The true decision boundary, x2
1 +x2
2 ≤1,
is also shown.
(b) The same data after mapping into a three-dimensional input space
(x2
1,x2
2,
√
2x1x2). The circular decision boundary in (a) becomes a linear decision boundary
in three dimensions. Figure 19.21(b) gives a closeup of the separator in (b).
evaluate dot products in some corresponding feature space. So, we can ﬁnd linear separators
in the higher-dimensional feature space F(x) simply by replacing xj ·xk in Equation (19.10)
with a kernel function K(xj,xk). Thus, we can learn in the higher-dimensional space, but we
compute only kernel functions rather than the full list of features for each data point.
The next step is to see that there’s nothing special about the kernel K(xj,xk)=(xj ·xk)2. It
corresponds to a particular higher-dimensional feature space, but other kernel functions corre-
spond to other feature spaces. A venerable result in mathematics, Mercer’s theorem (1909),
Mercer’s theorem
tells us that any “reasonable”14 kernel function corresponds to some feature space. These
feature spaces can be very large, even for innocuous-looking kernels. For example, the poly-
nomial kernel, K(xj,xk)=(1+xj ·xk)d, corresponds to a feature space whose dimension is
Polynomial kernel
exponential in d. A common kernel is the Gaussian: K(xj,xk)=e−γ|x j−xk|2.
19.7.6 The kernel trick
This then is the clever kernel trick: Plugging these kernels into Equation (19.10), optimal
Kernel trick
linear separators can be found efﬁciently in feature spaces with billions of (or even inﬁnitely
many) dimensions. The resulting linear separators, when mapped back to the original in-
put space, can correspond to arbitrarily wiggly, nonlinear decision boundaries between the
positive and negative examples.
In the case of inherently noisy data, we may not want a linear separator in some high-
dimensional space. Rather, we’d like a decision surface in a lower-dimensional space that
14 Here, “reasonable” means that the matrix K jk =K(x j,xk) is positive deﬁnite.

## Page 714
