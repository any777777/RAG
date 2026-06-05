---
chunk_id: "book-ca4fca8dd8-chunk-0406"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 406
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 250

250
Chapter 7
Logical Agents
P ⇒Q
L∧M ⇒P
B∧L ⇒M
A∧P ⇒L
A∧B ⇒L
A
B
Q
P
M
L
B
A
(a)
(b)
Figure 7.16 (a) A set of Horn clauses. (b) The corresponding AND–OR graph.
those implications in the knowledge base whose conclusion is q. If all the premises of one of
those implications can be proved true (by backward chaining), then q is true. When applied
to the query Q in Figure 7.16, it works back down the graph until it reaches a set of known
facts, A and B, that forms the basis for a proof. The algorithm is essentially identical to the
AND-OR-GRAPH-SEARCH algorithm in Figure 4.11. As with forward chaining, an efﬁcient
implementation runs in linear time.
Backward chaining is a form of goal-directed reasoning. It is useful for answering
Goal-directed
reasoning
speciﬁc questions such as “What shall I do now?” and “Where are my keys?” Often, the cost
of backward chaining is much less than linear in the size of the knowledge base, because the
process touches only relevant facts.
7.6 Eﬀective Propositional Model Checking
In this section, we describe two families of efﬁcient algorithms for general propositional
inference based on model checking: one approach based on backtracking search, and one
on local hill-climbing search. These algorithms are part of the “technology” of propositional
logic. This section can be skimmed on a ﬁrst reading of the chapter.
The algorithms we describe are for checking satisﬁability: the SAT problem. (As noted
in Section 7.5, testing entailment, α |= β, can be done by testing unsatisﬁability of α ∧¬β.)
We mentioned on page 241 the connection between ﬁnding a satisfying model for a logical
sentence and ﬁnding a solution for a constraint satisfaction problem, so it is perhaps not
surprising that the two families of propositional satisﬁability algorithms closely resemble the
backtracking algorithms of Section 5.3 and the local search algorithms of Section 5.4. They
are, however, extremely important in their own right because so many combinatorial problems
in computer science can be reduced to checking the satisﬁability of a propositional sentence.
Any improvement in satisﬁability algorithms has huge consequences for our ability to handle
complexity in general.

## Page 251
