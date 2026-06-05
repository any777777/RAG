---
chunk_id: "book-ca4fca8dd8-chunk-1276"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1276
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 21.2
Learning with Complete Data
775
We can see the effect of this tradeoff most clearly in the logical case, where H contains
only deterministic hypotheses (such as h1, which says that every candy is cherry). In that
case, P(d|hi) is 1 if hi is consistent and 0 otherwise. Looking at Equation (21.1), we see
that hMAP will then be the simplest logical theory that is consistent with the data. Therefore, ◀
maximum a posteriori learning provides a natural embodiment of Ockham’s razor.
Another insight into the tradeoff between complexity and degree of ﬁt is obtained by tak-
ing the logarithm of Equation (21.1). Choosing hMAP to maximize P(d|hi)P(hi) is equivalent
to minimizing
−log2 P(d|hi)−log2 P(hi).
Using the connection between information encoding and probability that we introduced in
Section 19.3.3, we see that the −log2 P(hi) term equals the number of bits required to spec-
ify the hypothesis hi. Furthermore, −log2 P(d|hi) is the additional number of bits required
to specify the data, given the hypothesis. (To see this, consider that no bits are required
if the hypothesis predicts the data exactly—as with h5 and the string of lime candies—and
log2 1=0.) Hence, MAP learning is choosing the hypothesis that provides maximum com-
pression of the data. The same task is addressed more directly by the minimum description
length, or MDL, learning method. Whereas MAP learning expresses simplicity by assigning
higher probabilities to simpler hypotheses, MDL expresses it directly by counting the bits in
a binary encoding of the hypotheses and data.
A ﬁnal simpliﬁcation is provided by assuming a uniform prior over the space of hypothe-
ses. In that case, MAP learning reduces to choosing an hi that maximizes P(d|hi). This is
called a maximum-likelihood hypothesis, hML. Maximum-likelihood learning is very com-
Maximum-likelihood
mon in statistics, a discipline in which many researchers distrust the subjective nature of hy-
pothesis priors. It is a reasonable approach when there is no reason to prefer one hypothesis
over another a priori—for example, when all hypotheses are equally complex.
When the data set is large, the prior distribution over hypotheses is less important—the
evidence from the data is strong enough to swamp the prior distribution over hypotheses. That
means maximum likelihood learning is a good approximation to Bayesian and MAP learning
with large data sets, but it has problems (as we shall see) with small data sets.
21.2 Learning with Complete Data
The general task of learning a probability model, given data that are assumed to be generated
from that model, is called density estimation. (The term applied originally to probability
Density estimation
density functions for continuous variables, but it is used now for discrete distributions too.)
Density estimation is a form of unsupervised learning. This section covers the simplest case,
where we have complete data. Data are complete when each data point contains values
Complete data
for every variable in the probability model being learned. We focus on parameter learn-
ing—ﬁnding the numerical parameters for a probability model whose structure is ﬁxed. For
Parameter learning
example, we might be interested in learning the conditional probabilities in a Bayesian net-
work with a given structure. We will also look brieﬂy at the problem of learning structure and
at nonparametric density estimation.
