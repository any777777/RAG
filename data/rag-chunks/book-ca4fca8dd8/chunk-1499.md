---
chunk_id: "book-ca4fca8dd8-chunk-1499"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1499
confidence: "first-pass"
extraction_method: "structured-local"
---

904
Chapter 24
Natural Language Processing
PCFG. Lexicalized PCFGs (Charniak, 1997; Hwa, 1998) combine the best aspects of PCFGs
and n-gram models. Collins (1999) describes PCFG parsing that is lexicalized with head fea-
tures, and Johnson (1998) shows how the accuracy of a PCFG depends on the structure of the
treebank from which its probabilities were learned.
There have been many attempts to write formal grammars of natural languages, both in
“pure” linguistics and in computational linguistics. There are several comprehensive but in-
formal grammars of English (Quirk et al., 1985; McCawley, 1988; Huddleston and Pullum,
2002). Since the 1980s, there has been a trend toward lexicalization: putting more informa-
tion in the lexicon and less in the grammar.
Lexical-functional grammar, or LFG (Bresnan, 1982) was the ﬁrst major grammar for-
malism to be highly lexicalized. If we carry lexicalization to an extreme, we end up with
categorial grammar (Clark and Curran, 2004), in which there can be as few as two grammar
rules, or with dependency grammar (Smith and Eisner, 2008; K¨ubler et al., 2009) in which
there are no syntactic categories, only relations between words.
Computerized parsing was ﬁrst demonstrated by Yngve (1955). Efﬁcient algorithms were
developed in the 1960s, with a few twists since then (Kasami, 1965; Younger, 1967; Earley,
1970; Graham et al., 1980). Church and Patil (1982) describe syntactic ambiguity and address
ways to resolve it.
Klein and Manning (2003) describe A∗parsing, and Pauls and Klein (2009) extend that
to K-best A∗parsing, in which the result is not a single parse but the K best. Goldberg et al.
(2013) describe the necessary implementation tricks to make sure that a beam search parser
is O(n) and not O(n2). Zhu et al. (2013) describe a fast deterministic shift-reduce parser
for natural languages, and Sagae and Lavie (2006) show how adding search to a shift-reduce
parser can make it more accurate, at the cost of some speed.
Today, highly accurate open-source parsers include Google’s Parsey McParseface (Andor
et al., 2016), the Stanford Parser (Chen and Manning, 2014), the Berkeley Parser (Kitaev and
Klein, 2018), and the SPACY parser. They all do generalization through neural networks and
achieve roughly 95% accuracy on Wall Street Journal or Penn Treebank test sets. There is
some criticism of the ﬁeld that it is focusing too narrowly on measuring performance on a
few select corpora, and perhaps overﬁtting on them.
Formal semantic interpretation of natural languages originates within philosophy and
formal logic, particularly Alfred Tarski’s (1935) work on the semantics of formal languages.
Bar-Hillel (1954) was the ﬁrst to consider the problems of pragmatics (such as indexicals) and
propose that they could be handled by formal logic. Richard Montague’s essay “English as a
formal language” (1970) is a kind of manifesto for the logical analysis of language, but there
are other books that are more readable (Dowty et al., 1991; Portner and Partee, 2002; Cruse,
2011). While semantic interpretation programs are designed to pick the most likely inter-
pretation, literary critics (Empson, 1953; Hobbs, 1990) have been ambiguous about whether
ambiguity is something to be resolved or cherished. Norvig (1988) discusses the problems of
considering multiple simultaneous interpretations, rather than settling for a single maximum-
likelihood interpretation. Lakoff and Johnson (1980) give an engaging analysis and catalog of
common metaphors in English. Martin (1990) and Gibbs (2006) offer computational models
of metaphor interpretation.
The ﬁrst NLP system to solve an actual task was the BASEBALL question answering
system (Green et al., 1961), which handled questions about a database of baseball statistics.
