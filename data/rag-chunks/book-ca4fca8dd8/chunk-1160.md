---
chunk_id: "book-ca4fca8dd8-chunk-1160"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1160
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.6
Linear Regression and Classiﬁcation
697
The preceding equations cover one training example. For N training examples, we want
to minimize the sum of the individual losses for each example. The derivative of a sum is the
sum of the derivatives, so we have:
w0 ←w0 +α∑
j
(yj −hw(xj));
w1 ←w1 +α∑
j
(yj −hw(xj))×xj .
These updates constitute the batch gradient descent learning rule for univariate linear re-
Batch gradient
descent
gression (also called deterministic gradient descent). The loss surface is convex, which
means that there are no local minima to get stuck in, and convergence to the global minimum
is guaranteed (as long as we don’t pick an α that is so large that it overshoots), but may be
very slow: we have to sum over all N training examples for every step, and there may be
many steps. The problem is compounded if N is larger than the processor’s memory size. A
step that covers all the training examples is called an epoch.
Epoch
A faster variant is called stochastic gradient descent or SGD: it randomly selects a small
Stochastic gradient
descent
SGD
number of training examples at each step, and updates according to Equation (19.5). The
original version of SGD selected only one training example for each step, but it is now more
common to select a minibatch of m out of the N examples. Suppose we have N = 10,000
Minibatch
examples and choose a minibatch of size m = 100. Then on each step we have reduced the
amount of computation by a factor of 100; but because the standard error of the estimated
mean gradient is proportional to the square root of the number of examples, the standard
error increases by only a factor of 10. So even if we have to take 10 times more steps before
convergence, minibatch SGD is still 10 times faster than full batch SGD in this case.
With some CPU or GPU architectures, we can choose m to take advantage of parallel
vector operations, making a step with m examples almost as fast as a step with only a single
example. Within these constraints, we would treat m as a hyperparameter that should be tuned
for each learning problem.
Convergence of minibatch SGD is not strictly guaranteed; it can oscillate around the
minimum without settling down. We will see on page 702 how a schedule of decreasing the
learning rate, α, (as in simulated annealing) does guarantee convergence.
SGD can be helpful in an online setting, where new data are coming in one at a time, and
the stationarity assumption may not hold. (In fact, SGD is also known as online gradient
descent.) With a good choice for α a model will slowly evolve, remembering some of what
Online gradient
descent
it learned in the past, but also adapting to the changes represented by the new data.
SGD is widely applied to models other than linear regression, in particular neural net-
works. Even when the loss surface is not convex, the approach has proven effective in ﬁnding
good local minima that are close to the global minimum.
19.6.3 Multivariable linear regression
We can easily extend to multivariable linear regression problems, in which each example
Multivariable linear
regression
xj is an n-element vector.8 Our hypothesis space is the set of functions of the form
hw(xj) = w0 +w1xj,1 +···+wnxj,n = w0 +∑
i
wixj,i .
8
The reader may wish to consult Appendix A for a brief summary of linear algebra. Also, note that we use the
term “multivariable regression” to mean that the input is a vector of multiple values, but the output is a single
variable. We will use the term “multivariate regression” for the case where the output is also a vector of multiple
variables. However, other authors use the two terms interchangeably.
