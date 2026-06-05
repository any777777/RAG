---
chunk_id: "book-ca4fca8dd8-chunk-0556"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 556
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 10.2
Categories and Objects
337
with exactly two legs attached to a body:
Biped(a)
⇒
∃l1,l2,b Leg(l1)∧Leg(l2)∧Body(b) ∧
PartOf(l1,a)∧PartOf(l2,a)∧PartOf(b,a) ∧
Attached(l1,b)∧Attached(l2,b) ∧
l1 ̸= l2 ∧[∀l3 Leg(l3)∧PartOf(l3,a) ⇒(l3 =l1 ∨l3 =l2)].
The notation for “exactly two” is a little awkward; we are forced to say that there are two
legs, that they are not the same, and that if anyone proposes a third leg, it must be the same
as one of the other two. In Section 10.5.2, we describe a formalism called description logic
that makes it easier to represent constraints like “exactly two.”
We can deﬁne a PartPartition relation analogous to the Partition relation for categories.
(See Exercise 10.DECM.) An object is composed of the parts in its PartPartition and can be
viewed as deriving some properties from those parts. For example, the mass of a composite
object is the sum of the masses of the parts. Notice that this is not the case with categories,
which have no mass, even though their elements might.
It is also useful to deﬁne composite objects with deﬁnite parts but no particular struc-
ture. For example, we might want to say “The apples in this bag weigh two pounds.” The
temptation would be to ascribe this weight to the set of apples in the bag, but this would be
a mistake because the set is an abstract mathematical concept that has elements but does not
have weight. Instead, we need a new concept, which we will call a bunch. For example, if
Bunch
the apples are Apple1, Apple2, and Apple3, then
BunchOf({Apple1,Apple2,Apple3})
denotes the composite object with the three apples as parts (not elements). We can then use the
bunch as a normal, albeit unstructured, object. Notice that BunchOf({x})=x. Furthermore,
BunchOf(Apples) is the composite object consisting of all apples—not to be confused with
Apples, the category or set of all apples.
We can deﬁne BunchOf in terms of the PartOf relation. Obviously, each element of s is
part of BunchOf(s):
∀x x∈s ⇒PartOf(x,BunchOf(s)).
Furthermore, BunchOf(s) is the smallest object satisfying this condition. In other words,
BunchOf(s) must be part of any object that has all the elements of s as parts:
∀y [∀x x∈s ⇒PartOf(x,y)] ⇒PartOf(BunchOf(s),y).
These axioms are an example of a general technique called logical minimization, which
Logical minimization
means deﬁning an object as the smallest one satisfying certain conditions.
10.2.2 Measurements
In both scientiﬁc and commonsense theories of the world, objects have height, mass, cost,
and so on.
The values that we assign for these properties are called measures.
Ordi-
Measure
nary quantitative measures are quite easy to represent. We imagine that the universe in-
cludes abstract “measure objects,” such as the length that is the length of this line seg-
ment:
. We can call this length 1.5 inches or 3.81 centimeters. Thus,
the same length has different names in our language. We represent the length with a units
function that takes a number as argument. (An alternative is explored in Exercise 10.ALTM.)
Units function
