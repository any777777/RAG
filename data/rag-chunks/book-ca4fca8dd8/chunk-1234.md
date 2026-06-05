---
chunk_id: "book-ca4fca8dd8-chunk-1234"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1234
confidence: "first-pass"
extraction_method: "structured-local"
---

744
Chapter 20
Knowledge in Learning
20.1.3 Least-commitment search
Backtracking arises because the current-best-hypothesis approach has to choose a particular
hypothesis as its best guess even though it does not have enough data yet to be sure of the
choice. What we can do instead is to keep around all and only those hypotheses that are
consistent with all the data so far. Each new example will either have no effect or will get
rid of some of the hypotheses. Recall that the original hypothesis space can be viewed as a
disjunctive sentence
h1 ∨h2 ∨h3 ...∨hn .
As various hypotheses are found to be inconsistent with the examples, this disjunction shrinks,
retaining only those hypotheses not ruled out. Assuming that the original hypothesis space
does in fact contain the right answer, the reduced disjunction must still contain the right an-
swer because only incorrect hypotheses have been removed. The set of hypotheses remaining
is called the version space, and the learning algorithm (sketched in Figure 20.3) is called the
Version space
version space learning algorithm (also the candidate elimination algorithm).
Candidate
elimination
One important property of this approach is that it is incremental: one never has to go back
and reexamine the old examples. All remaining hypotheses are guaranteed to be consistent
with them already. But there is an obvious problem. We already said that the hypothesis
space is enormous, so how can we possibly write down this enormous disjunction?
The following simple analogy is very helpful. How do you represent all the real numbers
between 1 and 2? After all, there are an inﬁnite number of them! The answer is to use an
interval representation that just speciﬁes the boundaries of the set: [1,2]. It works because we
have an ordering on the real numbers.
We also have an ordering on the hypothesis space, namely, generalization/specialization.
This is a partial ordering, which means that each boundary will not be a point but rather a
set of hypotheses called a boundary set. The great thing is that we can represent the entire
Boundary set
version space using just two boundary sets: a most general boundary (the G-set) and a most
G-set
speciﬁc boundary (the S-set). Everything in between is guaranteed to be consistent with the
S-set
examples. Before we prove this, let us recap:
function VERSION-SPACE-LEARNING(examples) returns a version space
local variables: V, the version space: the set of all hypotheses
V ←the set of all hypotheses
for each example e in examples do
if V is not empty then V ←VERSION-SPACE-UPDATE(V,e)
return V
function VERSION-SPACE-UPDATE(V,e) returns an updated version space
V ←{h∈V : h is consistent with e}
Figure 20.3 The version space learning algorithm. It ﬁnds a subset of V that is consistent
with all the examples.
