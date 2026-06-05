---
chunk_id: "book-ca4fca8dd8-chunk-1387"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1387
confidence: "first-pass"
extraction_method: "structured-local"
---

842
Chapter 23
Reinforcement Learning
0.8516
0.9078
0.9578
0.8016
0.7003
0.7453
0.6953
0.6514
0.4279
(a)
(b)
Figure 23.1 (a) The optimal policies for the stochastic environment with R(s,a,s′)= −0.04
for transitions between nonterminal states. There are two policies because in state (3,1) both
Left and Up are optimal. We saw this before in Figure 16.2. (b) The utilities of the states in
the 4×3 world, given policy π.
We begin in Section 23.2 with passive reinforcement learning, where the agent’s policy
Passive
reinforcement
learning
is ﬁxed and the task is to learn the utilities of states (or of state–action pairs); this could
also involve learning a model of the environment. (An understanding of Markov decision
processes, as described in Chapter 16, is essential for this section.) Section 23.3 covers active
reinforcement learning, where the agent must also ﬁgure out what to do. The principal
Active reinforcement
learning
issue is exploration: an agent must experience as much as possible of its environment in
order to learn how to behave in it. Section 23.4 discusses how an agent can use inductive
learning (including deep learning methods) to learn much faster from its experiences. We
also discuss other approaches that can help scale up RL to solve real problems, including
providing intermediate pseudorewards to guide the learner and organizing behavior into a
hierarchy of actions. Section 23.5 covers methods for policy search. In Section 23.6, we
explore apprenticeship learning: training a learning agent using demonstrations rather than
reward signals. Finally, Section 23.7 reports on applications of reinforcement learning.
23.2 Passive Reinforcement Learning
We start with the simple case of a fully observable environment with a small number of
actions and states, in which an agent already has a ﬁxed policy π(s) that determines its actions.
The agent is trying to learn the utility function Uπ(s)—the expected total discounted reward
if policy π is executed beginning in state s. We call this a passive learning agent.
Passive learning
agent
The passive learning task is similar to the policy evaluation task, part of the policy iter-
ation algorithm described in Section 16.2.2. The difference is that the passive learning agent
does not know the transition model P(s′ |s,a), which speciﬁes the probability of reaching
state s′ from state s after doing action a; nor does it know the reward function R(s,a,s′),
which speciﬁes the reward for each transition.
We will use as our example the 4×3 world introduced in Chapter 16. Figure 23.1 shows
the optimal policies for that world and the corresponding utilities. The agent executes a set
