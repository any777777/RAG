---
chunk_id: "book-ca4fca8dd8-chunk-0848"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 848
confidence: "first-pass"
extraction_method: "structured-local"
---

512
Chapter 14
Probabilistic Reasoning over Time
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0
 20
 40
 60
 80
 100
Max norm error
Number of observations
SIS
PF
Figure 14.19 Max norm error in the grid-world location estimate (compared to exact infer-
ence) for likelihood weighting (sequential importance sampling) with 100,000 samples and
particle ﬁltering with 1,000 samples; data averaged over 50 runs.
works on real-world problems: the algorithm supports thousands of applications in science
and engineering. (Some references are given at the end of the chapter.) It handles combina-
tions of discrete and continuous variables as well as nonlinear and non-Gaussian models for
continuous variables. Under certain assumptions—in particular, that the probabilities in the
transition and sensor models are bounded away from 0 and 1—it is also possible to prove that
the approximation maintains bounded error with high probability, as the ﬁgure suggests.
The particle ﬁltering algorithm does have weaknesses, however. Let’s see how it performs
for the vacuum world with dirt added. Recall from Section 14.3.2 that this increases the state
space size by a factor of 242, making exact HMM inference infeasible. We want the robot
to wander around and build a map of where the dirt is located. (This is a simple example
of simultaneous localization and mapping or SLAM, which we cover in more depth in
Chapter 26.) Let Dirti,t mean that square i is dirty at time t and let DirtSensort be true if and
only if the robot detects dirt at time t. We’ll assume that, in any given square, dirt persists
with probability p, whereas a clean square becomes dirty with probability 1−p (which means
that each square is dirty half the time, on average). The robot has a dirt sensor for its current
location; the sensor is accurate with probability 0.9. Figure 14.20 shows the DBN.
For simplicity, we’ll start by assuming that the robot has a perfect location sensor, rather
than the noisy wall sensor. The algorithm’s performance is shown in Figure 14.21(a), where
its estimates for dirt are compared to the results of exact inference. (We’ll see shortly how
exact inference is possible.) For low values of the dirt persistence p, the error remains small—
but this is no great achievement, because for every square the true posterior for dirt is close to
0.5 if the robot hasn’t visited that square recently. For higher values of p, the dirt stays around
longer, so visiting a square yields more useful information that is valid over a longer period.
Perhaps surprisingly, particle ﬁltering does worse for higher values of p. It fails completely
when p=1, even though that seems like the easiest case: the dirt arrives at time 0 and stays
put forever, so after a few tours of the world, the robot should have a close-to-perfect dirt
map. Why does particle ﬁltering fail in this case?
