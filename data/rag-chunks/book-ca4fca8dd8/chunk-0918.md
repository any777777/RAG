---
chunk_id: "book-ca4fca8dd8-chunk-0918"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 918
confidence: "first-pass"
extraction_method: "structured-local"
---

554
Chapter 16
Making Complex Decisions
The next question is, what does a solution to the problem look like? No ﬁxed action
sequence can solve the problem, because the agent might end up in a state other than the
goal. Therefore, a solution must specify what the agent should do for any state that the agent
might reach. A solution of this kind is called a policy. It is traditional to denote a policy by π,
Policy
and π(s) is the action recommended by the policy π for state s. No matter what the outcome
of the action, the resulting state will be in the policy, and the agent will know what to do next.
Each time a given policy is executed starting from the initial state, the stochastic nature
of the environment may lead to a different environment history. The quality of a policy is
therefore measured by the expected utility of the possible environment histories generated
by that policy. An optimal policy is a policy that yields the highest expected utility. We
Optimal policy
use π∗to denote an optimal policy. Given π∗, the agent decides what to do by consulting
its current percept, which tells it the current state s, and then executing the action π∗(s). A
policy represents the agent function explicitly and is therefore a description of a simple reﬂex
agent, computed from the information used for a utility-based agent.
The optimal policies for the world of Figure 16.1 are shown in Figure 16.2(a). There are
two policies because the agent is exactly indifferent between going left and going up from
(3,1): going left is safer but longer, while going up is quicker but risks falling into (4,2) by
accident. In general there will often be multiple optimal policies.
The balance of risk and reward changes depending on the value of r=R(s,a,s′) for tran-
sitions between nonterminal states. The policies shown in Figure 16.2(a) are optimal for
−0.0850 < r < −0.0273. Figure 16.2(b) shows optimal policies for four other ranges of r.
When r < −1.6497, life is so painful that the agent heads straight for the nearest exit, even
if the exit is worth –1. When −0.7311 < r < −0.4526, life is quite unpleasant; the agent
takes the shortest route to the +1 state from (2,1), (3,1), and (3,2), but from (4,1) the cost of
reaching +1 is so high that the agent prefers to dive straight into –1. When life is only slightly
dreary (−0.0274 < r < 0), the optimal policy takes no risks at all. In (4,1) and (3,2), the
agent heads directly away from the –1 state so that it cannot fall in by accident, even though
this means banging its head against the wall quite a few times. Finally, if r > 0, then life is
positively enjoyable and the agent avoids both exits. As long as the actions in (4,1), (3,2),
and (3,3) are as shown, every policy is optimal, and the agent obtains inﬁnite total reward
because it never enters a terminal state. It turns out that there are nine optimal policies in all
for various ranges of r; Exercise 16.THRC asks you to ﬁnd them.
The introduction of uncertainty brings MDPs closer to the real world than deterministic
search problems. For this reason, MDPs have been studied in several ﬁelds, including AI,
operations research, economics, and control theory. Dozens of solution algorithms have been
proposed, several of which we discuss in Section 16.2. First, however, we spell out in more
detail the deﬁnitions of utilities, optimal policies, and models for MDPs.
16.1.1 Utilities over time
In the MDP example in Figure 16.1, the performance of the agent was measured by a sum of
rewards for the transitions experienced. This choice of performance measure is not arbitrary,
but it is not the only possibility for the utility function2 on environment histories, which we
write as Uh([s0,a0,s1,a1 ...,sn]).
2
In this chapter we use U for the utility function (to be consistent with the rest of the book), but many works
about MDPs use V (for value) instead.
