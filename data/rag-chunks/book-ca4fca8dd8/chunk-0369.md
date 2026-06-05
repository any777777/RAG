---
chunk_id: "book-ca4fca8dd8-chunk-0369"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 369
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 7
LOGICAL AGENTS
In which we design agents that can form representations of a complex world, use a process
of inference to derive new representations about the world, and use these new representa-
tions to deduce what to do.
Humans, it seems, know things; and what they know helps them do things. In AI, knowledge-
based agents use a process of reasoning over an internal representation of knowledge to
Knowledge-based
agents
Reasoning
Representation
decide what actions to take.
The problem-solving agents of Chapters 3 and 4 know things, but only in a very limited,
inﬂexible sense. They know what actions are available and what the result of performing a
speciﬁc action from a speciﬁc state will be, but they don’t know general facts. A route-ﬁnding
agent doesn’t know that it is impossible for a road to be a negative number of kilometers long.
An 8-puzzle agent doesn’t know that two tiles cannot occupy the same space. The knowledge
they have is very useful for ﬁnding a path from the start to a goal, but not for anything else.
The atomic representations used by problem-solving agents are also very limiting. In
a partially observable environment, for example, a problem-solving agent’s only choice for
representing what it knows about the current state is to list all possible concrete states. I could
give a human the goal of driving to a U.S. town with population less than 10,000, but to say
that to a problem-solving agent, I could formally describe the goal only as an explicit set of
the 16,000 or so towns that satisfy the description.
Chapter 5 introduced our ﬁrst factored representation, whereby states are represented as
assignments of values to variables; this is a step in the right direction, enabling some parts of
the agent to work in a domain-independent way and allowing for more efﬁcient algorithms.
In this chapter, we take this step to its logical conclusion, so to speak—we develop logic as a
general class of representations to support knowledge-based agents. These agents can com-
bine and recombine information to suit myriad purposes. This can be far removed from the
needs of the moment—as when a mathematician proves a theorem or an astronomer calcu-
lates the Earth’s life expectancy. Knowledge-based agents can accept new tasks in the form
of explicitly described goals; they can achieve competence quickly by being told or learning
new knowledge about the environment; and they can adapt to changes in the environment by
updating the relevant knowledge.
We begin in Section 7.1 with the overall agent design. Section 7.2 introduces a simple
new environment, the wumpus world, and illustrates the operation of a knowledge-based
agent without going into any technical detail. Then we explain the general principles of logic
in Section 7.3 and the speciﬁcs of propositional logic in Section 7.4. Propositional logic is
a factored representation; while less expressive than ﬁrst-order logic (Chapter 8), which is
the canonical structured representation, propositional logic illustrates all the basic concepts
