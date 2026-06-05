---
chunk_id: "book-ca4fca8dd8-chunk-1558"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1558
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 26.4
Robotic Perception
941
function MONTE-CARLO-LOCALIZATIONa, z, N, P(X′|X, v, ω), P(z|z∗), map
returns a set of samples, S, for the next time step
inputs: a, robot velocities v and ω
z, a vector of M range scan data points
P(X′|X, v, ω), motion model
P(z|z∗), a range sensor noise model
map, a 2D map of the environment
persistent: S, a vector of N samples
local variables: W, a vector of N weights
S′, a temporary vector of N samples
if S is empty then
for i = 1 to N do
// initialization phase
S[i]←sample from P(X0)
for i = 1 to N do
// update cycle
S′[i]←sample from P(X′|X = S[i],v,ω)
W[i]←1
for j = 1 to M do
z∗←RAYCAST( j, X = S′[i], map)
W[i]←W[i] · P(z j| z∗)
S←WEIGHTED-SAMPLE-WITH-REPLACEMENT(N, S′, W)
return S
Figure 26.6 A Monte Carlo localization algorithm using a range-scan sensor model with
independent noise.
that the errors for the different beam directions are independent and identically distributed,
so we have
P(zt | xt) = α
M
∏
j=1
e−(zj−ˆzj)/2σ2.
Figure 26.5(b) shows an example of a four-beam range scan and two possible robot poses,
one of which is reasonably likely to have produced the observed scan and one of which is not.
Comparing the range-scan model to the landmark model, we see that the range-scan model
has the advantage that there is no need to identify a landmark before the range scan can be
interpreted; indeed, in Figure 26.5(b), the robot faces a featureless wall. On the other hand,
if there are visible, identiﬁable landmarks, they may provide instant localization.
Section 14.4 described the Kalman ﬁlter, which represents the belief state as a single
multivariate Gaussian, and the particle ﬁlter, which represents the belief state by a collection
of particles that correspond to states. Most modern localization algorithms use one of these
two representations of the robot’s belief P(Xt | z1:t,a1:t−1).
Localization using particle ﬁltering is called Monte Carlo localization, or MCL. The
Monte Carlo
localization
MCL algorithm is an instance of the particle-ﬁltering algorithm of Figure 14.17 (page 510).
All we need to do is supply the appropriate motion model and sensor model. Figure 26.6
shows one version using the range-scan sensor model. The operation of the algorithm is
illustrated in Figure 26.7 as the robot ﬁnds out where it is inside an ofﬁce building. In the ﬁrst
image, the particles are uniformly distributed based on the prior, indicating global uncertainty

## Page 942
