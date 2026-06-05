---
chunk_id: "book-ca4fca8dd8-chunk-0090"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 90
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 2
INTELLIGENT AGENTS
In which we discuss the nature of agents, perfect or otherwise, the diversity of environments,
and the resulting menagerie of agent types.
Chapter 1 identiﬁed the concept of rational agents as central to our approach to artiﬁcial
intelligence. In this chapter, we make this notion more concrete. We will see that the concept
of rationality can be applied to a wide variety of agents operating in any imaginable environ-
ment. Our plan in this book is to use this concept to develop a small set of design principles
for building successful agents—systems that can reasonably be called intelligent.
We begin by examining agents, environments, and the coupling between them. The ob-
servation that some agents behave better than others leads naturally to the idea of a rational
agent—one that behaves as well as possible. How well an agent can behave depends on the
nature of the environment; some environments are more difﬁcult than others. We give a crude
categorization of environments and show how properties of an environment inﬂuence the de-
sign of suitable agents for that environment. We describe a number of basic “skeleton” agent
designs, which we ﬂesh out in the rest of the book.
2.1 Agents and Environments
An agent is anything that can be viewed as perceiving its environment through sensors and
Environment
Sensor
acting upon that environment through actuators. This simple idea is illustrated in Figure 2.1.
Actuator
A human agent has eyes, ears, and other organs for sensors and hands, legs, vocal tract,
and so on for actuators. A robotic agent might have cameras and infrared range ﬁnders for
sensors and various motors for actuators. A software agent receives ﬁle contents, network
packets, and human input (keyboard/mouse/touchscreen/voice) as sensory inputs and acts on
the environment by writing ﬁles, sending network packets, and displaying information or
generating sounds. The environment could be everything—the entire universe! In practice it
is just that part of the universe whose state we care about when designing this agent—the part
that affects what the agent perceives and that is affected by the agent’s actions.
We use the term percept to refer to the content an agent’s sensors are perceiving. An
Percept
agent’s percept sequence is the complete history of everything the agent has ever perceived.
Percept sequence
In general, an agent’s choice of action at any given instant can depend on its built-in knowl-
▶
edge and on the entire percept sequence observed to date, but not on anything it hasn’t per-
ceived. By specifying the agent’s choice of action for every possible percept sequence, we
have said more or less everything there is to say about the agent. Mathematically speak-
ing, we say that an agent’s behavior is described by the agent function that maps any given
Agent function
percept sequence to an action.
