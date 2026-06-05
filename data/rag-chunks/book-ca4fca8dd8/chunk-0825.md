---
chunk_id: "book-ca4fca8dd8-chunk-0825"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 825
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 14.4
Kalman Filters
497
14.4 Kalman Filters
Imagine watching a small bird ﬂying through dense jungle foliage at dusk: you glimpse
brief, intermittent ﬂashes of motion; you try hard to guess where the bird is and where it will
appear next so that you don’t lose it. Or imagine that you are a World War II radar operator
peering at a faint, wandering blip that appears once every 10 seconds on the screen. Or, going
back further still, imagine you are Kepler trying to reconstruct the motions of the planets
from a collection of highly inaccurate angular observations taken at irregular and imprecisely
measured intervals.
In all these cases, you are doing ﬁltering: estimating state variables (here, the position
and velocity of a moving object) from noisy observations over time. If the variables were
discrete, we could model the system with a hidden Markov model. This section examines
methods for handling continuous variables, using an algorithm called Kalman ﬁltering, after
Kalman ﬁltering
one of its inventors, Rudolf Kalman.
The bird’s ﬂight might be speciﬁed by six continuous variables at each time point; three
for position (Xt,Yt,Zt) and three for velocity ( ˙Xt, ˙Yt, ˙Zt). We will need suitable conditional
densities to represent the transition and sensor models; as in Chapter 13, we will use linear–
Gaussian distributions. This means that the next state Xt+1 must be a linear function of the
current state Xt, plus some Gaussian noise, a condition that turns out to be quite reasonable in
practice. Consider, for example, the X-coordinate of the bird, ignoring the other coordinates
for now. Let the time interval between observations be ∆, and assume constant velocity during
the interval; then the position update is given by Xt+∆= Xt + ˙X ∆. Adding Gaussian noise (to
account for wind variation, etc.), we obtain a linear–Gaussian transition model:
P(Xt+∆=xt+∆|Xt =xt, ˙Xt = ˙xt) = N(xt+∆;xt + ˙xt ∆,σ2).
The Bayesian network structure for a system with position vector Xt and velocity ˙Xt is shown
in Figure 14.9. Note that this is a very speciﬁc form of linear–Gaussian model; the general
form will be described later in this section and covers a vast array of applications beyond the
simple motion examples of the ﬁrst paragraph. The reader might wish to consult Appendix A
for some of the mathematical properties of Gaussian distributions; for our immediate pur-
poses, the most important is that a multivariate Gaussian distribution for d variables is
speciﬁed by a d-element mean µ and a d ×d covariance matrix Σ.
14.4.1 Updating Gaussian distributions
In Chapter 13 on page 441, we alluded to a key property of the linear–Gaussian family of
distributions: it remains closed under Bayesian updating. (That is, given any evidence, the
posterior is still in the linear–Gaussian family.) Here we make this claim precise in the context
of ﬁltering in a temporal probability model. The required properties correspond to the two-
step ﬁltering calculation in Equation (14.5):
1. If the current distribution P(Xt |e1:t) is Gaussian and the transition model P(Xt+1 |xt)
is linear–Gaussian, then the one-step predicted distribution given by
P(Xt+1 |e1:t) =
Z
xt
P(Xt+1 |xt)P(xt |e1:t)dxt
(14.17)
is also a Gaussian distribution.
