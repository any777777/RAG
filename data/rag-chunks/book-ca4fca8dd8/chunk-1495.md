---
chunk_id: "book-ca4fca8dd8-chunk-1495"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1495
confidence: "first-pass"
extraction_method: "structured-local"
---

902
Chapter 24
Natural Language Processing
identiﬁcation, spelling correction, sentiment analysis, genre classiﬁcation, and named-
entity recognition.
• These language models can have millions of features, so preprocessing and smoothing
the data to reduce noise is important.
• In building a statistical language system, it is best to devise a model that can make good
use of available data, even if the model seems overly simplistic.
• Word embeddings can give a richer representation of words and their similarities.
• To capture the hierarchical structure of language, phrase structure grammars (and in
particular, context-free grammars) are useful. The probabilistic context-free grammar
(PCFG) formalism is widely used, as is the dependency grammar formalism.
• Sentences in a context-free language can be parsed in O(n3) time by a chart parser
such as the CYK algorithm, which requires grammar rules to be in Chomsky Normal
Form. With a small loss in accuracy, natural languages can be parsed in O(n) time,
using a beam search or a shift-reduce parser.
• A treebank can be a resource for learning a PCFG grammar with parameters.
• It is convenient to augment a grammar to handle issues such as subject–verb agreement
and pronoun case, and to represent information at the level of words rather than just at
the level of categories.
• Semantic interpretation can also be handled by an augmented grammar. We can learn
a semantic grammar from a corpus of questions paired either with the logical form of
the question, or with the answer.
• Natural language is complex and difﬁcult to capture in a formal grammar.
Bibliographical and Historical Notes
N-gram letter models for language modeling were proposed by Markov (1913). Claude Shan-
non (Shannon and Weaver, 1949) was the ﬁrst to generate n-gram word models of English.
The bag-of-words model gets its name from a passage from linguist Zellig Harris (1954),
“language is not merely a bag of words but a tool with particular properties.” Norvig (2009)
gives some examples of tasks that can be accomplished with n-gram models.
Chomsky (1956, 1957) pointed out the limitations of ﬁnite-state models compared with
context-free models, concluding, “Probabilistic models give no particular insight into some
of the basic problems of syntactic structure.” This is true, but probabilistic models do provide
insight into some other basic problems—problems that context-free models ignore. Chom-
sky’s remarks had the unfortunate effect of scaring many people away from statistical models
for two decades, until these models reemerged for use in the ﬁeld of speech recognition
(Jelinek, 1976), and in cognitive science, where optimality theory (Smolensky and Prince,
1993; Kager, 1999) posited that language works by ﬁnding the most probable candidate that
optimally satisﬁes competing constraints.
Add-one smoothing, ﬁrst suggested by Pierre-Simon Laplace (1816), was formalized by
Jeffreys (1948). Other smoothing techniques include interpolation smoothing (Jelinek and
Mercer, 1980), Witten–Bell smoothing (1991), Good–Turing smoothing (Church and Gale,
