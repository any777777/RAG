---
chunk_id: "book-ca4fca8dd8-chunk-1251"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1251
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 20.4
Learning Using Relevance Information
755
Sentences such as (20.6) express a strict form of relevance: given nationality, language is
fully determined. (Put another way: language is a function of nationality.) These sentences
are called functional dependencies or determinations. They occur so commonly in certain
Functional
dependency
Determination
kinds of applications (e.g., deﬁning database designs) that a special syntax is used to write
them. We adopt the notation of Davies (1985):
Nationality(x,n) ≻Language(x,l) .
As usual, this is simply a syntactic sugaring, but it makes it clear that the determination is
really a relationship between the predicates: nationality determines language. The relevant
properties determining conductance and density can be expressed similarly:
Material(x,m)∧Temperature(x,t) ≻Conductance(x,ρ) ;
Material(x,m)∧Temperature(x,t) ≻Density(x,d) .
The corresponding generalizations follow logically from the determinations and observations.
20.4.1 Determining the hypothesis space
Although the determinations sanction general conclusions concerning all Brazilians, or all
pieces of copper at a given temperature, they cannot, of course, yield a general predictive
theory for all nationalities, or for all temperatures and materials, from a single example.
Their main effect can be seen as limiting the space of hypotheses that the learning agent need
consider. In predicting conductance, for example, one need consider only material and tem-
perature and can ignore mass, ownership, day of the week, the current president, and so on.
Hypotheses can certainly include terms that are in turn determined by material and temper-
ature, such as molecular structure, thermal energy, or free-electron density. Determinations ◀
specify a sufﬁcient basis vocabulary from which to construct hypotheses concerning the target
predicate. This statement can be proven by showing that a given determination is logically
equivalent to a statement that the correct deﬁnition of the target predicate is one of the set of
all deﬁnitions expressible using the predicates on the left-hand side of the determination.
Intuitively, it is clear that a reduction in the hypothesis space size should make it eas-
ier to learn the target predicate. Using the basic results of computational learning theory
(Section 19.5), we can quantify the possible gains. First, recall that for Boolean functions,
log(|H|) examples are required to converge to a reasonable hypothesis, where |H| is the size
of the hypothesis space. If the learner has n Boolean features with which to construct hypothe-
ses, then, in the absence of further restrictions, |H| = O(22n), so the number of examples is
O(2n). If the determination contains d predicates in the left-hand side, the learner will require
only O(2d) examples, a reduction of O(2n−d).
20.4.2 Learning and using relevance information
As we stated in the introduction to this chapter, prior knowledge is useful in learning; but it too
has to be learned. In order to provide a complete story of relevance-based learning, we must
therefore provide a learning algorithm for determinations. The learning algorithm we now
present is based on a straightforward attempt to ﬁnd the simplest determination consistent
with the observations. A determination P ≻Q says that if any examples match on P, then they
must also match on Q. A determination is therefore consistent with a set of examples if every
pair that matches on the predicates on the left-hand side also matches on the goal predicate.
