---
chunk_id: "book-ca4fca8dd8-chunk-1556"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1556
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 939

Section 26.4
Robotic Perception
939
Figure 26.4 Robot perception can be viewed as temporal inference from sequences of ac-
tions and measurements, as illustrated by this dynamic decision network.
but there are two differences here: we condition on the actions as well as the observations,
and we deal with continuous rather than discrete variables. Thus, we modify the recursive
ﬁltering equation (14.5 on page 485) to use integration rather than summation:
P(Xt+1 | z1:t+1,a1:t)
= αP(zt+1 | Xt+1)
Z
P(Xt+1 | xt,at) P(xt | z1:t,a1:t−1) dxt .
(26.1)
This equation states that the posterior over the state variables X at time t + 1 is calculated
recursively from the corresponding estimate one time step earlier. This calculation involves
the previous action at and the current sensor measurement zt+1. For example, if our goal is
to develop a soccer-playing robot, Xt+1 might include the location of the soccer ball relative
to the robot. The posterior P(Xt |z1:t,a1:t−1) is a probability distribution over all states that
captures what we know from past sensor measurements and controls. Equation (26.1) tells us
how to recursively estimate this location, by incrementally folding in sensor measurements
(e.g., camera images) and robot motion commands. The probability P(Xt+1 | xt,at) is called
the transition model or motion model, and P(zt+1 | Xt+1) is the sensor model.
Motion model
26.4.1 Localization and mapping
Localization is the problem of ﬁnding out where things are—including the robot itself. To
Localization
keep things simple, let us consider a mobile robot that moves slowly in a ﬂat two-dimensional
world. Let us also assume the robot is given an exact map of the environment. (An example
of such a map appears in Figure 26.7.) The pose of such a mobile robot is deﬁned by its
two Cartesian coordinates with values x and y and its heading with value θ, as illustrated in
Figure 26.5(a). If we arrange those three values in a vector, then any particular state is given
by Xt =(xt,yt,θt)⊤. So far so good.
In the kinematic approximation, each action consists of the “instantaneous” speciﬁcation
of two velocities—a translational velocity vt and a rotational velocity ωt. For small time
intervals ∆t, a crude deterministic model of the motion of such robots is given by
ˆXt+1 = f(Xt,vt,ωt
|{z}
at
) = Xt +


vt∆t cosθt
vt∆t sinθt
ωt∆t

.

## Page 940
