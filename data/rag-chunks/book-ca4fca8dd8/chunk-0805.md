---
chunk_id: "book-ca4fca8dd8-chunk-0805"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 805
confidence: "first-pass"
extraction_method: "structured-local"
---

484
Chapter 14
Probabilistic Reasoning over Time
such that 0 ≤k < t. In the umbrella example, it might mean computing the probability
that it rained last Wednesday, given all the observations of the umbrella carrier made up
to today. Smoothing provides a better estimate of the state at time k than was available
at that time, because it incorporates more evidence.3
• Most likely explanation: Given a sequence of observations, we might wish to ﬁnd the
sequence of states that is most likely to have generated those observations. That is, we
wish to compute argmaxx1:t P(x1:t |e1:t). For example, if the umbrella appears on each
of the ﬁrst three days and is absent on the fourth, then the most likely explanation is that
it rained on the ﬁrst three days and did not rain on the fourth. Algorithms for this task
are useful in many applications, including speech recognition—where the aim is to ﬁnd
the most likely sequence of words, given a series of sounds—and the reconstruction of
bit strings transmitted over a noisy channel.
In addition to these inference tasks, we also have
• Learning: The transition and sensor models, if not yet known, can be learned from
observations. Just as with static Bayesian networks, dynamic Bayes net learning can be
done as a by-product of inference. Inference provides an estimate of what transitions
actually occurred and of what states generated the sensor readings, and these estimates
can be used to learn the models. The learning process can operate via an iterative up-
date algorithm called expectation–maximization or EM, or it can result from Bayesian
updating of the model parameters given the evidence. See Chapter 21 for more details.
The remainder of this section describes generic algorithms for the four inference tasks, inde-
pendent of the particular kind of model employed. Improvements speciﬁc to each model are
described in subsequent sections.
14.2.1 Filtering and prediction
As we pointed out in Section 7.7.3, a useful ﬁltering algorithm needs to maintain a current
state estimate and update it, rather than going back over the entire history of percepts for each
update. (Otherwise, the cost of each update increases as time goes by.) In other words, given
the result of ﬁltering up to time t, the agent needs to compute the result for t +1 from the new
evidence et+1. So we have
P(Xt+1 |e1:t+1) = f(et+1,P(Xt |e1:t))
for some function f. This process is called recursive estimation. (See also Sections 4.4
and 7.7.3.) We can view the calculation as being composed of two parts: ﬁrst, the current
state distribution is projected forward from t to t +1; then it is updated using the new evidence
et+1. This two-part process emerges quite simply when the formula is rearranged:
P(Xt+1 |e1:t+1) = P(Xt+1 |e1:t,et+1)
(dividing up the evidence)
= αP(et+1 |Xt+1,e1:t)P(Xt+1 |e1:t)
(using Bayes’ rule, given e1:t)
= α P(et+1 |Xt+1)
|
{z
}
update
P(Xt+1 |e1:t)
|
{z
}
prediction
(by the sensor Markov assumption).
(14.4)
Here and throughout this chapter, α is a normalizing constant used to make probabilities sum
up to 1. Now we plug in an expression for the one-step prediction P(Xt+1 |e1:t), obtained by
3
In particular, when tracking a moving object with inaccurate position observations, smoothing gives a smoother
estimated trajectory than ﬁltering—hence the name.
