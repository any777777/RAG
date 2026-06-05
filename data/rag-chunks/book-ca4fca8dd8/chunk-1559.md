---
chunk_id: "book-ca4fca8dd8-chunk-1559"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1559
confidence: "first-pass"
extraction_method: "structured-local"
---

942
Chapter 26
Robotics
about the robot’s position. In the second image, the ﬁrst set of measurements arrives and the
particles form clusters in the areas of high posterior belief. In the third, enough measurements
are available to push all the particles to a single location.
The Kalman ﬁlter is the other major way to localize. A Kalman ﬁlter represents the
posterior P(Xt | z1:t,a1:t−1) by a Gaussian. The mean of this Gaussian will be denoted µt and
its covariance Σt. The main problem with Gaussian beliefs is that they are closed only under
linear motion models f and linear measurement models h. For nonlinear f or h, the result of
updating a ﬁlter is in general not Gaussian. Thus, localization algorithms using the Kalman
ﬁlter linearize the motion and sensor models. Linearization is a local approximation of a
Linearization
nonlinear function by a linear function. Figure 26.8 illustrates the concept of linearization
for a (one-dimensional) robot motion model. On the left, it depicts a nonlinear motion model
f(xt,at) (the control at is omitted in this graph since it plays no role in the linearization). On
the right, this function is approximated by a linear function ˜f(xt,at). This linear function is
tangent to f at the point µt, the mean of our state estimate at time t. Such a linearization
is called ﬁrst degree Taylor expansion. A Kalman ﬁlter that linearizes f and h via Taylor
Taylor expansion
expansion is called an extended Kalman ﬁlter (or EKF). Figure 26.9 shows a sequence of
estimates of a robot running an extended Kalman ﬁlter localization algorithm.
As the robot moves, the uncertainty in its location estimate increases, as shown by the
error ellipses. Its error decreases as it senses the range and bearing to a landmark with known
location and increases again as the robot loses sight of the landmark. EKF algorithms work
well if landmarks are easily identiﬁed. Otherwise, the posterior distribution may be multi-
modal, as in Figure 26.7(b). The problem of needing to know the identity of landmarks is an
instance of the data association problem discussed in Figure 18.3.
In some situations, no map of the environment is available. Then the robot will have to
acquire a map. This is a bit of a chicken-and-egg problem: the navigating robot will have to
determine its location relative to a map it doesn’t quite know, at the same time building this
map while it doesn’t quite know its actual location. This problem is important for many robot
applications, and it has been studied extensively under the name simultaneous localization
and mapping, abbreviated as SLAM.
Simultaneous
localization and
mapping
SLAM problems are solved using many different probabilistic techniques, including the
extended Kalman ﬁlter discussed above. Using the EKF is straightforward: just augment
the state vector to include the locations of the landmarks in the environment. Luckily, the
EKF update scales quadratically, so for small maps (e.g., a few hundred landmarks) the com-
putation is quite feasible. Richer maps are often obtained using graph relaxation methods,
similar to the Bayesian network inference techniques discussed in Chapter 13. Expectation–
maximization is also used for SLAM.
26.4.2 Other types of perception
Not all of robot perception is about localization or mapping. Robots also perceive temper-
ature, odors, sound, and so on. Many of these quantities can be estimated using variants of
dynamic Bayes networks. All that is required for such estimators are conditional probability
distributions that characterize the evolution of state variables over time, and sensor models
that describe the relation of measurements to state variables.
It is also possible to program a robot as a reactive agent, without explicitly reasoning
about probability distributions over states. We cover that approach in Section 26.9.1.
