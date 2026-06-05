---
chunk_id: "book-ca4fca8dd8-chunk-1280"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1280
confidence: "first-pass"
extraction_method: "structured-local"
---

778
Chapter 21
Learning Probabilistic Models
tant point is that with complete data, the maximum-likelihood parameter learning problem
▶
for a Bayesian network decomposes into separate learning problems, one for each parame-
ter. (See Exercise 21.NORX for the nontabulated case, where each parameter affects several
conditional probabilities.) The second point is that the parameter values for a variable, given
its parents, are just the observed frequencies of the variable values for each setting of the
parent values. As before, we must be careful to avoid zeroes when the data set is small.
21.2.2 Naive Bayes models
Probably the most common Bayesian network model used in machine learning is the naive
Bayes model ﬁrst introduced on page 420. In this model, the “class” variable C (which is to
be predicted) is the root and the “attribute” variables Xi are the leaves. The model is “naive”
because it assumes that the attributes are conditionally independent of each other, given the
class. (The model in Figure 21.2(b) is a naive Bayes model with class Flavor and just one
attribute, Wrapper.) In the case of Boolean variables, the parameters are
θ=P(C=true),θi1 =P(Xi =true|C=true),θi2 =P(Xi =true|C=false).
The maximum-likelihood parameter values are found in exactly the same way as in Fig-
ure 21.2(b). Once the model has been trained in this way, it can be used to classify new ex-
amples for which the class variable C is unobserved. With observed attribute values x1,...,xn,
the probability of each class is given by
P(C|x1,...,xn) = α P(C)∏
i
P(xi |C).
A deterministic prediction can be obtained by choosing the most likely class. Figure 21.3
shows the learning curve for this method when it is applied to the restaurant problem from
Chapter 19. The method learns fairly well but not as well as decision tree learning; this is pre-
sumably because the true hypothesis—which is a decision tree—is not representable exactly
using a naive Bayes model. Naive Bayes learning turns out to do surprisingly well in a wide
range of applications; the boosted version (Exercise 21.BNBX) is one of the most effective
general-purpose learning algorithms. Naive Bayes learning scales well to very large prob-
lems: with n Boolean attributes, there are just 2n + 1 parameters, and no search is required
▶
to ﬁnd hML, the maximum-likelihood naive Bayes hypothesis. Finally, naive Bayes learning
systems deal well with noisy or missing data and can give probabilistic predictions when ap-
propriate. Their primary drawback is the fact that the conditional independence assumption
is seldom accurate; as noted on page 421, the assumption leads to overconﬁdent probabilities
that are often very close to 0 or 1, especially with large numbers of attributes.
21.2.3 Generative and discriminative models
We can distinguish two kinds of machine learning models used for classiﬁers: generative and
discriminative. A generative model models the probability distribution of each class. For
Generative model
example, the naive Bayes text classiﬁer from Section 12.6.1 creates a separate model for each
possible category of text—one for sports, one for weather, and so on. Each model includes
the prior probability of the category—for example P(Category=weather)—as well as the
conditional probability P(Inputs|Category=weather). From these we can compute the joint
probability P(Inputs,Category=weather)) and we can generate a random selection of words
that is representative of texts in the weather category.
