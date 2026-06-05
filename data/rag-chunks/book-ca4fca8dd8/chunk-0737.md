---
chunk_id: "book-ca4fca8dd8-chunk-0737"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 737
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 13.3
Exact Inference in Bayesian Networks
445
Continuous variables provide more precision, but they make exact inference impossible
except in a few special cases. A discrete variable with many possible values can make it te-
dious to ﬁll in the correspondingly large conditional probability tables and makes exact infer-
ence more expensive unless the variable’s value is always observed. For example, MakeModel
in a real system would have thousands of possible values, and this causes its child CarValue
to have an enormous CPT that would have to be ﬁlled in from industry databases; but, be-
cause the MakeModel is always observed, this does not contribute to inference complexity:
in fact, the observed values for the three parents pick out exactly one relevant row of the CPT
for CarValue.
The conditional distributions in the model are given in the code repository for the book;
we provide a version with only discrete variables, for which exact inference can be per-
formed. In practice, many of the variables would be continuous and the conditional distribu-
tions would be learned from historical data on applicants and their insurance claims. We will
see how to learn Bayes net models from data in Chapter 21.
The ﬁnal question is, of course, how to do inference in the network to make predictions.
We turn now to this question. For each inference method that we describe, we will evaluate
the method on the insurance net to measure the time and space requirements of the method.
13.3 Exact Inference in Bayesian Networks
The basic task for any probabilistic inference system is to compute the posterior probability
distribution for a set of query variables, given some observed event—usually, some assign-
Event
ment of values to a set of evidence variables.5 To simplify the presentation, we will consider
only one query variable at a time; the algorithms can easily be extended to queries with mul-
tiple variables. (For example, we can solve the query P(U,V |e) by multiplying P(V |e) and
P(U |V,e).) We will use the notation from Chapter 12: X denotes the query variable; E de-
notes the set of evidence variables E1,...,Em, and e is a particular observed event; Y denotes
the hidden (nonevidence, nonquery) variables Y1,...,Yℓ. Thus, the complete set of variables
is {X}∪E∪Y. A typical query asks for the posterior probability distribution P(X |e).
In the burglary network, we might observe the event in which JohnCalls=true and
MaryCalls=true. We could then ask for, say, the probability that a burglary has occurred:
P(Burglary|JohnCalls=true,MaryCalls=true) = ⟨0.284,0.716⟩.
In this section we discuss exact algorithms for computing posterior probabilities as well as
the complexity of this task. It turns out that the general case is intractable, so Section 13.4
covers methods for approximate inference.
13.3.1 Inference by enumeration
Chapter 12 explained that any conditional probability can be computed by summing terms
from the full joint distribution. More speciﬁcally, a query P(X |e) can be answered using
Equation (12.9), which we repeat here for convenience:
P(X |e) = αP(X,e) = α ∑
y
P(X,e,y).
5
Another widely studied task is ﬁnding the most probable explanation for some observed evidence. This and
other tasks are discussed in the notes at the end of the chapter.
