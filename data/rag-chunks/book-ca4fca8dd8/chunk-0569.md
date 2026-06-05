---
chunk_id: "book-ca4fca8dd8-chunk-0569"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 569
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 10.4
Mental Objects and Modal Logic
345
a good thing; if our agent knows that 2 + 2 = 4 and 4 < 5, then we want our agent to know
that 2 + 2 < 5. This property is called referential transparency—it doesn’t matter what
Referential
transparency
term a logic uses to refer to an object, what matters is the object that the term names. But for
propositional attitudes like believes and knows, we would like to have referential opacity—the
terms used do matter, because not all agents know which terms are co-referential.
We could patch this up with even more reiﬁcation: we could have one object to represent
Clark/Superman, another object to represent the person that Lois knows as Clark, and yet
another for the person Lois knows as Superman. However, this proliferation of objects means
that the sentences we want to write quickly become verbose and clumsy.
Modal logic is designed to address this problem. Regular logic is concerned with a single
Modal logic
modality, the modality of truth, allowing us to express “P is true” or “P is false.” Modal logic
includes special modal operators that take sentences (rather than terms) as arguments. For
Modal operators
example, “A knows P” is represented with the notation KAP, where K is the modal operator
for knowledge. It takes two arguments, an agent (written as the subscript) and a sentence.
The syntax of modal logic is the same as ﬁrst-order logic, except that sentences can also be
formed with modal operators.
The semantics of modal logic is more complicated. In ﬁrst-order logic a model contains a
set of objects and an interpretation that maps each name to the appropriate object, relation, or
function. In modal logic we want to be able to consider both the possibility that Superman’s
secret identity is Clark and the possibility that it isn’t.
Therefore, we will need a more complicated model, one that consists of a collection of
possible worlds rather than just one true world. The worlds are connected in a graph by ac-
Possible world
cessibility relations, one relation for each modal operator. We say that world w1 is accessible
Accessibility relation
from world w0 with respect to the modal operator KA if everything in w1 is consistent with
what A knows in w0. As an example, in the real world, Bucharest is the capital of Romania,
but for an agent that did not know that, a world where the capital of Romania is, say, Soﬁa is
accessible. Hopefully a world where 2+2 = 5 would not be accessible to any agent.
In general, a knowledge atom KAP is true in world w if and only if P is true in every
world accessible from w. The truth of more complex sentences is derived by recursive appli-
cation of this rule and the normal rules of ﬁrst-order logic. That means that modal logic can
be used to reason about nested knowledge sentences: what one agent knows about another
agent’s knowledge. For example, we can say that even though Lois doesn’t know whether
Superman’s secret identity is Clark Kent, she does know that Clark knows:
KLois[KClarkIdentity(Superman,Clark)∨KClark¬Identity(Superman,Clark)]
Modal logic solves some tricky issues with the interplay of quantiﬁers and knowledge.
The English sentence “Bond knows that someone is a spy” is ambiguous. The ﬁrst reading is
that there is a particular someone who Bond knows is a spy; we can write this as
∃x KBondSpy(x),
which in modal logic means that there is an x that, in all accessible worlds, Bond knows to be
a spy. The second reading is that Bond just knows that there is at least one spy:
KBond∃x Spy(x).
The modal logic interpretation is that in each accessible world there is an x that is a spy, but
it need not be the same x in each world.
