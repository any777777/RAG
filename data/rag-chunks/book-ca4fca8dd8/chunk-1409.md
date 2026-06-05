---
chunk_id: "book-ca4fca8dd8-chunk-1409"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1409
confidence: "first-pass"
extraction_method: "structured-local"
---

854
Chapter 23
Reinforcement Learning
function Q-LEARNING-AGENT(percept) returns an action
inputs: percept, a percept indicating the current state s′ and reward signal r
persistent: Q, a table of action values indexed by state and action, initially zero
Nsa, a table of frequencies for state–action pairs, initially zero
s, a, the previous state and action, initially null
if s is not null then
increment Nsa[s,a]
Q[s,a]←Q[s,a] + α(Nsa[s,a])(r + γ maxa′ Q[s′,a′] −Q[s,a])
s,a←s′,argmaxa′ f(Q[s′,a′],Nsa[s′,a′])
return a
Figure 23.8 An exploratory Q-learning agent. It is an active learner that learns the value
Q(s,a) of each action in each situation. It uses the same exploration function f as the ex-
ploratory ADP agent, but avoids having to learn the transition model.
policy?” Q-learning is more ﬂexible than SARSA, in the sense that a Q-learning agent can
learn how to behave well when under the control of a wide variety of exploration policies. On
the other hand, SARSA is appropriate if the overall policy is even partly controlled by other
agents or programs, in which case it is better to learn a Q-function for what will actually
happen rather than what would happen if the agent got to pick estimated best actions. Both
Q-learning and SARSA learn the optimal policy for the 4×3 world, but they do so at a much
slower rate than the ADP agent. This is because the local updates do not enforce consistency
among all the Q-values via the model.
23.4 Generalization in Reinforcement Learning
So far, we have assumed that utility functions and Q-functions are represented in tabular form
with one output value for each state. This works for state spaces with up to about 106 states,
which is more than enough for our toy two-dimensional grid environments. But in real-world
environments with many more states, convergence will be too slow. Backgammon is simpler
than most real-world applications, yet it has about 1020 states. We cannot easily visit them all
in order to learn how to play the game.
Chapter 6 introduced the idea of an evaluation function as a compact measure of de-
sirability for potentially vast state spaces. In the terminology of this chapter, the evaluation
function is an approximate utility function; we use the term function approximation for the
Function
approximation
process of constructing a compact approximation of the true utility function or Q-function.
For example, we might approximate the utility function using a weighted linear combination
of features f1,..., fn:
ˆUθ(s) = θ1 f1(s)+θ2 f2(s)+···+θn fn(s).
Instead of learning 1020 state values in a table, a reinforcement learning algorithm can learn,
say, 20 values for the parameters θ=θ1,...,θ20 that make ˆUθ a good approximation to the true
utility function. Sometimes this approximate utility function is combined with look-ahead
search to produce more accurate decisions. Adding look-ahead search means that effective
