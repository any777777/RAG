---
chunk_id: "book-ca4fca8dd8-chunk-0826"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 826
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 498

498
Chapter 14
Probabilistic Reasoning over Time
Figure 14.9 Bayesian network structure for a linear dynamical system with position Xt,
velocity ˙Xt, and position measurement Zt.
2. If the prediction P(Xt+1 |e1:t) is Gaussian and the sensor model P(et+1 |Xt+1) is linear–
Gaussian, then, after conditioning on the new evidence, the updated distribution
P(Xt+1 |e1:t+1) = αP(et+1 |Xt+1)P(Xt+1 |e1:t)
(14.18)
is also a Gaussian distribution.
Thus, the FORWARD operator for Kalman ﬁltering takes a Gaussian forward message f1:t,
speciﬁed by a mean µt and covariance Σt, and produces a new multivariate Gaussian forward
message f1:t+1, speciﬁed by a mean µt+1 and covariance Σt+1. So if we start with a Gaussian
prior f1:0 =P(X0)=N(µ0,Σ0), ﬁltering with a linear–Gaussian model produces a Gaussian
state distribution for all time.
This seems to be a nice, elegant result, but why is it so important? The reason is that
except for a few special cases such as this, ﬁltering with continuous or hybrid (discrete and
▶
continuous) networks generates state distributions whose representation grows without bound
over time. This statement is not easy to prove in general, but Exercise 14.KFSW shows what
happens for a simple example.
14.4.2 A simple one-dimensional example
We have said that the FORWARD operator for the Kalman ﬁlter maps a Gaussian into a new
Gaussian. This translates into computing a new mean and covariance from the previous mean
and covariance. Deriving the update rule in the general (multivariate) case requires rather a
lot of linear algebra, so we will stick to a very simple univariate case for now, and later give
the results for the general case. Even for the univariate case, the calculations are somewhat
tedious, but we feel that they are worth seeing because the usefulness of the Kalman ﬁlter is
tied so intimately to the mathematical properties of Gaussian distributions.
The temporal model we consider describes a random walk of a single continuous state
variable Xt with a noisy observation Zt. An example might be the “consumer conﬁdence” in-
dex, which can be modeled as undergoing a random Gaussian-distributed change each month
and is measured by a random consumer survey that also introduces Gaussian sampling noise.
The prior distribution is assumed to be Gaussian with variance σ2
0:
P(x0) = αe
−1
2

(x0−µ0)2
σ2
0

.

## Page 499
