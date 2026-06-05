---
chunk_id: "book-ca4fca8dd8-chunk-0413"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 413
confidence: "first-pass"
extraction_method: "structured-local"
---

254
Chapter 7
Logical Agents
solution. Alas, if max ﬂips is inﬁnity and the sentence is unsatisﬁable, then the algorithm
never terminates!
For this reason, WALKSAT is most useful when we expect a solution to exist—for exam-
ple, the problems discussed in Chapters 3 and 5 usually have solutions. On the other hand,
WALKSAT cannot always detect unsatisﬁability, which is required for deciding entailment.
For example, an agent cannot reliably use WALKSAT to prove that a square is safe in the
wumpus world. Instead, it can say, “I thought about it for an hour and couldn’t come up with
a possible world in which the square isn’t safe.” This may be a good empirical indicator that
the square is safe, but it’s certainly not a proof.
7.6.3 The landscape of random SAT problems
Some SAT problems are harder than others. Easy problems can be solved by any old algo-
rithm, but because we know that SAT is NP-complete, at least some problem instances must
require exponential run time. In Chapter 5, we saw some surprising discoveries about certain
kinds of problems. For example, the n-queens problem—thought to be quite tricky for back-
tracking search algorithms—turned out to be trivially easy for local search methods, such as
min-conﬂicts. This is because solutions are very densely distributed in the space of assign-
ments, and any initial assignment is guaranteed to have a solution nearby. Thus, n-queens is
easy because it is underconstrained.
Underconstrained
When we look at satisﬁability problems in conjunctive normal form, an underconstrained
problem is one with relatively few clauses constraining the variables. For example, here is a
randomly generated 3-CNF sentence with ﬁve symbols and ﬁve clauses:
(¬D∨¬B∨C)∧(B∨¬A∨¬C)∧(¬C ∨¬B∨E)
∧(E ∨¬D∨B)∧(B∨E ∨¬C).
Sixteen of the 32 possible assignments are models of this sentence, so, on average, it would
take just two random guesses to ﬁnd a model. This is an easy satisﬁability problem, as are
most such underconstrained problems. On the other hand, an overconstrained problem has
many clauses relative to the number of variables and is likely to have no solutions. Over-
constrained problems are often easy to solve, because the constraints quickly lead either to a
solution or to a dead end from which there is no escape.
To go beyond these basic intuitions, we must deﬁne exactly how random sentences are
generated. The notation CNFk(m,n) denotes a k-CNF sentence with m clauses and n symbols,
where the clauses are chosen uniformly, independently, and without replacement from among
all clauses with k different literals, which are positive or negative at random. (A symbol may
not appear twice in a clause, nor may a clause appear twice in a sentence.)
Given a source of random sentences, we can measure the probability of satisﬁability.
Figure 7.19(a) plots the probability for CNF3(m,50), that is, sentences with 50 variables and
3 literals per clause, as a function of the clause/symbol ratio, m/n. As we expect, for small
m/n the probability of satisﬁability is close to 1, and at large m/n the probability is close to
0. The probability drops fairly sharply around m/n=4.3. Empirically, we ﬁnd that the “cliff”
stays in roughly the same place (for k=3) and gets sharper and sharper as n increases.
Theoretically, the satisﬁability threshold conjecture says that for every k ≥3, there is a
Satisﬁability
threshold conjecture
threshold ratio rk such that, as n goes to inﬁnity, the probability that CNFk(rn,n) is satisﬁable
becomes 1 for all values of r below the threshold, and 0 for all values above. The conjecture
remains unproven, even for special cases like k = 3. Whether it is a theorem or not, this kind
