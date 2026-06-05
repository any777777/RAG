---
chunk_id: "book-ca4fca8dd8-chunk-0114"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 114
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 2.4
The Structure of Agents
67
function REFLEX-VACUUM-AGENT([location,status]) returns an action
if status = Dirty then return Suck
else if location = A then return Right
else if location = B then return Left
Figure 2.8 The agent program for a simple reﬂex agent in the two-location vacuum environ-
ment. This program implements the agent function tabulated in Figure 2.3.
The key challenge for AI is to ﬁnd out how to write programs that, to the extent possible,
produce rational behavior from a smallish program rather than from a vast table.
We have many examples showing that this can be done successfully in other areas: for
example, the huge tables of square roots used by engineers and schoolchildren prior to the
1970s have now been replaced by a ﬁve-line program for Newton’s method running on elec-
tronic calculators. The question is, can AI do for general intelligent behavior what Newton
did for square roots? We believe the answer is yes.
In the remainder of this section, we outline four basic kinds of agent programs that em-
body the principles underlying almost all intelligent systems:
• Simple reﬂex agents;
• Model-based reﬂex agents;
• Goal-based agents; and
• Utility-based agents.
Each kind of agent program combines particular components in particular ways to generate
actions. Section 2.4.6 explains in general terms how to convert all these agents into learning
agents that can improve the performance of their components so as to generate better actions.
Finally, Section 2.4.7 describes the variety of ways in which the components themselves can
be represented within the agent. This variety provides a major organizing principle for the
ﬁeld and for the book itself.
2.4.2 Simple reﬂex agents
The simplest kind of agent is the simple reﬂex agent. These agents select actions on the basis
Simple reﬂex agent
of the current percept, ignoring the rest of the percept history. For example, the vacuum agent
whose agent function is tabulated in Figure 2.3 is a simple reﬂex agent, because its decision
is based only on the current location and on whether that location contains dirt. An agent
program for this agent is shown in Figure 2.8.
Notice that the vacuum agent program is very small indeed compared to the correspond-
ing table. The most obvious reduction comes from ignoring the percept history, which cuts
down the number of relevant percept sequences from 4T to just 4. A further, small reduc-
tion comes from the fact that when the current square is dirty, the action does not depend on
the location. Although we have written the agent program using if-then-else statements, it is
simple enough that it can also be implemented as a Boolean circuit.
Simple reﬂex behaviors occur even in more complex environments. Imagine yourself as
the driver of the automated taxi. If the car in front brakes and its brake lights come on, then
you should notice this and initiate braking. In other words, some processing is done on the
