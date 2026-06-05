---
chunk_id: "book-ca4fca8dd8-chunk-0478"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 478
confidence: "first-pass"
extraction_method: "structured-local"
---

290
Chapter 8
First-Order Logic
whose range of queries is known in advance. General-purpose knowledge bases, which cover
a broad range of human knowledge and are intended to support tasks such as natural language
understanding, are discussed in Chapter 10.
8.4.1 The knowledge engineering process
Knowledge engineering projects vary widely in content, scope, and difﬁculty, but all such
projects include the following steps:
1. Identify the questions. The knowledge engineer must delineate the range of questions
that the knowledge base will support and the kinds of facts that will be available for
each speciﬁc problem instance. For example, does the wumpus knowledge base need to
be able to choose actions, or is it required only to answer questions about the contents
of the environment? Will the sensor facts include the current location? The task will
determine what knowledge must be represented in order to connect problem instances to
answers. This step is analogous to the PEAS process for designing agents in Chapter 2.
2. Assemble the relevant knowledge. The knowledge engineer might already be an expert
in the domain, or might need to work with real experts to extract what they know—a
process called knowledge acquisition. At this stage, the knowledge is not represented
Knowledge
acquisition
formally. The idea is to understand the scope of the knowledge base, as determined by
the task, and to understand how the domain actually works.
For the wumpus world, which is deﬁned by an artiﬁcial set of rules, the relevant
knowledge is easy to identify. (Notice, however, that the deﬁnition of adjacency was
not supplied explicitly in the wumpus-world rules.) For real domains, the issue of
relevance can be quite difﬁcult—for example, a system for simulating VLSI designs
might or might not need to take into account stray capacitances and skin effects.
3. Decide on a vocabulary of predicates, functions, and constants. That is, translate the
important domain-level concepts into logic-level names. This involves many questions
of knowledge-engineering style. Like programming style, this can have a signiﬁcant
impact on the eventual success of the project. For example, should pits be represented
by objects or by a unary predicate on squares? Should the agent’s orientation be a
function or a predicate? Should the wumpus’s location depend on time? Once the
choices have been made, the result is a vocabulary that is known as the ontology of
Ontology
the domain. The word ontology means a particular theory of the nature of being or
existence. The ontology determines what kinds of things exist, but does not determine
their speciﬁc properties and interrelationships.
4. Encode general knowledge about the domain. The knowledge engineer writes down
the axioms for all the vocabulary terms. This pins down (to the extent possible) the
meaning of the terms, enabling the expert to check the content. Often, this step reveals
misconceptions or gaps in the vocabulary that must be ﬁxed by returning to step 3 and
iterating through the process.
5. Encode a description of the problem instance. If the ontology is well thought out, this
step is easy. It involves writing simple atomic sentences about instances of concepts that
are already part of the ontology. For a logical agent, problem instances are supplied by
the sensors, whereas a “disembodied” knowledge base is given sentences in the same
way that traditional programs are given input data.
