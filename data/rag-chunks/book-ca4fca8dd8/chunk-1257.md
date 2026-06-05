---
chunk_id: "book-ca4fca8dd8-chunk-1257"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1257
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 20.5
Inductive Logic Programming
761
20.5.2 Top-down inductive learning methods
The ﬁrst approach to ILP works by starting with a very general rule and gradually specializing
it so that it ﬁts the data. This is essentially what happens in decision-tree learning, where a
decision tree is gradually grown until it is consistent with the observations. To do ILP we
use ﬁrst-order literals instead of attributes, and the hypothesis is a set of clauses instead of a
decision tree. This section describes FOIL (Quinlan, 1990), one of the ﬁrst ILP programs.
Suppose we are trying to learn a deﬁnition of the Grandfather(x,y) predicate, using the
same family data as before. As with decision-tree learning, we can divide the examples into
positive and negative examples. Positive examples are
⟨George,Anne⟩, ⟨Philip,Peter⟩, ⟨Spencer,Harry⟩, ...
and negative examples are
⟨George,Elizabeth⟩, ⟨Harry,Zara⟩, ⟨Charles,Philip⟩, ...
Notice that each example is a pair of objects, because Grandfather is a binary predicate. In
all, there are 12 positive examples in the family tree and 388 negative examples (all the other
pairs of people).
FOIL constructs a set of clauses, each with Grandfather(x,y) as the head. The clauses
must classify the 12 positive examples as instances of the Grandfather(x,y) relationship,
while ruling out the 388 negative examples. The clauses are Horn clauses, with the extension
that negated literals are allowed in the body of a clause and are interpreted using negation as
failure, as in Prolog. The initial clause has an empty body:
⇒Grandfather(x,y) .
This clause classiﬁes every example as positive, so it needs to be specialized. We do this by
adding literals one at a time to the left-hand side. Here are three potential additions:
Father(x,y) ⇒Grandfather(x,y) .
Parent(x,z) ⇒Grandfather(x,y) .
Father(x,z) ⇒Grandfather(x,y) .
(Notice that we are assuming that a clause deﬁning Parent is already part of the background
knowledge.) The ﬁrst of these three clauses incorrectly classiﬁes all of the 12 positive exam-
ples as negative and can thus be ignored. The second and third agree with all of the positive
examples, but the second is incorrect on a larger fraction of the negative examples—twice as
many, because it allows mothers as well as fathers. Hence, we prefer the third clause.
Now we need to specialize this clause further, to rule out the cases in which x is the father
of some z, but z is not a parent of y. Adding the single literal Parent(z,y) gives
Father(x,z)∧Parent(z,y) ⇒Grandfather(x,y) ,
which correctly classiﬁes all the examples. FOIL will ﬁnd and choose this literal, thereby
solving the learning task. In general, the solution is a set of Horn clauses, each of which
implies the target predicate. For example, if we didn’t have the Parent predicate in our vo-
cabulary, then the solution might be
Father(x,z)∧Father(z,y) ⇒Grandfather(x,y)
Father(x,z)∧Mother(z,y) ⇒Grandfather(x,y) .
Note that each of these clauses covers some of the positive examples, that together they cover
all the positive examples, and that NEW-CLAUSE is designed in such a way that no clause
