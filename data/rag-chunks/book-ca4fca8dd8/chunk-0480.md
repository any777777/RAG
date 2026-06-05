---
chunk_id: "book-ca4fca8dd8-chunk-0480"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 480
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 8.4
Knowledge Engineering in First-Order Logic
291
6. Pose queries to the inference procedure and get answers. This is where the reward is:
we can let the inference procedure operate on the axioms and problem-speciﬁc facts to
derive the facts we are interested in knowing. Thus, we avoid the need for writing an
application-speciﬁc solution algorithm.
7. Debug and evaluate the knowledge base. Alas, the answers to queries will seldom be
correct on the ﬁrst try. More precisely, the answers will be correct for the knowledge
base as written, assuming that the inference procedure is sound, but they will not be the
ones that the user is expecting. For example, if an axiom is missing, some queries will
not be answerable from the knowledge base. A considerable debugging process could
ensue. Missing axioms or axioms that are too weak can be easily identiﬁed by noticing
places where the chain of reasoning stops unexpectedly. For example, if the knowledge
base includes a diagnostic rule (see Exercise 8.WUMD) for ﬁnding the wumpus,
∀s Smelly(s) ⇒Adjacent(Home(Wumpus),s),
instead of the biconditional, then the agent will never be able to prove the absence of
wumpuses. Incorrect axioms can be identiﬁed because they are false statements about
the world. For example, the sentence
∀x NumOfLegs(x,4) ⇒Mammal(x)
is false for reptiles, amphibians, and tables. The falsehood of this sentence can be ◀
determined independently of the rest of the knowledge base. In contrast, a typical error
in a program looks like this:
offset = position + 1.
It is impossible to tell whether offset should be position or position + 1 without
understanding the surrounding context.
When you get to the point where there are no obvious errors in your knowledge base, it is
tempting to declare success. But unless there are obviously no errors, it is better to formally
evaluate your system by running it on a test suite of queries and measuring how many you get
right. Without objective measurement, it is too easy to convince yourself that the job is done.
To understand this seven-step process better, we now apply it to an extended example—the
domain of electronic circuits.
8.4.2 The electronic circuits domain
We will develop an ontology and knowledge base that allow us to reason about digital circuits
of the kind shown in Figure 8.6. We follow the seven-step process for knowledge engineering.
Identify the questions
There are many reasoning tasks associated with digital circuits. At the highest level, one
analyzes the circuit’s functionality. For example, does the circuit in Figure 8.6 actually add
properly? If all the inputs are high, what is the output of gate A2? Questions about the
circuit’s structure are also interesting. For example, what are all the gates connected to the
ﬁrst input terminal? Does the circuit contain feedback loops? These will be our tasks in this
section. There are more detailed levels of analysis, including those related to timing delays,
circuit area, power consumption, production cost, and so on. Each of these levels would
require additional knowledge.
