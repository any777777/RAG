---
chunk_id: "book-ca4fca8dd8-chunk-0552"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 552
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 10.2
Categories and Objects
335
10.2 Categories and Objects
The organization of objects into categories is a vital part of knowledge representation. Al-
Category
though interaction with the world takes place at the level of individual objects, much reason- ◀
ing takes place at the level of categories. For example, a shopper would normally have the
goal of buying a basketball, rather than a particular basketball such as BB9. Categories also
serve to make predictions about objects once they are classiﬁed. One infers the presence of
certain objects from perceptual input, infers category membership from the perceived proper-
ties of the objects, and then uses category information to make predictions about the objects.
For example, from its green and yellow mottled skin, one-foot diameter, ovoid shape, red
ﬂesh, black seeds, and presence in the fruit aisle, one can infer that an object is a watermelon;
from this, one infers that it would be useful for fruit salad.
There are two choices for representing categories in ﬁrst-order logic: predicates and ob-
jects. That is, we can use the predicate Basketball(b), or we can reify1 the category as
Reiﬁcation
an object, Basketballs. We could then say Member(b,Basketballs), which we will abbre-
viate as b∈Basketballs, to say that b is a member of the category of basketballs. We say
Subset(Basketballs,Balls), abbreviated as Basketballs ⊂Balls, to say that Basketballs is a
subcategory of Balls. We will use subcategory, subclass, and subset interchangeably.
Subcategory
Categories organize knowledge through inheritance. If we say that all instances of the
Inheritance
category Food are edible, and if we assert that Fruit is a subclass of Food and Apples is a sub-
class of Fruit, then we can infer that every apple is edible. We say that the individual apples
inherit the property of edibility, in this case from their membership in the Food category.
Subclass relations organize categories into a taxonomic hierarchy or taxonomy. Tax-
Taxonomic hierarchy
onomies have been used explicitly for centuries in technical ﬁelds. The largest such taxonomy
organizes about 10 million living and extinct species, many of them beetles,2 into a single hi-
erarchy; library science has developed a taxonomy of all ﬁelds of knowledge, encoded as the
Dewey Decimal system; and tax authorities and other government departments have devel-
oped extensive taxonomies of occupations and commercial products.
First-order logic makes it easy to state facts about categories, either by relating objects to
categories or by quantifying over their members. Here are some example facts:
• An object is a member of a category.
BB9 ∈Basketballs
• A category is a subclass of another category.
Basketballs ⊂Balls
• All members of a category have some properties.
(x∈Basketballs) ⇒Spherical(x)
• Members of a category can be recognized by some properties.
Orange(x)∧Round(x)∧Diameter(x)=9.5′′ ∧x∈Balls ⇒x∈Basketballs
• A category as a whole has some properties.
Dogs∈DomesticatedSpecies
1
Turning a proposition into an object is called reiﬁcation, from the Latin word res, or thing. John McCarthy
proposed the term “thingiﬁcation,” but it never caught on.
2
When asked what one could deduce about the Creator from the study of nature, biologist J. B. S. Haldane said
“An inordinate fondness for beetles.”
