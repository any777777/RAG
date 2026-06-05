---
chunk_id: "book-ca4fca8dd8-chunk-0801"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 801
confidence: "first-pass"
extraction_method: "structured-local"
---

482
Chapter 14
Probabilistic Reasoning over Time
P(Rt|Rt-1)
0.7
0.3
P(Ut|Rt)
Figure 14.2 Bayesian network structure and conditional distributions describing the um-
brella world.
The transition model is P(Raint |Raint−1) and the sensor model is
P(Umbrellat |Raint).
goes in the other direction; the distinction between the direction of modeled dependencies
and the direction of inference is one of the principal advantages of Bayesian networks.)
In addition to specifying the transition and sensor models, we need to say how everything
gets started—the prior probability distribution at time 0, P(X0). With that, we have a speciﬁ-
cation of the complete joint distribution over all the variables, using Equation (13.2). For any
time step t,
P(X0:t,E1:t) = P(X0)
t
∏
i=1
P(Xi |Xi−1)P(Ei |Xi).
(14.3)
The three terms on the right-hand side are the initial state model P(X0), the transition model
P(Xi |Xi−1), and the sensor model P(Ei |Xi). This equation deﬁnes the semantics of the
family of temporal models represented by the three terms. Notice that standard Bayesian net-
works cannot represent such models because they require a ﬁnite set of variables. The ability
to handle an inﬁnite set of variables comes from two things: ﬁrst, deﬁning the inﬁnite set us-
ing integer indices; and second, the use of implicit universal quantiﬁcation (see Section 8.2)
to deﬁne the sensor and transition models for every time step.
The structure in Figure 14.2 is a ﬁrst-order Markov process—the probability of rain is
assumed to depend only on whether it rained the previous day. Whether such an assumption
is reasonable depends on the domain itself. The ﬁrst-order Markov assumption says that the
state variables contain all the information needed to characterize the probability distribution
for the next time slice. Sometimes the assumption is exactly true—for example, if a particle
is executing a random walk along the x-axis, changing its position by ±1 at each time step,
then using the x-coordinate as the state gives a ﬁrst-order Markov process. Sometimes the
assumption is only approximate, as in the case of predicting rain only on the basis of whether
it rained the previous day. There are two ways to improve the accuracy of the approximation:
1. Increasing the order of the Markov process model. For example, we could make a
second-order model by adding Raint−2 as a parent of Raint, which might give slightly
more accurate predictions. For example, in Palo Alto, California, it very rarely rains
more than two days in a row.
