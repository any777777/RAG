---
chunk_id: "book-ca4fca8dd8-chunk-1091"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1091
confidence: "first-pass"
extraction_method: "structured-local"
---

652
Chapter 18
Probabilistic Programming
worlds, each corresponding to a disjoint set of complete worlds. A partial world is a minimal
self-supporting instantiation6 of a subset of the relevant variables—that is, ancestors of the
evidence and query variables. For example, variables X(a,t) for values of t greater than the
last observation time (or the query time, whichever is greater) are irrelevant, so the algorithm
can consider just a ﬁnite preﬁx of the inﬁnite sequence.
18.2.3 Examples
The standard “use case” for an OUPM has three elements: the model, the evidence (the
known facts in a given scenario), and the query, which may be any expression, possibly
with free logical variables. The answer is a posterior joint probability for each possible set
of substitutions for the free variables, given the evidence, according to the model.7 Every
model includes type declarations, type signatures for the predicates and functions, one or
more number statements for each type, and one dependency statement for each predicate and
function. (In the examples below, declarations and signatures are omitted where the meaning
is clear.) As in RPMs, dependency statements use an if-then-else syntax to handle context-
speciﬁc dependencies.
Citation matching
Millions of academic research papers and technical reports are to be found online in the
form of pdf ﬁles. Such papers usually contain a section near the end called “References” or
“Bibliography,” in which citations—strings of characters—are provided to inform the reader
of related work. These strings can be located and “scraped” from the pdf ﬁles with the aim of
creating a database-like representation that relates papers and researchers by authorship and
citation links. Systems such as CiteSeer and Google Scholar present such a representation to
their users; behind the scenes, algorithms operate to ﬁnd papers, scrape the citation strings,
and identify the actual papers to which the citation strings refer. This is a difﬁcult task because
these strings contain no object identiﬁers and include errors of syntax, spelling, punctuation,
and content. To illustrate this, here are two relatively benign examples:
1. [Lashkari et al 94] Collaborative Interface Agents, Yezdi Lashkari, Max Metral, and
Pattie Maes, Proceedings of the Twelfth National Conference on Articial Intelligence,
MIT Press, Cambridge, MA, 1994.
2. Metral M. Lashkari, Y. and P. Maes. Collaborative interface agents. In Conference of
the American Association for Artiﬁcial Intelligence, Seattle, WA, August 1994.
The key question is one of identity: are these citations of the same paper or different pa-
pers? Asked this question, even experts disagree or are unwilling to decide, indicating that
reasoning under uncertainty is going to be an important part of solving this problem.8 Ad hoc
approaches—such as methods based on a textual similarity metric—often fail miserably. For
example, in 2002, CiteSeer reported over 120 distinct books written by Russell and Norvig.
6
A self-supporting instantiation of a set of variables is one in which the parents of every variable in the set are
also in the set.
7
As with Prolog, there may be inﬁnitely many sets of substitutions of unbounded size; designing exploratory
interfaces for such answers is an interesting visualization challenge.
8
The answer is yes, they are the same paper. The “National Conference on Articial Intelligence” (notice how
the “ﬁ” is missing, thanks to an error in scraping the ligature character) is another name for the AAAI conference;
the conference took place in Seattle whereas the proceedings publisher is in Cambridge.
