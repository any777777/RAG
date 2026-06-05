---
chunk_id: "book-ca4fca8dd8-chunk-1278"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1278
confidence: "first-pass"
extraction_method: "structured-local"
---

776
Chapter 21
Learning Probabilistic Models
21.2.1 Maximum-likelihood parameter learning: Discrete models
Suppose we buy a bag of lime and cherry candy from a new manufacturer whose ﬂavor pro-
portions are completely unknown; the fraction of cherry could be anywhere between 0 and 1.
In that case, we have a continuum of hypotheses. The parameter in this case, which we
call θ, is the proportion of cherry candies, and the hypothesis is hθ. (The proportion of lime
candies is just 1 −θ.) If we assume that all proportions are equally likely a priori, then
a maximum-likelihood approach is reasonable. If we model the situation with a Bayesian
network, we need just one random variable, Flavor (the ﬂavor of a randomly chosen candy
from the bag). It has values cherry and lime, where the probability of cherry is θ (see Fig-
ure 21.2(a)). Now suppose we unwrap N candies, of which c are cherry and ℓ=N −c are
lime. According to Equation (21.3), the likelihood of this particular data set is
P(d|hθ) =
N
∏
j=1
P(dj |hθ) = θc ·(1−θ)ℓ.
The maximum-likelihood hypothesis is given by the value of θ that maximizes this expres-
sion. Because the log function is monotonic, the same value is obtained by maximizing the
log likelihood instead:
Log likelihood
L(d|hθ) = logP(d|hθ) =
N
∑
j=1
logP(dj |hθ) = clogθ +ℓlog(1−θ).
(By taking logarithms, we reduce the product to a sum over the data, which is usually easier
to maximize.) To ﬁnd the maximum-likelihood value of θ, we differentiate L with respect to
θ and set the resulting expression to zero:
dL(d|hθ)
dθ
= c
θ −
ℓ
1−θ = 0
⇒
θ =
c
c+ℓ= c
N .
In English, then, the maximum-likelihood hypothesis hML asserts that the actual proportion
of cherry candies in the bag is equal to the observed proportion in the candies unwrapped so
far!
It appears that we have done a lot of work to discover the obvious. In fact, though, we
have laid out one standard method for maximum-likelihood parameter learning, a method
with broad applicability:
1. Write down an expression for the likelihood of the data as a function of the parameter(s).
2. Write down the derivative of the log likelihood with respect to each parameter.
3. Find the parameter values such that the derivatives are zero.
The trickiest step is usually the last. In our example, it was trivial, but we will see that in
many cases we need to resort to iterative solution algorithms or other numerical optimiza-
tion techniques, as described in Section 4.2. (We will need to verify that the Hessian ma-
trix is negative-deﬁnite.) The example also illustrates a signiﬁcant problem with maximum-
likelihood learning in general: when the data set is small enough that some events have not
▶
yet been observed—for instance, no cherry candies—the maximum-likelihood hypothesis as-
signs zero probability to those events. Various tricks are used to avoid this problem, such as
initializing the counts for each event to 1 instead of 0.
Let us look at another example. Suppose this new candy manufacturer wants to give a
little hint to the consumer and uses candy wrappers colored red and green. The Wrapper for
