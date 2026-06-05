---
chunk_id: "book-ca4fca8dd8-chunk-0282"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 282
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 5.2
Constraint Propagation: Inference in CSPs
173
This leads to the following simple algorithm: First, remove any variable in the constraint
that has a singleton domain, and delete that variable’s value from the domains of the re-
maining variables. Repeat as long as there are singleton variables. If at any point an empty
domain is produced or there are more variables than domain values left, then an inconsistency
has been detected.
This method can detect the inconsistency in the assignment {WA=red, NSW =red} for
Figure 5.1. Notice that the variables SA, NT, and Q are effectively connected by an Alldiff
constraint because each pair must have two different colors. After applying AC-3 with the
partial assignment, the domains of SA, NT, and Q are all reduced to {green,blue}. That is,
we have three variables and only two colors, so the Alldiff constraint is violated. Thus, a
simple consistency procedure for a higher-order constraint is sometimes more effective than
applying arc consistency to an equivalent set of binary constraints.
Another important higher-order constraint is the resource constraint, sometimes called
Resource constraint
the Atmost constraint. For example, in a scheduling problem, let P1,...,P4 denote the numbers
of personnel assigned to each of four tasks. The constraint that no more than 10 personnel
are assigned in total is written as Atmost(10,P1,P2,P3,P4). We can detect an inconsistency
simply by checking the sum of the minimum values of the current domains; for example, if
each variable has the domain {3,4,5,6}, the Atmost constraint cannot be satisﬁed. We can
also enforce consistency by deleting the maximum value of any domain if it is not consistent
with the minimum values of the other domains. Thus, if each variable in our example has the
domain {2,3,4,5,6}, the values 5 and 6 can be deleted from each domain.
For large resource-limited problems with integer values—such as logistical problems in-
volving moving thousands of people in hundreds of vehicles—it is usually not possible to
represent the domain of each variable as a large set of integers and gradually reduce that
set by consistency-checking methods. Instead, domains are represented by upper and lower
bounds and are managed by bounds propagation. For example, in an airline-scheduling
Bounds propagation
problem, let’s suppose there are two ﬂights, F1 and F2, for which the planes have capacities
165 and 385, respectively. The initial domains for the numbers of passengers on ﬂights F1
and F2 are then
D1 = [0,165]
and
D2 = [0,385].
Now suppose we have the additional constraint that the two ﬂights together must carry 420
people: F1 +F2 = 420. Propagating bounds constraints, we reduce the domains to
D1 = [35,165]
and
D2 = [255,385].
We say that a CSP is bounds-consistent if for every variable X, and for both the lower-bound
Bounds-consistent
and upper-bound values of X, there exists some value of Y that satisﬁes the constraint between
X and Y for every variable Y. This kind of bounds propagation is widely used in practical
constraint problems.
5.2.6 Sudoku
The popular Sudoku puzzle has introduced millions of people to constraint satisfaction prob-
Sudoku
lems, although they may not realize it. A Sudoku board consists of 81 squares, some of which
are initially ﬁlled with digits from 1 to 9. The puzzle is to ﬁll in all the remaining squares
such that no digit appears twice in any row, column, or 3×3 box (see Figure 5.4). A row,
column, or box is called a unit.
