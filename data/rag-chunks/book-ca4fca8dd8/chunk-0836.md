---
chunk_id: "book-ca4fca8dd8-chunk-0836"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 836
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 14.5
Dynamic Bayesian Networks
505
represent the actual battery charge level, which has as parents the previous battery level and
the velocity, and we add BMetert, which measures the battery charge level. This gives us the
basic model shown in Figure 14.13(b).
It is worth looking in more depth at the nature of the sensor model for BMetert. Let us
suppose, for simplicity, that both Batteryt and BMetert can take on discrete values 0 through
5. (Exercise 14.BATT asks you to relate this discrete model to a corresponding continuous
model.) If the meter is always accurate, then the CPT P(BMetert |Batteryt) should have
probabilities of 1.0 “along the diagonal” and probabilities of 0.0 elsewhere. In reality, noise
always creeps into measurements. For continuous measurements, a Gaussian distribution
with a small variance might be used.7 For our discrete variables, we can approximate a
Gaussian using a distribution in which the probability of error drops off in the appropriate
way, so that the probability of a large error is very small. We use the term Gaussian error
model to cover both the continuous and discrete versions.
Gaussian error model
Anyone with hands-on experience of robotics, computerized process control, or other
forms of automatic sensing will readily testify to the fact that small amounts of measurement
noise are often the least of one’s problems. Real sensors fail. When a sensor fails, it does
not necessarily send a signal saying, “Oh, by the way, the data I’m about to send you is a
load of nonsense.” Instead, it simply sends the nonsense. The simplest kind of failure is
called a transient failure, where the sensor occasionally decides to send some nonsense. For
Transient failure
example, the battery level sensor might have a habit of sending a reading of 0 when someone
bumps the robot, even if the battery is fully charged.
Let’s see what happens when a transient failure occurs with a Gaussian error model that
doesn’t accommodate such failures. Suppose, for example, that the robot is sitting quietly
and observes 20 consecutive battery readings of 5. Then the battery meter has a temporary
seizure and the next reading is BMeter21 =0. What will the simple Gaussian error model lead
us to believe about Battery21? According to Bayes’ rule, the answer depends on both the
sensor model P(BMeter21 =0|Battery21) and the prediction P(Battery21 |BMeter1:20). If the
probability of a large sensor error is signiﬁcantly less than the probability of a transition to
Battery21 =0, even if the latter is very unlikely, then the posterior distribution will assign a
high probability to the battery’s being empty.
A second reading of 0 at t =22 will make this conclusion almost certain. If the transient
failure then disappears and the reading returns to 5 from t =23 onwards, the estimate for the
battery level will quickly return to 5. (This does not mean the algorithm thinks the battery
magically recharged itself, which may be physically impossible; instead, the algorithm now
believes that the battery was never low and the extremely unlikely hypothesis that the battery
meter had two consecutive huge errors must be the right explanation.) This course of events
is illustrated in the upper curve of Figure 14.14(a), which shows the expected value (see
Appendix A) of Batteryt over time, using a discrete Gaussian error model.
Despite the recovery, there is a time (t =22) when the robot is convinced that its battery
is empty; presumably, then, it should send out a mayday signal and shut down. Alas, its
oversimpliﬁed sensor model has led it astray. The moral of the story is simple: for the system ◀
to handle sensor failure properly, the sensor model must include the possibility of failure.
7
Strictly speaking, a Gaussian distribution is problematic because it assigns nonzero probability to large nega-
tive charge levels. The beta distribution is sometimes a better choice for a variable whose range is restricted.
