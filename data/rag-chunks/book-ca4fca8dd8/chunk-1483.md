---
chunk_id: "book-ca4fca8dd8-chunk-1483"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1483
confidence: "first-pass"
extraction_method: "structured-local"
---

896
Chapter 24
Natural Language Processing
24.4.2 Learning semantic grammars
Unfortunately, the Penn Treebank does not include semantic representations of its sentences,
just syntactic trees. So if we are going to learn a semantic grammar, we will need a different
source of examples. Zettlemoyer and Collins (2005) describe a system that learns a grammar
for a question-answering system from examples that consist of a sentence paired with the
semantic form for the sentence:
• Sentence: What states border Texas?
• Logical Form: λx.state(x)∧λx.borders(x,Texas)
Given a large collection of pairs like this and a little bit of hand-coded knowledge for each
new domain, the system generates plausible lexical entries (for example, that “Texas” and
“state” are nouns such that state(Texas) is true), and simultaneously learns parameters for a
grammar that allows the system to parse sentences into semantic representations. Zettlemoyer
and Collins’s system achieved 79% accuracy on two different test sets of unseen sentences.
Zhao and Huang (2015) demonstrate a shift-reduce parser that runs faster, and achieves 85%
to 89% accuracy.
A limitation of these systems is that the training data includes logical forms. These are
expensive to create, requiring human annotators with specialized expertise—not everyone
understands the subtleties of lambda calculus and predicate logic. It is much easier to gather
examples of question/answer pairs:
• Question: What states border Texas?
• Answer: Louisiana, Arkansas, Oklahoma, New Mexico.
• Question: How many times would Rhode Island ﬁt into California?
• Answer: 135
Such question/answer pairs are quite common on the Web, so a large database can be put
together without human experts. Using this large source of data it is possible to build parsers
that outperform those that use a small database of annotated logical forms (Liang et al., 2011;
Liang and Potts, 2015). The key approach described in these papers is to invent an internal
logical form that is compositional but does not allow an exponentially large search space.
24.5 Complications of Real Natural Language
The grammar of real English is endlessly complex (and other languages are equally complex).
We will brieﬂy mention some of the topics that contribute to this complexity.
Quantiﬁcation: Consider the sentence “Every agent feels a breeze.” The sentence has
Quantiﬁcation
only one syntactic parse under E0, but it is semantically ambiguous: is there one breeze
that is felt by all the agents, or does each agent feel a separate personal breeze? The two
interpretations can be represented as
∀a a∈Agents ⇒
∃b b∈Breezes∧Feel(a,b) ;
∃b b∈Breezes∧∀a a∈Agents ⇒
Feel(a,b).
