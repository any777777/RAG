---
chunk_id: "book-ca4fca8dd8-chunk-0431"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 431
confidence: "first-pass"
extraction_method: "structured-local"
---

264
Chapter 7
Logical Agents
valid plan for the original problem. Modern SAT-solving technology makes the approach
quite practical. For example, a DPLL-style solver has no difﬁculty in generating the solution
for the wumpus world instance shown in Figure 7.2.
This section has described a declarative approach to agent construction: the agent works
by a combination of asserting sentences in the knowledge base and performing logical infer-
ence. This approach has some weaknesses hidden in phrases such as “for each time t” and
“for each square [x,y].” For any practical agent, these phrases have to be implemented by
code that generates instances of the general sentence schema automatically for insertion into
the knowledge base. For a wumpus world of reasonable size—one comparable to a smallish
computer game—we might need a 100×100 board and 1000 time steps, leading to knowl-
edge bases with tens or hundreds of millions of sentences.
Not only does this become rather impractical, but it also illustrates a deeper problem:
we know something about the wumpus world—namely, that the “physics” works the same
way across all squares and all time steps—that we cannot express directly in the language of
propositional logic. To solve this problem, we need a more expressive language, one in which
phrases like “for each time t” and “for each square [x,y]” can be written in a natural way. First-
order logic, described in Chapter 8, is such a language; in ﬁrst-order logic a wumpus world
of any size and duration can be described in about ten logic sentences rather than ten million
or ten trillion.
Summary
We have introduced knowledge-based agents and have shown how to deﬁne a logic with
which such agents can reason about the world. The main points are as follows:
• Intelligent agents need knowledge about the world in order to reach good decisions.
• Knowledge is contained in agents in the form of sentences in a knowledge represen-
tation language that are stored in a knowledge base.
• A knowledge-based agent is composed of a knowledge base and an inference mecha-
nism. It operates by storing sentences about the world in its knowledge base, using the
inference mechanism to infer new sentences, and using these sentences to decide what
action to take.
• A representation language is deﬁned by its syntax, which speciﬁes the structure of
sentences, and its semantics, which deﬁnes the truth of each sentence in each possible
world or model.
• The relationship of entailment between sentences is crucial to our understanding of
reasoning. A sentence α entails another sentence β if β is true in all worlds where
α is true. Equivalent deﬁnitions include the validity of the sentence α ⇒β and the
unsatisﬁability of the sentence α∧¬β.
• Inference is the process of deriving new sentences from old ones. Sound inference algo-
rithms derive only sentences that are entailed; complete algorithms derive all sentences
that are entailed.
• Propositional logic is a simple language consisting of proposition symbols and logical
connectives. It can handle propositions that are known to be true, known to be false, or
completely unknown.
