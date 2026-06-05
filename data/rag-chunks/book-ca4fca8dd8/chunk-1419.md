---
chunk_id: "book-ca4fca8dd8-chunk-1419"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1419
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 23.4
Generalization in Reinforcement Learning
859
teammates one could pass to, and so on, so each higher-level action may have many different
lower-level implementations.
To illustrate these ideas, we’ll use a simpliﬁed soccer game called keepaway, in which
Keepaway
one team of three players tries to keep possession of the ball for as long as possible by drib-
bling and passing amongst themselves while the other team of two players tries to take pos-
session by intercepting a pass or tackling a player in possession.5 The game is implemented
within the RoboCup 2D simulator, which provides detailed continuous-state motion models
with 100ms time steps and has proved to be a good testbed for RL systems.
A hierarchical reinforcement learning agent begins with a partial program that outlines
Partial program
a hierarchical structure for the agent’s behavior. The partial-programming language for agent
programs extends any ordinary programming language by adding primitives for unspeciﬁed
choices that must be ﬁlled in by learning. (Here, we use pseudocode for the programming
language.) The partial program can be arbitrarily complicated, as long as it terminates.
It is easy to see that HRL includes ordinary RL as a special case. We simply provide the
trivial partial program that allows the agent to keep choosing any action from A(s), the set of
actions that can be executed in the current state s:
while true do
choose(A(s)).
The choose operator allows the agent to choose any element of the speciﬁed set. The learning
process converts the partial agent program into a complete program by learning how each
choice should be made. For example, the learning process might associate a Q-function with
each choice; once the Q-functions are learned, the program produces behavior by choosing
the option with the highest Q-value each time it encounters a choice.
The agent programs for keepaway are more interesting. We’ll look at the partial program
for a single player on the “keeper” team. The choice of what to do at the top level depends
mainly on whether the player has the ball or not:
while not IS-TERMINAL(s) do
if BALL-IN-MY-POSSESSION(s) then choose({PASS, HOLD, DRIBBLE})
else choose({STAY, MOVE, INTERCEPT-BALL}).
Each of these choices invokes a subroutine that may itself make further choices, all the way
down to primitive actions that can be executed directly. For example, the high-level action
PASS chooses a teammate to pass to, but also has the choice to do nothing and return control
to the higher level if appropriate (e.g., if there is no one to pass to):
choose({PASS-TO(choose(TEAMMATES(s))),return}).
The PASS-TO routine then has to choose a speed and direction for the pass. While it is
relatively easy for a human—even one with little expertise in soccer—to provide this kind of
high-level advice to the learning agent, it would be difﬁcult, if not impossible, to write down
the rules for determining the speed and direction of the kick to maximize the probability of
maintaining possession. Similarly, it is far from obvious how to choose the right teammate to
receive the ball or where to move in order to make oneself available to receive the ball. The
partial program provides general know-how—overall scaffolding and structural organization
for complex behaviors—and the learning process works out all the details.
5
Rumors that keepaway was inspired by the real-world tactics of Barcelona FC are probably unfounded.
