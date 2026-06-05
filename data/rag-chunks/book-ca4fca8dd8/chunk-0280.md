---
chunk_id: "book-ca4fca8dd8-chunk-0280"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 280
confidence: "first-pass"
extraction_method: "structured-local"
---

172
Chapter 5
Constraint Satisfaction Problems
Arc consistency tightens down the domains (unary constraints) using the arcs (binary
constraints). To make progress on problems like map coloring, we need a stronger notion of
consistency. Path consistency tightens the binary constraints by using implicit constraints
Path consistency
that are inferred by looking at triples of variables.
A two-variable set {Xi,Xj} is path-consistent with respect to a third variable Xm if, for
every assignment {Xi = a,Xj = b} consistent with the constraints (if any) on {Xi,Xj}, there is
an assignment to Xm that satisﬁes the constraints on {Xi,Xm} and {Xm,Xj}. The name refers
to the overall consistency of the path from Xi to Xj with Xm in the middle.
Let’s see how path consistency fares in coloring the Australia map with two colors. We
will make the set {WA,SA} path-consistent with respect to NT. We start by enumerating the
consistent assignments to the set. In this case, there are only two: {WA = red,SA = blue} and
{WA = blue,SA = red}. We can see that with both of these assignments NT can be neither red
nor blue (because it would conﬂict with either WA or SA). Because there is no valid choice for
NT, we eliminate both assignments, and we end up with no valid assignments for {WA,SA}.
Therefore, we know that there can be no solution to this problem.
5.2.4 K-consistency
Stronger forms of propagation can be deﬁned with the notion of k-consistency. A CSP is k-
K-consistency
consistent if, for any set of k−1 variables and for any consistent assignment to those variables,
a consistent value can always be assigned to any kth variable. 1-consistency says that, given
the empty set, we can make any set of one variable consistent: this is what we called node
consistency. 2-consistency is the same as arc consistency. For binary constraint graphs, 3-
consistency is the same as path consistency.
A CSP is strongly k-consistent if it is k-consistent and is also (k−1)-consistent, (k−2)-
Strongly
k-consistent
consistent, ... all the way down to 1-consistent. Now suppose we have a CSP with n nodes
and make it strongly n-consistent (i.e., strongly k-consistent for k=n). We can then solve
the problem as follows: First, we choose a consistent value for X1. We are then guaranteed
to be able to choose a value for X2 because the graph is 2-consistent, for X3 because it is
3-consistent, and so on. For each variable Xi, we need only search through the d values in the
domain to ﬁnd a value consistent with X1,...,Xi−1. The total run time is only O(n2d).
Of course, there is no free lunch: constraint satisfaction is NP-complete in general, and
any algorithm for establishing n-consistency must take time exponential in n in the worst case.
Worse, n-consistency also requires space that is exponential in n. In practice, determining
the appropriate level of consistency checking is mostly an empirical science. Computing
2-consistency is common, and 3-consistency less common.
5.2.5 Global constraints
Remember that a global constraint is one involving an arbitrary number of variables (but not
necessarily all variables). Global constraints occur frequently in real problems and can be
handled by special-purpose algorithms that are more efﬁcient than the general-purpose meth-
ods described so far. For example, the Alldiff constraint says that all the variables involved
must have distinct values (as in the cryptarithmetic problem above and Sudoku puzzles be-
low). One simple form of inconsistency detection for Alldiff constraints works as follows:
if m variables are involved in the constraint, and if they have n possible distinct values alto-
gether, and m > n, then the constraint cannot be satisﬁed.
