---
chunk_id: "book-ca4fca8dd8-chunk-0125"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 125
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 74

74
Chapter 2
Intelligent Agents
Performance standard
Agent
Environment
Sensors
Performance
element
changes
knowledge
learning
  goals
Problem
generator 
feedback
  Learning  
element
Critic
Actuators
Figure 2.15 A general learning agent. The “performance element” box represents what we
have previously considered to be the whole agent program. Now, the “learning element” box
gets to modify that program to improve its performance.
unachievable in practice because of computational complexity, as we noted in Chapter 1. We
also note that not all utility-based agents are model-based; we will see in Chapters 23 and 26
that a model-free agent can learn what action is best in a particular situation without ever
Model-free agent
learning exactly how that action changes the environment.
Finally, all of this assumes that the designer can specify the utility function correctly;
Chapters 16, 17, and 23 consider the issue of unknown utility functions in more depth.
2.4.6 Learning agents
We have described agent programs with various methods for selecting actions. We have
not, so far, explained how the agent programs come into being. In his famous early paper,
Turing (1950) considers the idea of actually programming his intelligent machines by hand.
He estimates how much work this might take and concludes, “Some more expeditious method
seems desirable.” The method he proposes is to build learning machines and then to teach
them. In many areas of AI, this is now the preferred method for creating state-of-the-art
systems. Any type of agent (model-based, goal-based, utility-based, etc.) can be built as a
learning agent (or not).
Learning has another advantage, as we noted earlier: it allows the agent to operate in
initially unknown environments and to become more competent than its initial knowledge
alone might allow. In this section, we brieﬂy introduce the main ideas of learning agents.
Throughout the book, we comment on opportunities and methods for learning in particu-
lar kinds of agents. Chapters 19, 21, 22, and 23 go into much more depth on the learning
algorithms themselves.
A learning agent can be divided into four conceptual components, as shown in Fig-
ure 2.15. The most important distinction is between the learning element, which is re-
Learning element
sponsible for making improvements, and the performance element, which is responsible for
Performance
element
selecting external actions. The performance element is what we have previously considered
