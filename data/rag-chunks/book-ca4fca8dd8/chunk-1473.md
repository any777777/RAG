---
chunk_id: "book-ca4fca8dd8-chunk-1473"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1473
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 24.3
Parsing
889
I
detect
the
Adjective
wumpus
near
Pronoun
I
detect
the
smelly
wumpus
near
me
Pronoun
NP
S
VP
Verb
NP
Article
Prep
Noun
NP
PP
NP
Adjs
me
smelly
Figure 24.7 A dependency-style parse (top) and the corresponding phrase structure parse
(bottom) for the sentence I detect the smelly wumpus near me.
guaranteed to ﬁnd the parse with highest probability, but (with a careful implementation) the
parser can operate in O(n) time and still ﬁnds the best parse most of the time.
A beam search parser with b = 1 is called a deterministic parser. One popular determin-
Deterministic parser
istic approach is shift-reduce parsing, in which we go through the sentence word by word,
Shift-reduce parsing
choosing at each point whether to shift the word onto a stack of constituents, or to reduce
the top constituent(s) on the stack according to a grammar rule. Each style of parsing has its
adherents within the NLP community. Even though it is possible to transform a shift-reduce
system into a PCFG (and vice versa), when you apply machine learning to the problem of
inducing a grammar, the inductive bias and hence the generalizations that each system will
make will be different (Abney et al., 1999).
24.3.1 Dependency parsing
There is a widely used alternative syntactic approach called dependency grammar, which
Dependency
grammar
assumes that syntactic structure is formed by binary relations between lexical items, without
a need for syntactic constituents. Figure 24.7 shows a sentence with a dependency parse and
a phrase structure parse.
In one sense, dependency grammar and phrase structure grammar are just notational vari-
ants. If the phrase structure tree is annotated with the head of each phrase, you can recover

## Page 890
