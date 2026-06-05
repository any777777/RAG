---
chunk_id: "book-ca4fca8dd8-chunk-1560"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1560
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 943

Section 26.4
Robotic Perception
943
Robot position
(a)
Robot position
(b)
Robot position
(c)
Figure 26.7 Monte Carlo localization, a particle ﬁltering algorithm for mobile robot localiza-
tion. (a) Initial, global uncertainty. (b) Approximately bimodal uncertainty after navigating
in the (symmetric) corridor. (c) Unimodal uncertainty after entering a room and ﬁnding it to
be distinctive.

## Page 944

944
Chapter 26
Robotics
Xt+1
Xt
μt
Σt
f(Xt, at)
f(μt, at)
Σt+1
Xt+1
Xt
μt
Σt
f(Xt, at)
f(μt, at)
Σt+1
Σt+1
~
f(Xt, at) = f(μt, at) + Ft(Xt − μt)
~
(a)
(b)
Figure 26.8 One-dimensional illustration of a linearized motion model: (a) The function f,
and the projection of a mean µt and a covariance interval (based on Σt) into time t + 1. (b)
The linearized version is the tangent of f at µt. The projection of the mean µt is correct.
However, the projected covariance ˜Σt+1 differs from Σt+1.
robot
landmark
Figure 26.9 Localization using the extended Kalman ﬁlter. The robot moves on a straight
line. As it progresses, its uncertainty in its location estimate increases, as illustrated by the
error ellipses. When it observes a landmark with known position, the uncertainty is reduced.
The trend in robotics is clearly towards representations with well-deﬁned semantics.
Probabilistic techniques outperform other approaches in many hard perceptual problems such
as localization and mapping. However, statistical techniques are sometimes too cumbersome,
and simpler solutions may be just as effective in practice. To help decide which approach to
take, experience working with real physical robots is your best teacher.
26.4.3 Supervised and unsupervised learning in robot perception
Machine learning plays an important role in robot perception. This is particularly the case
when the best internal representation is not known. One common approach is to map high-
dimensional sensor streams into lower-dimensional spaces using unsupervised machine learn-
ing methods (see Chapter 19). Such an approach is called low-dimensional embedding.
Low-dimensional
embedding
Machine learning makes it possible to learn sensor and motion models from data, while si-
multaneously discovering a suitable internal representation.
Another machine learning technique enables robots to continuously adapt to big changes
in sensor measurements. Picture yourself walking from a sunlit space into a dark room with
neon lights. Clearly, things are darker inside. But the change of light source also affects all
