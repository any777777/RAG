---
chunk_id: "book-ca4fca8dd8-chunk-1152"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1152
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.5
The Theory of Learning
691
Questions like this are addressed by computational learning theory, which lies at the
Computational
learning theory
intersection of AI, statistics, and theoretical computer science. The underlying principle is
that any hypothesis that is seriously wrong will almost certainly be “found out” with high
probability after a small number of examples, because it will make an incorrect prediction.
Thus, any hypothesis that is consistent with a sufﬁciently large set of training examples is
unlikely to be seriously wrong: that is, it must be probably approximately correct (PAC).
Probably
approximately
correct (PAC)
Any learning algorithm that returns hypotheses that are probably approximately correct
is called a PAC learning algorithm; we can use this approach to provide bounds on the
PAC learning
performance of various learning algorithms.
PAC-learning theorems, like all theorems, are logical consequences of axioms. When a
theorem (as opposed to, say, a political pundit) states something about the future based on
the past, the axioms have to provide the “juice” to make that connection. For PAC learn-
ing, the juice is provided by the stationarity assumption introduced on page 683, which says
that future examples are going to be drawn from the same ﬁxed distribution P(E)=P(X,Y)
as past examples. (Note that we do not have to know what distribution that is, just that it
doesn’t change.) In addition, to keep things simple, we will assume that the true function f
is deterministic and is a member of the hypothesis space H that is being considered.
The simplest PAC theorems deal with Boolean functions, for which the 0/1 loss is appro-
priate. The error rate of a hypothesis h, deﬁned informally earlier, is deﬁned formally here
as the expected generalization error for examples drawn from the stationary distribution:
error(h) = GenLossL0/1(h) = ∑
x,y
L0/1(y,h(x))P(x,y).
In other words, error(h) is the probability that h misclassiﬁes a new example. This is the same
quantity being measured experimentally by the learning curves shown earlier.
A hypothesis h is called approximately correct if error(h) ≤ϵ, where ϵ is a small con-
stant. We will show that we can ﬁnd an N such that, after training on N examples, with high
probability, all consistent hypotheses will be approximately correct. One can think of an ap-
proximately correct hypothesis as being “close” to the true function in hypothesis space: it
lies inside what is called the ϵ-ball around the true function f. The hypothesis space outside
ϵ-ball
this ball is called Hbad.
We can derive a bound on the probability that a “seriously wrong” hypothesis hb ∈Hbad
is consistent with the ﬁrst N examples as follows. We know that error(hb) > ϵ. Thus, the
probability that it agrees with a given example is at most 1 −ϵ. Since the examples are
independent, the bound for N examples is:
P(hb agrees with N examples) ≤(1−ϵ)N .
The probability that Hbad contains at least one consistent hypothesis is bounded by the sum
of the individual probabilities:
P(Hbad contains a consistent hypothesis) ≤|Hbad|(1−ϵ)N ≤|H|(1−ϵ)N ,
where we have used the fact that Hbad is a subset of H and thus |Hbad| ≤|H|. We would like
to reduce the probability of this event below some small number δ:
P(Hbad contains a consistent hypothesis) ≤|H|(1−ϵ)N ≤δ.
Given that 1−ϵ ≤e−ϵ, we can achieve this if we allow the algorithm to see
N ≥1
ϵ

ln 1
δ +ln|H|

(19.1)
