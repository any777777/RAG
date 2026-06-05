---
chunk_id: "book-ca4fca8dd8-chunk-0554"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 554
confidence: "first-pass"
extraction_method: "structured-local"
---

336
Chapter 10
Knowledge Representation
Notice that because Dogs is a category and is a member of DomesticatedSpecies, the latter
must be a category of categories. Of course there are exceptions to many of the above rules
(punctured basketballs are not spherical); we deal with these exceptions later.
Although subclass and member relations are the most important ones for categories, we
also want to be able to state relations between categories that are not subclasses of each
other. For example, if we just say that Undergraduates and GraduateStudents are subclasses
of Students, then we have not said that an undergraduate cannot also be a graduate student.
We say that two or more categories are disjoint if they have no members in common. We
Disjoint
may also want to say that the classes undergrad and graduate student form an exhaustive
decomposition of university students. A exhaustive decomposition of disjoint sets is known
Exhaustive
decomposition
as a partition. Here are some more examples of these three concepts:
Partition
Disjoint({Animals,Vegetables})
ExhaustiveDecomposition({Americans,Canadians,Mexicans},
NorthAmericans)
Partition({Animals,Plants,Fungi,Protista,Monera},
LivingThings).
(Note that the ExhaustiveDecomposition of NorthAmericans is not a Partition, because some
people have dual citizenship.) The three predicates are deﬁned as follows:
Disjoint(s) ⇔(∀c1,c2 c1 ∈s∧c2 ∈s∧c1 ̸= c2 ⇒Intersection(c1,c2)={ })
ExhaustiveDecomposition(s,c) ⇔(∀i i∈c ⇔∃c2 c2 ∈s∧i∈c2)
Partition(s,c) ⇔Disjoint(s)∧ExhaustiveDecomposition(s,c).
Categories can also be deﬁned by providing necessary and sufﬁcient conditions for mem-
bership. For example, a bachelor is an unmarried adult male:
x∈Bachelors ⇔Unmarried(x)∧x∈Adults∧x∈Males.
As we discuss in the sidebar on natural kinds on page 338, strict logical deﬁnitions for cat-
egories are usually possible only for artiﬁcial formal terms, not for ordinary objects. But
deﬁnitions are not always necessary.
10.2.1 Physical composition
The idea that one object can be part of another is a familiar one. One’s nose is part of one’s
head, Romania is part of Europe, and this chapter is part of this book. We use the general
PartOf relation to say that one thing is part of another. Objects can be grouped into PartOf
hierarchies, reminiscent of the Subset hierarchy:
PartOf(Bucharest,Romania)
PartOf(Romania,EasternEurope)
PartOf(EasternEurope,Europe)
PartOf(Europe,Earth).
The PartOf relation is transitive and reﬂexive; that is,
PartOf(x,y)∧PartOf(y,z) ⇒PartOf(x,z)
PartOf(x,x).
Therefore, we can conclude PartOf(Bucharest,Earth). Categories of composite objects are
Composite object
often characterized by structural relations among parts. For example, a biped is an object
