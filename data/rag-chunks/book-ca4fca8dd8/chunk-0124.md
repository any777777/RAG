---
chunk_id: "book-ca4fca8dd8-chunk-0124"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 124
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 2.4
The Structure of Agents
73
Agent
Environment
Sensors
How happy I will be
in such a state
State
How the world evolves
What my actions do
Utility
Actuators
What action I
should do now
What it will be like
if I do action A
What the world
is like now
Figure 2.14 A model-based, utility-based agent. It uses a model of the world, along with a
utility function that measures its preferences among states of the world. Then it chooses the
action that leads to the best expected utility, where expected utility is computed by averaging
over all possible outcome states, weighted by the probability of the outcome.
aim for, none of which can be achieved with certainty, utility provides a way in which the
likelihood of success can be weighed against the importance of the goals.
Partial observability and nondeterminism are ubiquitous in the real world, and so, there-
fore, is decision making under uncertainty. Technically speaking, a rational utility-based
agent chooses the action that maximizes the expected utility of the action outcomes—that
Expected utility
is, the utility the agent expects to derive, on average, given the probabilities and utilities of
each outcome. (Appendix A deﬁnes expectation more precisely.) In Chapter 15, we show
that any rational agent must behave as if it possesses a utility function whose expected value
it tries to maximize. An agent that possesses an explicit utility function can make rational de-
cisions with a general-purpose algorithm that does not depend on the speciﬁc utility function
being maximized. In this way, the “global” deﬁnition of rationality—designating as rational
those agent functions that have the highest performance—is turned into a “local” constraint
on rational-agent designs that can be expressed in a simple program.
The utility-based agent structure appears in Figure 2.14. Utility-based agent programs
appear in Chapters 15 and 16, where we design decision-making agents that must handle the
uncertainty inherent in nondeterministic or partially observable environments. Decision mak-
ing in multiagent environments is also studied in the framework of utility theory, as explained
in Chapter 17.
At this point, the reader may be wondering, “Is it that simple? We just build agents that
maximize expected utility, and we’re done?” It’s true that such agents would be intelligent,
but it’s not simple. A utility-based agent has to model and keep track of its environment,
tasks that have involved a great deal of research on perception, representation, reasoning,
and learning. The results of this research ﬁll many of the chapters of this book. Choosing
the utility-maximizing course of action is also a difﬁcult task, requiring ingenious algorithms
that ﬁll several more chapters. Even with these algorithms, perfect rationality is usually
