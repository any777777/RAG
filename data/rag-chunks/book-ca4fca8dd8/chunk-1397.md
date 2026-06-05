---
chunk_id: "book-ca4fca8dd8-chunk-1397"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1397
confidence: "first-pass"
extraction_method: "structured-local"
---

848
Chapter 23
Reinforcement Learning
Using heuristics like this, approximate ADP algorithms can learn roughly as fast as full
ADP, in terms of the number of training sequences, but can be orders of magnitude more
efﬁcient in terms of total computation (see Exercise 23.PRSW). This enables them to handle
state spaces that are far too large for full ADP. Approximate ADP algorithms have an addi-
tional advantage: in the early stages of learning a new environment, the transition model P
often will be far from correct, so there is little point in calculating an exact utility function
to match it. An approximation algorithm can use a minimum adjustment size that decreases
as the transition model becomes more accurate. This eliminates the very long runs of value
iteration that can occur early in learning due to large changes in the model.
23.3 Active Reinforcement Learning
A passive learning agent has a ﬁxed policy that determines its behavior. An active learning
agent gets to decide what actions to take. Let us begin with the adaptive dynamic program-
ming (ADP) agent and consider how it can be modiﬁed to take advantage of this new freedom.
First, the agent will need to learn a complete transition model with outcome probabilities
for all actions, rather than just the model for the ﬁxed policy. The learning mechanism used
by PASSIVE-ADP-AGENT will do just ﬁne for this. Next, we need to take into account the
fact that the agent has a choice of actions. The utilities it needs to learn are those deﬁned by
the optimal policy; they obey the Bellman equations (which we repeat here):
U(s) = max
a∈A(s)∑
s′
P(s′ |s,a)[R(s,a,s′)+γU(s′)].
(23.4)
These equations can be solved to obtain the utility function U using the value iteration or
policy iteration algorithms from Chapter 16.
The ﬁnal issue is what to do at each step. Having obtained a utility function U that is
optimal for the learned model, the agent can extract an optimal action by one-step look-ahead
to maximize the expected utility; alternatively, if it uses policy iteration, the optimal policy is
already available, so it could simply execute the action the optimal policy recommends. But
should it?
23.3.1 Exploration
Figure 23.6 shows the results of one sequence of trials for an ADP agent that follows the
recommendation of the optimal policy for the learned model at each step. The agent does not
learn the true utilities or the true optimal policy! What happens instead is that in the third trial,
it ﬁnds a policy that reaches the +1 reward along the lower route via (2,1), (3,1), (3,2), and
(3,3). (See Figure 23.6(b).) After experimenting with minor variations, from the eighth trial
onward it sticks to that policy, never learning the utilities of the other states and never ﬁnding
the optimal route via (1,2), (1,3), and (2,3). We will call this agent a greedy agent, because
Greedy agent
it greedily takes the action that it currently believes to be optimal at each step. Sometimes
greed pays off and the agent converges to the optimal policy, but often it does not.
How can it be that choosing the optimal action leads to suboptimal results? The answer is
that the learned model is not the same as the true environment; what is optimal in the learned
model can therefore be suboptimal in the true environment. Unfortunately, the agent does
not know what the true environment is, so it cannot compute the optimal action for the true
environment. What, then, should it do?
