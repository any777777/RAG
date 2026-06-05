---
chunk_id: "book-ca4fca8dd8-chunk-0560"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 560
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 10.2
Categories and Objects
339
If the line segment is called L1, we can write
Length(L1)=Inches(1.5)=Centimeters(3.81).
Conversion between units is done by equating multiples of one unit to another:
Centimeters(2.54×d)=Inches(d).
Similar axioms can be written for pounds and kilograms, seconds and days, and dollars and
cents. Measures can be used to describe objects as follows:
Diameter(Basketball12)=Inches(9.5)
ListPrice(Basketball12)=$(19)
Weight(BunchOf({Apple1,Apple2,Apple3})) = Pounds(2)
d ∈Days ⇒Duration(d)=Hours(24).
Note that $(1) is not a dollar bill—it is a price. One can have two dollar bills, but there is
only one object named $(1). Note also that, while Inches(0) and Centimeters(0) refer to the
same zero length, they are not identical to other zero measures, such as Seconds(0).
Simple, quantitative measures are easy to represent. Other measures present more of a
problem, because they have no agreed scale of values. Exercises have difﬁculty, desserts have
deliciousness, and poems have beauty, yet numbers cannot be assigned to these qualities. One
might, in a moment of pure accountancy, dismiss such properties as useless for the purpose of
logical reasoning; or, still worse, attempt to impose a numerical scale on beauty. This would
be a grave mistake, because it is unnecessary. The most important aspect of measures is not
the particular numerical values, but the fact that measures can be ordered.
Although measures are not numbers, we can still compare them, using an ordering symbol
such as >. For example, we might well believe that Norvig’s exercises are tougher than
Russell’s, and that one scores less on tougher exercises:
e1 ∈Exercises∧e2 ∈Exercises∧Wrote(Norvig,e1)∧Wrote(Russell,e2) ⇒
Difﬁculty(e1) > Difﬁculty(e2).
e1 ∈Exercises∧e2 ∈Exercises∧Difﬁculty(e1) > Difﬁculty(e2) ⇒
ExpectedScore(e1) < ExpectedScore(e2).
This is enough to allow one to decide which exercises to do, even though no numerical values
for difﬁculty were ever used. (One does, however, have to discover who wrote which exer-
cises.) These sorts of monotonic relationships among measures form the basis for the ﬁeld of
qualitative physics, a subﬁeld of AI that investigates how to reason about physical systems
without plunging into detailed equations and numerical simulations. Qualitative physics is
discussed in the historical notes section.
10.2.3 Objects: Things and stuﬀ
The real world can be seen as consisting of primitive objects (e.g., atomic particles) and
composite objects built from them. By reasoning at the level of large objects such as apples
and cars, we can overcome the complexity involved in dealing with vast numbers of primitive
objects individually. There is, however, a signiﬁcant portion of reality that seems to defy any
obvious individuation—division into distinct objects. We give this portion the generic name
Individuation
stuff. For example, suppose I have some butter and an aardvark in front of me. I can say
Stuﬀ
there is one aardvark, but there is no obvious number of “butter-objects,” because any part of
a butter-object is also a butter-object, at least until we get to very small parts indeed. This is
