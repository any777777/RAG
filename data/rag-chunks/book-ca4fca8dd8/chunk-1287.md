---
chunk_id: "book-ca4fca8dd8-chunk-1287"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1287
confidence: "first-pass"
extraction_method: "structured-local"
---

784
Chapter 21
Learning Probabilistic Models
focus on a simple case: univariable data, a model that is constrained to go through the origin,
and known noise: a normal distribution with variance σ2. Then we have just one parameter θ
and the model is
P(y|x,θ) = N(y;θx,σ2
y) =
1
σ
√
2π
e
−1
2

(y−θx)2
σ2

.
(21.7)
As the log likelihood is quadratic in θ, the appropriate form for a conjugate prior on θ is also
a Gaussian. This ensures that the posterior for θ will also be Gaussian. We’ll assume a mean
θ0 and variance σ2
0 for the prior, so that
P(θ) = N(θ;θ0,σ2
0) =
1
σ0
√
2π
e
−1
2

(θ−θ0)2
σ2
0

.
(21.8)
Depending on the data being modeled, one might have some idea of what sort of slope θ
to expect, or one might be completely agnostic. In the latter case, it makes sense to choose
θ0 to be 0 and σ2
0 to be large—a so-called uninformative prior. Finally, we can assume a
Uninformative prior
prior P(x) for the x-value of each data point, but this is completely immaterial to the analysis
because it doesn’t depend on θ.
Now the setup is complete, so we can compute the posterior for θ using Equation (21.1):
P(θ|d) ∝P(d|θ)P(θ). The observed data points are d=(x1,y1),...,(xN,yN), so the likeli-
hood for the data is obtained from Equation (21.7) as follows:
P(d|θ) =
 
∏
i
P(xi)
!
∏
i
P(yi |xi,θ)) = α∏
i
e
−1
2

(yi−θxi)2
σ2

= αe
−1
2 ∑i

(yi−θxi)2
σ2

,
where we have absorbed the x-value priors and the normalizing constants for the N Gaussians
into a constant α that is independent of θ. Now we combine this and the parameter prior from
Equation (21.8) to obtain the posterior:
P(θ|d) = α′′e
−1
2

(θ−θ0)2
σ2
0

e
−1
2 ∑i

(yi−θxi)2
σ2

.
Although this looks complicated, each exponent is a quadratic function of θ, so the sum of
the two exponents is as well. Hence, the whole expression represents a Gaussian distribution
for θ. Using algebraic manipulations very similar to those in Section 14.4, we ﬁnd
P(θ|d) = α′′′e
−1
2

(θ−θN)2
σ2
N

with “updated” mean and variance given by
θN = σ2θ0 +σ2
0 ∑i xiyi
σ2 +σ2
0 ∑i x2
i
and
σ2
N =
σ2σ2
0
σ2 +σ2
0 ∑i x2
i
.
Let’s look at these formulas to see what they mean. When the data are narrowly concentrated
on a small region of the x-axis near the origin, ∑i x2
i will be small and the posterior variance
σ2
N will be large, roughly equal to the prior variance σ2
0. This is as one would expect: the data
do little to constrain the rotation of the line around the origin. Conversely, when the data are
widely spread along the axis, ∑i x2
i will be large and the posterior variance σ2
N will be small,
roughly equal to σ2/(∑i x2
i ), so the slope will be very tightly constrained.
