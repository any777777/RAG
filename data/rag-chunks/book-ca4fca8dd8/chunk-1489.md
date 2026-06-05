---
chunk_id: "book-ca4fca8dd8-chunk-1489"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1489
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 24.5
Complications of Real Natural Language
899
our current grammar, “Chrysler announced” gets interpreted as
x = Chrysler ∧e ∈Announce(x)∧After(Now,Extent(e)).
We need to change that to
x = Chrysler ∧e ∈Announce(m)∧After(Now,Extent(e))
∧Metonymy(m,x).
This says that there is one entity x that is equal to Chrysler, and another entity m that did the
announcing, and that the two are in a metonymy relation. The next step is to deﬁne what
kinds of metonymy relations can occur. The simplest case is when there is no metonymy at
all—the literal object x and the metonymic object m are identical:
∀m,x (m = x) ⇒Metonymy(m,x).
For the Chrysler example, a reasonable generalization is that an organization can be used to
stand for a spokesperson of that organization:
∀m,x x∈Organizations∧Spokesperson(m,x) ⇒Metonymy(m,x).
Other metonymies include the author for the works (I read Shakespeare) or more generally
the producer for the product (I drive a Honda) and the part for the whole (The Red Sox need
a strong arm). Some examples of metonymy, such as “The ham sandwich on Table 4 wants
another beer,” are more novel and are interpreted with respect to a situation (such as waiting
on tables and not knowing a customer’s name).
A metaphor is another ﬁgure of speech, in which a phrase with one literal meaning is
Metaphor
used to suggest a different meaning by way of an analogy. Thus, metaphor can be seen as a
kind of metonymy where the relation is one of similarity.
Disambiguation is the process of recovering the most probable intended meaning of an
Disambiguation
utterance. In one sense we already have a framework for solving this problem: each rule
has a probability associated with it, so the probability of an interpretation is the product of
the probabilities of the rules that led to the interpretation. Unfortunately, the probabilities
reﬂect how common the phrases are in the corpus from which the grammar was learned,
and thus reﬂect general knowledge, not speciﬁc knowledge of the current situation. To do
disambiguation properly, we need to combine four models:
1. The world model: the likelihood that a proposition occurs in the world. Given what we
know about the world, it is more likely that a speaker who says “I’m dead” means “I
am in big trouble” or “I lost this video game” rather than “My life ended, and yet I can
still talk.”
2. The mental model: the likelihood that the speaker forms the intention of communicat-
ing a certain fact to the hearer. This approach combines models of what the speaker
believes, what the speaker believes the hearer believes, and so on. For example, when
a politician says, “I am not a crook,” the world model might assign a probability of
only 50% to the proposition that the politician is not a criminal, and 99.999% to the
proposition that he is not a hooked shepherd’s staff. Nevertheless, we select the former
interpretation because it is a more likely thing to say.
3. The language model: the likelihood that a certain string of words will be chosen, given
that the speaker has the intention of communicating a certain fact.
