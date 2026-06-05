---
chunk_id: "book-ca4fca8dd8-chunk-0828"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 828
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 500

500
Chapter 14
Probabilistic Reasoning over Time
 0
 0.05
 0.1
 0.15
 0.2
 0.25
 0.3
 0.35
 0.4
 0.45
-10
-5
 0
 5
 10
P(x0)
P(x1)
P(x1 | z1 = 2.5)
*z1
P(x)
x position
Figure 14.10 Stages in the Kalman ﬁlter update cycle for a random walk with a prior given
by µ0 =0.0 and σ0 =1.5, transition noise given by σx =2.0, sensor noise given by σz =1.0,
and a ﬁrst observation z1 =2.5 (marked on the x-axis). Notice how the prediction P(x1) is
ﬂattened out, relative to P(x0), by the transition noise. Notice also that the mean of the
posterior distribution P(x1 |z1) is slightly to the left of the observation z1 because the mean is
a weighted average of the prediction and the observation.
Figure 14.10 shows one update cycle of the Kalman ﬁlter in the one-dimensional case for
particular values of the transition and sensor models.
Equation (14.20) plays exactly the same role as the general ﬁltering equation (14.5) or
the HMM ﬁltering equation (14.12). Because of the special nature of Gaussian distributions,
however, the equations have some interesting additional properties.
First, we can interpret the calculation for the new mean µt+1 as a weighted mean of the
new observation zt+1 and the old mean µt. If the observation is unreliable, then σ2
z is large
and we pay more attention to the old mean; if the old mean is unreliable (σ2
t is large) or the
process is highly unpredictable (σ2
x is large), then we pay more attention to the observation.
Second, notice that the update for the variance σ2
t+1 is independent of the observation. We
can therefore compute in advance what the sequence of variance values will be. Third, the
sequence of variance values converges quickly to a ﬁxed value that depends only on σ2
x and
σ2
z , thereby substantially simplifying the subsequent calculations. (See Exercise 14.VARI.)
14.4.3 The general case
The preceding derivation illustrates the key property of Gaussian distributions that allows
Kalman ﬁltering to work: the fact that the exponent is a quadratic form. This is true not just
for the univariate case; the full multivariate Gaussian distribution has the form
N(x;µ,Σ) = αe−1
2

(x−µ)⊤Σ
−1(x−µ)

.
Multiplying out the terms in the exponent, we see that the exponent is also a quadratic func-
tion of the values xi in x. Thus, ﬁltering preserves the Gaussian nature of the state distribution.

## Page 501
