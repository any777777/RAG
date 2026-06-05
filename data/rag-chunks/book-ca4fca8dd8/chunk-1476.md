---
chunk_id: "book-ca4fca8dd8-chunk-1476"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1476
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 24.3
Parsing
891
subtrees with root S in the corpus. If there are 1000 S nodes of which 600 are of this form,
then we create the rule:
S →NP VP [0.6].
All together, the Penn Treebank has over 10,000 different node types. This reﬂects the fact
that English is a complex language, but it also indicates that the annotators who created the
treebank favored ﬂat trees, perhaps ﬂatter than we would like. For example, the phrase “the
good and the bad” is parsed as a single noun phrase rather than as two conjoined noun phrases,
giving us the rule:
NP →Article Noun Conjunction Article Noun .
There are hundreds of similar rules that deﬁne a noun phrase as a string of categories with
a conjunction somewhere in the middle; a more concise grammar could capture all the con-
joined noun phrase rules with the single rule
NP →NP Conjunction NP.
Bod et al. (2003) and Bod (2008) show how to automatically recover generalized rules like
this, greatly reducing the number of rules that come out of the treebank, and creating a gram-
mar that ends up generalizing better for previously unseen sentences. They call their approach
data-oriented parsing.
We have seen that treebanks are not perfect—they contain errors, and have idiosyncratic
parses. It is also clear that creating a treebank requires a lot of hard work; that means that
treebanks will remain relatively small in size, compared to all the text that has not been
annotated with trees. An alternative approach is unsupervised parsing, in which we learn a
Unsupervised parsing
new grammar (or improve an existing grammar) using a corpus of sentences without trees.
The inside–outside algorithm (Dodd, 1988), which we will not cover here, learns to
estimate the probabilities in a PCFG from example sentences without trees, similar to the
way the forward-backward algorithm (Figure 14.4) estimates probabilities. Spitkovsky et al.
(2010a) describe an unsupervised learning approach that uses curriculum learning: start
Curriculum learning
with the easy part of the curriculum—short unambiguous 2-word sentences like “He left” can
be easily parsed based on prior knowledge or annotations. Each new parse of a short sentence
extends the system’s knowledge so that it can eventually tackle 3-word, then 4-word, and
eventually 40-word sentences.
We can also use semisupervised parsing, in which we start with a small number of trees
Semisupervised
parsing
as data to build an initial grammar, then add a large number of unparsed sentences to improve
the grammar. The semisupervised approach can make use of partial bracketing: we can
Partial bracketing
use widely available text that has been marked up by the authors, not by linguistic experts,
with a partial tree-like structure, in the form of HTML or similar annotations. In HTML text
most brackets correspond to a syntactic component, so partial bracketing can help learn a
grammar (Pereira and Schabes, 1992; Spitkovsky et al., 2010b). Consider this HTML text
from a newspaper article:
In 1998, however, as I <a>established in
<i>The New Republic</i></a> and Bill Clinton just
<a>confirmed in his memoirs</a>, Netanyahu changed his mind
The words surrounded by <i></i> tags form a noun phrase, and the two strings of words
surrounded by <a></a> tags each form verb phrases.
