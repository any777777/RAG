---
chunk_id: "book-ca4fca8dd8-chunk-0829"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 829
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 14.4
Kalman Filters
501
Let us ﬁrst deﬁne the general temporal model used with Kalman ﬁltering. Both the tran-
sition model and the sensor model are required to be a linear transformation with additive
Gaussian noise. Thus, we have
P(xt+1 |xt) = N(xt+1;Fxt,Σx)
P(zt |xt) = N(zt;Hxt,Σz),
(14.21)
where F and Σx are matrices describing the linear transition model and transition noise co-
variance, and H and Σz are the corresponding matrices for the sensor model. Now the update
equations for the mean and covariance, in their full, hairy horribleness, are
µt+1 = Fµt +Kt+1(zt+1 −HFµt)
Σt+1 = (I−Kt+1H)(FΣtF⊤+Σx),
(14.22)
where Kt+1 =(FΣtF⊤+Σx)H⊤(H(FΣtF⊤+Σx)H⊤+Σz)−1 is the Kalman gain matrix. Be-
Kalman gain matrix
lieve it or not, these equations make some intuitive sense. For example, consider the up-
date for the mean state estimate µ. The term Fµt is the predicted state at t + 1, so HFµt is
the predicted observation. Therefore, the term zt+1 −HFµt represents the error in the pre-
dicted observation. This is multiplied by Kt+1 to correct the predicted state; hence, Kt+1
is a measure of how seriously to take the new observation relative to the prediction. As in
Equation (14.20), we also have the property that the variance update is independent of the
observations. The sequence of values for Σt and Kt can therefore be computed ofﬂine, and
the actual calculations required during online tracking are quite modest.
To illustrate these equations at work, we have applied them to the problem of tracking an
object moving on the X–Y plane. The state variables are X = (X,Y, ˙X, ˙Y)⊤, so F, Σx, H, and
Σz are 4×4 matrices. Figure 14.11(a) shows the true trajectory, a series of noisy observations,
and the trajectory estimated by Kalman ﬁltering, along with the covariances indicated by the
one-standard-deviation contours. The ﬁltering process does a good job of tracking the actual
motion, and, as expected, the variance quickly reaches a ﬁxed point.
We can also derive equations for smoothing as well as ﬁltering with linear–Gaussian
models. The smoothing results are shown in Figure 14.11(b). Notice how the variance in the
position estimate is sharply reduced, except at the ends of the trajectory (why?), and that the
estimated trajectory is much smoother.
14.4.4 Applicability of Kalman ﬁltering
The Kalman ﬁlter and its elaborations are used in a vast array of applications. The “classical”
application is in radar tracking of aircraft and missiles. Related applications include acoustic
tracking of submarines and ground vehicles and visual tracking of vehicles and people. In a
slightly more esoteric vein, Kalman ﬁlters are used to reconstruct particle trajectories from
bubble-chamber photographs and ocean currents from satellite surface measurements. The
range of application is much larger than just the tracking of motion: any system characterized
by continuous state variables and noisy measurements will do. Such systems include pulp
mills, chemical plants, nuclear reactors, plant ecosystems, and national economies.
The fact that Kalman ﬁltering can be applied to a system does not mean that the re-
sults will be valid or useful. The assumptions made—linear–Gaussian transition and sensor
models—are very strong. The extended Kalman ﬁlter (EKF) attempts to overcome nonlin-
Extended Kalman
ﬁlter (EKF)
earities in the system being modeled. A system is nonlinear if the transition model cannot
Nonlinear
be described as a matrix multiplication of the state vector, as in Equation (14.21). The EKF
