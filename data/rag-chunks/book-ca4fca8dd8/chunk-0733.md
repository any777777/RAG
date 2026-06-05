---
chunk_id: "book-ca4fca8dd8-chunk-0733"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 733
confidence: "first-pass"
extraction_method: "structured-local"
---

442
Chapter 13
Probabilistic Reasoning
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0
 2
 4
 6
 8
 10
 12
P(c)
Cost c
 0
 0.2
 0.4
 0.6
 0.8
 1
 0
 2
 4
 6
 8
 10
 12
P(buys | c)
Cost c
Logit
Probit
(a)
(b)
Figure 13.8 (a) A normal (Gaussian) distribution for the cost threshold, centered on µ=6.0
with standard deviation σ=1.0. (b) Expit and probit models for the probability of buys given
cost, for the parameters µ=6.0 and σ=1.0.
Φ(x) is an increasing function of x, whereas the probability of buying decreases with cost, so
here we ﬂip the function around:
P(buys|Cost=c) = 1−Φ((c−µ)/σ),
which means that the cost threshold occurs around µ, the width of the threshold region is pro-
portional to σ, and the probability of buying decreases as cost increases. This probit model
Probit
(pronounced “pro-bit” and short for “probability unit”) is illustrated in Figure 13.8(a). The
form can be justiﬁed by proposing that the underlying decision process has a hard threshold,
but that the precise location of the threshold is subject to random Gaussian noise.
An alternative to the probit model is the expit or inverse logit model. It uses the logistic
Expit
Inverse logit
function 1/(1+e−x) to produce a soft threshold—it maps any x to a value between 0 and 1.
Logistic function
Again, for our example, we ﬂip it around to make a decreasing function; we also scale the
exponent by 4/
√
2π to match the probit’s slope at the mean:
P(buys|Cost=c) = 1−
1
1+exp(−
4
√
2π.c−µ
σ ) .
This is illustrated in Figure 13.8(b). The two distributions look similar, but the logit actually
has much longer “tails.” The probit is often a better ﬁt to real situations, but the logistic
function is sometimes easier to deal with mathematically. It is used widely in machine learn-
ing. Both models can be generalized to handle multiple continuous parents by taking a linear
combination of the parent values. This also works for discrete parents if their values are in-
tegers; for example, with k Boolean parents, each viewed as having values 0 or 1, the input
to the expit or probit distribution would be a weighted linear combination with k parameters,
yielding a model quite similar to the noisy-OR model discussed earlier.
13.2.4 Case study: Car insurance
A car insurance company receives an application from an individual to insure a speciﬁc ve-
hicle and must decide on the appropriate annual premium to charge, based on the anticipated
claims it will pay out for this applicant. The task is to build a Bayes net that captures the
