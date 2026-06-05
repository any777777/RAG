---
chunk_id: "book-ca4fca8dd8-chunk-1405"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1405
confidence: "first-pass"
extraction_method: "structured-local"
---

852
Chapter 23
Reinforcement Learning
because the agent must consider the effects of future observations on its beliefs about the
transition model. The problem becomes an exploration POMDP whose belief states are dis-
Exploration POMDP
tributions over models. In principle, this exploration POMDP can be formulated and solved
before the agent ever sets foot in the world. (Exercise 23.EPOM asks you to do this for
the Minesweeper game to ﬁnd the best ﬁrst move.) The result is a complete strategy that
tells the agent what to do next given any possible percept sequence. Solving the exploration
POMDP is usually wildly intractable, but the concept provides an analytical foundation for
understanding the exploration problem described in Section 23.3.
It is worth noting that being perfectly Bayesian will not protect the agent from an un-
timely death. Unless the prior gives some indication of percepts that suggest danger, there
is nothing to prevent the agent from taking an exploratory action that leads to an absorbing
state. For example, it used to be thought that human infants had an innate fear of heights and
would not crawl off a cliff, but this turns out not to be true (Adolph et al., 2014).
The second approach, derived from robust control theory, allows for a set of possible
Robust control
theory
models H without assigning probabilities to them, and deﬁnes an optimal robust policy as
one that gives the best outcome in the worst case over H:
π∗= argmax
π
min
h Uπ
h .
Often, the set H will be the set of models that exceed some likelihood threshold on P(h|e),
so the robust and Bayesian approaches are related.
The robust control approach can be considered as a game between the agent and an adver-
sary, where the adversary gets to pick the worst possible result for any action, and the policy
we get is the minimax solution for the game. Our logical wumpus agent (see Section 7.7) is a
robust control agent in this way: it considers all models that are logically possible, and does
not explore any locations that could possibly contain a pit or a wumpus, so it is ﬁnding the
action with maximum utility in the worst case over all possible hypotheses.
The problem with the worst-case assumption is that it results in overly conservative be-
havior. A self-driving car that assumes that every other driver will try to collide with it has no
choice but to stay in the garage. Real life is full of such risk–reward tradeoffs.
Although one reason for venturing into reinforcement learning was to escape the need for
a human teacher (as in supervised learning), it turns out that human knowledge can help keep
a system safe. One way is to record a series of actions by an experienced teacher, so that the
system will act reasonably from the start, and can learn to improve from there. A second way
is for a human to write down constraints on what a system can do, and have a program outside
of the reinforcement learning system enforce those constraints. For example, when training
an autonomous helicopter, a partial policy can be provided that takes over control when the
helicopter enters a state from which any further unsafe actions would lead to an irrecoverable
state—one in which the safety controller cannot guarantee that the absorbing state will be
avoided. In all other states, the learning agent is free to do as it pleases.
23.3.3 Temporal-diﬀerence Q-learning
Now that we have an active ADP agent, let us consider how to construct an active temporal-
difference (TD) learning agent. The most obvious change is that the agent will have to learn
a transition model so that it can choose an action based on U(s) via one-step look-ahead. The
model acquisition problem for the TD agent is identical to that for the ADP agent, and the
