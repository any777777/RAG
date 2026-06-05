---
chunk_id: "book-ca4fca8dd8-chunk-0375"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 375
confidence: "first-pass"
extraction_method: "structured-local"
---

230
Chapter 7
Logical Agents
A
B
G
P
S
W
 = Agent
 = Breeze
 = Glitter, Gold
 = Pit
 = Stench
 = Wumpus
OK = Safe square
V
 = Visited
A
OK
 1,1
 2,1
 3,1
 4,1
 1,2
 2,2
 3,2
 4,2
 1,3
 2,3
 3,3
 4,3
 1,4
 2,4
 3,4
 4,4
OK
OK
B
P?
P?
A
OK
OK
OK
 1,1
 2,1
 3,1
 4,1
 1,2
 2,2
 3,2
 4,2
 1,3
 2,3
 3,3
 4,3
 1,4
 2,4
 3,4
 4,4
V
(a)
(b)
Figure 7.3 The ﬁrst step taken by the agent in the wumpus world. (a) The initial situa-
tion, after percept [None,None,None,None,None]. (b) After moving to [2,1] and perceiving
[None,Breeze,None,None,None].
We can characterize the wumpus environment along the various dimensions given in Chap-
ter 2. Clearly, it is deterministic, discrete, static, and single-agent. (The wumpus doesn’t
move, fortunately.) It is sequential, because rewards may come only after many actions are
taken. It is partially observable, because some aspects of the state are not directly perceivable:
the agent’s location, the wumpus’s state of health, and the availability of an arrow. As for the
locations of the pits and the wumpus: we could treat them as unobserved parts of the state—
in which case, the transition model for the environment is completely known, and ﬁnding the
locations of pits completes the agent’s knowledge of the state. Alternatively, we could say
that the transition model itself is unknown because the agent doesn’t know which Forward
actions are fatal—in which case, discovering the locations of pits and wumpus completes the
agent’s knowledge of the transition model.
For an agent in the environment, the main challenge is its initial ignorance of the conﬁg-
uration of the environment; overcoming this ignorance seems to require logical reasoning. In
most instances of the wumpus world, it is possible for the agent to retrieve the gold safely.
Occasionally, the agent must choose between going home empty-handed and risking death to
ﬁnd the gold. About 21% of the environments are utterly unfair, because the gold is in a pit
or surrounded by pits.
Let us watch a knowledge-based wumpus agent exploring the environment shown in
Figure 7.2. We use an informal knowledge representation language consisting of writing
down symbols in a grid (as in Figures 7.3 and 7.4).
The agent’s initial knowledge base contains the rules of the environment, as described
previously; in particular, it knows that it is in [1,1] and that [1,1] is a safe square; we denote
that with an “A” and “OK,” respectively, in square [1,1].
The ﬁrst percept is [None,None,None,None,None], from which the agent can conclude
that its neighboring squares, [1,2] and [2,1], are free of dangers—they are OK. Figure 7.3(a)
shows the agent’s state of knowledge at this point.
