---
chunk_id: "book-ca4fca8dd8-chunk-0822"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 822
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 495

Section 14.3
Hidden Markov Models
495
(a) Posterior distribution over robot location after  E1 = 1011
(b) Posterior distribution over robot location after  E1 = 1011, E2 = 1010
Figure 14.7 Posterior distribution over robot location: (a) after one observation E1 =1011
(i.e., obstacles to the north, south, and west); (b) after a random move to an adjacent location
and a second observation E2 =1010 (i.e., obstacles to the north and south). The darkness of
each square corresponds to the probability that the robot is at that location. The sensor error
rate for each bit is ϵ=0.2.
bits that are different—between the true values for square i and the actual reading et, then the
probability that a robot in square i would receive a sensor reading et is
P(Et =et |Xt =i) = (Ot)ii = (1−ϵ)4−ditϵdit .
For example, the probability that a square with obstacles to the north and south would produce
a sensor reading 1110 is (1−ϵ)3ϵ1.
Given the matrices T and Ot, the robot can use Equation (14.12) to compute the posterior
distribution over locations—that is, to work out where it is. Figure 14.7 shows the distri-
butions P(X1 |E1 =1011) and P(X2 |E1 =1011,E2 =1010). This is the same maze we saw
before in Figure 4.18 (page 152), but there we used logical ﬁltering to ﬁnd the locations that
were possible, assuming perfect sensing. Those same locations are still the most likely with
noisy sensing, but now every location has some nonzero probability because any location
could produce any sensor values.
In addition to ﬁltering to estimate its current location, the robot can use smoothing (Equa-
tion (14.13)) to work out where it was at any given past time—for example, where it began
at time 0—and it can use the Viterbi algorithm to work out the most likely path it has taken
to get where it is now. Figure 14.8 shows the localization error and Viterbi path error for
various values of the per-bit sensor error rate ϵ. Even when ϵ is 0.20—which means that the
overall sensor reading is wrong 59% of the time—the robot is usually able to work out its lo-
cation to within two squares after 20 observations. This is because of the algorithm’s ability
to integrate evidence over time and to take into account the probabilistic constraints imposed

## Page 496
