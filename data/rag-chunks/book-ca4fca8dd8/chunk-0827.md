---
chunk_id: "book-ca4fca8dd8-chunk-0827"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 827
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 14.4
Kalman Filters
499
(For simplicity, we use the same symbol α for all normalizing constants in this section.) The
transition model adds a Gaussian perturbation of constant variance σ2
x to the current state:
P(xt+1 |xt) = αe
−1
2

(xt+1−xt )2
σ2x

.
The sensor model assumes Gaussian noise with variance σ2
z :
P(zt |xt) = αe
−1
2

(zt −xt )2
σ2z

.
Now, given the prior P(X0), the one-step predicted distribution comes from Equation (14.17):
P(x1) =
Z ∞
−∞P(x1 |x0)P(x0)dx0 = α
Z ∞
−∞e
−1
2

(x1−x0)2
σ2x

e
−1
2

(x0−µ0)2
σ2
0

dx0
= α
Z ∞
−∞e
−1
2

σ2
0(x1−x0)2+σ2x (x0−µ0)2
σ2
0σ2x

dx0 .
This integral looks rather complicated. The key to progress is to notice that the exponent is the
sum of two expressions that are quadratic in x0 and hence is itself a quadratic in x0. A simple
trick known as completing the square allows the rewriting of any quadratic ax2
0 +bx0 +c as
Completing the
square
the sum of a squared term a(x0 −−b
2a )2 and a residual term c −b2
4a that is independent of x0.
In this case, we have a=(σ2
0 + σ2
x)/(σ2
0σ2
x), b=−2(σ2
0x1 + σ2
xµ0)/(σ2
0σ2
x), and c=(σ2
0x2
1 +
σ2
xµ2
0)/(σ2
0σ2
x). The residual term can be taken outside the integral, giving us
P(x1) = αe−1
2

c−b2
4a
 Z ∞
−∞e−1
2(a(x0−−b
2a )2) dx0 .
Now the integral is just the integral of a Gaussian over its full range, which is simply 1. Thus,
we are left with only the residual term from the quadratic. Plugging back in the expressions
for a, b, and c and simplifying, we obtain
P(x1) = αe
−1
2

(x1−µ0)2
σ2
0+σ2x

.
That is, the one-step predicted distribution is a Gaussian with the same mean µ0 and a variance
equal to the sum of the original variance σ2
0 and the transition variance σ2
x.
To complete the update step, we need to condition on the observation at the ﬁrst time
step, namely, z1. From Equation (14.18), this is given by
P(x1 |z1) = αP(z1 |x1)P(x1)
= αe
−1
2

(z1−x1)2
σ2z

e
−1
2

(x1−µ0)2
σ2
0+σ2x

.
Once again, we combine the exponents and complete the square (Exercise 14.KALM), obtain-
ing the following expression for the posterior:
P(x1 |z1) = αe
−1
2

x1−(σ2
0+σ2x )z1+σ2z µ0
σ2
0+σ2x +σ2z
2
(σ2
0+σ2x )σ2z /(σ2
0+σ2x +σ2z ) .
(14.19)
Thus, after one update cycle, we have a new Gaussian distribution for the state variable.
From the Gaussian formula in Equation (14.19), we see that the new mean and standard
deviation can be calculated from the old mean and standard deviation as follows:
µt+1 = (σ2
t +σ2
x)zt+1 +σ2
z µt
σ2t +σ2x +σ2z
and
σ2
t+1 = (σ2
t +σ2
x)σ2
z
σ2t +σ2x +σ2z
.
(14.20)
