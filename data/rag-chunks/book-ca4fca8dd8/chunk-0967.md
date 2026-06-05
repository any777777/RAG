---
chunk_id: "book-ca4fca8dd8-chunk-0967"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 967
confidence: "first-pass"
extraction_method: "structured-local"
---

Summary
585
Left
Left
Up
Right
Right
Right
0011
0001
1111
1000
1010
1001
Figure 16.18 A sequence of percepts, belief states, and actions in the 4×3 POMDP with
a wall-sensing error of ϵ=0.2. Notice how the early Left moves are safe—they are very
unlikely to fall into (4,2)—and coerce the agent’s location into a small number of possible
locations. After moving Up, the agent thinks it is probably in (3,3), but possibly in (1,3).
Fortunately, moving Right is a good idea in both cases, so it moves Right, ﬁnds out that it had
been in (1,3) and is now in (2,3), and then continues moving Right and reaches the goal.
for dinner, which might take tens of millions of motor-control actions. It seems necessary
to borrow some of the hierarchical planning ideas described in Section 11.4. At the time of
writing, there are not yet satisfactory and efﬁcient ways to apply these ideas in stochastic,
partially observable environments.
Summary
This chapter shows how to use knowledge about the world to make decisions even when the
outcomes of an action are uncertain and the rewards for acting might not be reaped until many
actions have passed. The main points are as follows:
• Sequential decision problems in stochastic environments, also called Markov decision
processes, or MDPs, are deﬁned by a transition model specifying the probabilistic
outcomes of actions and a reward function specifying the reward in each state.
• The utility of a state sequence is the sum of all the rewards over the sequence, possibly
discounted over time. The solution of an MDP is a policy that associates a decision
with every state that the agent might reach. An optimal policy maximizes the utility of
the state sequences encountered when it is executed.
• The utility of a state is the expected sum of rewards when an optimal policy is executed
from that state. The value iteration algorithm iteratively solves a set of equations
relating the utility of each state to those of its neighbors.
• Policy iteration alternates between calculating the utilities of states under the current
policy and improving the current policy with respect to the current utilities.
• Partially observable MDPs, or POMDPs, are much more difﬁcult to solve than are
MDPs. They can be solved by conversion to an MDP in the continuous space of belief
states; both value iteration and policy iteration algorithms have been devised. Optimal
behavior in POMDPs includes information gathering to reduce uncertainty and there-
fore make better decisions in the future.
• A decision-theoretic agent can be constructed for POMDP environments. The agent
uses a dynamic decision network to represent the transition and sensor models, to
update its belief state, and to project forward possible action sequences.
We shall return MDPs and POMDPs in Chapter 23, which covers reinforcement learning
methods that allow an agent to improve its behavior from experience.
