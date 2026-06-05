---
chunk_id: "book-ca4fca8dd8-chunk-1393"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1393
confidence: "first-pass"
extraction_method: "structured-local"
---

846
Chapter 23
Reinforcement Learning
function PASSIVE-TD-LEARNER(percept) returns an action
inputs: percept, a percept indicating the current state s′ and reward signal r
persistent: π, a ﬁxed policy
s, the previous state, initially null
U, a table of utilities for states, initially empty
Ns, a table of frequencies for states, initially zero
if s′ is new then U[s′]←0
if s is not null then
increment Ns[s]
U[s]←U[s] + α(Ns[s]) × (r + γ U[s′] - U[s])
s←s′
return π[s′]
Figure 23.4 A passive reinforcement learning agent that learns utility estimates using tem-
poral differences. The step-size function α(n) is chosen to ensure convergence.
we apply the following update to Uπ(s):
Uπ(s) ←Uπ(s)+α[R(s,π(s),s′)+γUπ(s′)−Uπ(s)].
(23.3)
Here, α is the learning rate parameter. Because this update rule uses the difference in util-
ities between successive states (and thus successive times), it is often called the temporal-
difference (TD) equation. Just as in the weight update rules from Chapter 19 (e.g., Equa-
Temporal-diﬀerence
tion (19.6) on page 698), the TD term R(s,π(s),s′)+γUπ(s′)−Uπ(s) is effectively an error
signal, and the update is intended to reduce the error.
All temporal-difference methods work by adjusting the utility estimates toward the ideal
equilibrium that holds locally when the utility estimates are correct. In the case of passive
learning, the equilibrium is given by Equation (23.2). Now Equation (23.3) does in fact
cause the agent to reach the equilibrium given by Equation (23.2), but there is some subtlety
involved. First, notice that the update involves only the observed successor s′, whereas the
actual equilibrium conditions involve all possible next states. One might think that this causes
an improperly large change in Uπ(s) when a very rare transition occurs; but, in fact, because
rare transitions occur only rarely, the average value of Uπ(s) will converge to the correct
quantity in the limit, even if the value itself continues to ﬂuctuate.
Furthermore, if we turn the parameter α into a function that decreases as the number
of times a state has been visited increases, as shown in Figure 23.4, then Uπ(s) itself will
converge to the correct value.3 Figure 23.5 illustrates the performance of the passive TD
agent on the 4×3 world. It does not learn quite as fast as the ADP agent and shows much
higher variability, but it is much simpler and requires much less computation per observation.
Notice that TD does not need a transition model to perform its updates. The environment
▶
itself supplies the connection between neighboring states in the form of observed transitions.
The ADP and TD approaches are closely related. Both try to make local adjustments to
the utility estimates in order to make each state “agree” with its successors. One difference is
3
The technical conditions are given on page 702. In Figure 23.5 we have used α(n)=60/(59 + n), which
satisﬁes the conditions.
