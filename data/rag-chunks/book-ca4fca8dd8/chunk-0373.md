---
chunk_id: "book-ca4fca8dd8-chunk-0373"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 373
confidence: "first-pass"
extraction_method: "structured-local"
---

228
Chapter 7
Logical Agents
serting that the agent perceived the given percept at the given time. MAKE-ACTION-QUERY
constructs a sentence that asks what action should be done at the current time. Finally,
MAKE-ACTION-SENTENCE constructs a sentence asserting that the chosen action was ex-
ecuted. The details of the inference mechanisms are hidden inside TELL and ASK. Later
sections will reveal these details.
The agent in Figure 7.1 appears quite similar to the agents with internal state described
in Chapter 2. Because of the deﬁnitions of TELL and ASK, however, the knowledge-based
agent is not an arbitrary program for calculating actions. It is amenable to a description at the
knowledge level, where we need specify only what the agent knows and what its goals are,
Knowledge level
in order to determine its behavior.
For example, an automated taxi might have the goal of taking a passenger from San
Francisco to Marin County and might know that the Golden Gate Bridge is the only link
between the two locations. Then we can expect it to cross the Golden Gate Bridge because it
knows that that will achieve its goal. Notice that this analysis is independent of how the taxi
works at the implementation level. It doesn’t matter whether its geographical knowledge is
Implementation level
implemented as linked lists or pixel maps, or whether it reasons by manipulating strings of
symbols stored in registers or by propagating noisy signals in a network of neurons.
A knowledge-based agent can be built simply by TELLing it what it needs to know. Start-
ing with an empty knowledge base, the agent designer can TELL sentences one by one until
the agent knows how to operate in its environment. This is called the declarative approach
Declarative
to system building. In contrast, the procedural approach encodes desired behaviors directly
Procedural
as program code. In the 1970s and 1980s, advocates of the two approaches engaged in heated
debates. We now understand that a successful agent often combines both declarative and
procedural elements in its design, and that declarative knowledge can often be compiled into
more efﬁcient procedural code.
We can also provide a knowledge-based agent with mechanisms that allow it to learn for
itself. These mechanisms, which are discussed in Chapter 19, create general knowledge about
the environment from a series of percepts. A learning agent can be fully autonomous.
7.2 The Wumpus World
In this section we describe an environment in which knowledge-based agents can show their
worth. The wumpus world is a cave consisting of rooms connected by passageways. Lurking
Wumpus world
somewhere in the cave is the terrible wumpus, a beast that eats anyone who enters its room.
The wumpus can be shot by an agent, but the agent has only one arrow. Some rooms contain
bottomless pits that will trap anyone who wanders into these rooms (except for the wumpus,
which is too big to fall in). The only redeeming feature of this bleak environment is the
possibility of ﬁnding a heap of gold. Although the wumpus world is rather tame by modern
computer game standards, it illustrates some important points about intelligence.
A sample wumpus world is shown in Figure 7.2. The precise deﬁnition of the task envi-
ronment is given, as suggested in Section 2.3, by the PEAS description:
• Performance measure: +1000 for climbing out of the cave with the gold, –1000 for
falling into a pit or being eaten by the wumpus, –1 for each action taken, and –10 for
using up the arrow. The game ends either when the agent dies or when the agent climbs
out of the cave.
