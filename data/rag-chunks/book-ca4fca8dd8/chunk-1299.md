---
chunk_id: "book-ca4fca8dd8-chunk-1299"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1299
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 21.3
Learning with Hidden Variables: The EM Algorithm
793
are independent, given the bag, but the conditional probability distribution for each feature
depends on the bag. The parameters are as follows: θ is the prior probability that a candy
comes from Bag 1; θF1 and θF2 are the probabilities that the ﬂavor is cherry, given that the
candy comes from Bag 1 or Bag 2 respectively; θW1 and θW2 give the probabilities that the
wrapper is red; and θH1 and θH2 give the probabilities that the candy has a hole.
The overall model is a mixture model: a weighted sum of two different distributions, each
of which is a product of independent, univariate distributions. (In fact, we can also model the
mixture of Gaussians as a Bayesian network, as shown in Figure 21.14(b).) In the ﬁgure, the
bag is a hidden variable because, once the candies have been mixed together, we no longer
know which bag each candy came from. In such a case, can we recover the descriptions of
the two bags by observing candies from the mixture? Let us work through an iteration of
EM for this problem. First, let’s look at the data. We generated 1000 samples from a model
whose true parameters are as follows:
θ=0.5, θF1 =θW1 =θH1 =0.8, θF2 =θW2 =θH2 =0.3.
(21.9)
That is, the candies are equally likely to come from either bag; the ﬁrst is mostly cherry with
red wrappers and holes; the second is mostly lime with green wrappers and no holes. The
counts for the eight possible kinds of candy are as follows:
W =red
W =green
H =1 H =0 H =1 H =0
F =cherry
273
93
104
90
F =lime
79
100
94
167
We start by initializing the parameters. For numerical simplicity, we arbitrarily choose5
θ(0) =0.6, θ(0)
F1 =θ(0)
W1 =θ(0)
H1 =0.6, θ(0)
F2 =θ(0)
W2 =θ(0)
H2 =0.4.
(21.10)
First, let us work on the θ parameter. In the fully observable case, we would estimate this
directly from the observed counts of candies from bags 1 and 2. Because the bag is a hidden
variable, we calculate the expected counts instead. The expected count ˆN(Bag=1) is the
sum, over all candies, of the probability that the candy came from bag 1:
θ(1) = ˆN(Bag=1)/N =
N
∑
j=1
P(Bag=1|ﬂavor j,wrapper j,holes j)/N .
These probabilities can be computed by any inference algorithm for Bayesian networks. For
a naive Bayes model such as the one in our example, we can do the inference “by hand,”
using Bayes’ rule and applying conditional independence:
θ(1) = 1
N
N
∑
j=1
P(ﬂavor j |Bag=1)P(wrapper j |Bag=1)P(holesj |Bag=1)P(Bag=1)
∑i P(ﬂavor j |Bag=i)P(wrapper j |Bag=i)P(holes j |Bag=i)P(Bag=i) .
Applying this formula to, say, the 273 red-wrapped cherry candies with holes, we get a con-
tribution of
273
1000 ·
θ(0)
F1θ(0)
W1θ(0)
H1θ(0)
θ(0)
F1θ(0)
W1θ(0)
H1θ(0) +θ(0)
F2θ(0)
W2θ(0)
H2(1−θ(0))
≈0.22797.
5
It is better in practice to choose them randomly, to avoid local maxima due to symmetry.
