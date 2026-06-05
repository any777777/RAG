---
chunk_id: "book-ca4fca8dd8-chunk-0574"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 574
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 348

348
Chapter 10
Knowledge Representation
Mammals
John
Mary
Persons
Male
Persons
Female
Persons
1
2
SubsetOf
SubsetOf
SubsetOf
MemberOf
MemberOf
SisterOf
Legs
Legs
HasMother
Figure 10.4 A semantic network with four objects (John, Mary, 1, and 2) and four categories.
Relations are denoted by labeled links.
MemberOf
FlyEvents
Fly17
Shankar
NewYork
NewDelhi
Yesterday
Agent
Origin
Destination
During
Figure 10.5 A fragment of a semantic network showing the representation of the logical
assertion Fly(Shankar,NewYork,NewDelhi,Yesterday).
follows SubsetOf links up the hierarchy until it ﬁnds a category for which there is a boxed
Legs link—in this case, the Persons category. The simplicity and efﬁciency of this inference
mechanism, compared with semidecidable logical theorem proving, has been one of the main
attractions of semantic networks.
Inheritance becomes complicated when an object can belong to more than one category
or when a category can be a subset of more than one other category; this is called multiple in-
heritance. In such cases, the inheritance algorithm might ﬁnd two or more conﬂicting values
Multiple inheritance
answering the query. For this reason, multiple inheritance is banned in some object-oriented
programming (OOP) languages, such as Java, that use inheritance in a class hierarchy. It is
usually allowed in semantic networks, but we defer discussion of that until Section 10.6.
The reader might have noticed an obvious drawback of semantic network notation, com-
pared to ﬁrst-order logic: the fact that links between bubbles represent only binary relations.
For example, the sentence Fly(Shankar,NewYork,NewDelhi,Yesterday) cannot be asserted
directly in a semantic network. Nonetheless, we can obtain the effect of n-ary assertions
by reifying the proposition itself as an event belonging to an appropriate event category.
Figure 10.5 shows the semantic network structure for this particular event. Notice that the
restriction to binary relations forces the creation of a rich ontology of reiﬁed concepts.

## Page 349
