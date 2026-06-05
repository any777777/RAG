---
chunk_id: "book-ca4fca8dd8-chunk-0803"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 803
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 14.2
Inference in Temporal Models
483
2. Increasing the set of state variables.
For example, we could add Seasont to allow
us to incorporate historical records of rainy seasons, or we could add Temperaturet,
Humidityt, and Pressuret (perhaps at a range of locations) to allow us to use a physical
model of rainy conditions.
Exercise 14.AUGM asks you to show that the ﬁrst solution—increasing the order—can always
be reformulated as an increase in the set of state variables, keeping the order ﬁxed. Notice
that adding state variables might improve the system’s predictive power but also increases
the prediction requirements: we now have to predict the new variables as well. Thus, we are
looking for a “self-sufﬁcient” set of variables, which really means that we have to understand
the “physics” of the process being modeled. The requirement for accurate modeling of the
process is obviously lessened if we can add new sensors (e.g., measurements of temperature
and pressure) that provide information directly about the new state variables.
Consider, for example, the problem of tracking a robot wandering randomly on the X–Y
plane. One might propose that the position and velocity are a sufﬁcient set of state variables:
one can simply use Newton’s laws to calculate the new position, and the velocity may change
unpredictably. If the robot is battery-powered, however, then battery exhaustion would tend
to have a systematic effect on the change in velocity. Because this in turn depends on how
much power was used by all previous maneuvers, the Markov property is violated.
We can restore the Markov property by including the charge level Batteryt as one of the
state variables that make up Xt. This helps in predicting the motion of the robot, but in turn
requires a model for predicting Batteryt from Batteryt−1 and the velocity. In some cases, that
can be done reliably, but more often we ﬁnd that error accumulates over time. In that case,
accuracy can be improved by adding a new sensor for the battery level. We will return to the
battery example in Section 14.5.
14.2 Inference in Temporal Models
Having set up the structure of a generic temporal model, we can formulate the basic inference
tasks that must be solved:
• Filtering2 or state estimation is the task of computing the belief state P(Xt |e1:t)—
Filtering
State estimation
Belief state
the posterior distribution over the most recent state given all evidence to date. In the
umbrella example, this would mean computing the probability of rain today, given all
the umbrella observations made so far. Filtering is what a rational agent does to keep
track of the current state so that rational decisions can be made. It turns out that an
almost identical calculation provides the likelihood of the evidence sequence, P(e1:t).
• Prediction: This is the task of computing the posterior distribution over the future state,
Prediction
given all evidence to date. That is, we wish to compute P(Xt+k |e1:t) for some k > 0.
In the umbrella example, this might mean computing the probability of rain three days
from now, given all the observations to date. Prediction is useful for evaluating possible
courses of action based on their expected outcomes.
• Smoothing: This is the task of computing the posterior distribution over a past state,
Smoothing
given all evidence up to the present. That is, we wish to compute P(Xk |e1:t) for some k
2
The term “ﬁltering” refers to the roots of this problem in early work on signal processing, where the problem
is to ﬁlter out the noise in a signal by estimating its underlying properties.
