---
chunk_id: "book-ca4fca8dd8-chunk-0377"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 377
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 7.2
The Wumpus World
231
B
P!
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
OK
W!
V
P!
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
S
OK
W!
V
V
V
B
S G
P?
P?
(b)
(a)
S
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
B
Figure 7.4 Two later stages in the progress of the agent. (a) After moving to [1,1] and then
[1,2], and perceiving [Stench,None,None,None,None]. (b) After moving to [2,2] and then
[2,3], and perceiving [Stench,Breeze,Glitter,None,None].
A cautious agent will move only into a square that it knows to be OK. Let us suppose
the agent decides to move forward to [2,1]. The agent perceives a breeze (denoted by “B”) in
[2,1], so there must be a pit in a neighboring square. The pit cannot be in [1,1], by the rules of
the game, so there must be a pit in [2,2] or [3,1] or both. The notation “P?” in Figure 7.3(b)
indicates a possible pit in those squares. At this point, there is only one known square that is
OK and that has not yet been visited. So the prudent agent will turn around, go back to [1,1],
and then proceed to [1,2].
The agent perceives a stench in [1,2], resulting in the state of knowledge shown in Fig-
ure 7.4(a). The stench in [1,2] means that there must be a wumpus nearby. But the wumpus
cannot be in [1,1], by the rules of the game, and it cannot be in [2,2] (or the agent would
have detected a stench when it was in [2,1]). Therefore, the agent can infer that the wumpus
is in [1,3]. The notation W! indicates this inference. Moreover, the lack of a breeze in [1,2]
implies that there is no pit in [2,2]. Yet the agent has already inferred that there must be a pit
in either [2,2] or [3,1], so this means it must be in [3,1]. This is a fairly difﬁcult inference,
because it combines knowledge gained at different times in different places and relies on the
lack of a percept to make one crucial step.
The agent has now proved to itself that there is neither a pit nor a wumpus in [2,2], so it
is OK to move there. We do not show the agent’s state of knowledge at [2,2]; we just assume
that the agent turns and moves to [2,3], giving us Figure 7.4(b). In [2,3], the agent detects a
glitter, so it should grab the gold and then return home.
Note that in each case for which the agent draws a conclusion from the available infor-
mation, that conclusion is guaranteed to be correct if the available information is correct.
This is a fundamental property of logical reasoning. In the rest of this chapter, we describe
how to build logical agents that can represent information and draw conclusions such as those
described in the preceding paragraphs.
