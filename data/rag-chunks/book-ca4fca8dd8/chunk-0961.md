---
chunk_id: "book-ca4fca8dd8-chunk-0961"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 961
confidence: "first-pass"
extraction_method: "structured-local"
---

582
Chapter 16
Making Complex Decisions
represents the belief state, deﬁned by b(B), the probability of being in state B. Now let us con-
sider the one-step plans [Stay] and [Go], each of which receives the reward for one transition
as follows:
α[Stay](A) = 0.9R(A,Stay,A)+0.1R(A,Stay,B) = 0.1
α[Stay](B) = 0.1R(B,Stay,A)+0.9R(B,Stay,B) = 0.9
α[Go](A) = 0.1R(A,Go,A)+0.9R(A,Go,B) = 0.9
α[Go](B) = 0.9R(B,Go,A)+0.1R(B,Go,B) = 0.1
The hyperplanes (lines, in this case) for b·α[Stay] and b·α[Go] are shown in Figure 16.15(a) and
their maximum is shown in bold. The bold line therefore represents the utility function for
the ﬁnite-horizon problem that allows just one action, and in each “piece” of the piecewise
linear utility function an optimal action is the ﬁrst action of the corresponding conditional
plan. In this case, the optimal one-step policy is to Stay when b(B) > 0.5 and Go otherwise.
Once we have utilities αp(s) for all the conditional plans p of depth 1 in each physical
state s, we can compute the utilities for conditional plans of depth 2 by considering each
possible ﬁrst action, each possible subsequent percept, and then each way of choosing a
depth-1 plan to execute for each percept:
[Stay; if Percept=A then Stay else Stay]
[Stay; if Percept=A then Stay else Go]
[Go; if Percept=A then Stay else Stay]
...
There are eight distinct depth-2 plans in all, and their utilities are shown in Figure 16.15(b).
Notice that four of the plans, shown as dashed lines, are suboptimal across the entire belief
space—we say these plans are dominated, and they need not be considered further. There
Dominated plan
are four undominated plans, each of which is optimal in a speciﬁc region, as shown in Fig-
ure 16.15(c). The regions partition the belief-state space.
We repeat the process for depth 3, and so on. In general, let p be a depth-d conditional
plan whose initial action is a and whose depth-(d −1) subplan for percept e is p.e; then
αp(s) = ∑
s′
P(s′ |s,a)[R(s,a,s′)+γ ∑
e
P(e|s′)αp.e(s′)].
(16.18)
This recursion naturally gives us a value iteration algorithm, which is given in Figure 16.16.
The structure of the algorithm and its error analysis are similar to those of the basic value
iteration algorithm in Figure 16.6 on page 563; the main difference is that instead of comput-
ing one utility number for each state, POMDP-VALUE-ITERATION maintains a collection of
undominated plans with their utility hyperplanes.
The algorithm’s complexity depends primarily on how many plans get generated. Given
|A| actions and |E| possible observations, there are |A|O(|E|d−1) distinct depth-d plans. Even for
the lowly two-state world with d =8, that’s 2255 plans. The elimination of dominated plans
is essential for reducing this doubly exponential growth: the number of undominated plans
with d =8 is just 144. The utility function for these 144 plans is shown in Figure 16.15(d).
Notice that the intermediate belief states have lower value than state A and state B, be-
cause in the intermediate states the agent lacks the information needed to choose a good
action. This is why information has value in the sense deﬁned in Section 15.6 and optimal
policies in POMDPs often include information-gathering actions.
