---
chunk_id: "book-ca4fca8dd8-chunk-1158"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1158
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.6
Linear Regression and Classiﬁcation
695
Figure 19.13(a) shows an example of a training set of n points in the x,y plane, each point
representing the size in square feet and the price of a house offered for sale. The task of
ﬁnding the hw that best ﬁts these data is called linear regression. To ﬁt a line to the data, all
Linear regression
we have to do is ﬁnd the values of the weights ⟨w0,w1⟩that minimize the empirical loss. It
is traditional (going back to Gauss6) to use the squared-error loss function, L2, summed over
all the training examples:
Loss(hw) =
N
∑
j=1
L2(yj,hw(xj)) =
N
∑
j=1
(yj −hw(xj))2 =
N
∑
j=1
(y j −(w1xj +w0))2 .
We would like to ﬁnd w∗= argminw Loss(hw). The sum ∑N
j=1(yj −(w1xj + w0))2 is mini-
mized when its partial derivatives with respect to w0 and w1 are zero:
∂
∂w0
N
∑
j=1
(yj −(w1x j +w0))2 = 0 and
∂
∂w1
N
∑
j=1
(yj −(w1xj +w0))2 = 0.
(19.2)
These equations have a unique solution:
w1 = N(∑xjyj)−(∑xj)(∑yj)
N(∑x2
j)−(∑xj)2
; w0 =(∑yj −w1(∑xj))/N .
(19.3)
For the example in Figure 19.13(a), the solution is w1 =0.232, w0 = 246, and the line with
those weights is shown as a dashed line in the ﬁgure.
Many forms of learning involve adjusting weights to minimize a loss, so it helps to have a
mental picture of what’s going on in weight space—the space deﬁned by all possible settings
Weight space
of the weights. For univariate linear regression, the weight space deﬁned by w0 and w1 is
two-dimensional, so we can graph the loss as a function of w0 and w1 in a 3D plot (see
Figure 19.13(b)). We see that the loss function is convex, as deﬁned on page 140; this is true
for every linear regression problem with an L2 loss function, and implies that there are no
local minima. In some sense that’s the end of the story for linear models; if we need to ﬁt
lines to data, we apply Equation (19.3).7
19.6.2 Gradient descent
The univariate linear model has the nice property that it is easy to ﬁnd an optimal solution
where the partial derivatives are zero. But that won’t always be the case, so we introduce here
a method for minimizing loss that does not depend on solving to ﬁnd zeroes of the derivatives,
and can be applied to any loss function, no matter how complex.
As discussed in Section 4.2 (page 137) we can search through a continuous weight space
by incrementally modifying the parameters. There we called the algorithm hill climbing, but
here we are minimizing loss, not maximizing gain, so we will use the term gradient descent.
Gradient descent
We choose any starting point in weight space—here, a point in the (w0, w1) plane—and
then compute an estimate of the gradient and move a small amount in the steepest downhill
direction, repeating until we converge on a point in weight space with (local) minimum loss.
6
Gauss showed that if the yj values have normally distributed noise, then the most likely values of w1 and w0
are obtained by using L2 loss, minimizing the sum of the squares of the errors. (If the values have noise that
follows a Laplace (double exponential) distribution, then L1 loss is appropriate.)
7
With some caveats: the L2 loss function is appropriate when there is normally distributed noise that is inde-
pendent of x; all results rely on the stationarity assumption; etc.
