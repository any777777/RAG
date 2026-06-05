---
chunk_id: "book-ca4fca8dd8-chunk-0831"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 831
confidence: "first-pass"
extraction_method: "structured-local"
---

502
Chapter 14
Probabilistic Reasoning over Time
8
10
12
14
16
18
20
22
24
26
6
7
8
9
10
11
12
8
10
12
14
16
18
20
22
24
26
6
7
8
9
10
11
12
(a)
(b)
2D filtering
2D smoothing
X
Y
true
observed
filtered
X
Y
true
observed
smoothed
Figure 14.11 (a) Results of Kalman ﬁltering for an object moving on the X–Y plane, showing
the true trajectory (left to right), a series of noisy observations, and the trajectory estimated
by Kalman ﬁltering. Variance in the position estimate is indicated by the ovals. (b) The
results of Kalman smoothing for the same observation sequence.
works by modeling the system as locally linear in xt in the region of xt =µt, the mean of the
current state distribution. This works well for smooth, well-behaved systems and allows the
tracker to maintain and update a Gaussian state distribution that is a reasonable approximation
to the true posterior. A detailed example is given in Chapter 26.
What does it mean for a system to be “unsmooth” or “poorly behaved”? Technically,
it means that there is signiﬁcant nonlinearity in system response within the region that is
“close” (according to the covariance Σt) to the current mean µt. To understand this idea
in nontechnical terms, consider the example of trying to track a bird as it ﬂies through the
jungle. The bird appears to be heading at high speed straight for a tree trunk. The Kalman
ﬁlter, whether regular or extended, can make only a Gaussian prediction of the location of the
bird, and the mean of this Gaussian will be centered on the trunk, as shown in Figure 14.12(a).
A reasonable model of the bird, on the other hand, would predict evasive action to one side or
the other, as shown in Figure 14.12(b). Such a model is highly nonlinear, because the bird’s
decision varies sharply depending on its precise location relative to the trunk.
To handle examples like these, we clearly need a more expressive language for repre-
senting the behavior of the system being modeled. Within the control theory community, for
which problems such as evasive maneuvering by aircraft raise the same kinds of difﬁculties,
the standard solution is the switching Kalman ﬁlter. In this approach, multiple Kalman ﬁl-
Switching Kalman
ﬁlter
ters run in parallel, each using a different model of the system—for example, one for straight
ﬂight, one for sharp left turns, and one for sharp right turns. A weighted sum of predictions
is used, where the weight depends on how well each ﬁlter ﬁts the current data. We will see
in the next section that this is simply a special case of the general dynamic Bayesian net-
work model, obtained by adding a discrete “maneuver” state variable to the network shown
in Figure 14.9. Switching Kalman ﬁlters are discussed further in Exercise 14.KFSW.
