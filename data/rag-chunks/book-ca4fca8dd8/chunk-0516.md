---
chunk_id: "book-ca4fca8dd8-chunk-0516"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 516
confidence: "first-pass"
extraction_method: "structured-local"
---

316
Chapter 9
Inference in First-Order Logic
9.4.5 Constraint logic programming
In our discussion of forward chaining (Section 9.3), we showed how constraint satisfaction
problems (CSPs) can be encoded as deﬁnite clauses. Standard Prolog solves such problems
in exactly the same way as the backtracking algorithm given in Figure 5.5.
Because backtracking enumerates the domains of the variables, it works only for ﬁnite-
domain CSPs. In Prolog terms, there must be a ﬁnite number of solutions for any goal with
unbound variables. (For example, a map coloring problem in which each variable can take
on one of four different colors.) Inﬁnite-domain CSPs—for example, with integer- or real-
valued variables—require quite different algorithms, such as bounds propagation or linear
programming.
Consider the following example. We deﬁne triangle(X,Y,Z) as a predicate that holds
if the three arguments are numbers that satisfy the triangle inequality:
triangle(X,Y,Z) :-
X>0, Y>0, Z>0, X+Y>Z, Y+Z>X, X+Z>Y.
If we ask Prolog the query triangle(3,4,5), it succeeds. On the other hand, if we ask
triangle(3,4,Z), no solution will be found, because the subgoal Z>0 cannot be handled
by Prolog; we can’t compare an unbound value to 0.
Constraint logic programming (CLP) allows variables to be constrained rather than
Constraint logic
programming
bound. A CLP solution is the most speciﬁc set of constraints on the query variables that can
be derived from the knowledge base. For example, the solution to the triangle(3,4,Z)
query is the constraint 7 > Z > 1. Standard logic programs are just a special case of CLP in
which the solution constraints must be equality constraints—that is, bindings.
CLP systems incorporate various constraint-solving algorithms for the constraints al-
lowed in the language. For example, a system that allows linear inequalities on real-valued
variables might include a linear programming algorithm for solving those constraints. CLP
systems also adopt a much more ﬂexible approach to solving standard logic programming
queries. For example, instead of depth-ﬁrst, left-to-right backtracking, they might use any of
the more efﬁcient algorithms discussed in Chapter 5, including heuristic conjunct ordering,
backjumping, cutset conditioning, and so on. CLP systems therefore combine elements of
constraint satisfaction algorithms, logic programming, and deductive databases.
Several systems that allow the programmer more control over the search order for infer-
ence have been deﬁned. The MRS language (Genesereth and Smith, 1981; Russell, 1985)
allows the programmer to write metarules to determine which conjuncts are tried ﬁrst. The
Metarule
user could write a rule saying that the goal with the fewest variables should be tried ﬁrst or
could write domain-speciﬁc rules for particular predicates.
9.5 Resolution
The last of our three families of logical systems, and the only one that works for any knowl-
edge base, not just deﬁnite clauses, is resolution. We saw on page 241 that propositional
resolution is a complete inference procedure for propositional logic; in this section, we ex-
tend it to ﬁrst-order logic.
