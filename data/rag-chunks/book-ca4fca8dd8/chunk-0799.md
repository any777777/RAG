---
chunk_id: "book-ca4fca8dd8-chunk-0799"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 799
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 14.1
Time and Uncertainty
481
Xt–2
Xt–1
Xt
(a)
(b)
Xt+1
Xt+2
Xt–2
Xt–1
Xt
Xt+1
Xt+2
Figure 14.1 (a) Bayesian network structure corresponding to a ﬁrst-order Markov process
with state deﬁned by the variables Xt. (b) A second-order Markov process.
14.1.2 Transition and sensor models
With the set of state and evidence variables for a given problem decided on, the next step is
to specify how the world evolves (the transition model) and how the evidence variables get
their values (the sensor model).
The transition model speciﬁes the probability distribution over the latest state variables,
given the previous values, that is, P(Xt |X0:t−1). Now we face a problem: the set X0:t−1 is
unbounded in size as t increases. We solve the problem by making a Markov assumption—
Markov assumption
that the current state depends on only a ﬁnite ﬁxed number of previous states. Processes
satisfying this assumption were ﬁrst studied in depth by the statistician Andrei Markov (1856–
1922) and are called Markov processes or Markov chains. They come in various ﬂavors;
Markov process
the simplest is the ﬁrst-order Markov process, in which the current state depends only on
First-order Markov
process
the previous state and not on any earlier states. In other words, a state provides enough
information to make the future conditionally independent of the past, and we have
P(Xt |X0:t−1) = P(Xt |Xt−1).
(14.1)
Hence, in a ﬁrst-order Markov process, the transition model is the conditional distribution
P(Xt |Xt−1). The transition model for a second-order Markov process is the conditional dis-
tribution P(Xt |Xt−2,Xt−1). Figure 14.1 shows the Bayesian network structures correspond-
ing to ﬁrst-order and second-order Markov processes.
Even with the Markov assumption there is still a problem: there are inﬁnitely many pos-
sible values of t. Do we need to specify a different distribution for each time step? We avoid
this problem by assuming that changes in the world state are caused by a time-homogeneous
Time-homogeneous
process—that is, a process of change that is governed by laws that do not themselves change
over time. In the umbrella world, then, the conditional probability of rain, P(Rt |Rt−1), is the
same for all t, and we need specify only one conditional probability table.
Now for the sensor model. The evidence variables Et could depend on previous vari-
ables as well as the current state variables, but any state that’s worth its salt should sufﬁce to
generate the current sensor values. Thus, we make a sensor Markov assumption as follows:
Sensor Markov
assumption
P(Et |X0:t,E1:t−1) = P(Et |Xt).
(14.2)
Thus, P(Et |Xt) is our sensor model (sometimes called the observation model). Figure 14.2
shows both the transition model and the sensor model for the umbrella example. Notice the
direction of the dependence between state and sensors: the arrows go from the actual state
of the world to sensor values because the state of the world causes the sensors to take on
particular values: the rain causes the umbrella to appear. (The inference process, of course,
