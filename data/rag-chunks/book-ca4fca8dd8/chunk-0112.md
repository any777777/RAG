---
chunk_id: "book-ca4fca8dd8-chunk-0112"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 112
confidence: "first-pass"
extraction_method: "structured-local"
---

66
Chapter 2
Intelligent Agents
function TABLE-DRIVEN-AGENT(percept) returns an action
persistent: percepts, a sequence, initially empty
table, a table of actions, indexed by percept sequences, initially fully speciﬁed
append percept to the end of percepts
action←LOOKUP(percepts,table)
return action
Figure 2.7 The TABLE-DRIVEN-AGENT program is invoked for each new percept and re-
turns an action each time. It retains the complete percept sequence in memory.
2.4.1 Agent programs
The agent programs that we design in this book all have the same skeleton: they take the
current percept as input from the sensors and return an action to the actuators.5 Notice the
difference between the agent program, which takes the current percept as input, and the agent
function, which may depend on the entire percept history. The agent program has no choice
but to take just the current percept as input because nothing more is available from the envi-
ronment; if the agent’s actions need to depend on the entire percept sequence, the agent will
have to remember the percepts.
We describe the agent programs in the simple pseudocode language that is deﬁned in
Appendix B. (The online code repository contains implementations in real programming
languages.) For example, Figure 2.7 shows a rather trivial agent program that keeps track of
the percept sequence and then uses it to index into a table of actions to decide what to do.
The table—an example of which is given for the vacuum world in Figure 2.3—represents
explicitly the agent function that the agent program embodies. To build a rational agent in
this way, we as designers must construct a table that contains the appropriate action for every
possible percept sequence.
It is instructive to consider why the table-driven approach to agent construction is doomed
to failure. Let P be the set of possible percepts and let T be the lifetime of the agent (the total
number of percepts it will receive). The lookup table will contain ∑T
t =1 |P|t entries. Consider
the automated taxi: the visual input from a single camera (eight cameras is typical) comes
in at the rate of roughly 70 megabytes per second (30 frames per second, 1080×720 pixels
with 24 bits of color information). This gives a lookup table with over 10600,000,000,000 entries
for an hour’s driving. Even the lookup table for chess—a tiny, well-behaved fragment of the
real world—has (it turns out) at least 10150 entries. In comparison, the number of atoms in
the observable universe is less than 1080. The daunting size of these tables means that (a) no
physical agent in this universe will have the space to store the table; (b) the designer would
not have time to create the table; and (c) no agent could ever learn all the right table entries
from its experience.
Despite all this, TABLE-DRIVEN-AGENT does do what we want, assuming the table is
ﬁlled in correctly: it implements the desired agent function.
▶
5
There are other choices for the agent program skeleton; for example, we could have the agent programs be
coroutines that run asynchronously with the environment. Each such coroutine has an input and output port and
consists of a loop that reads the input port for percepts and writes actions to the output port.
