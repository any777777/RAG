---
chunk_id: "book-ca4fca8dd8-chunk-0838"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 838
confidence: "first-pass"
extraction_method: "structured-local"
---

506
Chapter 14
Probabilistic Reasoning over Time
-1
 0
 1
 2
 3
 4
 5
 15
 20
 25
 30
E(Batteryt |...5555005555...)
E(Batteryt |...5555000000...)
E(Batteryt)
Time step t
-1
 0
 1
 2
 3
 4
 5
 15
 20
 25
 30
E(Batteryt |...5555005555...)
E(Batteryt |...5555000000...)
E(Batteryt)
Time step
(a)
(b)
Figure 14.14 (a) Upper curve: trajectory of the expected value of Batteryt for an observation
sequence consisting of all 5s except for 0s at t =21 and t =22, using a simple Gaussian error
model. Lower curve: trajectory when the observation remains at 0 from t =21 onwards. (b)
The same experiment run with the transient failure model. The transient failure is handled
well, but the persistent failure results in excessive pessimism about the battery charge.
The simplest kind of failure model for a sensor allows a certain probability that the sensor
will return some completely incorrect value, regardless of the true state of the world. For
example, if the battery meter fails by returning 0, we might say that
P(BMetert =0|Batteryt =5)=0.03,
which is presumably much larger than the probability assigned by the simple Gaussian error
model. Let’s call this the transient failure model. How does it help when we are faced
Transient failure
model
with a reading of 0? Provided that the predicted probability of an empty battery, according
to the readings so far, is much less than 0.03, then the best explanation of the observation
BMeter21 =0 is that the sensor has temporarily failed. Intuitively, we can think of the belief
about the battery level as having a certain amount of “inertia” that helps to overcome tempo-
rary blips in the meter reading. The upper curve in Figure 14.14(b) shows that the transient
failure model can handle transient failures without a catastrophic change in beliefs.
So much for temporary blips. What about a persistent sensor failure? Sadly, failures of
this kind are all too common. If the sensor returns 20 readings of 5 followed by 20 readings
of 0, then the transient sensor failure model described in the preceding paragraph will result
in the robot gradually coming to believe that its battery is empty when in fact it may be that
the meter has failed. The lower curve in Figure 14.14(b) shows the belief “trajectory” for
this case. By t =25—ﬁve readings of 0—the robot is convinced that its battery is empty.
Obviously, we would prefer the robot to believe that its battery meter is broken—if indeed
this is the more likely event.
Unsurprisingly, to handle persistent failure, we need a persistent failure model that
Persistent failure
model
describes how the sensor behaves under normal conditions and after failure. To do this,
we need to augment the state of the system with an additional variable, say, BMBroken, that
describes the status of the battery meter. The persistence of failure must be modeled by an
