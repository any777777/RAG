---
chunk_id: "book-ca4fca8dd8-chunk-0936"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 936
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 16.2
Algorithms for MDPs
567
function POLICY-ITERATION(mdp) returns a policy
inputs: mdp, an MDP with states S, actions A(s), transition model P(s′ |s,a)
local variables: U, a vector of utilities for states in S, initially zero
π, a policy vector indexed by state, initially random
repeat
U ←POLICY-EVALUATION(π,U,mdp)
unchanged?←true
for each state s in S do
a∗←argmax
a∈A(s)
Q-VALUE(mdp,s,a,U)
if Q-VALUE(mdp,s,a∗,U) > Q-VALUE(mdp,s,π[s],U) then
π[s]←a∗; unchanged?←false
until unchanged?
return π
Figure 16.9 The policy iteration algorithm for calculating an optimal policy.
better policy, policy iteration must terminate. The algorithm is shown in Figure 16.9. As with
value iteration, we use the Q-VALUE function deﬁned on page 559.
How do we implement POLICY-EVALUATION? It turns out that doing so is simpler than
solving the standard Bellman equations (which is what value iteration does), because the
action in each state is ﬁxed by the policy. At the ith iteration, the policy πi speciﬁes the action
πi(s) in state s. This means that we have a simpliﬁed version of the Bellman equation (16.5)
relating the utility of s (under πi) to the utilities of its neighbors:
Ui(s) = ∑
s′
P(s′ |s,πi(s))[R(s,πi(s),s′)+γUi(s′)].
(16.14)
For example, suppose πi is the policy shown in Figure 16.2(a). Then we have πi(1,1)=Up,
πi(1,2)=Up, and so on, and the simpliﬁed Bellman equations are
Ui(1,1) = 0.8[−0.04+Ui(1,2)]+0.1[−0.04+Ui(2,1)+0.1[−0.04+Ui(1,1)]],
Ui(1,2) = 0.8[−0.04+Ui(1,3)]+0.2[−0.04+Ui(1,2)],
and so on for all the states. The important point is that these equations are linear, because
the “max” operator has been removed. For n states, we have n linear equations with n un-
knowns, which can be solved exactly in time O(n3) by standard linear algebra methods. If the
transition model is sparse—that is, if each state transitions only to a small number of other
states—then the solution process can be faster still.
For small state spaces, policy evaluation using exact solution methods is often the most
efﬁcient approach. For large state spaces, O(n3) time might be prohibitive. Fortunately, it
is not necessary to do exact policy evaluation. Instead, we can perform some number of
simpliﬁed value iteration steps (simpliﬁed because the policy is ﬁxed) to give a reasonably
good approximation of the utilities. The simpliﬁed Bellman update for this process is
Ui+1(s) ←∑
s′
P(s′ |s,πi(s))[R(s,πi(s),s′)+γUi(s′)],

## Page 568
