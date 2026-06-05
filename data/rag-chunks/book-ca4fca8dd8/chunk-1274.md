---
chunk_id: "book-ca4fca8dd8-chunk-1274"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1274
confidence: "first-pass"
extraction_method: "structured-local"
---

774
Chapter 21
Learning Probabilistic Models
 0
 0.2
 0.4
 0.6
 0.8
 1
 0
 2
 4
 6
 8
 10
Posterior probability of hypothesis
Number of observations in d
P(h1 | d)
P(h2 | d)
P(h3 | d)
P(h4 | d)
P(h5 | d)
 0.4
 0.5
 0.6
 0.7
 0.8
 0.9
 1
 0
 2
 4
 6
 8
 10
Probability that next candy is lime
Number of observations in d
(a)
(b)
Figure 21.1 (a) Posterior probabilities P(hi |d1,...,dN) from Equation (21.1). The number
of observations N ranges from 1 to 10, and each observation is of a lime candy. (b) Bayesian
prediction P(DN+1 =lime|d1,...,dN) from Equation (21.2).
optimal, whether the data set is small or large. Given the hypothesis prior, any other predic-
tion is expected to be correct less often.
The optimality of Bayesian learning comes at a price, of course. For real learning prob-
lems, the hypothesis space is usually very large or inﬁnite, as we saw in Chapter 19. In some
cases, the summation in Equation (21.2) (or integration, in the continuous case) can be carried
out tractably, but in most cases we must resort to approximate or simpliﬁed methods.
A very common approximation—one that is usually adopted in science—is to make pre-
dictions based on a single most probable hypothesis—that is, an hi that maximizes P(hi |d).
This is often called a maximum a posteriori or MAP (pronounced “em-ay-pee”) hypothesis.
Maximum a
posteriori
Predictions made according to an MAP hypothesis hMAP are approximately Bayesian to the
extent that P(X |d) ≈P(X |hMAP). In our candy example, hMAP =h5 after three lime can-
dies in a row, so the MAP learner then predicts that the fourth candy is lime with probability
1.0—a much more dangerous prediction than the Bayesian prediction of 0.8 shown in Fig-
ure 21.1(b). As more data arrive, the MAP and Bayesian predictions become closer, because
the competitors to the MAP hypothesis become less and less probable.
Although this example doesn’t show it, ﬁnding MAP hypotheses is often much easier
than Bayesian learning, because it requires solving an optimization problem instead of a
large summation (or integration) problem.
In both Bayesian learning and MAP learning, the hypothesis prior P(hi) plays an im-
portant role. We saw in Chapter 19 that overﬁtting can occur when the hypothesis space is
too expressive, that is, when it contains many hypotheses that ﬁt the data set well. Bayesian
and MAP learning methods use the prior to penalize complexity. Typically, more complex
hypotheses have a lower prior probability—in part because there so many of them. On the
other hand, more complex hypotheses have a greater capacity to ﬁt the data. (In the extreme
case, a lookup table can reproduce the data exactly.) Hence, the hypothesis prior embodies a
tradeoff between the complexity of a hypothesis and its degree of ﬁt to the data.
