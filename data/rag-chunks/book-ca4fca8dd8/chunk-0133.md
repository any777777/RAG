---
chunk_id: "book-ca4fca8dd8-chunk-0133"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 133
confidence: "first-pass"
extraction_method: "structured-local"
---

78
Chapter 2
Intelligent Agents
if the representation of a concept is spread over many memory locations, and each memory
location is employed as part of the representation of multiple different concepts, we call
that a distributed representation. Distributed representations are more robust against noise
Distributed
representation
and information loss. With a localist representation, the mapping from concept to memory
location is arbitrary, and if a transmission error garbles a few bits, we might confuse Truck
with the unrelated concept Truce. But with a distributed representation, you can think of each
concept representing a point in multidimensional space, and if you garble a few bits you move
to a nearby point in that space, which will have similar meaning.
Summary
This chapter has been something of a whirlwind tour of AI, which we have conceived of as
the science of agent design. The major points to recall are as follows:
• An agent is something that perceives and acts in an environment. The agent function
for an agent speciﬁes the action taken by the agent in response to any percept sequence.
• The performance measure evaluates the behavior of the agent in an environment. A
rational agent acts so as to maximize the expected value of the performance measure,
given the percept sequence it has seen so far.
• A task environment speciﬁcation includes the performance measure, the external en-
vironment, the actuators, and the sensors. In designing an agent, the ﬁrst step must
always be to specify the task environment as fully as possible.
• Task environments vary along several signiﬁcant dimensions. They can be fully or par-
tially observable, single-agent or multiagent, deterministic or nondeterministic, episodic
or sequential, static or dynamic, discrete or continuous, and known or unknown.
• In cases where the performance measure is unknown or hard to specify correctly, there
is a signiﬁcant risk of the agent optimizing the wrong objective. In such cases the agent
design should reﬂect uncertainty about the true objective.
• The agent program implements the agent function. There exists a variety of basic
agent program designs reﬂecting the kind of information made explicit and used in the
decision process. The designs vary in efﬁciency, compactness, and ﬂexibility. The
appropriate design of the agent program depends on the nature of the environment.
• Simple reﬂex agents respond directly to percepts, whereas model-based reﬂex agents
maintain internal state to track aspects of the world that are not evident in the current
percept. Goal-based agents act to achieve their goals, and utility-based agents try to
maximize their own expected “happiness.”
• All agents can improve their performance through learning.
Bibliographical and Historical Notes
The central role of action in intelligence—the notion of practical reasoning—goes back at
least as far as Aristotle’s Nicomachean Ethics. Practical reasoning was also the subject of
McCarthy’s inﬂuential paper “Programs with Common Sense” (1958). The ﬁelds of robotics
and control theory are, by their very nature, concerned principally with physical agents. The
