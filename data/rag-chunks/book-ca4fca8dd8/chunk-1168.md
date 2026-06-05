---
chunk_id: "book-ca4fca8dd8-chunk-1168"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1168
confidence: "first-pass"
extraction_method: "structured-local"
---

702
Chapter 19
Learning from Examples
 0.4
 0.5
 0.6
 0.7
 0.8
 0.9
 1
 0  100 200 300 400 500 600 700
Proportion correct
Number of weight updates
 0.4
 0.5
 0.6
 0.7
 0.8
 0.9
 1
 0
 25000  50000 75000
Proportion correct
Number of weight updates
 0.4
 0.5
 0.6
 0.7
 0.8
 0.9
 1
 0
 25000 50000 75000
Proportion correct
Number of weight updates
(a)
(b)
(c)
Figure 19.16 (a) Plot of total training-set accuracy vs. number of iterations through the
training set for the perceptron learning rule, given the earthquake/explosion data in Fig-
ure 19.15(a). (b) The same plot for the noisy, nonseparable data in Figure 19.15(b); note
the change in scale of the x-axis. (c) The same plot as in (b), with a learning rate schedule
α(t)=1000/(1000+t).
We have said that the perceptron learning rule converges to a perfect linear separator
when the data points are linearly separable; but what if they are not? This situation is all
too common in the real world. For example, Figure 19.15(b) adds back in the data points
left out by Kebeasy et al. (1998) when they plotted the data shown in Figure 19.15(a). In
Figure 19.16(b), we show the perceptron learning rule failing to converge even after 10,000
steps: even though it hits the minimum-error solution (three errors) many times, the algorithm
keeps changing the weights. In general, the perceptron rule may not converge to a stable
solution for ﬁxed learning rate α, but if α decays as O(1/t) where t is the iteration number,
then the rule can be shown to converge to a minimum-error solution when examples are
presented in a random sequence.10 It can also be shown that ﬁnding the minimum-error
solution is NP-hard, so one expects that many presentations of the examples will be required
for convergence to be achieved. Figure 19.16(c) shows the training process with a learning
rate schedule α(t)=1000/(1000+t): convergence is not perfect after 100,000 iterations, but
it is much better than the ﬁxed-α case.
19.6.5 Linear classiﬁcation with logistic regression
We have seen that passing the output of a linear function through the threshold function
creates a linear classiﬁer; yet the hard nature of the threshold causes some problems: the hy-
pothesis hw(x) is not differentiable and is in fact a discontinuous function of its inputs and its
weights. This makes learning with the perceptron rule a very unpredictable adventure. Fur-
thermore, the linear classiﬁer always announces a completely conﬁdent prediction of 1 or 0,
even for examples that are very close to the boundary; it would be better if it could classify
some examples as a clear 0 or 1, and others as unclear borderline cases.
All of these issues can be resolved to a large extent by softening the threshold function—
approximating the hard threshold with a continuous, differentiable function. In Chapter 13
(page 442), we saw two functions that look like soft thresholds: the integral of the standard
normal distribution (used for the probit model) and the logistic function (used for the logit
10 Technically, we require that ∑∞
t =1 α(t)=∞and ∑∞
t =1 α2(t) < ∞. The learning rate α(t)=O(1/t) satisﬁes these
conditions. Often we use c/(c+t) for some fairly large constant c.
