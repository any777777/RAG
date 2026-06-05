---
chunk_id: "book-ca4fca8dd8-chunk-1282"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1282
confidence: "first-pass"
extraction_method: "structured-local"
---

780
Chapter 21
Learning Probabilistic Models
 0
 0.2  0.4  0.6  0.8
 1
 0  0.2 0.4 0.6 0.8 1
 0
 1
 2
 3
 4
x
y
P(y|x)
 0
 0.2
 0.4
 0.6
 0.8
 1
 0  0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1
y
x
(a)
(b)
Figure 21.4 (a) A linear–Gaussian model described as y=θ1x+θ2 plus Gaussian noise with
ﬁxed variance. (b) A set of 50 data points generated from this model and the best-ﬁt line.
x1,...,xN. Then the log likelihood is
L =
N
∑
j=1
log
1
σ
√
2π
e−
(x j−µ)2
2σ2
= N(−log
√
2π −logσ)−
N
∑
j=1
(xj −µ)2
2σ2
.
Setting the derivatives to zero as usual, we obtain
∂L
∂µ = −1
σ2 ∑N
j=1(xj −µ) = 0
⇒
µ = ∑j x j
N
∂L
∂σ = −N
σ + 1
σ3 ∑N
j=1(xj −µ)2 = 0
⇒
σ =
q
∑j(xj−µ)2
N
.
(21.4)
That is, the maximum-likelihood value of the mean is the sample average and the maximum-
likelihood value of the standard deviation is the square root of the sample variance. Again,
these are comforting results that conﬁrm “commonsense” practice.
Now consider a linear–Gaussian model with one continuous parent X and a continuous
child Y. As explained on page 440, Y has a Gaussian distribution whose mean depends
linearly on the value of X and whose standard deviation is ﬁxed. To learn the conditional
distribution P(Y |X), we can maximize the conditional likelihood
P(y|x) =
1
σ
√
2π
e−(y−(θ1x+θ2))2
2σ2
.
(21.5)
Here, the parameters are θ1, θ2, and σ. The data are a collection of (x j,yj) pairs, as illustrated
in Figure 21.4. Using the usual methods (Exercise 21.LINR), we can ﬁnd the maximum-
likelihood values of the parameters. The point here is different. If we consider just the
parameters θ1 and θ2 that deﬁne the linear relationship between x and y, it becomes clear
that maximizing the log likelihood with respect to these parameters is the same as minimizing
the numerator (y −(θ1x + θ2))2 in the exponent of Equation (21.5). This is the L2 loss, the
squared error between the actual value y and the prediction θ1x+θ2.
This is the quantity minimized by the standard linear regression procedure described in
Section 19.6. Now we can understand why: minimizing the sum of squared errors gives the
maximum-likelihood straight-line model, provided that the data are generated with Gaussian
noise of ﬁxed variance.

## Page 781
