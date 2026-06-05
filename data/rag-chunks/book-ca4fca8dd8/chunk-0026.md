---
chunk_id: "book-ca4fca8dd8-chunk-0026"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 26
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 1.1
What Is AI?
21
problems correctly. They were more concerned with comparing the sequence and timing of
its reasoning steps to those of human subjects solving the same problems. The interdisci-
plinary ﬁeld of cognitive science brings together computer models from AI and experimental
Cognitive science
techniques from psychology to construct precise and testable theories of the human mind.
Cognitive science is a fascinating ﬁeld in itself, worthy of several textbooks and at least
one encyclopedia (Wilson and Keil, 1999). We will occasionally comment on similarities or
differences between AI techniques and human cognition. Real cognitive science, however, is
necessarily based on experimental investigation of actual humans or animals. We will leave
that for other books, as we assume the reader has only a computer for experimentation.
In the early days of AI there was often confusion between the approaches. An author
would argue that an algorithm performs well on a task and that it is therefore a good model
of human performance, or vice versa. Modern authors separate the two kinds of claims; this
distinction has allowed both AI and cognitive science to develop more rapidly. The two ﬁelds
fertilize each other, most notably in computer vision, which incorporates neurophysiological
evidence into computational models. Recently, the combination of neuroimaging methods
combined with machine learning techniques for analyzing such data has led to the beginnings
of a capability to “read minds”—that is, to ascertain the semantic content of a person’s inner
thoughts. This capability could, in turn, shed further light on how human cognition works.
1.1.3 Thinking rationally: The “laws of thought” approach
The Greek philosopher Aristotle was one of the ﬁrst to attempt to codify “right thinking”—
that is, irrefutable reasoning processes. His syllogisms provided patterns for argument struc-
Syllogism
tures that always yielded correct conclusions when given correct premises. The canonical
example starts with Socrates is a man and all men are mortal and concludes that Socrates is
mortal. (This example is probably due to Sextus Empiricus rather than Aristotle.) These laws
of thought were supposed to govern the operation of the mind; their study initiated the ﬁeld
called logic.
Logicians in the 19th century developed a precise notation for statements about objects
in the world and the relations among them. (Contrast this with ordinary arithmetic notation,
which provides only for statements about numbers.) By 1965, programs could, in principle,
solve any solvable problem described in logical notation. The so-called logicist tradition
Logicist
within artiﬁcial intelligence hopes to build on such programs to create intelligent systems.
Logic as conventionally understood requires knowledge of the world that is certain—
a condition that, in reality, is seldom achieved. We simply don’t know the rules of, say,
politics or warfare in the same way that we know the rules of chess or arithmetic. The theory
of probability ﬁlls this gap, allowing rigorous reasoning with uncertain information. In
Probability
principle, it allows the construction of a comprehensive model of rational thought, leading
from raw perceptual information to an understanding of how the world works to predictions
about the future. What it does not do, is generate intelligent behavior. For that, we need a
theory of rational action. Rational thought, by itself, is not enough.
1.1.4 Acting rationally: The rational agent approach
An agent is just something that acts (agent comes from the Latin agere, to do). Of course,
Agent
all computer programs do something, but computer agents are expected to do more: operate
autonomously, perceive their environment, persist over a prolonged time period, adapt to
