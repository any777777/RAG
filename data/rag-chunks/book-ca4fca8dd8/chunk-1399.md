---
chunk_id: "book-ca4fca8dd8-chunk-1399"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1399
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 23.3
Active Reinforcement Learning
849
 0
 0.5
 1
 1.5
 2
 0
 100
 200
 300
 400
 500
RMS error, policy loss
Number of trials
RMS error
Policy loss
(a)
(b)
Figure 23.6 Performance of a greedy ADP agent that executes the action recommended by
the optimal policy for the learned model. (a) The root mean square (RMS) error averaged
across all nine nonterminal squares and the policy loss in (1,1). We see that the policy con-
verges quickly, after just eight trials, to a suboptimal policy with a loss of 0.235. (b) The
suboptimal policy to which the greedy agent converges in this particular sequence of trials.
Notice the Down action in (1,2).
The greedy agent has overlooked the fact that actions do more than provide rewards;
they also provide information in the form of percepts in the resulting states. As we saw with
bandit problems in Section 16.3, an agent must make a tradeoff between exploitation of the
current best action to maximize its short-term reward and exploration of previously unknown
states to gain information that can lead to a change in policy (and to greater rewards in the
future). In the real world, one constantly has to decide between continuing in a comfortable
existence, versus striking out into the unknown in the hopes of a better life.
Although bandit problems are difﬁcult to solve exactly to obtain an optimal exploration
scheme, it is nonetheless possible to come up with a scheme that will eventually discover an
optimal policy, even if it might take longer to do so than is optimal. Any such scheme should
not be greedy in terms of the immediate next move, but should be what is called “greedy in
the limit of inﬁnite exploration,” or GLIE. A GLIE scheme must try each action in each state
GLIE
an unbounded number of times to avoid having a ﬁnite probability that an optimal action is
missed. An ADP agent using such a scheme will eventually learn the true transition model,
and can then operate under exploitation.
There are several GLIE schemes; one of the simplest is to have the agent choose a random
action at time step t with probability 1/t and to follow the greedy policy otherwise. While this
does eventually converge to an optimal policy, it can be slow. A better approach would give
some weight to actions that the agent has not tried very often, while tending to avoid actions
that are believed to be of low utility (as we did with Monte Carlo tree search in Section 6.4).
This can be implemented by altering the constraint equation (23.4) so that it assigns a higher
utility estimate to relatively unexplored state–action pairs.
This amounts to an optimistic prior over the possible environments and causes the agent
to behave initially as if there were wonderful rewards scattered all over the place. Let us use
U+(s) to denote the optimistic estimate of the utility (i.e., the expected reward-to-go) of the
