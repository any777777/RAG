---
chunk_id: "book-ca4fca8dd8-chunk-0407"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 407
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 7.6
Effective Propositional Model Checking
251
7.6.1 A complete backtracking algorithm
The ﬁrst algorithm we consider is often called the Davis–Putnam algorithm, after the sem-
Davis–Putnam
algorithm
inal paper by Martin Davis and Hilary Putnam (1960). The algorithm is in fact the version
described by Davis, Logemann, and Loveland (1962), so we will call it DPLL after the ini-
tials of all four authors. DPLL takes as input a sentence in conjunctive normal form—a set
of clauses. Like BACKTRACKING-SEARCH and TT-ENTAILS?, it is essentially a recursive,
depth-ﬁrst enumeration of possible models. It embodies three improvements over the simple
scheme of TT-ENTAILS?:
• Early termination: The algorithm detects whether the sentence must be true or false,
even with a partially completed model. A clause is true if any literal is true, even if
the other literals do not yet have truth values; hence, the sentence as a whole could be
judged true even before the model is complete. For example, the sentence (A ∨B) ∧
(A∨C) is true if A is true, regardless of the values of B and C. Similarly, a sentence is
false if any clause is false, which occurs when each of its literals is false. Again, this
can occur long before the model is complete. Early termination avoids examination of
entire subtrees in the search space.
• Pure symbol heuristic: A pure symbol is a symbol that always appears with the same
Pure symbol
“sign” in all clauses. For example, in the three clauses (A∨¬B), (¬B∨¬C), and (C∨A),
the symbol A is pure because only the positive literal appears, B is pure because only the
negative literal appears, and C is impure. It is easy to see that if a sentence has a model,
then it has a model with the pure symbols assigned so as to make their literals true,
because doing so can never make a clause false. Note that, in determining the purity
of a symbol, the algorithm can ignore clauses that are already known to be true in the
model constructed so far. For example, if the model contains B=false, then the clause
(¬B ∨¬C) is already true, and in the remaining clauses C appears only as a positive
literal; therefore C becomes pure.
• Unit clause heuristic: A unit clause was deﬁned earlier as a clause with just one literal.
In the context of DPLL, it also means clauses in which all literals but one are already
assigned false by the model. For example, if the model contains B=true, then (¬B ∨
¬C) simpliﬁes to ¬C, which is a unit clause. Obviously, for this clause to be true, C must
be set to false. The unit clause heuristic assigns all such symbols before branching on
the remainder. One important consequence of the heuristic is that any attempt to prove
(by refutation) a literal that is already in the knowledge base will succeed immediately
(Exercise 7.KNOW). Notice also that assigning one unit clause can create another unit
clause—for example, when C is set to false, (C∨A) becomes a unit clause, causing true
to be assigned to A. This “cascade” of forced assignments is called unit propagation.
Unit propagation
It resembles the process of forward chaining with deﬁnite clauses, and indeed, if the
CNF expression contains only deﬁnite clauses then DPLL essentially replicates forward
chaining. (See Exercise 7.DPLL.)
The DPLL algorithm is shown in Figure 7.17, which gives the essential skeleton of the search
process without the implementation details.
What Figure 7.17 does not show are the tricks that enable SAT solvers to scale up to large
problems. It is interesting that most of these tricks are in fact rather general, and we have
seen them before in other guises:
