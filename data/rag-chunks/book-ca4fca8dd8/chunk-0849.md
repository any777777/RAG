---
chunk_id: "book-ca4fca8dd8-chunk-0849"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 849
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 513

Section 14.5
Dynamic Bayesian Networks
513
Location0
Location1
Dirt1,0
Dirt2,0
Dirt42,0
Dirt1,1
Dirt2,1
Dirt42,1
WallSensor1
DirtSensor1
Figure 14.20 A dynamic Bayes net for simultaneous localization and mapping in the
stochastic-dirt vacuum world. Dirty squares persist with probability p, and clean squares
become dirty with probability 1−p. The local dirt sensor is 90% accurate, for the square in
which the robot is currently located.
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0
 20
 40
 60
 80
 100
RMS error in dirt probabilities
Number of observations
p = 1.00
p = 0.95
p = 0.90
p = 0.80
p = 0.70
 0.25
 0.3
 0.35
 0.4
 0.45
 0.5
 0
 100
 200
 300
 400
 500
RMS dirt error
Number of observations
Exact, p = 1.00
Noisy, p = 1.00
(a)
(b)
Figure 14.21 (a) Performance of the standard particle ﬁltering algorithm with 1,000 par-
ticles, showing RMS error in marginal dirt probabilities compared to exact inference for
different values of the dirt persistence p. (b) Performance of Rao-Blackwellized particle ﬁl-
tering (100 particles) compared to ground truth, for both exact location sensing and noisy
wall sensing and with deterministic dirt. Data averaged over 20 runs.
It turns out that the theoretical condition requiring that “the probabilities in the transition
and sensor models are strictly greater than 0 and less than 1” is more than mere mathematical
pedantry. What happens is ﬁrst each particle initially contains 42 guesses from P(X0) about
which squares have dirt and which do not. Then, the state for each particle is projected
forward in time according to the transition model. Unfortunately, the transition model for
deterministic dirt is deterministic: the dirt stays exactly where it is. Thus, the initial guesses
in each particle are never updated by the evidence.

## Page 514
