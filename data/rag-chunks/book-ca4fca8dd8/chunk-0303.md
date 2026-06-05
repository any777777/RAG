---
chunk_id: "book-ca4fca8dd8-chunk-0303"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 303
confidence: "first-pass"
extraction_method: "structured-local"
---

Summary
187
one less than the size of the largest node; the tree width of the graph itself is deﬁned to be
the minimum width among all its tree decompositions. If a graph has tree width w then the
problem can be solved in O(ndw+1) time given the corresponding tree decomposition. Hence,
CSPs with constraint graphs of bounded tree width are solvable in polynomial time.
◀
Unfortunately, ﬁnding the decomposition with minimal tree width is NP-hard, but there
are heuristic methods that work well in practice. Which is better: the cutset decomposition
with time O(dc · (n −c)d2), or the tree decomposition with time O(ndw+1)? Whenever you
have a cycle-cutset of size c, there is also a tree width of size w < c + 1, and it may be far
smaller in some cases. So time consideration favors tree decomposition, but the advantage of
the cycle-cutset approach is that it can be executed in linear memory, while tree decomposi-
tion requires memory exponential in w.
5.5.3 Value symmetry
So far, we have looked at the structure of the constraint graph. There can also be important
structure in the values of variables, or in the structure of the constraint relations themselves.
Consider the map-coloring problem with d colors. For every consistent solution, there is
actually a set of d! solutions formed by permuting the color names. For example, on the
Australia map we know that WA, NT, and SA must all have different colors, but there are
3! = 6 ways to assign three colors to three regions. This is called value symmetry. We would
Value symmetry
like to reduce the search space by a factor of d! by breaking the symmetry in assignments.
We do this by introducing a symmetry-breaking constraint. For our example, we might
Symmetry-breaking
constraint
impose an arbitrary ordering constraint, NT < SA < WA, that requires the three values to be
in alphabetical order. This constraint ensures that only one of the d! solutions is possible:
{NT = blue,SA = green,WA = red}.
For map coloring, it was easy to ﬁnd a constraint that eliminates the symmetry. In gen-
eral it is NP-hard to eliminate all symmetry, but breaking value symmetry has proved to be
important and effective on a wide range of problems.
Summary
• Constraint satisfaction problems (CSPs) represent a state with a set of variable/value
pairs and represent the conditions for a solution by a set of constraints on the variables.
Many important real-world problems can be described as CSPs.
• A number of inference techniques use the constraints to rule out certain variable as-
signments. These include node, arc, path, and k-consistency.
• Backtracking search, a form of depth-ﬁrst search, is commonly used for solving CSPs.
Inference can be interwoven with search.
• The minimum-remaining-values and degree heuristics are domain-independent meth-
ods for deciding which variable to choose next in a backtracking search. The least-
constraining-value heuristic helps in deciding which value to try ﬁrst for a given
variable. Backtracking occurs when no legal assignment can be found for a variable.
Conﬂict-directed backjumping backtracks directly to the source of the problem. Con-
straint learning records the conﬂicts as they are encountered during search in order to
avoid the same conﬂict later in the search.
