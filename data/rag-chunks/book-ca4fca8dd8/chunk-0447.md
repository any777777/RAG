---
chunk_id: "book-ca4fca8dd8-chunk-0447"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 447
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 8.1
Representation Revisited
273
Language
Ontological Commitment
Epistemological Commitment
(What exists in the world)
(What an agent believes about facts)
Propositional logic
facts
true/false/unknown
First-order logic
facts, objects, relations
true/false/unknown
Temporal logic
facts, objects, relations, times
true/false/unknown
Probability theory
facts
degree of belief ∈[0,1]
Fuzzy logic
facts with degree of truth ∈[0,1]
known interval value
Figure 8.1 Formal languages and their ontological and epistemological commitments.
This ontological commitment is a great strength of logic (both propositional and ﬁrst-
order), because it allows us to start with true statements and infer other true statements. It is
especially powerful in domains where every proposition has clear boundaries, such as math-
ematics or the wumpus world, where a square either does or doesn’t have a pit; there is no
possibility of a square with a vaguely pit-like indentation. But in the real world, many propo-
sitions have vague boundaries: Is Vienna a large city? Does this restaurant serve delicious
food? Is that person tall? It depends who you ask, and their answer might be “kind of.”
One response is to reﬁne the representation: if a crude line dividing cities into “large”
and “not large” leaves out too much information for the application in question, then one
can increase the number of size categories or use a Population function symbol. Another
proposed solution comes from Fuzzy logic, which makes the ontological commitment that
Fuzzy logic
propositions have a degree of truth between 0 and 1. For example, the sentence “Vienna is a
Degree of truth
large city” might be true to degree 0.8 in fuzzy logic, while “Paris is a large city” might be true
to degree 0.9. This corresponds better to our intuitive conception of the world, but it makes it
harder to do inference: instead of one rule to determine the truth of A∧B, fuzzy logic needs
different rules depending on the domain. Another possibility, covered in Section 25.1, is to
assign each concept to a point in a multidimensional space, and then measure the distance
between the concept “large city” and the concept “Vienna” or “Paris.”
Various special-purpose logics make still further ontological commitments; for example,
temporal logic assumes that facts hold at particular times and that those times (which may
Temporal logic
be points or intervals) are ordered. Thus, special-purpose logics give certain kinds of objects
(and the axioms about them) “ﬁrst class” status within the logic, rather than simply deﬁn-
ing them within the knowledge base. Higher-order logic views the relations and functions
Higher-order logic
referred to by ﬁrst-order logic as objects in themselves. This allows one to make assertions
about all relations—for example, one could wish to deﬁne what it means for a relation to
be transitive. Unlike most special-purpose logics, higher-order logic is strictly more expres-
sive than ﬁrst-order logic, in the sense that some sentences of higher-order logic cannot be
expressed by any ﬁnite number of ﬁrst-order logic sentences.
A logic can also be characterized by its epistemological commitments—the possible
Epistemological
commitment
states of knowledge that it allows with respect to each fact. In both propositional and ﬁrst-
order logic, a sentence represents a fact and the agent either believes the sentence to be true,
believes it to be false, or has no opinion. These logics therefore have three possible states of
knowledge regarding any sentence.
