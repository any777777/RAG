---
chunk_id: "book-ca4fca8dd8-chunk-1117"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1117
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 669

CHAPTER 19
LEARNING FROM EXAMPLES
In which we describe agents that can improve their behavior through diligent study of past
experiences and predictions about the future.
An agent is learning if it improves its performance after making observations about the world.
Learning can range from the trivial, such as jotting down a shopping list, to the profound, as
when Albert Einstein inferred a new theory of the universe. When the agent is a computer,
we call it machine learning: a computer observes some data, builds a model based on the
Machine learning
data, and uses the model as both a hypothesis about the world and a piece of software that
can solve problems.
Why would we want a machine to learn? Why not just program it the right way to begin
with? There are two main reasons. First, the designers cannot anticipate all possible future
situations. For example, a robot designed to navigate mazes must learn the layout of each new
maze it encounters; a program for predicting stock market prices must learn to adapt when
conditions change from boom to bust. Second, sometimes the designers have no idea how
to program a solution themselves. Most people are good at recognizing the faces of family
members, but they do it subconsciously, so even the best programmers don’t know how to
program a computer to accomplish that task, except by using machine learning algorithms.
In this chapter, we interleave a discussion of various model classes—decision trees (Sec-
tion 19.3), linear models (Section 19.6), nonparametric models such as nearest neighbors
(Section 19.7), ensemble models such as random forests (Section 19.8)—with practical ad-
vice on building machine learning systems (Section 19.9), and discussion of the theory of
machine learning (Sections 19.1 to 19.5).
19.1 Forms of Learning
Any component of an agent program can be improved by machine learning. The improve-
ments, and the techniques used to make them, depend on these factors:
• Which component is to be improved.
• What prior knowledge the agent has, which inﬂuences the model it builds.
• What data and feedback on that data is available.
Chapter 2 described several agent designs. The components of these agents include:
1. A direct mapping from conditions on the current state to actions.
2. A means to infer relevant properties of the world from the percept sequence.
3. Information about the way the world evolves and about the results of possible actions
the agent can take.

## Page 670
