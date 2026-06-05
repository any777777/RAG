---
chunk_id: "book-ca4fca8dd8-chunk-0449"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 449
confidence: "first-pass"
extraction_method: "structured-local"
---

274
Chapter 8
First-Order Logic
Systems using probability theory, on the other hand, can have any degree of belief, or
subjective likelihood, ranging from 0 (total disbelief) to 1 (total belief). It is important not
to confuse the degree of belief in probability theory with the degree of truth in fuzzy logic.
Indeed, some fuzzy systems allow uncertainty (degree of belief) about degrees of truth. For
example, a probabilistic wumpus-world agent might believe that the wumpus is in [1,3] with
probability 0.75 and in [2, 3] with probability 0.25 (although the wumpus is deﬁnitely in one
particular square).
8.2 Syntax and Semantics of First-Order Logic
We begin this section by specifying more precisely the way in which the possible worlds of
ﬁrst-order logic reﬂect the ontological commitment to objects and relations. Then we intro-
duce the various elements of the language, explaining their semantics as we go along. The
main points are how the language facilitates concise representations and how its semantics
leads to sound reasoning procedures.
8.2.1 Models for ﬁrst-order logic
Chapter 7 said that the models of a logical language are the formal structures that constitute
the possible worlds under consideration. Each model links the vocabulary of the logical sen-
tences to elements of the possible world, so that the truth of any sentence can be determined.
Thus, models for propositional logic link proposition symbols to predeﬁned truth values.
Models for ﬁrst-order logic are much more interesting. First, they have objects in them!
The domain of a model is the set of objects or domain elements it contains. The domain is
Domain
Domain elements
required to be nonempty—every possible world must contain at least one object. (See Exer-
cise 8.EMPT for a discussion of empty worlds.) Mathematically speaking, it doesn’t matter
what these objects are—all that matters is how many there are in each particular model—but
for pedagogical purposes we’ll use a concrete example. Figure 8.2 shows a model with ﬁve
objects: Richard the Lionheart, King of England from 1189 to 1199; his younger brother, the
evil King John, who ruled from 1199 to 1215; the left legs of Richard and John; and a crown.
The objects in the model may be related in various ways. In the ﬁgure, Richard and John
are brothers. Formally speaking, a relation is just the set of tuples of objects that are related.
Tuple
(A tuple is a collection of objects arranged in a ﬁxed order and is written with angle brackets
surrounding the objects.) Thus, the brotherhood relation in this model is the set
{⟨Richard the Lionheart, King John⟩, ⟨King John, Richard the Lionheart⟩}.
(8.1)
(Here we have named the objects in English, but you may, if you wish, mentally substitute the
pictures for the names.) The crown is on King John’s head, so the “on head” relation contains
just one tuple, ⟨the crown, King John⟩. The “brother” and “on head” relations are binary
relations—that is, they relate pairs of objects. The model also contains unary relations, or
properties: the “person” property is true of both Richard and John; the “king” property is true
only of John (presumably because Richard is dead at this point); and the “crown” property is
true only of the crown.
Certain kinds of relationships are best considered as functions, in that a given object must
be related to exactly one object in this way. For example, each person has one left leg, so the
model has a unary “left leg” function—a mapping from a one-element tuple to an object—that
