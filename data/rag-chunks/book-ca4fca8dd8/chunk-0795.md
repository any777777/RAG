---
chunk_id: "book-ca4fca8dd8-chunk-0795"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 795
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 14
PROBABILISTIC REASONING OVER
TIME
In which we try to interpret the present, understand the past, and perhaps predict the future,
even when very little is crystal clear.
Agents in partially observable environments must be able to keep track of the current state, to
the extent that their sensors allow. In Section 4.4 we showed a methodology for doing that: an
agent maintains a belief state that represents which states of the world are currently possible.
From the belief state and a transition model, the agent can predict how the world might
evolve in the next time step. From the percepts observed and a sensor model, the agent can
update the belief state. This is a pervasive idea: in Chapter 4 belief states were represented by
explicitly enumerated sets of states, whereas in Chapters 7 and 11 they were represented by
logical formulas. Those approaches deﬁned belief states in terms of which world states were
possible, but could say nothing about which states were likely or unlikely. In this chapter, we
use probability theory to quantify the degree of belief in elements of the belief state.
As we show in Section 14.1, time itself is handled in the same way as in Chapter 7: a
changing world is modeled using a variable for each aspect of the world state at each point
in time. The transition and sensor models may be uncertain: the transition model describes
the probability distribution of the variables at time t, given the state of the world at past
times, while the sensor model describes the probability of each percept at time t, given the
current state of the world. Section 14.2 deﬁnes the basic inference tasks and describes the
general structure of inference algorithms for temporal models. Then we describe three spe-
ciﬁc kinds of models: hidden Markov models, Kalman ﬁlters, and dynamic Bayesian
networks (which include hidden Markov models and Kalman ﬁlters as special cases).
14.1 Time and Uncertainty
We have developed our techniques for probabilistic reasoning in the context of static worlds,
in which each random variable has a single ﬁxed value. For example, when repairing a car,
we assume that whatever is broken remains broken during the process of diagnosis; our job
is to infer the state of the car from observed evidence, which also remains ﬁxed.
Now consider a slightly different problem: treating a diabetic patient. As in the case of
car repair, we have evidence such as recent insulin doses, food intake, blood sugar measure-
ments, and other physical signs. The task is to assess the current state of the patient, including
the actual blood sugar level and insulin level. Given this information, we can make a deci-
sion about the patient’s food intake and insulin dose. Unlike the case of car repair, here the
