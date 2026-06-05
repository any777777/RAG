---
chunk_id: "book-ca4fca8dd8-chunk-1272"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1272
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 21.1
Statistical Learning
773
is to predict the ﬂavor of the next piece of candy.1 Despite its apparent triviality, this scenario
serves to introduce many of the major issues. The agent really does need to infer a theory of
its world, albeit a very simple one.
Bayesian learning simply calculates the probability of each hypothesis, given the data,
Bayesian learning
and makes predictions on that basis. That is, the predictions are made by using all the hy-
potheses, weighted by their probabilities, rather than by using just a single “best” hypothesis.
In this way, learning is reduced to probabilistic inference.
Let D represent all the data, with observed value d. The key quantities in the Bayesian ap-
proach are the hypothesis prior, P(hi), and the likelihood of the data under each hypothesis,
Hypothesis prior
Likelihood
P(d|hi). The probability of each hypothesis is obtained by Bayes’ rule:
P(hi |d) = αP(d|hi)P(hi).
(21.1)
Now, suppose we want to make a prediction about an unknown quantity X. Then we have
P(X |d) = ∑
i
P(X |hi)P(hi |d),
(21.2)
where each hypothesis determines a probability distribution over X. This equation shows that
predictions are weighted averages over the predictions of the individual hypotheses, where the
weight P(hi |d) is proportional to the prior probability of hi and its degree of ﬁt, according
to Equation (21.1). The hypotheses themselves are essentially “intermediaries” between the
raw data and the predictions.
For our candy example, we will assume for the time being that the prior distribution
over h1,...,h5 is given by ⟨0.1,0.2,0.4,0.2,0.1⟩, as advertised by the manufacturer. The
likelihood of the data is calculated under the assumption that the observations are i.i.d. (see
page 683), so that
P(d|hi) = ∏
j
P(dj |hi).
(21.3)
For example, suppose the bag is really an all-lime bag (h5) and the ﬁrst 10 candies are all
lime; then P(d|h3) is 0.510, because half the candies in an h3 bag are lime.2 Figure 21.1(a)
shows how the posterior probabilities of the ﬁve hypotheses change as the sequence of 10
lime candies is observed. Notice that the probabilities start out at their prior values, so h3
is initially the most likely choice and remains so after 1 lime candy is unwrapped. After 2
lime candies are unwrapped, h4 is most likely; after 3 or more, h5 (the dreaded all-lime bag)
is the most likely. After 10 in a row, we are fairly certain of our fate. Figure 21.1(b) shows
the predicted probability that the next candy is lime, based on Equation (21.2). As we would
expect, it increases monotonically toward 1.
The example shows that the Bayesian prediction eventually agrees with the true hypoth- ◀
esis. This is characteristic of Bayesian learning. For any ﬁxed prior that does not rule out the
true hypothesis, the posterior probability of any false hypothesis will, under certain techni-
cal conditions, eventually vanish. This happens simply because the probability of generating
“uncharacteristic” data indeﬁnitely is vanishingly small. (This point is analogous to one made
in the discussion of PAC learning in Chapter 19.) More important, the Bayesian prediction is
1
Statistically sophisticated readers will recognize this scenario as a variant of the urn-and-ball setup. We ﬁnd
urns and balls less compelling than candy.
2
We stated earlier that the bags of candy are very large; otherwise, the i.i.d. assumption fails to hold. Technically,
it is more correct (but less hygienic) to rewrap each candy after inspection and return it to the bag.
