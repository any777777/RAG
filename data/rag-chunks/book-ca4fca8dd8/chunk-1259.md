---
chunk_id: "book-ca4fca8dd8-chunk-1259"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1259
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 20.5
Inductive Logic Programming
763
There are three kinds of literals that can be added:
1. Literals using predicates: the literal can be negated or unnegated, any existing predicate
(including the goal predicate) can be used, and the arguments must all be variables.
Any variable can be used for any argument of the predicate, with one restriction: each
literal must include at least one variable from an earlier literal or from the head of the
clause. Literals such as Mother(z,u), Married(z,z), ¬Male(y), and Grandfather(v,x)
are allowed, whereas Married(u,v) is not. Notice that the use of the predicate from the
head of the clause allows FOIL to learn recursive deﬁnitions.
2. Equality and inequality literals: these relate variables already appearing in the clause.
For example, we might add z ̸= x. These literals can also include user-speciﬁed con-
stants. For learning arithmetic we might use 0 and 1, and for learning list functions we
might use the empty list [].
3. Arithmetic comparisons: when dealing with functions of continuous variables, literals
such as x > y and y ≤z can be added. As in decision-tree learning, a constant threshold
value can be chosen to maximize the discriminatory power of the test.
The resulting branching factor in this search space is very large (see Exercise 20.6), but FOIL
can also use type information to reduce it. For example, if the domain included numbers as
well as people, type restrictions would prevent NEW-LITERALS from generating literals such
as Parent(x,n), where x is a person and n is a number.
CHOOSE-LITERAL uses a heuristic somewhat similar to information gain (see page 680)
to decide which literal to add. The exact details are not important here, and a number of
different variations have been tried. One interesting additional feature of FOIL is the use of
Ockham’s razor to eliminate some hypotheses. If a clause becomes longer (according to some
metric) than the total length of the positive examples that the clause explains, that clause is
not considered as a potential hypothesis. This technique provides a way to avoid overcomplex
clauses that ﬁt noise in the data.
FOIL and its relatives have been used to learn a wide variety of deﬁnitions. One of the
most impressive demonstrations (Quinlan and Cameron-Jones, 1993) involved solving a long
sequence of exercises on list-processing functions from Bratko’s (1986) Prolog textbook. In
each case, the program was able to learn a correct deﬁnition of the function from a small set
of examples, using the previously learned functions as background knowledge.
20.5.3 Inductive learning with inverse deduction
The second major approach to ILP involves inverting the normal deductive proof process.
Inverse resolution is based on the observation that if the example Classiﬁcations follow
Inverse resolution
from Background ∧Hypothesis ∧Descriptions, then one must be able to prove this fact by
resolution (because resolution is complete). If we can “run the proof backward,” then we can
ﬁnd a Hypothesis such that the proof goes through. The key, then, is to ﬁnd a way to invert
the resolution process.
We will show a backward proof process for inverse resolution that consists of individual
backward steps. Recall that an ordinary resolution step takes two clauses C1 and C2 and
resolves them to produce the resolvent C. An inverse resolution step takes a resolvent C and
produces two clauses C1 and C2, such that C is the result of resolving C1 and C2. Alternatively,
it may take a resolvent C and clause C1 and produce a clause C2 such that C is the result of
resolving C1 and C2.
