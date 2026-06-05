---
chunk_id: "book-ca4fca8dd8-chunk-0575"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 575
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 10.5
Reasoning Systems for Categories
349
Reiﬁcation of propositions makes it possible to represent every ground, function-free
atomic sentence of ﬁrst-order logic in the semantic network notation. Certain kinds of univer-
sally quantiﬁed sentences can be asserted using inverse links and the singly boxed and doubly
boxed arrows applied to categories, but that still leaves us a long way short of full ﬁrst-order
logic. Negation, disjunction, nested function symbols, and existential quantiﬁcation are all
missing. Now it is possible to extend the notation to make it equivalent to ﬁrst-order logic—as
in Peirce’s existential graphs—but doing so negates one of the main advantages of semantic
networks, which is the simplicity and transparency of the inference processes. Designers can
build a large network and still have a good idea about what queries will be efﬁcient, because
(a) it is easy to visualize the steps that the inference procedure will go through and (b) in
some cases the query language is so simple that difﬁcult queries cannot be posed.
In cases where the expressive power proves to be too limiting, many semantic network
systems provide for procedural attachment to ﬁll in the gaps. Procedural attachment is a
Procedural
attachment
technique whereby a query about (or sometimes an assertion of) a certain relation results in a
call to a special procedure designed for that relation rather than a general inference algorithm.
One of the most important aspects of semantic networks is their ability to represent de-
fault values for categories. Examining Figure 10.4 carefully, one notices that John has one
Default value
leg, despite the fact that he is a person and all persons have two legs. In a strictly logical KB,
this would be a contradiction, but in a semantic network, the assertion that all persons have
two legs has only default status; that is, a person is assumed to have two legs unless this is
contradicted by more speciﬁc information. The default semantics is enforced naturally by the
inheritance algorithm, because it follows links upwards from the object itself (John in this
case) and stops as soon as it ﬁnds a value. We say that the default is overridden by the more
Overriding
speciﬁc value. Notice that we could also override the default number of legs by creating a
category of OneLeggedPersons, a subset of Persons of which John is a member.
We can retain a strictly logical semantics for the network if we say that the Legs assertion
for Persons includes an exception for John:
∀x x∈Persons∧x ̸= John ⇒Legs(x,2).
For a ﬁxed network, this is semantically adequate but will be much less concise than the
network notation itself if there are lots of exceptions. For a network that will be updated with
more assertions, however, such an approach fails—we really want to say that any persons as
yet unknown with one leg are exceptions too. Section 10.6 goes into more depth on this issue
and on default reasoning in general.
10.5.2 Description logics
The syntax of ﬁrst-order logic is designed to make it easy to say things about objects. De-
scription logics are notations that are designed to make it easier to describe deﬁnitions and
Description logic
properties of categories. Description logic systems evolved from semantic networks in re-
sponse to pressure to formalize what the networks mean while retaining the emphasis on
taxonomic structure as an organizing principle.
The principal inference tasks for description logics are subsumption (checking if one
Subsumption
category is a subset of another by comparing their deﬁnitions) and classiﬁcation (checking
Classiﬁcation
whether an object belongs to a category). Some systems also include consistency of a cate-
Consistency
gory deﬁnition—whether the membership criteria are logically satisﬁable.
