---
chunk_id: "book-ca4fca8dd8-chunk-0546"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 546
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 10
KNOWLEDGE REPRESENTATION
In which we show how to represent diverse facts about the real world in a form that can be
used to reason and solve problems.
The previous chapters showed how an agent with a knowledge base can make inferences
that enable it to act appropriately. In this chapter we address the question of what content
to put into such an agent’s knowledge base—how to represent facts about the world. We
will use ﬁrst-order logic as the representation language, but later chapters will introduce dif-
ferent representation formalisms such as hierarchical task networks for reasoning about plans
(Chapter 11), Bayesian networks for reasoning with uncertainty (Chapter 13), Markov models
for reasoning over time (Chapter 16), and deep neural networks for reasoning about images,
sounds, and other data (Chapter 22). But no matter what representation you use, the facts
about the world still need to be handled, and this chapter gives you a feeling for the issues.
Section 10.1 introduces the idea of a general ontology, which organizes everything in
the world into a hierarchy of categories. Section 10.2 covers the basic categories of objects,
substances, and measures; Section 10.3 covers events; and Section 10.4 discusses knowledge
about beliefs. We then return to consider the technology for reasoning with this content:
Section 10.5 discusses reasoning systems designed for efﬁcient inference with categories,
and Section 10.6 discusses reasoning with default information.
10.1 Ontological Engineering
In “toy” domains, the choice of representation is not that important; many choices will work.
Complex domains such as shopping on the Internet or driving a car in trafﬁc require more
general and ﬂexible representations. This chapter shows how to create these representations,
concentrating on general concepts—such as Events, Time, Physical Objects, and Beliefs—
that occur in many different domains. Representing these abstract concepts is sometimes
called ontological engineering.
Ontological
engineering
We cannot hope to represent everything in the world, even a 1000-page textbook, but
we will leave placeholders where new knowledge for any domain can ﬁt in. For example,
we will deﬁne what it means to be a physical object, and the details of different types of
objects—robots, televisions, books, or whatever—can be ﬁlled in later. This is analogous to
the way that designers of an object-oriented programming framework (such as the Java Swing
graphical framework) deﬁne general concepts like Window, expecting users to use these to
deﬁne more speciﬁc concepts like SpreadsheetWindow. The general framework of concepts
is called an upper ontology because of the convention of drawing graphs with the general
Upper ontology
concepts at the top and the more speciﬁc concepts below them, as in Figure 10.1.
