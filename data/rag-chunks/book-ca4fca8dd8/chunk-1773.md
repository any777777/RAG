---
chunk_id: "book-ca4fca8dd8-chunk-1773"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1773
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 1079

Section A.3
Probability Distributions
1079
tion that is a function of x with mean µ and standard deviation σ (and therefore variance σ2).
It is deﬁned as
N(x;µ,σ2)=
1
σ
√
2π
e−(x−µ)2/(2σ2) ,
where x is a continuous variable ranging from −∞to +∞. With mean µ=0 and variance
σ2 =1, we get the special case of the standard normal distribution. For a distribution over
Standard normal
distribution
a vector x in n dimensions, there is the multivariate Gaussian distribution:
Multivariate
Gaussian
N(x;µ,Σ)=
1
p
(2π)n|Σ|
e−1
2

(x−µ)⊤Σ
−1(x−µ)

,
where µ is the mean vector and Σ is the covariance matrix (see below). The cumulative
distribution for a univariate normal distribution is given by
F(x)=
x
Z
−∞
N(z;µ,σ2)dz= 1
2(1+erf(x−µ
σ
√
2
)),
where erf(x) is the so-called error function, which has no closed-form representation.
The central limit theorem states that the distribution formed by sampling n independent
Central limit
theorem
random variables and taking their mean tends to a normal distribution as n tends to inﬁn-
ity. This holds for almost any collection of random variables, even if they are not strictly
independent, unless the variance of any ﬁnite subset of variables dominates the others.
The expectation of a random variable, E(X), is the mean or average value, weighted by
Expectation
the probability of each value. For a discrete variable it is:
E(X)= ∑
i
xi P(X =xi).
For a continuous variable, replace the summation with an integral and use the probability
density function, P(x):
E(X)=
∞
Z
−∞
xP(x)dx.
For any function f, we also have
E(f(X))=
∞
Z
−∞
f(x)P(x)dx.
Finally, when necessary, one may specify the distribution for the random variable as a sub-
script to the expectation operator:
EX∼Q(x)(g(X))=
∞
Z
−∞
g(x)Q(x)dx.
Besides the expectation, other important statistical properties of a distribution include the
variance, which is the expected value of the square of the difference from the mean, µ, of the
Variance
distribution:
Var(X)=E((X −µ)2)
and the standard deviation, which is the square root of the variance.
Standard deviation

## Page 1080
