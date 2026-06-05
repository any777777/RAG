---
chunk_id: "book-ca4fca8dd8-chunk-0567"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 567
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 343

Section 10.3
Events
343
Meet(i, j)
Starts(i, j)
Finishes(i, j)
Equals(i, j)
Before(i, j)
After(j,i)
During(i, j)
Overlap(i, j)
j
j
j
j
j
j
j
i
i
i
i
i
i
i
Figure 10.2 Predicates on time intervals.
writing axioms. To say that the reign of Elizabeth II immediately followed that of George VI,
and the reign of Elvis overlapped with the 1950s, we can write the following:
Meets(ReignOf(GeorgeVI),ReignOf(ElizabethII)).
Overlap(Fifties,ReignOf(Elvis)).
Begin(Fifties)=Begin(AD1950).
End(Fifties)=End(AD1959).
10.3.2 Fluents and objects
Physical objects can be viewed as generalized events, in the sense that a physical object is
a chunk of space–time. For example, USA can be thought of as an event that began in 1776
as a union of 13 states and is still in progress today as a union of 50. We can describe the
changing properties of USA using state ﬂuents, such as Population(USA). A property of USA
that changes every four or eight years, barring mishaps, is its president. One might propose
that President(USA) is a logical term that denotes a different object at different times.
Unfortunately, this is not possible, because a term denotes exactly one object in a given
model structure. (The term President(USA,t) can denote different objects, depending on the
value of t, but our ontology keeps time indices separate from ﬂuents.) The only possibility is
that President(USA) denotes a single object that consists of different people at different times.
It is the object that is George Washington from 1789 to 1797, John Adams from 1797 to 1801,
and so on, as in Figure 10.3. To say that George Washington was president throughout 1790,
we can write
T(Equals(President(USA),GeorgeWashington),Begin(AD1790),End(AD1790)).
We use the function symbol Equals rather than the standard logical predicate =, because
we cannot have a predicate as an argument to T, and because the interpretation is not that
GeorgeWashington and President(USA) are logically identical in 1790; logical identity is not
something that can change over time. The identity is between the subevents of the objects
President(USA) and GeorgeWashington that are deﬁned by the period 1790.

## Page 344
