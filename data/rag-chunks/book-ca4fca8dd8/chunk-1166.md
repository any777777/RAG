---
chunk_id: "book-ca4fca8dd8-chunk-1166"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1166
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.6
Linear Regression and Classiﬁcation
701
0. We can make the equation easier to deal with by changing it into the vector dot product
form—with x0 =1 we have
−4.9x0 +1.7x1 −x2 = 0,
and we can deﬁne the vector of weights,
w = ⟨−4.9,1.7,−1⟩,
and write the classiﬁcation hypothesis
hw(x) = 1 if w·x ≥0 and 0 otherwise.
Alternatively, we can think of h as the result of passing the linear function w · x through a
threshold function:
Threshold function
hw(x) = Threshold(w·x) where Threshold(z)=1 if z ≥0 and 0 otherwise.
The threshold function is shown in Figure 19.17(a).
Now that the hypothesis hw(x) has a well-deﬁned mathematical form, we can think about
choosing the weights w to minimize the loss. In Sections 19.6.1 and 19.6.3, we did this both
in closed form (by setting the gradient to zero and solving for the weights) and by gradient
descent in weight space. Here we cannot do either of those things because the gradient is zero
almost everywhere in weight space except at those points where w·x=0, and at those points
the gradient is undeﬁned.
There is, however, a simple weight update rule that converges to a solution—that is, to
a linear separator that classiﬁes the data perfectly—provided the data are linearly separable.
For a single example (x,y), we have
wi ←wi +α(y−hw(x))×xi
(19.8)
which is essentially identical to Equation (19.6), the update rule for linear regression! This
rule is called the perceptron learning rule, for reasons that will become clear in Chapter 22.
Perceptron learning
rule
Because we are considering a 0/1 classiﬁcation problem, however, the behavior is somewhat
different. Both the true value y and the hypothesis output hw(x) are either 0 or 1, so there are
three possibilities:
• If the output is correct (i.e., y=hw(x)) then the weights are not changed.
• If y is 1 but hw(x) is 0, then wi is increased when the corresponding input xi is positive
and decreased when xi is negative. This makes sense, because we want to make w · x
bigger so that hw(x) outputs a 1.
• If y is 0 but hw(x) is 1, then wi is decreased when the corresponding input xi is positive
and increased when xi is negative. This makes sense, because we want to make w · x
smaller so that hw(x) outputs a 0.
Typically the learning rule is applied one example at a time, choosing examples at random (as
in stochastic gradient descent). Figure 19.16(a) shows a training curve for this learning rule
Training curve
applied to the earthquake/explosion data shown in Figure 19.15(a). A training curve measures
the classiﬁer performance on a ﬁxed training set as the learning process proceeds one update
at a time on that training set. The curve shows the update rule converging to a zero-error
linear separator. The “convergence” process isn’t exactly pretty, but it always works. This
particular run takes 657 steps to converge, for a data set with 63 examples, so each example
is presented roughly 10 times on average. Typically, the variation across runs is large.
