---
chunk_id: "book-ca4fca8dd8-chunk-1407"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1407
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 23.3
Active Reinforcement Learning
853
TD update rule remains unchanged. Once again, it can be shown that the TD algorithm will
converge to the same values as ADP, as the number of training sequences tends to inﬁnity.
The Q-learning method avoids the need for a model by learning an action-utility function
Q(s,a) instead of a utility function U(s). Q(s,a) denotes the expected total discounted reward
if the agent takes action a in s and acts optimally thereafter. Knowing the Q-function enables
the agent to act optimally simply by choosing argmaxa Q(s,a), with no need for look-ahead
based on a transition model.
We can also derive a model-free TD update for the Q-values. We begin with the Bellman
equation for Q(s,a), repeated here from Equation (16.8):
Q(s,a) = ∑
s′
P(s′ |s,a)[R(s,a,s′)+γ max
a′ Q(s′,a′)]
(23.6)
From this, we can write down the Q-learning TD update, by analogy to the TD update for
utilities in Equation (23.3):
Q(s,a) ←Q(s,a)+α[R(s,a,s′)+γ max
a′ Q(s′,a′)−Q(s,a)].
(23.7)
This update is calculated whenever action a is executed in state s leading to state s′. As in
Equation (23.3), the term R(s,a,s′) + γ maxa′ Q(s′,a′) −Q(s,a) represents an error that the
update is trying to minimize.
The important part of this equation is what it does not contain: a TD Q-learning agent ◀
does not need a transition model, P(s′ |s,a), either for learning or for action selection. As
noted at the beginning of the chapter, model-free methods can be applied even in very com-
plex domains because no model need be provided or learned. On the other hand, the Q-
learning agent has no means of looking into the future, so it may have difﬁculty when rewards
are sparse and long action sequences must be constructed to reach them.
The complete agent design for an exploratory TD Q-learning agent is shown in Fig-
ure 23.8. Notice that it uses exactly the same exploration function f as that used by the
exploratory ADP agent—hence the need to keep statistics on actions taken (the table N). If
a simpler exploration policy is used—say, acting randomly on some fraction of steps, where
the fraction decreases over time—then we can dispense with the statistics.
Q-learning has a close relative called SARSA (for state, action, reward, state, action).
SARSA
The update rule for SARSA is very similar to the Q-learning update rule (Equation (23.7)),
except that SARSA updates with the Q-value of the action a′ that is actually taken:
Q(s,a) ←Q(s,a)+α[R(s,a,s′)+γ Q(s′,a′)−Q(s,a)],
(23.8)
The rule is applied at the end of each s, a, r, s′, a′ quintuplet—hence the name. The differ-
ence from Q-learning is quite subtle: whereas Q-learning backs up the Q-value from the best
action in s′, SARSA waits until an action is taken and backs up the Q-value for that action.
If the agent is greedy and always takes the action with the best Q-value, the two algorithms
are identical. When exploration is happening, however, they differ: if the exploration yields
a negative reward, SARSA penalizes the action, while Q-learning does not.
Q-learning is an off-policy learning algorithm, because it learns Q-values that answer the
Oﬀ-policy
question “What would this action be worth in this state, assuming that I stop using whatever
policy I am using now, and start acting according to a policy that chooses the best action
(according to my estimates)?” SARSA is an on-policy algorithm: it learns Q-values that
On-policy
answer the question “What would this action be worth in this state, assuming I stick with my
