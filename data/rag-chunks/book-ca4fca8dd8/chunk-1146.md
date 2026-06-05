---
chunk_id: "book-ca4fca8dd8-chunk-1146"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1146
confidence: "first-pass"
extraction_method: "structured-local"
---

688
Chapter 19
Learning from Examples
Absolute-value loss: L1(y, ˆy) = |y−ˆy|
Squared-error loss:
L2(y, ˆy) = (y−ˆy)2
0/1 loss:
L0/1(y, ˆy) = 0 if y = ˆy, else 1
Theoretically, the learning agent maximizes its expected utility by choosing the hypothesis
that minimizes expected loss over all input–output pairs it will see. To compute this expec-
tation we need to deﬁne a prior probability distribution P(X,Y) over examples. Let E be
the set of all possible input–output examples. Then the expected generalization loss for a
Generalization loss
hypothesis h (with respect to loss function L) is
GenLossL(h) = ∑
(x,y)∈E
L(y,h(x))P(x,y),
and the best hypothesis, h∗, is the one with the minimum expected generalization loss:
h∗= argmin
h∈H
GenLossL(h).
Because P(x,y) is not known in most cases, the learning agent can only estimate generaliza-
tion loss with empirical loss on a set of examples E of size N:
Empirical loss
EmpLossL,E(h) = ∑
(x,y)∈E
L(y,h(x)) 1
N .
The estimated best hypothesis ˆh∗is then the one with minimum empirical loss:
ˆh∗= argmin
h∈H
EmpLossL,E(h).
There are four reasons why ˆh∗may differ from the true function, f: unrealizability, variance,
noise, and computational complexity.
First, we say that a learning problem is realizable if the hypothesis space H actually
Realizable
contains the true function f. If H is the set of linear functions, and the true function f
is a quadratic function, then no amount of data will recover the true f. Second, variance
means that a learning algorithm will in general return different hypotheses for different sets
of examples. If the problem is realizable, then variance decreases towards zero as the number
of training examples increases. Third, f may be nondeterministic or noisy—it may return
Noise
different values of f(x) for the same x. By deﬁnition, noise cannot be predicted (it can only
be characterized). And ﬁnally, when H is a complicated function in a large hypothesis space,
it can be computationally intractable to systematically search all possibilities; in that case,
a search can explore part of the space and return a reasonably good hypothesis, but can’t
always guarantee the best one.
Traditional methods in statistics and the early years of machine learning concentrated on
small-scale learning, where the number of training examples ranged from dozens to the low
Small-scale learning
thousands. Here the generalization loss mostly comes from the approximation error of not
having the true f in the hypothesis space, and from the estimation error of not having enough
training examples to limit variance.
In recent years there has been more emphasis on large-scale learning, with millions of
Large-scale learning
examples. Here the generalization loss may be dominated by limits of computation: there are
enough data and a rich enough model that we could ﬁnd an h that is very close to the true f,
but the computation to ﬁnd it is complex, so we settle for an approximation.
