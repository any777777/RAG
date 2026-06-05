---
chunk_id: "book-ca4fca8dd8-chunk-0562"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 562
confidence: "first-pass"
extraction_method: "structured-local"
---

340
Chapter 10
Knowledge Representation
the major distinction between stuff and things. If we cut an aardvark in half, we do not get
two aardvarks (unfortunately).
The English language distinguishes clearly between stuff and things. We say “an aard-
vark,” but, except in pretentious California restaurants, one cannot say “a butter.” Linguists
distinguish between count nouns, such as aardvarks, holes, and theorems, and mass nouns,
Count nouns
Mass noun
such as butter, water, and energy. Several competing ontologies claim to handle this distinc-
tion. Here we describe just one; the others are covered in the historical notes section.
To represent stuff properly, we begin with the obvious. We need to have as objects in
our ontology at least the gross “lumps” of stuff we interact with. For example, we might
recognize a lump of butter as the one left on the table the night before; we might pick it up,
weigh it, sell it, or whatever. In these senses, it is an object just like the aardvark. Let us call
it Butter3. We also deﬁne the category Butter. Informally, its elements will be all those things
of which one might say “It’s butter,” including Butter3. With some caveats about very small
parts that we will omit for now, any part of a butter-object is also a butter-object:
b∈Butter ∧PartOf(p,b) ⇒p∈Butter.
We can now say that butter melts at around 30 degrees centigrade:
b∈Butter ⇒MeltingPoint(b,Centigrade(30)).
We could go on to say that butter is yellow, is less dense than water, is soft at room tempera-
ture, has a high fat content, and so on. On the other hand, butter has no particular size, shape,
or weight. We can deﬁne more specialized categories of butter such as UnsaltedButter, which
is also a kind of stuff. Note that the category PoundOfButter, which includes as members all
butter-objects weighing one pound, is not a kind of stuff. If we cut a pound of butter in half,
we do not, alas, get two pounds of butter.
What is actually going on is this: some properties are intrinsic: they belong to the very
Intrinsic
substance of the object, rather than to the object as a whole. When you cut an instance of stuff
in half, the two pieces retain the intrinsic properties—things like density, boiling point, ﬂavor,
color, ownership, and so on. On the other hand, their extrinsic properties—weight, length,
Extrinsic
shape, and so on—are not retained under subdivision. A category of objects that includes in
its deﬁnition only intrinsic properties is then a substance, or mass noun; a class that includes
any extrinsic properties in its deﬁnition is a count noun. Stuff and Thing are the most general
substance and object categories, respectively.
10.3 Events
In Section 7.7.1 we discussed actions: things that happen, such as Shoott; and ﬂuents: aspects
of the world that change, such as HaveArrowt. Both were represented as propositions, and
we used successor-state axioms to say that a ﬂuent will be true at time t + 1 if the action at
time t caused it to be true, or if it was already true at time t and the action did not cause it to
be false. That was for a world in which actions are discrete, instantaneous, happen one at a
time, and have no variation in how they are performed (that is, there is only one kind of Shoot
action, there is no distinction between shooting quickly, slowly, nervously, etc.).
But as we move from simplistic domains to the real world, there is a much richer range
of actions or events3 to deal with. Consider a continuous action, such as ﬁlling a bathtub. A
3
The terms “event” and “action” may be used interchangeably—they both mean “something that can happen.”
