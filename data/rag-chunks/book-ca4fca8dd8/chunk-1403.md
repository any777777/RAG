---
chunk_id: "book-ca4fca8dd8-chunk-1403"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1403
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 23.3
Active Reinforcement Learning
851
 0.6
 0.8
 1
 1.2
 1.4
 1.6
 1.8
 2
 2.2
 0
 20
 40
 60
 80
 100
Utility estimates
Number of trials
(1,1)
(1,3)
(2,1)
(3,2)
(3,3)
 0
 0.2
 0.4
 0.6
 0.8
 1
 1.2
 1.4
 0
 20
 40
 60
 80
 100
RMS error, policy loss
Number of trials
RMS error
Policy loss
(a)
(b)
Figure 23.7 Performance of the exploratory ADP agent using R+ = 2 and Ne = 5. (a) Utility
estimates for selected states over time. (b) The RMS error in utility values and the associated
policy loss.
taking actions that might lead to any of the following:
• states with large negative rewards, such as serious car crashes;
• states from which there is no escape, such as driving the car into a deep ditch;
• states that permanently limit future rewards, such as damaging the car’s engine so that
its maximum speed is reduced.
We can end up in a bad state either because our model is unknown, and we actively choose
to explore in a direction that turns out to be bad, or because our model is incorrect and
we don’t know that a given action can have a disastrous result. Note that the algorithm in
Figure 23.2 is using maximum-likelihood estimation (see Chapter 21) to learn the transition
model; moreover, by choosing a policy based solely on the estimated model, it is acting as if
the model were correct. This is not necessarily a good idea! For example, a taxi agent that
didn’t know how trafﬁc lights work might ignore a red light once or twice with no ill effects
and then formulate a policy to ignore all red lights from then on.
A better idea would be to choose a policy that works reasonably well for the whole range
of models that have a reasonable chance of being the true model, even if the policy happens to
be suboptimal for the maximum-likelihood model. There are three mathematical approaches
that have this ﬂavor.
The ﬁrst approach, Bayesian reinforcement learning, assumes a prior probability P(h)
Bayesian
reinforcement
learning
over hypotheses h about what the true model is; the posterior probability P(h|e) is obtained
in the usual way by Bayes’ rule given the observations to date. Then, if the agent has decided
to stop learning, the optimal policy is the one that gives the highest expected utility. Let Uπ
h
be the expected utility, averaged over all possible start states, obtained by executing policy π
in model h. Then we have
π∗= argmax
π
∑
h
P(h|e)Uπ
h .
In some special cases, this policy can even be computed! If the agent will continue learning
in the future, however, then ﬁnding an optimal policy becomes considerably more difﬁcult,
