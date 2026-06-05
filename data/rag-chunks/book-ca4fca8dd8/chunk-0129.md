---
chunk_id: "book-ca4fca8dd8-chunk-0129"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 129
confidence: "first-pass"
extraction_method: "structured-local"
---

76
Chapter 2
Intelligent Agents
More generally, human choices can provide information about human preferences. For
example, suppose the taxi does not know that people generally don’t like loud noises, and
settles on the idea of blowing its horn continuously as a way of ensuring that pedestrians
know it’s coming. The consequent human behavior—covering ears, using bad language, and
possibly cutting the wires to the horn—would provide evidence to the agent with which to
update its utility function. This issue is discussed further in Chapter 23.
In summary, agents have a variety of components, and those components can be repre-
sented in many ways within the agent program, so there appears to be great variety among
learning methods. There is, however, a single unifying theme. Learning in intelligent agents
can be summarized as a process of modiﬁcation of each component of the agent to bring the
components into closer agreement with the available feedback information, thereby improv-
ing the overall performance of the agent.
2.4.7 How the components of agent programs work
We have described agent programs (in very high-level terms) as consisting of various compo-
nents, whose function it is to answer questions such as: “What is the world like now?” “What
action should I do now?” “What do my actions do?” The next question for a student of AI
is, “How on Earth do these components work?” It takes about a thousand pages to begin to
answer that question properly, but here we want to draw the reader’s attention to some basic
distinctions among the various ways that the components can represent the environment that
the agent inhabits.
Roughly speaking, we can place the representations along an axis of increasing complex-
ity and expressive power—atomic, factored, and structured. To illustrate these ideas, it helps
to consider a particular agent component, such as the one that deals with “What my actions
do.” This component describes the changes that might occur in the environment as the result
of taking an action, and Figure 2.16 provides schematic depictions of how those transitions
might be represented.
B
C
(a) Atomic
(b) Factored
(c) Structured
B
C
Figure 2.16 Three ways to represent states and the transitions between them. (a) Atomic
representation: a state (such as B or C) is a black box with no internal structure; (b) Factored
representation: a state consists of a vector of attribute values; values can be Boolean, real-
valued, or one of a ﬁxed set of symbols. (c) Structured representation: a state includes
objects, each of which may have attributes of its own as well as relationships to other objects.
