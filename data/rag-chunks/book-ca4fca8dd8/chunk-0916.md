---
chunk_id: "book-ca4fca8dd8-chunk-0916"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 916
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 16.1
Sequential Decision Problems
553
Figure 16.1 (a) A simple, stochastic 4×3 environment that presents the agent with a se-
quential decision problem. (b) Illustration of the transition model of the environment: the
“intended” outcome occurs with probability 0.8, but with probability 0.2 the agent moves
at right angles to the intended direction. A collision with a wall results in no movement.
Transitions into the two terminal states have reward +1 and –1, respectively, and all other
transitions have a reward of –0.04.
As in Chapter 3, the transition model (or just “model,” when the meaning is clear) de-
scribes the outcome of each action in each state. Here, the outcome is stochastic, so we write
P(s′ |s,a) for the probability of reaching state s′ if action a is done in state s. (Some authors
write T(s,a,s′) for the transition model.) We will assume that transitions are Markovian: the
probability of reaching s′ from s depends only on s and not on the history of earlier states.
To complete the deﬁnition of the task environment, we must specify the utility function
for the agent. Because the decision problem is sequential, the utility function will depend
on a sequence of states and actions—an environment history—rather than on a single state.
Later in this section, we investigate the nature of utility functions on histories; for now, we
simply stipulate that for every transition from s to s′ via action a, the agent receives a reward
Reward
R(s,a,s′). The rewards may be positive or negative, but they are bounded by ±Rmax.1
For our particular example, the reward is −0.04 for all transitions except those entering
terminal states (which have rewards +1 and –1). The utility of an environment history is just
(for now) the sum of the rewards received. For example, if the agent reaches the +1 state after
10 steps, its total utility will be (9× −0.04)+1=0.64. The negative reward of –0.04 gives
the agent an incentive to reach (4,3) quickly, so our environment is a stochastic generalization
of the search problems of Chapter 3. Another way of saying this is that the agent does not
enjoy living in this environment and so it wants to leave as soon as possible.
To sum up: a sequential decision problem for a fully observable, stochastic environment
with a Markovian transition model and additive rewards is called a Markov decision process,
Markov decision
process
or MDP, and consists of a set of states (with an initial state s0); a set ACTIONS(s) of actions
in each state; a transition model P(s′ |s,a); and a reward function R(s,a,s′). Methods for
solving MDPs usually involve dynamic programming: simplifying a problem by recursively
Dynamic
programming
breaking it into smaller pieces and remembering the optimal solutions to the pieces.
1
It is also possible to use costs c(s,a,s′), as we did in the deﬁnition of search problems in Chapter 3. The use
of rewards is, however, standard in the literature on sequential decisions under uncertainty.
