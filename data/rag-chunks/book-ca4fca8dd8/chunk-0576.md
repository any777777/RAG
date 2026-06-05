---
chunk_id: "book-ca4fca8dd8-chunk-0576"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 576
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 350

350
Chapter 10
Knowledge Representation
Concept →Thing | ConceptName
|
And(Concept,...)
|
All(RoleName,Concept)
|
AtLeast(Integer,RoleName)
|
AtMost(Integer,RoleName)
|
Fills(RoleName,IndividualName,...)
|
SameAs(Path,Path)
|
OneOf(IndividualName,...)
Path →[RoleName,...]
ConceptName →Adult | Female | Male | ...
RoleName →Spouse | Daughter | Son | ...
Figure 10.6 The syntax of descriptions in a subset of the CLASSIC language.
The CLASSIC language (Borgida et al., 1989) is a typical description logic. The syntax
of CLASSIC descriptions is shown in Figure 10.6.6 For example, to say that bachelors are
unmarried adult males we would write
Bachelor = And(Unmarried,Adult,Male).
The equivalent in ﬁrst-order logic would be
Bachelor(x) ⇔Unmarried(x)∧Adult(x)∧Male(x).
Notice that the description logic has an algebra of operations on predicates, which of course
we can’t do in ﬁrst-order logic. Any description in CLASSIC can be translated into an equiv-
alent ﬁrst-order sentence, but some descriptions are more straightforward in CLASSIC. For
example, to describe the set of men with at least three sons who are all unemployed and
married to doctors, and at most two daughters who are all professors in physics or math
departments, we would use
And(Man,AtLeast(3,Son),AtMost(2,Daughter),
All(Son,And(Unemployed,Married,All(Spouse,Doctor))),
All(Daughter,And(Professor,Fills(Department,Physics,Math)))).
We leave it as an exercise to translate this into ﬁrst-order logic.
Perhaps the most important aspect of description logics is their emphasis on tractability of
inference. A problem instance is solved by describing it and then asking if it is subsumed by
one of several possible solution categories. In standard ﬁrst-order logic systems, predicting
the solution time is often impossible. It is frequently left to the user to engineer the represen-
tation to detour around sets of sentences that seem to be causing the system to take several
6
Notice that the language does not allow one to simply state that one concept, or category, is a subset of
another. This is a deliberate policy: subsumption between categories must be derivable from some aspects of the
descriptions of the categories. If not, then something is missing from the descriptions.

## Page 351
