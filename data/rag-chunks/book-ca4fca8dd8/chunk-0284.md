---
chunk_id: "book-ca4fca8dd8-chunk-0284"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 284
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 5.3
Backtracking Search for CSPs
175
and we are left with only the value 7 in the domain of I6. Now there are 8 known values in
column 6, so arc consistency can infer that A6 must be 1. Inference continues along these
lines, and eventually, AC-3 can solve the entire puzzle—all the variables have their domains
reduced to a single value, as shown in Figure 5.4(b).
Of course, Sudoku would soon lose its appeal if every puzzle could be solved by a me-
chanical application of AC-3, and indeed AC-3 works only for the easiest Sudoku puzzles.
Slightly harder ones can be solved by PC-2, but at a greater computational cost: there are
255,960 different path constraints to consider in a Sudoku puzzle. To solve the hardest puz-
zles and to make efﬁcient progress, we will have to be more clever.
Indeed, the appeal of Sudoku puzzles for the human solver is the need to be resourceful
in applying more complex inference strategies. Aﬁcionados give them colorful names, such
as “naked triples.” That strategy works as follows: in any unit (row, column or box), ﬁnd
three squares that each have a domain that contains the same three numbers or a subset of
those numbers. For example, the three domains might be {1,8}, {3,8}, and {1,3,8}. From
that we don’t know which square contains 1, 3, or 8, but we do know that the three numbers
must be distributed among the three squares. Therefore we can remove 1, 3, and 8 from the
domains of every other square in the unit.
It is interesting to note how far we can go without saying much that is speciﬁc to Sudoku.
We do of course have to say that there are 81 variables, that their domains are the digits 1 to 9,
and that there are 27 Alldiff constraints. But beyond that, all the strategies—arc consistency,
path consistency, and so on—apply generally to all CSPs, not just to Sudoku problems. Even
naked triples is really a strategy for enforcing consistency of Alldiff constraints and is not
speciﬁc to Sudoku per se. This is the power of the CSP formalism: for each new problem
area, we only need to deﬁne the problem in terms of constraints; then the general constraint-
solving mechanisms can take over.
5.3 Backtracking Search for CSPs
Sometimes we can ﬁnish the constraint propagation process and still have variables with
multiple possible values. In that case we have to search for a solution. In this section we
cover backtracking search algorithms that work on partial assignments; in the next section
we look at local search algorithms over complete assignments.
Consider how a standard depth-limited search (from Chapter 3) could solve CSPs. A
state would be a partial assignment, and an action would extend the assignment, adding, say,
NSW = red or SA = blue for the Australia map-coloring problem. For a CSP with n variables
of domain size d we would end up with a search tree where all the complete assignments (and
thus all the solutions) are leaf nodes at depth n. But notice that the branching factor at the top
level would be nd because any of d values can be assigned to any of n variables. At the next
level, the branching factor is (n −1)d, and so on for n levels. So the tree has n! · dn leaves,
even though there are only dn possible complete assignments!
We can get back that factor of n! by recognizing a crucial property of CSPs: commuta-
tivity. A problem is commutative if the order of application of any given set of actions does
Commutativity
not matter. In CSPs, it makes no difference if we ﬁrst assign NSW = red and then SA = blue,
or the other way around. Therefore, we need only consider a single variable at each node
in the search tree. At the root we might make a choice between SA=red, SA=green, and
