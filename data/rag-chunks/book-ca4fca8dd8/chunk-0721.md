---
chunk_id: "book-ca4fca8dd8-chunk-0721"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 721
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 13.2
The Semantics of Bayesian Networks
433
Bayes nets deﬁnes each entry in the joint distribution as follows:
P(x1,...,xn) =
n
∏
i=1
θ(xi | parents(Xi)),
(13.1)
where parents(Xi) denotes the values of Parents(Xi) that appear in x1,...,xn. Thus, each
entry in the joint distribution is represented by the product of the appropriate elements of the
local conditional distributions in the Bayes net.
To illustrate this, we can calculate the probability that the alarm has sounded, but neither
a burglary nor an earthquake has occurred, and both John and Mary call. We simply multiply
the relevant entries from the local conditional distributions (abbreviating the variable names):
P(j,m,a,¬b,¬e) = P(j|a)P(m|a)P(a|¬b∧¬e)P(¬b)P(¬e)
= 0.90×0.70×0.001×0.999×0.998 = 0.000628.
Section 12.3 explained that the full joint distribution can be used to answer any query about
the domain. If a Bayes net is a representation of the joint distribution, then it too can be used
to answer any query, by summing all the relevant joint probability values, each calculated by
multiplying probabilities from the local conditional distributions. Section 13.3 explains this
in more detail, but also describes methods that are much more efﬁcient.
So far, we have glossed over one important point: what is the meaning of the numbers
that go into the local conditional distributions θ(xi | parents(Xi))? It turns out that from Equa-
tion (13.1) we can prove that the parameters θ(xi | parents(Xi)) are exactly the conditional
probabilities P(xi | parents(Xi)) implied by the joint distribution. Remember that the condi-
tional probabilities can be computed from the joint distribution as follows:
P(xi | parents(Xi)) ≡P(xi, parents(Xi))
P(parents(Xi))
=
∑y P(xi, parents(Xi),y)
∑x′
i, yP(x′
i, parents(Xi),y)
where y represents the values of all variables other than Xi and its parents. From this last line
one can prove that P(xi | parents(Xi)) = θ(xi | parents(Xi)) (Exercise 13.CPTE). Hence, we
can rewrite Equation (13.1) as
P(x1,...,xn) =
n
∏
i=1
P(xi | parents(Xi)).
(13.2)
This means that when one estimates values for the local conditional distributions, they need
to be the actual conditional probabilities for the variable given its parents. So, for example,
when we specify θ(JohnCalls=true|Alarm=true)=0.90, it should be the case that about
90% of the time when the alarm sounds, John calls. The fact that each parameter of the
network has a precise meaning in terms of only a small set of variables is crucially important
for robustness and ease of speciﬁcation of the models.
A method for constructing Bayesian networks
Equation (13.2) deﬁnes what a given Bayes net means. The next step is to explain how to
construct a Bayesian network in such a way that the resulting joint distribution is a good
representation of a given domain. We will now show that Equation (13.2) implies certain
conditional independence relationships that can be used to guide the knowledge engineer in
