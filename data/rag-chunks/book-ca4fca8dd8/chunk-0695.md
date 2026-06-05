---
chunk_id: "book-ca4fca8dd8-chunk-0695"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 695
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 12.5
Bayes’ Rule and Its Use
417
When they are available, then, independence assertions can help in reducing the size of
the domain representation and the complexity of the inference problem. Unfortunately, clean
separation of entire sets of variables by independence is quite rare. Whenever a connection,
however indirect, exists between two variables, independence will fail to hold. Moreover,
even independent subsets can be quite large—for example, dentistry might involve dozens of
diseases and hundreds of symptoms, all of which are interrelated. To handle such problems,
we need more subtle methods than the straightforward concept of independence.
12.5 Bayes’ Rule and Its Use
On page 408, we deﬁned the product rule (Equation (12.4)). It can actually be written in
two forms:
P(a∧b) = P(a|b)P(b)
and
P(a∧b) = P(b|a)P(a).
Equating the two right-hand sides and dividing by P(a), we get
P(b|a) = P(a|b)P(b)
P(a)
.
(12.12)
This equation is known as Bayes’ rule (also Bayes’ law or Bayes’ theorem). This simple
Bayes’ rule
equation underlies most modern AI systems for probabilistic inference.
The more general case of Bayes’ rule for multivalued variables can be written in the P
notation as follows:
P(Y |X) = P(X |Y)P(Y)
P(X)
.
As before, this is to be taken as representing a set of equations, each dealing with speciﬁc val-
ues of the variables. We will also have occasion to use a more general version conditionalized
on some background evidence e:
P(Y |X,e) = P(X |Y,e)P(Y |e)
P(X |e)
.
(12.13)
12.5.1 Applying Bayes’ rule: The simple case
On the surface, Bayes’ rule does not seem very useful. It allows us to compute the single
term P(b|a) in terms of three terms: P(a|b), P(b), and P(a). That seems like two steps
backwards; but Bayes’ rule is useful in practice because there are many cases where we do
have good probability estimates for these three numbers and need to compute the fourth.
Often, we perceive as evidence the effect of some unknown cause and we would like to
determine that cause. In that case, Bayes’ rule becomes
P(cause|effect) = P(effect|cause)P(cause)
P(effect)
.
The conditional probability P(effect|cause) quantiﬁes the relationship in the causal direc-
Causal
tion, whereas P(cause|effect) describes the diagnostic direction. In a task such as medical
Diagnostic
diagnosis, we often have conditional probabilities on causal relationships. The doctor knows
P(symptoms|disease) and wants to derive a diagnosis, P(disease|symptoms).
For example, a doctor knows that the disease meningitis causes a patient to have a stiff
neck, say, 70% of the time. The doctor also knows some unconditional facts: the prior
