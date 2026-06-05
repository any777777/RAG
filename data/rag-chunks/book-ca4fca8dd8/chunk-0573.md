---
chunk_id: "book-ca4fca8dd8-chunk-0573"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 573
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 10.5
Reasoning Systems for Categories
347
10.5 Reasoning Systems for Categories
Categories are the primary building blocks of large-scale knowledge representation schemes.
This section describes systems specially designed for organizing and reasoning with cate-
gories. There are two closely related families of systems: semantic networks provide graph-
Semantic networks
ical aids for visualizing a knowledge base and efﬁcient algorithms for inferring properties
of an object on the basis of its category membership; and description logics provide a for-
Description logics
mal language for constructing and combining category deﬁnitions and efﬁcient algorithms
for deciding subset and superset relationships between categories.
10.5.1 Semantic networks
In 1909, Charles S. Peirce proposed a graphical notation of nodes and edges called existential
graphs that he called “the logic of the future.” Thus began a long-running debate between ad-
Existential graphs
vocates of “logic” and advocates of “semantic networks.” Unfortunately, the debate obscured
the fact that semantic networks are a form of logic. The notation that semantic networks pro-
vide for certain kinds of sentences is often more convenient, but if we strip away the “human
interface” issues, the underlying concepts—objects, relations, quantiﬁcation, and so on—are
the same.
There are many variants of semantic networks, but all are capable of representing individ-
ual objects, categories of objects, and relations among objects. A typical graphical notation
displays object or category names in ovals or boxes, and connects them with labeled links. For
example, Figure 10.4 has a MemberOf link between Mary and FemalePersons, corresponding
to the logical assertion Mary∈FemalePersons; similarly, the SisterOf link between Mary and
John corresponds to the assertion SisterOf(Mary,John). We can connect categories using
SubsetOf links, and so on. It is such fun drawing bubbles and arrows that one can get carried
away. For example, we know that persons have female persons as mothers, so can we draw a
HasMother link from Persons to FemalePersons? The answer is no, because HasMother is a
relation between a person and his or her mother, and categories do not have mothers.5
For this reason, we have used a special notation—the double-boxed link—in Figure 10.4.
This link asserts that
∀x x∈Persons ⇒[∀y HasMother(x,y) ⇒y∈FemalePersons].
We might also want to assert that persons have two legs—that is,
∀x x∈Persons ⇒Legs(x,2).
As before, we need to be careful not to assert that a category has legs; the single-boxed link
in Figure 10.4 is used to assert properties of every member of a category.
The semantic network notation makes it convenient to perform inheritance reasoning of
the kind introduced in Section 10.2. For example, by virtue of being a person, Mary inherits
the property of having two legs. Thus, to ﬁnd out how many legs Mary has, the inheritance
algorithm follows the MemberOf link from Mary to the category she belongs to, and then
5
Several early systems failed to distinguish between properties of members of a category and properties of the
category as a whole. This can lead directly to inconsistencies, as pointed out by Drew McDermott (1976) in his
article “Artiﬁcial Intelligence Meets Natural Stupidity.” Another common problem was the use of IsA links for
both subset and membership relations, in correspondence with English usage: “a cat is a mammal” and “Fiﬁis a
cat.” See Exercise 10.NATS for more on these issues.
