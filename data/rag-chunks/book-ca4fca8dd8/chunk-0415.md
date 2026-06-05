---
chunk_id: "book-ca4fca8dd8-chunk-0415"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 415
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 7.7
Agents Based on Propositional Logic
255
 0
 0.2
 0.4
 0.6
 0.8
 1
 0
 1
 2
 3
 4
 5
 6
 7
 8
P(satisfiable)
Clause/symbol ratio m/n
 0
 200
 400
 600
 800
 1000
 1200
 1400
 1600
 1800
 2000
 0
 1
 2
 3
 4
 5
 6
 7
 8
Runtime
Clause/symbol ratio m/n
DPLL
WalkSAT
(a)
(b)
Figure 7.19 (a) Graph showing the probability that a random 3-CNF sentence with n=50
symbols is satisﬁable, as a function of the clause/symbol ratio m/n. (b) Graph of the median
run time (measured in number of iterations) for both DPLL and WALKSAT on random 3-
CNF sentences. The most difﬁcult problems have a clause/symbol ratio of about 4.3.
of thresholding effect is certainly common, for satisﬁability problems as well as other types
of NP-hard problems.
Now that we have a good idea where the satisﬁable and unsatisﬁable problems are, the
next question is, where are the hard problems? It turns out that they are also often at the
threshold value. Figure 7.19(b) shows that 50-symbol problems at the threshold value of 4.3
are about 20 times more difﬁcult to solve than those at a ratio of 3.3. The underconstrained
problems are easiest to solve (because it is so easy to guess a solution); the overconstrained
problems are not as easy as the underconstrained, but still are much easier than the ones right
at the threshold.
7.7 Agents Based on Propositional Logic
In this section, we bring together what we have learned so far in order to construct wumpus
world agents that use propositional logic. The ﬁrst step is to enable the agent to deduce, to the
extent possible, the state of the world given its percept history. This requires writing down a
complete logical model of the effects of actions. We then show how logical inference can be
used by an agent in the wumpus world. We also show how the agent can keep track of the
world efﬁciently without going back into the percept history for each inference. Finally, we
show how the agent can use logical inference to construct plans that are guaranteed to achieve
its goals, provided its knowledge base is true in the actual world.
7.7.1 The current state of the world
As stated at the beginning of the chapter, a logical agent operates by deducing what to do
from a knowledge base of sentences about the world. The knowledge base is composed of
axioms—general knowledge about how the world works—and percept sentences obtained
from the agent’s experience in a particular world. In this section, we focus on the problem of
deducing the current state of the wumpus world—where am I, is that square safe, and so on.
