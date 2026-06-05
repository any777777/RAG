---
chunk_id: "book-ca4fca8dd8-chunk-0122"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 122
confidence: "first-pass"
extraction_method: "structured-local"
---

72
Chapter 2
Intelligent Agents
Agent
Environment
Sensors
What action I
should do now
State
How the world evolves
What my actions do
Actuators
What the world
is like now
What it will be like
  if I do action A
Goals
Figure 2.13 A model-based, goal-based agent. It keeps track of the world state as well as
a set of goals it is trying to achieve, and chooses an action that will (eventually) lead to the
achievement of its goals.
simply by specifying that destination as the goal. The reﬂex agent’s rules for when to turn
and when to go straight will work only for a single destination; they must all be replaced to
go somewhere new.
2.4.5 Utility-based agents
Goals alone are not enough to generate high-quality behavior in most environments. For
example, many action sequences will get the taxi to its destination (thereby achieving the
goal), but some are quicker, safer, more reliable, or cheaper than others. Goals just provide a
crude binary distinction between “happy” and “unhappy” states. A more general performance
measure should allow a comparison of different world states according to exactly how happy
they would make the agent. Because “happy” does not sound very scientiﬁc, economists and
computer scientists use the term utility instead.7
Utility
We have already seen that a performance measure assigns a score to any given sequence
of environment states, so it can easily distinguish between more and less desirable ways of
getting to the taxi’s destination. An agent’s utility function is essentially an internalization
Utility function
of the performance measure. Provided that the internal utility function and the external per-
formance measure are in agreement, an agent that chooses actions to maximize its utility will
be rational according to the external performance measure.
Let us emphasize again that this is not the only way to be rational—we have already seen
a rational agent program for the vacuum world (Figure 2.8) that has no idea what its utility
function is—but, like goal-based agents, a utility-based agent has many advantages in terms
of ﬂexibility and learning. Furthermore, in two kinds of cases, goals are inadequate but a
utility-based agent can still make rational decisions. First, when there are conﬂicting goals,
only some of which can be achieved (for example, speed and safety), the utility function
speciﬁes the appropriate tradeoff. Second, when there are several goals that the agent can
7
The word “utility” here refers to “the quality of being useful,” not to the electric company or waterworks.
