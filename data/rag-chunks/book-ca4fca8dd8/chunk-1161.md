---
chunk_id: "book-ca4fca8dd8-chunk-1161"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1161
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 698

698
Chapter 19
Learning from Examples
The w0 term, the intercept, stands out as different from the others. We can ﬁx that by inventing
a dummy input attribute, xj,0, which is deﬁned as always equal to 1. Then h is simply the
dot product of the weights and the input vector (or equivalently, the matrix product of the
transpose of the weights and the input vector):
hw(x j) = w·xj = w⊤xj = ∑
i
wixj,i .
The best vector of weights, w∗, minimizes squared-error loss over the examples:
w∗= argmin
w
∑
j
L2(yj,w·xj).
Multivariable linear regression is actually not much more complicated than the univariate
case we just covered. Gradient descent will reach the (unique) minimum of the loss function;
the update equation for each weight wi is
wi ←wi +α ∑
j
(yj −hw(xj))×xj,i .
(19.6)
With the tools of linear algebra and vector calculus, it is also possible to solve analytically
for the w that minimizes loss. Let y be the vector of outputs for the training examples, and X
be the data matrix—that is, the matrix of inputs with one n-dimensional example per row.
Data matrix
Then the vector of predicted outputs is ˆy=Xw and the squared-error loss over all the training
data is
L(w) = ∥ˆy−y∥2 = ∥Xw−y∥2 .
We set the gradient to zero:
∇wL(w) = 2X⊤(Xw−y) = 0.
Rearranging, we ﬁnd that the minimum-loss weight vector is given by
w∗= (X⊤X)−1X⊤y.
(19.7)
We call the expression (X⊤X)−1X⊤the pseudoinverse of the data matrix, and Equation (19.7)
Pseudoinverse
is called the normal equation.
Normal equation
With univariate linear regression we didn’t have to worry about overﬁtting. But with
multivariable linear regression in high-dimensional spaces it is possible that some dimension
that is actually irrelevant appears by chance to be useful, resulting in overﬁtting.
Thus, it is common to use regularization on multivariable linear functions to avoid over-
ﬁtting. Recall that with regularization we minimize the total cost of a hypothesis, counting
both the empirical loss and the complexity of the hypothesis:
Cost(h) = EmpLoss(h)+λComplexity(h).
For linear functions the complexity can be speciﬁed as a function of the weights. We can
consider a family of regularization functions:
Complexity(hw) = Lq(w) = ∑
i
|wi|q .
As with loss functions, with q=1 we have L1 regularization9, which minimizes the sum
of the absolute values; with q=2, L2 regularization minimizes the sum of squares. Which

## Page 699
