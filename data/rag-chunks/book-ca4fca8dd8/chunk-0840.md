---
chunk_id: "book-ca4fca8dd8-chunk-0840"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 840
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 14.5
Dynamic Bayesian Networks
507
1
Battery
Battery0
1
BMeter
0
BMBroken
1
BMBroken
f
t
0
B
1
P(B )
1.000
0.001
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
P(BMBrokent |...5555000000...)
P(BMBrokent |...5555005555...)
E(Batteryt)
Time step
(a)
(b)
Figure 14.15 (a) A DBN fragment showing the sensor status variable required for modeling
persistent failure of the battery sensor. (b) Upper curves: trajectories of the expected value of
Batteryt for the “transient failure” and “permanent failure” observations sequences. Lower
curves: probability trajectories for BMBroken given the two observation sequences.
arc linking BMBroken0 to BMBroken1. This persistence arc has a CPT that gives a small
Persistence arc
probability of failure in any given time step, say, 0.001, but speciﬁes that the sensor stays
broken once it breaks. When the sensor is OK, the sensor model for BMeter is identical to
the transient failure model; when the sensor is broken, it says BMeter is always 0, regardless
of the actual battery charge.
The persistent failure model for the battery sensor is shown in Figure 14.15(a). Its per-
formance on the two data sequences (temporary blip and persistent failure) is shown in Fig-
ure 14.15(b). There are several things to notice about these curves. First, in the case of the
temporary blip, the probability that the sensor is broken rises signiﬁcantly after the second
0 reading, but immediately drops back to zero once a 5 is observed. Second, in the case of
persistent failure, the probability that the sensor is broken rises quickly to almost 1 and stays
there. Finally, once the sensor is known to be broken, the robot can only assume that its
battery discharges at the “normal” rate. This is shown by the gradually descending level of
E(Batteryt |. . .).
So far, we have merely scratched the surface of the problem of representing complex
processes. The variety of transition models is huge, encompassing topics as disparate as
modeling the human endocrine system and modeling multiple vehicles driving on a freeway.
Sensor modeling is also a vast subﬁeld in itself. But dynamic Bayesian networks can model
even subtle phenomena, such as sensor drift, sudden decalibration, and the effects of exoge-
nous conditions (such as weather) on sensor readings.
14.5.2 Exact inference in DBNs
Having sketched some ideas for representing complex processes as DBNs, we now turn to the
question of inference. In a sense, this question has already been answered: dynamic Bayesian
networks are Bayesian networks, and we already have algorithms for inference in Bayesian
networks. Given a sequence of observations, one can construct the full Bayesian network rep-
