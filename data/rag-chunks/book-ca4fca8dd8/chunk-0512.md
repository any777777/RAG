---
chunk_id: "book-ca4fca8dd8-chunk-0512"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 512
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 9.4
Backward Chaining
313
and the clause is written “backwards” from what we are used to; instead of A ∧B ⇒C in
Prolog we have C :- A, B. Here is a typical example:
criminal(X) :- american(X), weapon(Y), sells(X,Y,Z), hostile(Z).
In Prolog the notation [E|L] denotes a list whose ﬁrst element is E and whose rest is L. Here
is a Prolog program for append(X,Y,Z), which succeeds if list Z is the result of appending
lists X and Y:
append([],Y,Y).
append([A|X],Y,[A|Z]) :- append(X,Y,Z).
In English, we can read these clauses as (1) appending the empty list and the list Y pro-
duces the same list Y, and (2) [A|Z] is the result of appending [A|X] and Y, provided that
Z is the result of appending X and Y. In most high-level languages we can write a similar
recursive function that describes how to append two lists. The Prolog deﬁnition is actually
more powerful, however, because it describes a relation that holds among three arguments,
rather than a function computed from two arguments. For example, we can ask the query
append(X,Y,[1,2,3]): what two lists can be appended to give [1,2,3]? Prolog gives us
back the solutions
X=[]
Y=[1,2,3];
X=[1]
Y=[2,3];
X=[1,2]
Y=[3];
X=[1,2,3] Y=[]
The execution of Prolog programs is done through depth-ﬁrst backward chaining, where
clauses are tried in the order in which they are written in the knowledge base. Prolog’s design
represents a compromise between declarativeness and execution efﬁciency. Some aspects of
Prolog fall outside standard logical inference:
• Prolog uses the database semantics of Section 8.2.8 rather than ﬁrst-order semantics,
and this is apparent in its treatment of equality and negation (see Section 9.4.4).
• There is a set of built-in functions for arithmetic. Literals using these function symbols
are “proved” by executing code rather than doing further inference. For example, the
goal “X is 4+3” succeeds with X bound to 7. On the other hand, the goal “5 is X+Y”
fails, because the built-in functions do not do arbitrary equation solving.
• There are built-in predicates that have side effects when executed. These include input–
output predicates and the assert/retract predicates for modifying the knowledge
base. Such predicates have no counterpart in logic and can produce confusing results—
for example, if facts are asserted in a branch of the proof tree that eventually fails.
• The occur check is omitted from Prolog’s uniﬁcation algorithm. This means that some
unsound inferences can be made; these are almost never a problem in practice.
• Prolog uses depth-ﬁrst backward-chaining search with no checks for inﬁnite recursion.
This makes for a usable programming language that is very fast when used properly,
but it means that some programs that look like valid logic will fail to terminate.
9.4.3 Redundant inference and inﬁnite loops
We now turn to the Achilles heel of Prolog: the mismatch between depth-ﬁrst search and
search trees that include repeated states and inﬁnite paths. Consider the following logic pro-
gram that decides if a path exists between two points on a directed graph:
