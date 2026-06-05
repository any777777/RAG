---
chunk_id: "book-ca4fca8dd8-chunk-0593"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 593
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
359
Knowledge (Fagin et al., 1995) provides a thorough introduction, and Gordon and Hobbs
(2017) provide A Formal Theory of Commonsense Psychology.
The second approach is a ﬁrst-order theory in which mental objects are ﬂuents. Davis
(2005) and Davis and Morgenstern (2005) describe this approach. It relies on the possible-
worlds formalism, and builds on work by Robert Moore (1980, 1985).
The third approach is a syntactic theory, in which mental objects are represented by
character strings. A string is just a complex term denoting a list of symbols, so CanFly(Clark)
can be represented by the list of symbols [C,a,n,F,l,y,(,C,l,a,r,k,)]. The syntactic theory
of mental objects was ﬁrst studied in depth by Kaplan and Montague (1960), who showed
that it led to paradoxes if not handled carefully. Ernie Davis (1990) provides an excellent
comparison of the syntactic and modal theories of knowledge. Pnueli (1977) describes a
temporal logic used to reason about programs, work that won him the Turing Award and
which was expanded upon by Vardi (1996). Littman et al. (2017) show that a temporal logic
can be a good language for specifying goals to a reinforcement learning robot in a way that
is easy for a human to specify, and generalizes well to different environments.
The Greek philosopher Porphyry (c. 234–305 CE), commenting on Aristotle’s Cate-
gories, drew what might qualify as the ﬁrst semantic network. Charles S. Peirce (1909)
developed existential graphs as the ﬁrst semantic network formalism using modern logic.
Ross Quillian (1961), driven by an interest in human memory and language processing, ini-
tiated work on semantic networks within AI. An inﬂuential paper by Marvin Minsky (1975)
presented a version of semantic networks called frames; a frame was a representation of an
object or category, with attributes and relations to other objects or categories.
The question of semantics arose quite acutely with respect to Quillian’s semantic net-
works (and those of others who followed his approach), with their ubiquitous and very vague
“IS-A links.” Bill Woods’s (1975) famous article “What’s In a Link?” drew the attention of AI
researchers to the need for precise semantics in knowledge representation formalisms. Ron
Brachman (1979) elaborated on this point and proposed solutions. Patrick Hayes’s (1979)
“The Logic of Frames” cut even deeper, claiming that “Most of ‘frames’ is just a new syntax
for parts of ﬁrst-order logic.” Drew McDermott’s (1978b) “Tarskian Semantics, or, No No-
tation without Denotation!” argued that the model-theoretic approach to semantics used in
ﬁrst-order logic should be applied to all knowledge representation formalisms. This remains
a controversial idea; notably, McDermott himself has reversed his position in “A Critique of
Pure Reason” (McDermott, 1987). Selman and Levesque (1993) discuss the complexity of
inheritance with exceptions, showing that in most formulations it is NP-complete.
Description logics were developed as a useful subset of ﬁrst-order logic for which infer-
ence is computationally tractable. Hector Levesque and Ron Brachman (1987) showed that
certain uses of disjunction and negation were primarily responsible for the intractability of
logical inference. This led to a better understanding of the interaction between complexity
and expressiveness in reasoning systems. Calvanese et al. (1999) summarize the state of the
art, and Baader et al. (2007) present a comprehensive handbook of description logic.
The three main formalisms for dealing with nonmonotonic inference—circumscription
(McCarthy, 1980), default logic (Reiter, 1980), and modal nonmonotonic logic (McDermott
and Doyle, 1980)—were all introduced in one special issue of the AI Journal. Delgrande
and Schaub (2003) discuss the merits of the variants, given 25 years of hindsight. Answer
set programming can be seen as an extension of negation as failure or as a reﬁnement of
