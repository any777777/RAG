---
chunk_id: "book-ca4fca8dd8-chunk-0092"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 92
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 2.1
Agents and Environments
55
Agent
Sensors
Actuators
Environment
Percepts
Actions
?
Figure 2.1 Agents interact with environments through sensors and actuators.
We can imagine tabulating the agent function that describes any given agent; for most
agents, this would be a very large table—inﬁnite, in fact, unless we place a bound on the
length of percept sequences we want to consider. Given an agent to experiment with, we can,
in principle, construct this table by trying out all possible percept sequences and recording
which actions the agent does in response.1 The table is, of course, an external characterization
of the agent. Internally, the agent function for an artiﬁcial agent will be implemented by an
agent program. It is important to keep these two ideas distinct. The agent function is an
Agent program
abstract mathematical description; the agent program is a concrete implementation, running
within some physical system.
To illustrate these ideas, we use a simple example—the vacuum-cleaner world, which
consists of a robotic vacuum-cleaning agent in a world consisting of squares that can be
either dirty or clean. Figure 2.2 shows a conﬁguration with just two squares, A and B. The
vacuum agent perceives which square it is in and whether there is dirt in the square. The
agent starts in square A. The available actions are to move to the right, move to the left, suck
up the dirt, or do nothing.2 One very simple agent function is the following: if the current
square is dirty, then suck; otherwise, move to the other square. A partial tabulation of this
agent function is shown in Figure 2.3 and an agent program that implements it appears in
Figure 2.8 on page 67.
Looking at Figure 2.3, we see that various vacuum-world agents can be deﬁned simply
by ﬁlling in the right-hand column in various ways. The obvious question, then, is this: What ◀
is the right way to ﬁll out the table? In other words, what makes an agent good or bad,
intelligent or stupid? We answer these questions in the next section.
1
If the agent uses some randomization to choose its actions, then we would have to try each sequence many
times to identify the probability of each action. One might imagine that acting randomly is rather silly, but we
show later in this chapter that it can be very intelligent.
2
In a real robot, it would be unlikely to have an actions like “move right” and “move left.” Instead the actions
would be “spin wheels forward” and “spin wheels backward.” We have chosen the actions to be easier to follow
on the page, not for ease of implementation in an actual robot.
