---
chunk_id: "book-ca4fca8dd8-chunk-1288"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1288
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 785

Section 21.2
Learning with Complete Data
785
-6
-4
-2
 0
 2
 4
 6
-2
-1.5
-1
-0.5
 0
 0.5
 1
 1.5
 2
y
x
-6
-4
-2
 0
 2
 4
 6
-2
-1.5
-1
-0.5
 0
 0.5
 1
 1.5
 2
y
x
(a)
(b)
Figure 21.7 Bayesian linear regression with a model constrained to pass through the origin
and ﬁxed noise variance σ2 =0.2. Contours at ±1, ±2, and ±3 standard deviations are
shown for the predictive density. (a) With three data points near the origin, the slope is quite
uncertain, with σ2
N ≈0.3861. Notice how the uncertainty increases with distance from the
observed data points. (b) With two additional data points further away, the slope θ is very
tightly constrained, with σ2
N ≈0.0286. The remaining variance in the predictive density is
almost entirely due to the ﬁxed noise σ2.
To make a prediction at a speciﬁc data point, we have to integrate over the possible values
of θ, as suggested by Equation (21.2):
P(y|x,d) =
Z ∞
−∞P(y|x,d,θ)P(θ|x,d)dθ =
Z ∞
−∞P(y|x,θ)P(θ|d)dθ
= α
Z ∞
−∞e
−1
2

(y−θx)2
σ2

e
−1
2

(θ−θN)2
σ2
N

dθ
Again, the sum of the two exponents is a quadratic function of θ, so we have a Gaussian over
θ whose integral is 1. The remaining terms in y form another Gaussian:
P(y|x,d) ∝e
−1
2

(y−θNx)2
σ2+σ2
Nx2

.
Looking at this expression, we see that the mean prediction for y is θNx, that is, it is based
on the posterior mean for θ. The variance of the prediction is given by the model noise σ2
plus a term proportional to x2, which means that the standard deviation of the prediction
increases asymptotically linearly with the distance from the origin. Figure 21.7 illustrates
this phenomenon. As noted at the beginning of this section, having greater uncertainty for
predictions that are further from the observed data points makes perfect sense.
21.2.7 Learning Bayes net structures
So far, we have assumed that the structure of the Bayes net is given and we are just trying to
learn the parameters. The structure of the network represents basic causal knowledge about
the domain that is often easy for an expert, or even a naive user, to supply. In some cases,
however, the causal model may be unavailable or subject to dispute—for example, certain
corporations have long claimed that smoking does not cause cancer and other corporations

## Page 786
