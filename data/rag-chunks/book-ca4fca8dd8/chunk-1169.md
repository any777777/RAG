---
chunk_id: "book-ca4fca8dd8-chunk-1169"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1169
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 703

Section 19.6
Linear Regression and Classiﬁcation
703
 0
 0.5
 1
-6 -4 -2  0  2  4  6
 0
 0.5
 1
-6 -4 -2  0  2  4  6
-2
 0
 2
 4
 6
-4
-2
 0
 2
 4
 6
 8
 10
 0
 0.2
 0.4
 0.6
 0.8
 1
x1
x2
(a)
(b)
(c)
Figure 19.17 (a) The hard threshold function Threshold(z) with 0/1 output.
Note
that the function is nondifferentiable at z=0.
(b) The logistic function, Logistic(z) =
1
1+e−z , also known as the sigmoid function.
(c) Plot of a logistic regression hypothesis
hw(x)=Logistic(w·x) for the data shown in Figure 19.15(b).
model). Although the two functions are very similar in shape, the logistic function
Logistic(z) =
1
1+e−z
has more convenient mathematical properties. The function is shown in Figure 19.17(b).
With the logistic function replacing the threshold function, we now have
hw(x) = Logistic(w·x) =
1
1+e−w·x .
An example of such a hypothesis for the two-input earthquake/explosion problem is shown in
Figure 19.17(c). Notice that the output, being a number between 0 and 1, can be interpreted
as a probability of belonging to the class labeled 1. The hypothesis forms a soft boundary
in the input space and gives a probability of 0.5 for any input at the center of the boundary
region, and approaches 0 or 1 as we move away from the boundary.
The process of ﬁtting the weights of this model to minimize loss on a data set is called
logistic regression. There is no easy closed-form solution to ﬁnd the optimal value of w with
Logistic regression
this model, but the gradient descent computation is straightforward. Because our hypotheses
no longer output just 0 or 1, we will use the L2 loss function; also, to keep the formulas
readable, we’ll use g to stand for the logistic function, with g′ its derivative.
For a single example (x,y), the derivation of the gradient is the same as for linear re-
gression (Equation (19.5)) up to the point where the actual form of h is inserted. (For this
derivation, we again need the chain rule.) We have
∂
∂wi
Loss(w) =
∂
∂wi
(y−hw(x))2
= 2(y−hw(x))× ∂
∂wi
(y−hw(x))
= −2(y−hw(x))×g′(w·x)× ∂
∂wi
w·x
= −2(y−hw(x))×g′(w·x)×xi .

## Page 704
