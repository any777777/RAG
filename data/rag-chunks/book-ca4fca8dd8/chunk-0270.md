---
chunk_id: "book-ca4fca8dd8-chunk-0270"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 270
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 5.1
Deﬁning Constraint Satisfaction Problems
167
Next we say that for each wheel, we must afﬁx the wheel (which takes 1 minute), then tighten
the nuts (2 minutes), and ﬁnally attach the hubcap (1 minute, but not represented yet):
WheelRF +1 ≤NutsRF; NutsRF +2 ≤CapRF;
WheelLF +1 ≤NutsLF; NutsLF +2 ≤CapLF;
WheelRB +1 ≤NutsRB; NutsRB +2 ≤CapRB;
WheelLB +1 ≤NutsLB; NutsLB +2 ≤CapLB .
Suppose we have four workers to install wheels, but they have to share one tool that helps
put the axle in place. We need a disjunctive constraint to say that AxleF and AxleB must not
Disjunctive
constraint
overlap in time; either one comes ﬁrst or the other does:
(AxleF +10 ≤AxleB)
or
(AxleB +10 ≤AxleF).
This looks like a more complicated constraint, combining arithmetic and logic. But it still
reduces to a set of pairs of values that AxleF and AxleB can take on.
We also need to assert that the inspection comes last and takes 3 minutes. For every
variable except Inspect we add a constraint of the form X + dX ≤Inspect. Finally, suppose
there is a requirement to get the whole assembly done in 30 minutes. We can achieve that by
limiting the domain of all variables:
Di = {0,1,2,3,...,30}.
This particular problem is trivial to solve, but CSPs have been successfully applied to job-
shop scheduling problems like this with thousands of variables.
5.1.3 Variations on the CSP formalism
The simplest kind of CSP involves variables that have discrete, ﬁnite domains. Map-coloring
Discrete domain
Finite domain
problems and scheduling with time limits are both of this kind. The 8-queens problem (Fig-
ure 4.3) can also be viewed as a ﬁnite-domain CSP, where the variables Q1,...,Q8 correspond
to the queens in columns 1 to 8, and the domain of each variable speciﬁes the possible row
numbers for the queen in that column, Di = {1,2,3,4,5,6,7,8}. The constraints say that no
two queens can be in the same row or diagonal.
A discrete domain can be inﬁnite, such as the set of integers or strings. (If we didn’t put
Inﬁnite
a deadline on the job-scheduling problem, there would be an inﬁnite number of start times for
each variable.) With inﬁnite domains, we must use implicit constraints like T1+d1 ≤T2 rather
than explicit tuples of values. Special solution algorithms (which we do not discuss here) exist
for linear constraints on integer variables—that is, constraints, such as the one just given, in
Linear constraints
which each variable appears only in linear form. It can be shown that no algorithm exists for
solving general nonlinear constraints on integer variables—the problem is undecidable.
Nonlinear
constraints
Constraint satisfaction problems with continuous domains are common in the real world
Continuous domains
and are widely studied in the ﬁeld of operations research. For example, the scheduling of ex-
periments on the Hubble Space Telescope requires very precise timing of observations; the
start and ﬁnish of each observation and maneuver are continuous-valued variables that must
obey a variety of astronomical, precedence, and power constraints. The best-known category
of continuous-domain CSPs is that of linear programming problems, where constraints must
be linear equalities or inequalities. Linear programming problems can be solved in time poly-
nomial in the number of variables. Problems with different types of constraints and objective
functions have also been studied—quadratic programming, second-order conic programming,
and so on. These problems constitute an important area of applied mathematics.
