---
chunk_id: "book-ca4fca8dd8-chunk-1285"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1285
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 21.2
Learning with Complete Data
783
θ2 is the probability of a red wrapper on a lime candy. The Bayesian hypothesis prior must
cover all three parameters—that is, we need to specify P(Θ,Θ1,Θ2). Usually, we assume
parameter independence:
Parameter
independence
P(Θ,Θ1,Θ2) = P(Θ)P(Θ1)P(Θ2).
With this assumption, each parameter can have its own beta distribution that is updated sepa-
rately as data arrive. Figure 21.6 shows how we can incorporate the hypothesis prior and any
data into a Bayesian network, in which we have a node for each parameter variable.
The nodes Θ,Θ1,Θ2 have no parents. For the ith observation of a wrapper and corre-
sponding ﬂavor of a piece of candy, we add nodes Wrapperi and Flavori. Flavori is dependent
on the ﬂavor parameter Θ:
P(Flavori =cherry|Θ=θ) = θ.
Wrapperi is dependent on Θ1 and Θ2:
P(Wrapperi =red|Flavori =cherry,Θ1 =θ1) = θ1
P(Wrapperi =red|Flavori =lime,Θ2 =θ2) = θ2 .
Now, the entire Bayesian learning process for the original Bayes net in Figure 21.2(b) can be
formulated as an inference problem in the derived Bayes net shown in Figure 21.6, where the
data and parameters become nodes. Once we have added all the new evidence nodes, we can
then query the parameter variables (in this case, Θ,Θ1,Θ2). Under this formulation there is ◀
just one learning algorithm—the inference algorithm for Bayesian networks.
Of course, the nature of these networks is somewhat different from those of Chapter 13
because of the potentially huge number of evidence variables representing the training set
and the prevalence of continuous-valued parameter variables. Exact inference may be impos-
sible except in very simple cases such as the naive Bayes model. Practitioners typically use
approximate inference methods such as MCMC (Section 13.4.2); many statistical software
packages incorporate efﬁcient implementations of MCMC for this purpose.
21.2.6 Bayesian linear regression
Here we illustrate how to apply a Bayesian approach to a standard statistical task: linear
regression. The conventional approach was described in Section 19.6 as minimizing the sum
of squared errors and reinterpreted in Section 21.2.4 as maximizing likelihood assuming a
Gaussian error model. These produce a single best hypothesis: a straight line with speciﬁc
values for the slope and intercept and a ﬁxed variance for the prediction error at any given
point. There is no measure of how conﬁdent one should be in the slope and intercept values.
Furthermore, if one is predicting a value for an unseen data point far from the observed
data points, it seems to make no sense to assume a prediction error that is the same as the
prediction error for a data point right next to an observed data point. It would seem more
sensible for the prediction error to be larger, the farther the data point is from the observed
data, because a small change in the slope will cause a large change in the predicted value for
a distant point.
The Bayesian approach ﬁxes both of these problems. The general idea, as in the preceding
section, is to place a prior on the model parameters—here, the coefﬁcients of the linear model
and the noise variance—and then to compute the parameter posterior given the data. For
multivariate data and unknown noise model, this leads to rather a lot of linear algebra, so we
