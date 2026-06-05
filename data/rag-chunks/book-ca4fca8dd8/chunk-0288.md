---
chunk_id: "book-ca4fca8dd8-chunk-0288"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 288
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 5.3
Backtracking Search for CSPs
177
Figure 5.6 Part of the search tree for the map-coloring problem in Figure 5.1.
5.3.1 Variable and value ordering
The backtracking algorithm contains the line
var←SELECT-UNASSIGNED-VARIABLE(csp,assignment) .
The simplest strategy for SELECT-UNASSIGNED-VARIABLE is static ordering: choose the
variables in order, {X1,X2,...}. The next simplest is to choose randomly. Neither strategy
is optimal. For example, after the assignments for WA=red and NT =green in Figure 5.6,
there is only one possible value for SA, so it makes sense to assign SA=blue next rather than
assigning Q. In fact, after SA is assigned, the choices for Q, NSW, and V are all forced.
This intuitive idea—choosing the variable with the fewest “legal” values—is called the
minimum-remaining-values (MRV) heuristic. It also has been called the “most constrained
Minimum-remaining-
values
variable” or “fail-ﬁrst” heuristic, the latter because it picks a variable that is most likely to
cause a failure soon, thereby pruning the search tree. If some variable X has no legal values
left, the MRV heuristic will select X and failure will be detected immediately—avoiding
pointless searches through other variables. The MRV heuristic usually performs better than
a random or static ordering, sometimes by orders of magnitude, although the results vary
depending on the problem.
The MRV heuristic doesn’t help at all in choosing the ﬁrst region to color in Australia,
because initially every region has three legal colors. In this case, the degree heuristic comes
Degree heuristic
in handy. It attempts to reduce the branching factor on future choices by selecting the variable
that is involved in the largest number of constraints on other unassigned variables. In Fig-
ure 5.1, SA is the variable with highest degree, 5; the other variables have degree 2 or 3, except
for T, which has degree 0. If we assign the SA ﬁrst, we can then go around the ﬁve mainland
regions in clockwise or counterclockwise order and assign each one a color that is different
than SA and different than the previous region. The minimum-remaining-values heuristic is
usually a more powerful guide, but the degree heuristic can be useful as a tie-breaker.
Once a variable has been selected, the algorithm must decide on the order in which to
examine its values. The least-constraining-value heuristic is effective for this. It prefers
Least-constraining-
value
the value that rules out the fewest choices for the neighboring variables in the constraint
