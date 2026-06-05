---
chunk_id: "book-ca4fca8dd8-chunk-1474"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1474
confidence: "first-pass"
extraction_method: "structured-local"
---

890
Chapter 24
Natural Language Processing
[ [S [NP-2 Her eyes]
[VP were
[VP glazed
[NP *-2]
[SBAR-ADV as if
[S [NP she]
[VP did n’t
[VP [VP hear [NP *-1]]
or
[VP [ADVP even] see [NP *-1]]
[NP-1 him]]]]]]]]
.]
Figure 24.8 Annotated tree for the sentence “Her eyes were glazed as if she didn’t hear
or even see him.” from the Penn Treebank. Note a grammatical phenomenon we have not
covered yet: the movement of a phrase from one part of the tree to another. This tree analyzes
the phrase “hear or even see him” as consisting of two constituent VPs, [VP hear [NP *-1]]
and [VP [ADVP even] see [NP *-1]], both of which have a missing object, denoted *-1, which
refers to the NP labeled elsewhere in the tree as [NP-1 him]. Similarly, the [NP *-2] refers to
the [NP-2 Her eyes].
the dependency tree from it. In the other direction, we can convert a dependency tree into a
phrase structure tree by introducing arbitrary categories (although we might not always get a
natural-looking tree this way).
Therefore we wouldn’t prefer one notation over the other because one is more powerful;
rather we would prefer one because it is more natural—either more familiar for the human
developers of a system, or more natural for a machine learning system which will have to
learn the structures. In general, phrase structure trees are natural for languages (like English)
with mostly ﬁxed word order; dependency trees are natural for languages (such as Latin) with
mostly free word order, where the order of words is determined more by pragmatics than by
syntactic categories.
The popularity of dependency grammar today stems in large part from the
Universal Dependencies project (Nivre et al., 2016), an open-source treebank project that
deﬁnes a set of relations and provides millions of parsed sentences in over 70 languages.
24.3.2 Learning a parser from examples
Building a grammar for a signiﬁcant portion of English is laborious and error prone. This
suggests that it would be better to learn the grammar rules (and probabilities) rather than
writing them down by hand. To apply supervised learning, we need input/output pairs of
sentences and their parse trees. The Penn Treebank is the best known source of such data,
with over 100 thousand sentences annotated with parse-tree structure. Figure 24.8 shows an
annotated tree from the Penn Treebank.
Given a treebank, we can create a PCFG just by counting the number of times each node-
type appears in a tree (with the usual caveats about smoothing low counts). In Figure 24.8,
there are two nodes of the form [S[NP...][VP...]]. We would count these, and all the other
