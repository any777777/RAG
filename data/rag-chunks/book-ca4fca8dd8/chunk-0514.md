---
chunk_id: "book-ca4fca8dd8-chunk-0514"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 514
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 9.4
Backward Chaining
315
inference can be exponential in the number of ground facts that are generated. If we apply
forward chaining instead, at most n2 path(X,Y) facts can be generated linking n nodes. For
the problem in Figure 9.8(b), only 62 inferences are needed.
Forward chaining on graph search problems is an example of dynamic programming,
Dynamic
programming
in which the solutions to subproblems are constructed incrementally from those of smaller
subproblems and are cached to avoid recomputation. We can obtain a similar effect in a
backward chaining system, except that here we are breaking down large goals into smaller
ones, rather than building them up.
Either way, storing intermediate results to avoid duplication is key. This is the approach
taken by tabled logic programming systems, which use efﬁcient storage and retrieval mech-
Tabled logic
programming
anisms. Tabled logic programming combines the goal-directedness of backward chaining
with the dynamic-programming efﬁciency of forward chaining. It is also complete for Data-
log knowledge bases, which means that the programmer need worry less about inﬁnite loops.
(It is still possible to get an inﬁnite loop with predicates like father(X,Y) that refer to a
potentially unbounded number of objects.)
9.4.4 Database semantics of Prolog
Prolog uses database semantics, as discussed in Section 8.2.8. The unique names assumption
says that every Prolog constant and every ground term refers to a distinct object, and the
closed world assumption says that the only sentences that are true are those that are entailed
by the knowledge base. There is no way to assert that a sentence is false in Prolog. This
makes Prolog less expressive than ﬁrst-order logic, but it is part of what makes Prolog more
efﬁcient and more concise. Consider the following assertions about some course offerings:
Course(CS,101), Course(CS,102), Course(CS,106), Course(EE,101).
(9.11)
Under the unique names assumption, CS and EE are different (as are 101, 102, and 106), so
this means that there are four distinct courses. Under the closed-world assumption there are
no other courses, so there are exactly four courses. But if these were assertions in FOL rather
than in database semantics, then all we could say is that there are somewhere between one
and inﬁnity courses. That’s because the assertions (in FOL) do not deny the possibility that
other unmentioned courses are also offered, nor do they say that the courses mentioned are
different from each other. If we wanted to translate Equation (9.11) into FOL, we would get
the following sentence:
Course(d,n)
⇔
(d =CS∧n = 101)∨(d =CS∧n = 102)
∨(d =CS∧n = 106)∨(d =EE ∧n = 101).
(9.12)
This is called the completion of Equation (9.11). It expresses in FOL the idea that there are
Completion
at most four courses. To express in FOL the idea that there are at least four courses, we need
to write the completion of the equality predicate:
x = y
⇔
(x = CS∧y = CS)∨(x = EE ∧y = EE)∨(x = 101∧y = 101)
∨(x = 102∧y = 102)∨(x = 106∧y = 106).
The completion is useful for understanding database semantics, but for practical purposes, if
your problem can be described with database semantics, it is more efﬁcient to reason with
Prolog or some other database semantics system, rather than translating into FOL and rea-
soning with a full FOL theorem prover.
