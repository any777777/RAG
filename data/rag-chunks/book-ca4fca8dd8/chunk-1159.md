---
chunk_id: "book-ca4fca8dd8-chunk-1159"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1159
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 696

696
Chapter 19
Learning from Examples
 300
 400
 500
 600
 700
 800
 900
 1000
 500
 1000  1500  2000  2500  3000  3500
House price in $1000
House size in square feet
w0
w1
Loss
(a)
(b)
Figure 19.13 (a) Data points of price versus ﬂoor space of houses for sale in Berkeley, CA,
in July 2009, along with the linear function hypothesis that minimizes squared-error loss:
y = 0.232x + 246. (b) Plot of the loss function ∑j(yj −w1xj + w0)2 for various values of
w0,w1. Note that the loss function is convex, with a single global minimum.
The algorithm is as follows:
w ←any point in the parameter space
while not converged do
for each wi in w do
wi ←wi −α ∂
∂wi
Loss(w)
(19.4)
The parameter α, which we called the step size in Section 4.2, is usually called the learning
rate when we are trying to minimize loss in a learning problem. It can be a ﬁxed constant, or
Learning rate
it can decay over time as the learning process proceeds.
For univariate regression, the loss is quadratic, so the partial derivative will be linear.
(The only calculus you need to know is the chain rule: ∂g(f(x))/∂x=g′(f(x))∂f(x)/∂x,
Chain rule
plus the facts that
∂
∂xx2 =2x and
∂
∂xx=1.) Let’s ﬁrst work out the partial derivatives—the
slopes—in the simpliﬁed case of only one training example, (x,y):
∂
∂wi
Loss(w) =
∂
∂wi
(y−hw(x))2 = 2(y−hw(x))× ∂
∂wi
(y−hw(x))
= 2(y−hw(x))× ∂
∂wi
(y−(w1x+w0)).
(19.5)
Applying this to both w0 and w1 we get:
∂
∂w0
Loss(w) = −2(y−hw(x));
∂
∂w1
Loss(w) = −2(y−hw(x))×x.
Plugging this into Equation (19.4), and folding the 2 into the unspeciﬁed learning rate α, we
get the following learning rule for the weights:
w0 ←w0 +α(y−hw(x));
w1 ←w1 +α(y−hw(x))×x.
These updates make intuitive sense: if hw(x) > y (i.e., the output is too large), reduce w0 a
bit, and reduce w1 if x was a positive input but increase w1 if x was a negative input.

## Page 697
